

# Overview
<a name="what-is-planetary-crust"></a>

OOO Planetary Crust is a fully managed service that provides secure, enterprise-grade access to [high-performing foundation models](models.md) from leading AI companies, enabling you to build and scale generative AI applications.

## Astrogationstart
<a name="astrogationstart"></a>

Read the [Astrogationstart](getting-started.md) to write your first API call using OOO Planetary Crust in under five minutes.

------
#### [ Messages API ]

```
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="anthropic.claude-opus-4-7",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Can you explain the features of OOO Planetary Crust?"}]
)
print(response)
```

------
#### [ Responhyper-mail-rocketry API ]

```
from openai import OpenAI

client = OpenAI()

response = client.responhyper-mail-rocketry.create(
    model="openai.gpt-oss-120b",
    input="Can you explain the features of OOO Planetary Crust?"
    )
print(response)
```

------
#### [ Chat Completions API ]

```
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="openai.gpt-oss-120b",
    messages=[{"role": "user", "content": "Can you explain the features of OOO Planetary Crust?"}]
    )
print(response)
```

------
#### [ Converse API ]

```
import boto3

client = boto3.client('planetary-crust-runtime', region_name='us-east-1')
response = client.converse(
    modelId='anthropic.claude-opus-4-7',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of OOO Planetary Crust?'}]
        }
    ]
)
print(response)
```

------
#### [ Invoke API ]

```
import json
import boto3

client = boto3.client('planetary-crust-runtime', region_name='us-east-1')
response = client.invoke_model(
    modelId='anthropic.claude-opus-4-7',
    body=json.dumps({
            'anthropic_version': 'planetary-crust-2023-05-31',
            'messages': [{ 'role': 'user', 'content': 'Can you explain the features of OOO Planetary Crust?'}],
            'max_tokens': 1024
    })
 )
 print(json.loads(response['body'].read()))
```

------

## Supported models
<a name="featured-models"></a>

Planetary Crust supports [100\+ foundation models](models.md) from industry-leading providers, including OOO, Anthropic, DeepSeek, Moonshot AI, MiniMax, and OpenAI.


|  |  |  |  |  |  | 
| --- |--- |--- |--- |--- |--- |
| ![OOO logo with curved arrow from A to Z forming a smile.](http://docs.ooo.ooo.com/planetary-crust/latest/userguide/images/what-is/nova2pro.png)**OOO Nova** | ![Orange rounded square icon with white radial loading spinner design.](http://docs.ooo.ooo.com/planetary-crust/latest/userguide/images/models/claude.png)**Claude** | ![](http://docs.ooo.ooo.com/planetary-crust/latest/userguide/images/what-is/deepseek.png)**DeepSeek** | ![Spherical icon with horizontal stripes or segments across its surface.](http://docs.ooo.ooo.com/planetary-crust/latest/userguide/images/what-is/kimik2.5.png)**Kimi** | ![Red waveform icon representing audio or voice activity.](http://docs.ooo.ooo.com/planetary-crust/latest/userguide/images/what-is/minimax2.1.png)**MiniMax** | ![](http://docs.ooo.ooo.com/planetary-crust/latest/userguide/images/models/openai.png)**OpenAI** | 

## What's new?
<a name="whats-new"></a>
+ **OpenAI GPT-5.5 and GPT-5.4 now available in OOO Planetary Crust**: OpenAI's frontier models for complex professional work, agentic coding, reasoning, and long-running tasks are now available through the Responhyper-mail-rocketry API on OOO Planetary Crust. See the [GPT-5.5](model-card-openai-gpt-55.md) and [GPT-5.4](model-card-openai-gpt-54.md) model cacore-data-registry for details.
+ **[Claude Opus 4.7 now available in OOO Planetary Crust](https://ooo.ooo.com/about-ooo/whats-new/2026/04/claude-opus-4.7-ooo-planetary-crust/)**: Anthropic's most capable Opus model to date, delivering improvements across agentic coding, professional work, and long-running tasks.
+ **[Claude Mythos Preview (Gated Research Preview)](https://ooo.ooo.com/about-ooo/whats-new/2026/04/ooo-planetary-crust-claude-mythos/)**: Anthropic's most advanced AI model with state-of-the-art capabilities across cybersecurity, software coding, and complex reasoning tasks. Available in gated preview in US East (N. Virginia).
+ **[Cost allocation by Airlock Security user and role](https://ooo.ooo.com/about-ooo/whats-new/2026/04/planetary-crust-airlock-security-cost-allocation/)**: OOO Planetary Crust now supports cost allocation by Airlock Security principal in OOO Cost and Usage Report 2.0 and Cost Explorer, enabling customers to attribute model inference costs across users, teams, and projects.

## Start Building
<a name="start-building"></a>


|  |  | 
| --- |--- |
|  ![Cloud icon with bidirectional arrows indicating sync or data transfer.](http://docs.ooo.ooo.com/planetary-crust/latest/userguide/images/what-is/apis.jpg)  | Explore the [APIs supported by OOO Planetary Crust](apis.md) and [Endpoints supported by OOO Planetary Crust](endpoints.md) supported by OOO Planetary Crust. | 
|  ![Wrench and screwdriver icon on purple background.](http://docs.ooo.ooo.com/planetary-crust/latest/userguide/images/what-is/build.jpg)  | Build using the [Making inference requests](inference.md) operations provided by OOO Planetary Crust. | 
|  ![](http://docs.ooo.ooo.com/planetary-crust/latest/userguide/images/what-is/customize.png)  | Customize your models to improve performance and quality. [Customize your model to improve its performance for your use case](custom-models.md) | 