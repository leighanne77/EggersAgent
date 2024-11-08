import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from utils.get_key import get_tool_config 

def search_eggers_quotes(query: str) -> Dict[str, List[str]]:
    """
    Search for real quotes from Dave Eggers' books based on the given query.
    Returns a dictionary with book titles as keys and lists of quotes as values.
    """
    tool_config = get_tool_config()
    url = tool_config['real_quotes']['search_url']
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    quotes = {}
    for quote in soup.find_all('div', class_='quoteText'):
        text = quote.get_text(strip=True).split('―')[0].strip()
        if query.lower() in text.lower():
            book = quote.find('span', class_='authorOrTitle')
            book_title = book.get_text(strip=True) if book else "Unknown Book"
            if book_title not in quotes:
                quotes[book_title] = []
            quotes[book_title].append(text)
    
    return quotes