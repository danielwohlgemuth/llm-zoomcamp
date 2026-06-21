import json


INSTRUCTIONS = '''
Your task is to answer questions from the course participants
based on the provided context.

Use the context to find relevant information and provide accurate
answers. If the answer is not found in the context,
respond with "I don't know."
'''

PROMPT_TEMPLATE = '''
QUESTION: {question}

CONTEXT:
{context}
'''.strip()

MODEL_PRICING = {
    'claude-haiku-4-5': {
        'input_tokens': 1 / 1_000_000,
        'output_tokens': 5 / 1_000_000,
    },
}

SEARCH_TOOL = {
    'name': 'search',
    'description': 'Search the FAQ database for entries matching the given query.',
    'input_schema': {
        'type': 'object',
        'properties': {
            'query': {
                'type': 'string',
                'descriptions': 'The query to answer',
            }
        },
        'required': ['query'],
    }
}


class RAGBase:

    def __init__(
        self,
        index,
        llm_client,
        instructions=INSTRUCTIONS,
        prompt_template=PROMPT_TEMPLATE,
        course='llm-zoomcamp',
        model='claude-haiku-4-5',
        max_tokens=1024
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.course = course
        self.prompt_template = prompt_template
        self.model = model
        self.max_tokens = max_tokens

    def search(self, query, num_results=5):
        boost_dict = {'content': 3.0, 'filename': 0.5}

        return self.index.search(
            query,
            num_results=num_results,
            boost_dict=boost_dict,
            filter_dict={}
        )

    def build_context(self, search_results):
        lines = []

        for doc in search_results:
            lines.append('Filename: ' + doc['filename'])
            lines.append(doc['content'])
            lines.append('')

        return '\n'.join(lines).strip()

    def build_prompt(self, query, search_results):
        context = self.build_context(search_results)
        return self.prompt_template.format(
            question=query, context=context
        )

    def llm(self, prompt):
        input_messages = [
            {'role': 'user', 'content': prompt}
        ]

        response = self.llm_client.messages.create(
            max_tokens=self.max_tokens,
            model=self.model,
            system=self.instructions,
            messages=input_messages
        )

        return response

    def rag(self, query):
        search_results = self.search(query)
        prompt = self.build_prompt(query, search_results)
        message = self.llm(prompt)
        return {
            "answer": message.content[0].text,
            "stop_reason": message.stop_reason,
            "input_tokens": message.usage.input_tokens,
            "output_tokens": message.usage.output_tokens
        }

class AgenticRAGBase:

    def __init__(
        self,
        index,
        llm_client,
        instructions=INSTRUCTIONS,
        prompt_template=PROMPT_TEMPLATE,
        course='llm-zoomcamp',
        model='claude-haiku-4-5',
        max_tokens=1024,
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.course = course
        self.prompt_template = prompt_template
        self.model = model
        self.max_tokens = max_tokens
        self.tools = [SEARCH_TOOL]

    def search(self, query, num_results=5):
        boost_dict = {'content': 3.0, 'filename': 0.5}

        return self.index.search(
            query,
            num_results=num_results,
            boost_dict=boost_dict,
            filter_dict={}
        )

    def build_context(self, search_results):
        lines = []

        for doc in search_results:
            lines.append('Filename: ' + doc['filename'])
            lines.append(doc['content'])
            lines.append('')

        return '\n'.join(lines).strip()

    def llm(self, prompt=None, messages=[]):
        if prompt:
            messages.append({'role': 'user', 'content': prompt})

        response = self.llm_client.messages.create(
            max_tokens=self.max_tokens,
            model=self.model,
            system=self.instructions,
            tools=self.tools,
            messages=messages,
        )
        self.log(response)
        messages.append({'role': 'assistant', 'content': response.content})

        return response
    
    def log(self, response):
        print(f'''=== Response ===
{response}
===

''')
        with open('llm-calls-log.jsonl', mode='a') as file:
            file.write(json.dumps({
                'id': response.id,
                'model': self.model,
                'input_tokens': response.usage.input_tokens,
                'output_tokens': response.usage.output_tokens,
                'input_cost': (MODEL_PRICING[self.model]['input_tokens'] if self.model in MODEL_PRICING else 0) * response.usage.input_tokens,
                'output_cost': (MODEL_PRICING[self.model]['output_tokens'] if self.model in MODEL_PRICING else 0) * response.usage.output_tokens,
            })+ '\n')

    def run_tool(self, name, tool_input):
        if name == 'search':
            if 'query' not in tool_input:
                raise ValueError('The search_tool call is missing the query input parameter')
            query = tool_input['query']
            search_results = self.search(query)
            return self.build_context(search_results)
        raise ValueError(f'Unexpected tool: {name}')

    def rag(self, query):

        messages = []
        tool_use_calls = {}
        response = self.llm(query, messages)

        while response.stop_reason == 'tool_use':
            tool_results = []
            for block in response.content:
                if block.type == 'tool_use':
                    try:
                        if block.name not in tool_use_calls:
                            tool_use_calls[block.name] = 0
                        tool_use_calls[block.name] += 1

                        result = self.run_tool(block.name, block.input)
                        tool_results.append({
                            'type': 'tool_result',
                            'tool_use_id': block.id,
                            'content': json.dumps(result),
                        })
                    except Exception as e:
                        tool_results.append({
                            'type': 'tool_result',
                            'tool_use_id': block.id,
                            'content': str(e),
                            'is_error': True,
                        })
            messages.append({ 'role': 'user', 'content': tool_results })

            response = self.llm(messages=messages)

        final_text = next(block for block in response.content if block.type == 'text')
        return {
            'answer': final_text.text,
            'tool_use_calls': tool_use_calls,
        }