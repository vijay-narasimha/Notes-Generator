from typing import Dict, List
from utils.openrouter_client import OpenRouterClient

class WriterAgent:
    def __init__(self, client: OpenRouterClient):
        self.client = client

    def write_subtopic_content(self, research_data: Dict[str, any]) -> str:
        """
        Transforms research data into beginner-friendly Markdown content.
        """
        subtopic = research_data.get("subtopic")
        description = research_data.get("description")
        search_results = research_data.get("search_results")
        search_context = "\n".join([f"- {r.get('title')}: {r.get('snippet')}" for r in search_results])
        
        prompt = f"""
        You are a technical writer for a platform like GeeksforGeeks. Your task is to write a comprehensive, beginner-friendly Markdown guide for the subtopic: '{subtopic}'.
        
        Context: {description}
        
        Search Results Context:
        {search_context}
        
        The content MUST include:
        1.  **Clear and in-depth conceptual explanations**: Explain the 'what' and 'why' in simple terms.
        2.  **Real-world analogies**: Use analogies to simplify complex concepts.
        3.  **Python code examples**: Provide clear, well-commented Python code snippets where applicable.
        4.  **Mermaid diagrams**: Include at least one Mermaid diagram (e.g., flowchart, sequence diagram) to visually represent the concept.
        
        Formatting Guidelines:
        - Use proper Markdown headers (e.g., ## for the subtopic title).
        - Use **bold** for key terms.
        - Ensure the tone is professional yet accessible.
        - Do NOT include a references section here; it will be handled separately.
        
        Return ONLY the Markdown content.
        """
        
        messages = [{"role": "user", "content": prompt}]
        content = self.client.generate_completion(messages, max_tokens=3000)
        
        if content is None:
            content = f"## {subtopic}\n\n{description}\n\nContent generation failed. Please check your API key and try again."
        
        return content
