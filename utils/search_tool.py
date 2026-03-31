from ddgs import DDGS
import time

class SearchTool:
    def __init__(self):
        self.ddgs = DDGS()

    def search(self, query, max_results=5):
        """
        Perform a search and return a list of results with title, link, and snippet.
        """
        results = []
        try:
            time.sleep(1)
            search_results = self.ddgs.text(query, max_results=max_results)
            for r in search_results:
                results.append({
                    "title": r.get("title"),
                    "link": r.get("href"),
                    "snippet": r.get("body")
                })
        except Exception as e:
            print(f"Error performing search for query '{query}': {e}")
        return results

    def search_youtube(self, query, max_results=3):
        """
        Specifically search for YouTube videos related to the topic.
        """
        return self.search(f"site:youtube.com {query}", max_results=max_results)

    def search_geeksforgeeks(self, query, max_results=3):
        """
        Specifically search for GeeksforGeeks articles related to the topic.
        """
        return self.search(f"site:geeksforgeeks.org {query}", max_results=max_results)

    def search_official_docs(self, query, topic, max_results=3):
        """
        Specifically search for official documentation related to the topic.
        """
        return self.search(f"official documentation {topic} {query}", max_results=max_results)
