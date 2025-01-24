from langchain.tools import BaseTool
from typing import Optional, Type
import python_weather
import asyncio

class WeatherTool(BaseTool):
    name = "weather"
    description = "Useful for getting weather information for a specific location"
    
    def _run(self, location: str) -> str:
        return asyncio.run(self._get_weather(location))
            
    async def _get_weather(self, location: str) -> str:
        try:
            async with python_weather.Client() as client:
                weather = await client.get(location)
                current = weather.current
                return f"Current weather in {location}: {current.temperature}°C, {current.description}"
        except Exception as e:
            return f"Error getting weather: {str(e)}"
            
    def _arun(self, location: str):
        raise NotImplementedError("Weather tool does not support async")
