import requests

def get_titles():

    
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"

    titles = []

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for post in data["posts"]:
            title = post["title"]
            if title:
                titles.append(title)
    else:
        print("Error")

    return titles


print(get_titles())