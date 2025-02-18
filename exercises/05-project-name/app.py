import requests

# Your code here


response = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")

if response.status_code == 200:
    Data = response.json()

    name = Data["name"]

    print(name)
else:
   print("Failed to fetch current time.")
    
