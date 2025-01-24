from langchain.tools import BaseTool
from typing import Optional, Type
import math

class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Useful for performing mathematical calculations"
    
    def _run(self, query: str) -> str:
        try:
            # Create a safe dictionary of allowed mathematical functions
            safe_dict = {
                'abs': abs,
                'round': round,
                'min': min,
                'max': max,
                'pow': pow,
                'math': math
            }
            
            # Evaluate the expression using the safe dictionary
            result = eval(query, {"__builtins__": {}}, safe_dict)
            return f"Result: {result}"
        except Exception as e:
            return f"Error: {str(e)}"
            
    def _arun(self, query: str):
        raise NotImplementedError("Calculator tool does not support async")
