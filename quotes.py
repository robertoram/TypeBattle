import json
import requests
import re
from game.config import *

# Fallback word list in case of API failure
FALLBACK_WORD_LIST = [
    "algorithm", "library", "computer", "debugging",
    "structure", "function", "hardware", "variable"
]
def clean_word(word):
    """Removes punctuation and special characters from a word."""
    return re.sub(r'[^\w\s]', '', word)  # Removes everything except letters and numbers

def get_quote_as_list(min_length=WORD_LIST_LENGHT ):
    """Fetches a random quote with a minimum length and returns it as a list of words.
    If the request fails, it returns a fallback list.
    """
    url = f"https://api.quotable.io/random?minLength={min_length}"

    try:
        response = requests.get(url, timeout=5, verify=False)
        response.raise_for_status()  # Raises an error for non-200 status codes

        data = response.json()
        quote = data.get("content", "").strip()

        if not quote:  # If the API response is empty
            raise ValueError("Received an empty quote from API")
        
        words = quote.split() 
        clean_words = [clean_word(word) for word in words if clean_word(word)]  # Removes empty words
        
        return clean_words
    except (requests.RequestException, json.JSONDecodeError, ValueError) as e:
        print(f"❌ Error fetching quote: {e}")
        return FALLBACK_WORD_LIST  # Returns the fallback list if an error occurs

# Example usage
if __name__ == "__main__":
    print(get_quote_as_list())  # Fetches and prints a random quote as a list of words
