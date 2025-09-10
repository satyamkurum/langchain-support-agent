from langchain.agents import initialize_agent, AgentType
from .llm import get_llm
from .memory import get_memory
from .tools import get_tools

def get_agent():
    llm = get_llm()
    memory = get_memory()
    tools = get_tools()

    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True
    )
