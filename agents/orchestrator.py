import json
from typing import List, Dict
from utils.openrouter_client import OpenRouterClient

class OrchestratorAgent:
    def __init__(self, client: OpenRouterClient):
        self.client = client

    def plan_subtopics(self, topic: str) -> List[Dict[str, str]]:
        """
        Breaks down the main topic into a logical sequence of subtopics.
        """
        prompt = f"""
        You are an expert technical curriculum designer. Your task is to break down the topic '{topic}' into a logical sequence of subtopics for a comprehensive tutorial, similar to GeeksforGeeks.
        
        The structure should:
        1. Start with basic concepts (Introduction, What is it?, Why use it?).
        2. Progress to intermediate concepts (Syntax, Key Features, Common Use Cases).
        3. End with advanced concepts (Best Practices, Performance, Advanced Patterns).
        
        Return the subtopics as a JSON list of objects, where each object has:
        - 'title': The title of the subtopic.
        - 'description': A brief description of what should be covered in this subtopic.
        
        Example Output:
        [
            {{"title": "Introduction to Python Decorators", "description": "Basic definition and the concept of higher-order functions."}},
            {{"title": "Basic Syntax and Usage", "description": "How to define and apply a simple decorator using the @ symbol."}}
        ]
        
        Return ONLY the JSON list.
        """
        
        messages = [{"role": "user", "content": prompt}]
        response = self.client.generate_completion(messages)
        
        try:
            # Clean response in case of markdown formatting
            clean_response = response.strip()
            if clean_response.startswith("```json"):
                clean_response = clean_response[7:-3].strip()
            elif clean_response.startswith("```"):
                clean_response = clean_response[3:-3].strip()
                
            subtopics = json.loads(clean_response)
            return subtopics
        except Exception as e:
            print(f"Error parsing subtopics: {e}")
            # Fallback if parsing fails
            return [{"title": f"Introduction to {topic}", "description": "Basic overview of the topic."}]
