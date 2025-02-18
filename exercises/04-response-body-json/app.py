import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")

if response.status_code == 200:
    timeData = response.json()

    hours = timeData["hours"]
    minutes = timeData["minutes"]
    seconds = timeData["seconds"]

    print(f"Current time: { hours } hrs { minutes } min and { seconds } sec")
else:
   print("Failed to fetch current time.")
    
