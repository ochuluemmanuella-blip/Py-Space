import os
def get_api_key():
    Api = os.environ.get("API_KEY")

    if Api == "" or Api is None:
        raise KeyError("API_KEY is missing")
    return Api  
print(get_api_key())