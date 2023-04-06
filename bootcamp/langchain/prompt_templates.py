# -*- coding: utf-8 -*-

from langchain import PromptTemplate

# 一、Prompt模版案例

template = '''
I want you to act as a naming consultant for new companies.

Here are some examples of good company names:

- search engine, Google
- social media, Facebook
- video sharing, YouTube

The name should be short, catchy and easy to remember.

What is a good name for a company that makes {product}?
'''

prompt = PromptTemplate(
    input_variables=['product'],
    template=template
)

# 二、创建Prompt模版

from langchain import PromptTemplate

no_input_prompt = PromptTemplate(input_variables=[], template='给我讲一个笑话。')
no_input_prompt.format()

one_input_prompt = PromptTemplate(input_variables=['adj'], template='给我讲一个{adj}笑话。')
one_input_prompt.format(adj='幽默的')

mul_input_prompt = PromptTemplate(
    input_variables=['adj', 'content'], 
    template='给我讲一个{adj}笑话，内容包含{content}'
)
mul_input_prompt.format(adj='幽默的', content='老爷爷和小女孩')


# 三、从LangChainHub加载Prompt模版

from langchain.prompts import load_prompt

prompt = load_prompt('lc://prompts/conversation/prompt.json')
prompt.format(history='', input='What is 1 + 1?')


# 四、

from langchain import PromptTemplate, FewShotPromptTemplate

examples = [
    {'word': 'happy', 'antonym': 'sad'},
    {'word': 'tall', 'antonym': 'short'}
]

example_formatter_template = '''
Word: {word}
Antonym: {antonym}\n
'''
example_prompt = PromptTemplate(
    input_variables=['word', 'antonym'],
    template=example_formatter_template,
)
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix='Give the antonym of every input',
    suffix='Word: {input}\nAntonym:',
    input_variables=['input'],
    example_separator='\n\n',
)
print(few_shot_prompt.format(input='big'))

# 五、选择Prompt

from langchain.prompts.example_selector import LengthBasedExampleSelector

examples = [
    {'word': 'happy', 'antonym': 'sad'},
    {'word': 'tall', 'antonym': 'short'},
    {"word": "energetic", "antonym": "lethargic"},
    {"word": "sunny", "antonym": "gloomy"},
    {"word": "windy", "antonym": "calm"},
]
example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=25,
)
dynamic_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix='Give the antonym of every input.',
    suffix='Word: {input}\nAntonym:',
    input_variables=['input'],
    example_separator='\n\n',
)

print(dynamic_prompt.format(input='big'))


import inspect
def get_source_code(func_name):
    return inspect.getsource(func_name)

from langchain.prompts import StringPromptTemplate
from pydantic import BaseModel, validator

class FunctionExplainerPromptTemplate(StringPromptTemplate, BaseModel):
    
    @validator('input_variables')
    def validate_input_variables(cls, v):
        if len(v) != 1 or 'func_name' not in v:
            raise ValueError('func_name must be the only input_variable.')
        return v

