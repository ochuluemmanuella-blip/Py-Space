import requests

response = requests.get('https://api.github.com/users/raymondproguy')

print(f"status code: {response.status_code}")
user_info =response.json()

logs = user_info['login']
followers = user_info['followers']
public_repos = user_info['public_repos']
bio = user_info['bio']

print(f"login: {logs}")
print(f"followers: {followers}")
print(f"public repos: {public_repos}")
print(f"bio: {bio}")