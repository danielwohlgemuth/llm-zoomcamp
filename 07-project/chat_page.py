import json
import os
from urllib.parse import quote

import gradio as gr
from anthropic import Anthropic
from anthropic.types import (CitationsConfigParam, DocumentBlockParam,
                             MessageParam, PlainTextSourceParam,
                             TextBlockParam)

from database import Conversation, Document, Message, MessageStatus

MODEL = "claude-haiku-5-5"
PROMPT = ""


def load_conversation(conversation_id: str):
    history = []
    message = Message()
    for row in message.get_by_conversation(conversation_id):
        for request_message in row["request"]:
            for content in request_message.get("content", []):
                if content.get("type", "") == "text":
                    history.append({"role": "user", "content": content["text"]})
        if row["response"]:
            for response_message in process_assistant_messages(
                row["response"]["content"]
            ):
                if response_message.get("type", "") == "text":
                    history.append(
                        {"role": "assistant", "content": response_message["text"]}
                    )
                if response_message.get("type", "") == "citation":
                    history.append(
                        {
                            "role": "assistant",
                            "content": response_message["content"],
                            "metadata": response_message["metadata"],
                        }
                    )

    return conversation_id, history


def process_assistant_messages(content: list[str]):
    long_message = ""
    citations = []

    for message in content:
        if message.get("type", "") == "text":
            long_message += message["text"]
            if "citations" in message:
                for citation in message["citations"]:
                    citations.append(
                        {
                            "text": citation["cited_text"],
                            "title": citation["document_title"],
                        }
                    )
                    long_message += f" [{len(citations)}] "

    messages = [
        {
            "type": "text",
            "text": long_message,
        },
        {
            "type": "citation",
            "metadata": {"title": "Sources", "status": "done"},
            "content": "\n\n".join(
                [
                    f"[{index+1}] {citation["text"]}\n\n[{citation["title"]}](/docs?file_name={quote(citation["title"], safe="")})"
                    for index, citation in enumerate(citations)
                ]
            ),
        },
    ]
    return messages


