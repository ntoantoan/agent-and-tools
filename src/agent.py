from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

class AgentBuilder:
    def __init__(self, tools, temperature=0):
        self.llm = ChatOpenAI(temperature=temperature)
        self.tools = tools
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        
    def build(self):
        return initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            memory=self.memory,
            verbose=True
        )
