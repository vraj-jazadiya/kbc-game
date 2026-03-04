import requests

def get_ques(limit=3,difficulty="easy"):
    
    res = requests.get(f"https://the-trivia-api.com/v2/questions?limit={limit}&difficulty={difficulty}")
    
    if res.status_code == 200:
        return res.json()
    
    print("Failed to fetch questions")
    return []