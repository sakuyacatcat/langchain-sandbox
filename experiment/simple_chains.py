from langchain import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

chat = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

cot_template = """
以下の質問に回答してください。
質問: {question}

ステップ・バイ・ステップで考えましょう。
"""

cot_prompt = PromptTemplate(input_variables=["question"], template=cot_template)
cot_chain = LLMChain(prompt=cot_prompt, llm=chat)

summarize_template = """
以下の文章を要約してください。
文章: {text}
"""

summarize_prompt = PromptTemplate(input_variables=["text"], template=summarize_template)
summarize_chain = LLMChain(prompt=summarize_prompt, llm=chat)

cot_summarize_chain = SimpleSequentialChain(
    chains=[cot_chain, summarize_chain],
)

result = cot_summarize_chain(
    "私は市場に行って10個のりんごを買いました。隣人に2つあげました。残りは何個ですか？"
)
print(result["output"])
