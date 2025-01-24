import os
from dotenv import load_dotenv
from agent import AgentBuilder
from tools.calculator import CalculatorTool
from tools.search import SearchTool
from tools.weather import WeatherTool

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize tools
    tools = [
        CalculatorTool(),
        SearchTool(),
        WeatherTool()
    ]
    
    # Build agent
    agent_builder = AgentBuilder(tools)
    agent = agent_builder.build()
    
    # Interactive chat loop
    print("Chat with the agent (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
            
        try:
            response = agent.run(user_input)
            print(f"Agent: {response}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