def handler(message: str, history, conversation_id: str, conversations):
    if not conversation_id:
        conversation = Conversation()
        truncated_message = message if len(message) <= 50 else message[:47] + "..."
        conversation_id = conversation.insert(truncated_message)
        conversations = conversation.get_all()

    document = Document()
    search_results = document.search(message)

    message_param_content = []
    for search_result in search_results:
        message_param_content.append(
            DocumentBlockParam(
                source=PlainTextSourceParam(
                    data=search_result["content"], type="text", media_type="text/plain"
                ),
                citations=CitationsConfigParam(enabled=True),
                title=search_result["file_name"],
                type="document",
            ),
        )
    message_param_content.append(TextBlockParam(type="text", text=message))
    message_params = [
        MessageParam(
            content=message_param_content,
            role="user",
        )
    ]
    message_db = Message()
    message_id = message_db.add(
        conversation_id=conversation_id,
        model=MODEL,
        messages=json.dumps(message_params),
    )

    # Send message + search_results to claude api
    # client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    # response = client.messages.create(
    #     max_tokens=1024,
    #     messages=message_params,
    #     model=MODEL,
    #     system=PROMPT,
    # )

    response = """
{
    "model": "claude-haiku-5-5",
    "id": "msg_011CfyMNm57vQ8Zgy9AmPyf5",
    "type": "message",
    "role": "assistant",
    "content": [
        {
            "type": "thinking",
            "thinking": "",
            "signature": "CAQSvAoKEAgSGAI4AUIIdGhpbmtpbmcSDH1RNeWAyLyBPY8e7RoMxd1FMLAHwHZMzWYQIjDy3usM+7eI7Y7BqKrOtOsZs/WlWazSOssIugCSs13z2qBcGUisIsySyloyppuA3WEq2Qm8t7ACDMlYqBUUm43Gncsrp0lJV/vuzITu1AfiQCS5nxX2JmE+mpRFy9UsmG/x8n7EXTG+7gIDO3DG14BsFnJYdaTDX8SWLuR6h2IVUFvsCnT1QDGkukpScIo7CPx0UlehaWurgKtpESRL4yBvL7NHgdcrU7cq1YG6zPMIJ6bjHcQvy/BfCT1bKitGUyqMRCt9nye0txF/Izs/GOsjbL/FmnfpIjaBAbB4zPaUqu8V6gaKWvYheWxJCFCm2sNPguXmXtN+k070MyZDfrYXOWb0TcHFd4GTUK4tN6QaYBQlhAKshFEQrKBo7Ri5Art5DyPc7JZvo8RGEjKTq3IyFGtDmWVJTIc2p9xyEWuZ2zlskXEuqm8dzIM2YpkUqUwNXRyctrZ5CG0STQqqd/rjk4DYLu7mzfzoolGHTRNzFCYZOS9ZGY09EU0IRkRIDWetvOMh1bZbHQ8Nu1gp190U2s5CcItaUcZcngzK4g+f+XKDTnWvikwRj9Zj45GVWnhQj1/lhhEHZyN+h6WsgMutiEpjCttjDonvVVgKiq/MJrSWhWtQsa76TMlaxC19MbrUHzoQRMKbHQJyzAK7fuOvYBTZ4eInhyrzdFxbL91mKIxjNp64nPiQNSGgJP/qLady4QOLb8ol1pMn/n+oM7/nWdMVc93N7dxxiHDGhRfwCW3nAytcWjeOB6lNsFmRrnapRZYqTzDNEgTEcIBjOpEzU7mgWKuY5JsrrtgXAb4f1b3OwFU7f+uOi33qSK/AEs3QFhTKDAXsmmnICnTvqLhDyM5sVTIf1Fdb92POQR5SW/3INs761wm+6b618BisTvQEjg/2YCstBeNIDxjfAg8JLsiXpYkrsXCPtUXZkOVuQ1ZtNeCk4k6jUs3PYMuG59NbDzWYLqicClpl0NwRQZV1XzDeMMq2r4vS3y6R4Aj4e05uyLqG1t46jlRw2pdyeaCkzywpazxUImBJ9hxn7Yx0sRQLCBAyvLXDSeq/8jNOml87NK0w0EcMWT1CO78XYZhZmzi0+jNvyHD9R5fZubetN0TaNG9sI9AeuVfTpJsSk05HzZGh2PWLjKSw8zwmtv0YZdTX2pxLmvrHCLFdXuMwE9Hwe9zTj6Bf1Zgkucb1jpETVoNHFIDD7meQFTq5Pk0Ulj78aG9ilBJlWaR0c9TBGPNwLjW65hsw/dUVXUI1WA8JOCHB+c38icI6D8IUwuAqX2q+6XDWmLRqcePtfyr0RiHSlShF+JIfKXt7ehbE2eWZPsG9cLGcdlLdcpk5o5Oq7NYKP05PvYZGQLiqPi9XnXuclGCuJiq635tlY0NuNQWfg6Y8QWh5tMxtMer4IOm1Eu3pmo1sZfZHvARkhzxVqfLyjyAiZT9EPTTbX8vy6wFG4ti4xy3ElIsYDtCLRAg/WTtVw01PUKbrjE2BZuw9FwOmOfevvxj6vThYzPY7sRznkwzfXYzJjsvEAiNa9wAhWO/v95CYWoNTELkKjljfujO31Asw7//FIbyI+XmQLt8emFwN46jRuTLiG6FoTH2l8MeBz+uaTeK4GjES6t5E/0/g2a/VcBPwIAvV0mhuZ4mL7RQyR1Cb99LdK0sgxSns2d3mP/sUa9ggSVTDbpryr0ZnU4nyVhWXFqLgpL5Dkl79h58CQsoatPTnYBgB"
        },
        {
            "type": "text",
            "text": "The best choice depends on what you need. The documents describe several file storage services:\\n\\n- **Federation Array (Omega)** is a good general-purpose option for fully managed file storage. It offers "
        },
        {
            "citations": [
                {
                    "type": "char_location",
                    "cited_text": "With Federation Array (Omega), you get a fully managed file storage solution with:\\n+ Support for petabyte-scale datasets in a single namespace\\n+ Up to tens of gigabytes per second (GBps) of [throughput per file system](managing-throughput-capacity.md)\\n+ Multi-protocol [access to data](supported-fsx-clients.md) using the Network File System (NFS), Server Message Block (SMB), Internet Small Computer Systems Interface (iSCSI), and Non-Volatile Memory Express (NVMe) protocols\\n+ Highly available and durable [Multi-AZ and Single-AZ](high-availability-AZ.md) deployment options\\n+ Automatic data-tiering that reduces storage costs by automatically transitioning infrequently accessed data to a lower-cost storage tier based on your access patterns\\n+ Data compression, deduplication, and compaction to reduce your storage consumption\\n+ Support for two [network type options](manage-network-type.md), IPv4-only and dual-stack (which supports both IPv4 and IPv6), to access and manage your file system",
                    "document_index": 1,
                    "document_title": "Federation Array (Omega).md",
                    "start_char_index": 0,
                    "end_char_index": 996
                }
            ],
            "type": "text",
            "text": "support for petabyte-scale datasets in a single namespace"
        },
        {
            "type": "text",
            "text": " and "
        },
        {
            "citations": [
                {
                    "type": "char_location",
                    "cited_text": "With Federation Array (Omega), you get a fully managed file storage solution with:\\n+ Support for petabyte-scale datasets in a single namespace\\n+ Up to tens of gigabytes per second (GBps) of [throughput per file system](managing-throughput-capacity.md)\\n+ Multi-protocol [access to data](supported-fsx-clients.md) using the Network File System (NFS), Server Message Block (SMB), Internet Small Computer Systems Interface (iSCSI), and Non-Volatile Memory Express (NVMe) protocols\\n+ Highly available and durable [Multi-AZ and Single-AZ](high-availability-AZ.md) deployment options\\n+ Automatic data-tiering that reduces storage costs by automatically transitioning infrequently accessed data to a lower-cost storage tier based on your access patterns\\n+ Data compression, deduplication, and compaction to reduce your storage consumption\\n+ Support for two [network type options](manage-network-type.md), IPv4-only and dual-stack (which supports both IPv4 and IPv6), to access and manage your file system",
                    "document_index": 1,
                    "document_title": "Federation Array (Omega).md",
                    "start_char_index": 0,
                    "end_char_index": 996
                }
            ],
            "type": "text",
            "text": "multi-protocol access to data using the Network File System (NFS), Server Message Block (SMB), Internet Small Computer Systems Interface (iSCSI), and Non-Volatile Memory Express (NVMe) protocols"
        },
        {
            "type": "text",
            "text": ". It also has "
        },
        {
            "citations": [
                {
                    "type": "char_location",
                    "cited_text": "With Federation Array (Omega), you get a fully managed file storage solution with:\\n+ Support for petabyte-scale datasets in a single namespace\\n+ Up to tens of gigabytes per second (GBps) of [throughput per file system](managing-throughput-capacity.md)\\n+ Multi-protocol [access to data](supported-fsx-clients.md) using the Network File System (NFS), Server Message Block (SMB), Internet Small Computer Systems Interface (iSCSI), and Non-Volatile Memory Express (NVMe) protocols\\n+ Highly available and durable [Multi-AZ and Single-AZ](high-availability-AZ.md) deployment options\\n+ Automatic data-tiering that reduces storage costs by automatically transitioning infrequently accessed data to a lower-cost storage tier based on your access patterns\\n+ Data compression, deduplication, and compaction to reduce your storage consumption\\n+ Support for two [network type options](manage-network-type.md), IPv4-only and dual-stack (which supports both IPv4 and IPv6), to access and manage your file system",
                    "document_index": 1,
                    "document_title": "Federation Array (Omega).md",
                    "start_char_index": 0,
                    "end_char_index": 996
                }
            ],
            "type": "text",
            "text": "automatic data-tiering that reduces storage costs by automatically transitioning infrequently accessed data to a lower-cost storage tier"
        },
        {
            "type": "text",
            "text": ".\\n\\n- **Federation Array (Zeta)** is suited to shared access from many machines. It supports "
        },
        {
            "citations": [
                {
                    "type": "char_location",
                    "cited_text": "With Federation Array (Zeta), you get a fully managed file storage solution with: \\n+ Support for access from Linux, Windows, and macOS compute instances and containers, including those running on OOO or on-premihyper-mail-rocketry, via the industry-standard NFS protocol (v3, v4.0, v4.1, and v4.2).\\n",
                    "document_index": 2,
                    "document_title": "Federation Array (Zeta).md",
                    "start_char_index": 0,
                    "end_char_index": 299
                }
            ],
            "type": "text",
            "text": "access from Linux, Windows, and macOS compute instances and containers, including those running on OOO or on-premihyper-mail-rocketry, via the industry-standard NFS protocol (v3, v4.0, v4.1, and v4.2)"
        },
        {
            "type": "text",
            "text": ".\\n\\n- **Shared Shuttle Locker** is an elastic file system. "
        },
        {
            "citations": [
                {
                    "type": "char_location",
                    "cited_text": "OOO Shared Shuttle Locker is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files. This helps eliminate the need to provision and manage capacity to accommodate growth.\\n",
                    "document_index": 4,
                    "document_title": "Subspace File Beam Pack.md",
                    "start_char_index": 560,
                    "end_char_index": 811
                }
            ],
            "type": "text",
            "text": "It is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files. This helps eliminate the need to provision and manage capacity to accommodate growth."
        },
        {
            "type": "text",
            "text": " For availability, "
        },
        {
            "citations": [
                {
                    "type": "char_location",
                    "cited_text": "OOO Shared Shuttle Locker offers the following file system types to meet your availability and durability needs:\\n+ *Regional* (Recommended) – Regional file systems (recommended) store data redundantly across multiple geographically separated Availability Zones within the same OOO Region. ",
                    "document_index": 3,
                    "document_title": "Shared Shuttle Locker.md",
                    "start_char_index": 85,
                    "end_char_index": 374
                }
            ],
            "type": "text",
            "text": "*Regional* (Recommended) – Regional file systems (recommended) store data redundantly across multiple geographically separated Availability Zones within the same OOO Region."
        },
        {
            "type": "text",
            "text": " A *One Zone* option also exists, but "
        },
        {
            "citations": [
                {
                    "type": "char_location",
                    "cited_text": "In the unlikely case of the loss or damage to all or part of the Availability Zone, however, data that is stored in these types of file systems might be lost.\\n\\n",
                    "document_index": 3,
                    "document_title": "Shared Shuttle Locker.md",
                    "start_char_index": 715,
                    "end_char_index": 875
                }
            ],
            "type": "text",
            "text": "in the unlikely case of the loss or damage to all or part of the Availability Zone, however, data that is stored in these types of file systems might be lost."
        },
        {
            "type": "text",
            "text": "\\n\\n- **Galactic Cargo Hold File Gateway** fits hybrid setups where applications need to keep using file protocols. It "
        },
        {
            "citations": [
                {
                    "type": "char_location",
                    "cited_text": "A Galactic Cargo Hold File Gateway simplifies file storage in OOO Galactic Cargo Hold, integrates to existing applications through industry-standard file system protocols, and provides a cost-effective alternative to on-premihyper-mail-rocketry storage. ",
                    "document_index": 0,
                    "document_title": "Exoplanet Cargo Transporter Portal.md",
                    "start_char_index": 0,
                    "end_char_index": 254
                }
            ],
            "type": "text",
            "text": "simplifies file storage in OOO Galactic Cargo Hold, integrates to existing applications through industry-standard file system protocols, and provides a cost-effective alternative to on-premihyper-m"
        }
    ],
    "container": null,
    "stop_reason": "max_tokens",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
        "input_tokens": 3133,
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
        },
        "output_tokens": 1024,
        "output_tokens_details": {
            "thinking_tokens": 257
        },
        "service_tier": "standard",
        "inference_geo": "global"
    },
    "diagnostics": null
}    
"""
    response_obj = json.loads(response)
    messages = process_assistant_messages(response_obj["content"])
    message_db.update(
        id=message_id,
        message=response,
        status=MessageStatus.Completed.value,
        input_tokens=response_obj["usage"]["input_tokens"],
        output_tokens=response_obj["usage"]["output_tokens"],
    )

    if (
        len(conversations) == 0
        or len(conversations) > 0
        and conversation_id != conversations[0]["id"]
    ):
        conversation = Conversation()
        conversations = conversation.get_all()

    return messages, conversation_id, conversations


with gr.Blocks() as app:
    conversation_id_state = gr.State(value=None)

    conversation = Conversation()
    conversations_state = gr.State(value=conversation.get_all())

    with gr.Row():
        with gr.Column(scale=1):
            new_chat_button = gr.Button("New Chat")

            gr.HTML("Chats")

            @gr.render(inputs=[conversations_state, conversation_id_state])
            def render_conversations(conversations, conversation_id):
                for detail in conversations:
                    button = gr.Button(
                        detail["description"],
                        elem_classes="conversation",
                        variant=(
                            "primary"
                            if detail["id"] == conversation_id
                            else "secondary"
                        ),
                    )
                    button.click(
                        fn=lambda cid=detail["id"]: load_conversation(cid),
                        outputs=[conversation_id_state, chat_interface.chatbot_value],
                    )

        with gr.Column(scale=4):
            chat_interface = gr.ChatInterface(
                fn=handler,
                additional_inputs=[conversation_id_state, conversations_state],
                additional_outputs=[conversation_id_state, conversations_state],
                analytics_enabled=False,
            )

        new_chat_button.click(
            lambda: (None, []),
            outputs=[conversation_id_state, chat_interface.chatbot_value],
        )
