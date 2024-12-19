import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": "4b5680c002mshcae545fe965cd0bp1e33e8jsn60213cecb02b"  # Replace with your RapidAPI key
    }
response = requests.get(url, headers=headers)
print(response.json())
  
