from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

chat_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            "あなたは{country}料理のプロフェッショナルです"
        ),
        HumanMessagePromptTemplate.from_template(
            "以下の料理のレシピを考えてください。\n\n料理名: {dish}"
        ),
    ]
)
messages = chat_prompt.format_prompt(country="イギリス", dish="肉じゃが")

ai_msg = llm.invoke(messages)
print(ai_msg.content)
