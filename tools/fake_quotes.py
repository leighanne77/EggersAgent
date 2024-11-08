import random
from typing import Dict, List
from utils.get_key import get_fake_quote_config

def generate_fake_title():
    adjectives = ["Circular", "Transparent", "Digital", "Holographic", "Quantum", "Neon", "Paradoxical"]
    nouns = ["Sphere", "Labyrinth", "Utopia", "Dystopia", "Algorithm", "Paradigm", "Conundrum"]
    return f"The {random.choice(adjectives)} {random.choice(nouns)}"

def generate_fake_year():
    config = get_fake_quote_config()
    return random.randint(config['min_year'], config['max_year'])

def generate_fake_eggers_quotes(theme: str) -> Dict[str, List[str]]:
    """
    Generate fake quotes for an imaginary Dave Eggers book based on the given theme.
    Returns a dictionary with a fake book title as the key and a list containing one fake quote as the value.
    """
    fake_title = generate_fake_title()
    fake_year = generate_fake_year()
    
    fake_quotes = [
        f"In a world where {theme} rules, we must remember that humanity is our greatest asset.",
        f"The irony of {theme} is that it both connects and isolates us simultaneously.",
        f"We've created a society obsessed with {theme}, but at what cost to our souls?",
        f"The beauty of {theme} lies not in its perfection, but in its imperfections.",
        f"In the age of {theme}, authenticity becomes our most valuable currency."
    ]
    
    chosen_quote = random.choice(fake_quotes)
    return {f"{fake_title} ({fake_year}) [FAKE]": [chosen_quote]}