import requests

# Your code here
response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

if response.status_code == 200:
    data = response.json()
    
    first_post = data["posts"][0]
        
    author_dict = first_post["author"]
        
    author_name = author_dict["name"]
        
    print(author_name)
else:
    print("Failed to fetch data from the endpoint.")