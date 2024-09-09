from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

tools = load_tools(["terminal"], allow_dangerous_tools=True)

agent_chain = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

result = agent_chain.run("experimentディレクトリにあるファイルの一覧を教えて。")
print(result)
