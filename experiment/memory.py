from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq

chat = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

conversation = ConversationChain(
    llm=chat,
    memory=ConversationBufferMemory(),
)

while True:
    user_message = input("You: ")
    ai_message = conversation.run(input=user_message)
    print(f"AI: {ai_message}")
