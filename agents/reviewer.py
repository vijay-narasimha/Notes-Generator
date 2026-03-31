from typing import List, Dict
from utils.openrouter_client import OpenRouterClient

class ReviewerAgent:
    def __init__(self, client: OpenRouterClient):
        self.client = client

    def review_content(self, content: str) -> str:
        """
        Reviews and refines the generated Markdown content for quality and consistency.
        """
        prompt = f"""
        You are a senior technical editor. Your task is to review and refine the following Markdown content for quality, clarity, and consistency.
        
        Content to Review:
        {content}
        
        Review Checklist:
        1.  **Clarity**: Is the explanation beginner-friendly and easy to understand?
        2.  **Consistency**: Is the tone professional and consistent?
        3.  **Markdown Syntax**: Are the headers, bold text, and code blocks correctly formatted?
        4.  **Mermaid Diagrams**: Are the Mermaid diagrams correctly defined and relevant?
        5.  **Analogies**: Are the analogies helpful and accurate?
        
        Refine the content if necessary to improve its quality. If the content is already excellent, return it as is.
        
        Return ONLY the refined Markdown content.
        """
        
        messages = [{"role": "user", "content": prompt}]
        refined_content = self.client.generate_completion(messages, max_tokens=3000)
        
        if refined_content is None:
            refined_content = content
        
        return refined_content

    def generate_references_section(self, all_source_links: List[str]) -> str:
        """
        Generates a separate references section in Markdown with all source links.
        """
        # Deduplicate and sort links
        unique_links = sorted(list(set(all_source_links)))
        
        references_md = "## References\n\n"
        references_md += "The following sources were used to gather and synthesize information for this documentation:\n\n"
        
        for link in unique_links:
            references_md += f"- [{link}]({link})\n"
            
        return references_md
