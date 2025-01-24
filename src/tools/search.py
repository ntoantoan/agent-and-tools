from langchain.tools import BaseTool
from typing import Optional, Type
from serpapi import GoogleSearch
import os

class SearchTool(BaseTool):
    name: str = "search"
    description: str = "Useful for searching information on the internet"
    
    def _run(self, query: str) -> str:
        try:
            search = GoogleSearch({
                "q": query,
                "api_key": os.getenv("SERPAPI_API_KEY")
            })
            results = search.get_dict()
            
            # Extract organic results
            organic_results = results.get("organic_results", [])
            if not organic_results:
                return "No results found"
                
            # Return the first result's snippet
            return organic_results[0].get("snippet", "No snippet available")
            
        except Exception as e:
            return f"Error performing search: {str(e)}"
            
    def _arun(self, query: str):
        raise NotImplementedError("Search tool does not support async")
