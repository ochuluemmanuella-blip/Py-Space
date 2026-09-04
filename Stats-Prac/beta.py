import requests
import json

def total_stars(username):
    response = requests.get(f"https://api.github.com/users/{username}/repos")

    print(f"status code: {response.status_code}")
    user_info = response.json()
    #cleaned = user_info[0]
    totalstars = 0
    for stars in user_info:
        totalstars += stars["stargazers_count"]
    return totalstars
    #print(f"cleaned: {json.dumps(cleaned, indent=2)}")

result = total_stars("raymondproguy")
print(result)