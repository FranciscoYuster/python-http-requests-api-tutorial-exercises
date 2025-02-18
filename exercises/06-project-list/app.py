import requests

# Your code here

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")


if response.status_code == 200:
    Data = response.json()

    second = Data[1]["name"]

    print(second)
else:
   print("Failed to fetch current time.")
    