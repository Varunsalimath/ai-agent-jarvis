from duckduckgo_search import DDGS

def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid calculation"

def web_search(query):
    with DDGS() as ddgs:
        results = [r["body"] for r in ddgs.text(query, max_results=3)]
    return results