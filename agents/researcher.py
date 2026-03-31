from typing import List, Dict
from utils.search_tool import SearchTool

class ResearcherAgent:
    def __init__(self, search_tool: SearchTool):
        self.search_tool = search_tool

    def research_subtopic(self, topic: str, subtopic: Dict[str, str]) -> Dict[str, any]:
        """
        Gathers information for a specific subtopic from multiple sources.
        """
        subtopic_title = subtopic.get("title")
        subtopic_desc = subtopic.get("description")
        
        print(f"Researching subtopic: {subtopic_title}...")
        
        # Perform targeted searches
        official_results = self.search_tool.search_official_docs(subtopic_title, topic)
        gfg_results = self.search_tool.search_geeksforgeeks(subtopic_title)
        youtube_results = self.search_tool.search_youtube(subtopic_title)
        
        # Combine all search results
        all_results = official_results + gfg_results + youtube_results
        source_links = [r.get("link") for r in all_results if r.get("link")]
        research_data = {
            "subtopic": subtopic_title,
            "description": subtopic_desc,
            "search_results": all_results,
            "source_links": list(set(source_links))
        }
        
        return research_data
