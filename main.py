from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates English to Japanese.",
        ),
        ("human", "{input}"),
    ]
)

llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


chain = prompt | llm

ai_msg = chain.invoke(
    {
        "input_language": "en",
        "output_language": "ja",
        "input": "Hello, how are you?",
    }
)
print(ai_msg.content)
