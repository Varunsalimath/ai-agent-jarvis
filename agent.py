from langchain.agents import initialize_agent, Tool, AgentType
from langchain_community.llms import Ollama
from tools import calculator, web_search

# Load local model
llm = Ollama(model="llama3")

tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="useful for math calculations"
    ),
    Tool(
        name="WebSearch",
        func=web_search,
        description="search the internet"
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def ask_agent(question):
    response = agent.invoke({"input": question})
    return response["output"]