# import requests
# import json


import requests
import json

# print("this is feature-cache branch")

def fetch_data(*, use_cache : bool = False, json_cache : str, URL : str):
    if not use_cache:
        json_data = None
    else:
        try:
            with open(json_cache, "r") as json_file:
                json_data = json.load(json_file)
                print(f"Fetched data from local cache...")    
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"No local cache found... {e}")
            json_data = None    
    if not json_data:
        print("Fetching new data...(Creating local cache)")
        json_data = requests.get(URL).json()
        with open(json_cache, "w") as json_file:
            json.dump(json_data, json_file)              
    return json_data

if __name__ == "__main__":
    URL = "https://dummyjson.com/comments"
    json_cache = "comments.json"
    data: dict = fetch_data(use_cache=True, json_cache=json_cache, URL=URL)
    print(f"Data is fetched successfully !!!")
    # print(data)
