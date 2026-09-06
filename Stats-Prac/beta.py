import requests
import json
#import Counter

def total_stars(username):
    response = requests.get(f"https://api.github.com/users/{username}/repos")
    resp = requests.get(f"https://api.github.com/users/{username}")
    print(f"status code: {response.status_code}")
    user_info = response.json()
    
    print(f"status code: {resp.status_code}")
    user_info2 =resp.json()

    #logs = user_info2['login']
    followers = user_info2['followers']
    #print(f"followers: {followers}")
    #cleaned = user_info[0]
    totalstars = 0
    for stars in user_info:
        totalstars += stars["stargazers_count"]
    return totalstars, followers

    #print(f"cleaned: {json.dumps(cleaned, indent=2)}")

stars, followers = total_stars("maddox-bayn")
print(f"stars: {stars}")
print(f"followers: {followers}")
"""
def top_lang(username):
        answ = requests.get(f"https://api.github.com/users/{username}/repos")
        print(f"status code: {answ.status_code}")
        user_data = answ.json()

        repo = user_data["repos"] #here i'm classifying the whole repos and i need to find a way to loop through the repos and pick the languages out before starting the tally
        for lang in repo:
            
"""
