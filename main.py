import os
import argparse
from typing import List, Dict
from dotenv import load_dotenv
from tqdm import tqdm

from utils.openrouter_client import OpenRouterClient
from utils.search_tool import SearchTool
from utils.file_manager import FileManager
from agents.orchestrator import OrchestratorAgent
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent

load_dotenv()

class DocumentationSystem:
    def __init__(self, topic: str, model="gpt-4.1-mini"):
        self.topic = topic
        self.client = OpenRouterClient(model=model)
        self.search_tool = SearchTool()
        self.file_manager = FileManager(base_dir="docs", topic=topic)
        self.orchestrator = OrchestratorAgent(self.client)
        self.researcher = ResearcherAgent(self.search_tool)
        self.writer = WriterAgent(self.client)
        self.reviewer = ReviewerAgent(self.client)

    def run(self, topic: str):
        """
        Runs the full documentation generation pipeline for a given topic.
        """
        print(f"\n🚀 Starting documentation generation for: {topic}\n")
        print("📋 Planning subtopics...")
        subtopics = self.orchestrator.plan_subtopics(topic)
        print(f"Found {len(subtopics)} subtopics to cover.\n")
        
        all_source_links = []
        filenames = []
        for subtopic in tqdm(subtopics, desc="Generating Subtopics"):
            research_data = self.researcher.research_subtopic(topic, subtopic)
            all_source_links.extend(research_data.get("source_links", []))
            content = self.writer.write_subtopic_content(research_data)
            refined_content = self.reviewer.review_content(content)
            filename = self.file_manager.save_subtopic(subtopic.get("title"), refined_content)
            filenames.append(filename)
        print("\n📝 Finalizing documentation...")
        index_file = self.file_manager.generate_index_page(topic, subtopics, filenames)
        references_content = self.reviewer.generate_references_section(all_source_links)
        references_file = self.file_manager.save_references(references_content)
        
        print(f"\n✅ Documentation complete!")
        print(f"Topic Folder: docs/{self.topic}")
        print(f"README: docs/{self.topic}/README.md")
        print(f"References: docs/{self.topic}/references.md\n")

def main():
    parser = argparse.ArgumentParser(description="Multi-Agent Documentation Generator")
    parser.add_argument("topic", type=str, help="The topic to generate documentation for")
    parser.add_argument("--model", type=str, default="gpt-4.1-mini", help="OpenRouter model to use")
    
    args = parser.parse_args()
    system = DocumentationSystem(topic=args.topic, model=args.model)
    system.run(args.topic)

if __name__ == "__main__":
    main()
