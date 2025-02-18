import requests

def get_post_tags(post_id):


    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"

    postTags = []

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for post in data["posts"]:
            if post["id"] == post_id:
                return post["tags"]
    else:
        print("Error")

    return postTags


print(get_post_tags(146))