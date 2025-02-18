import requests

def get_attachment_by_id(attachment_id):

    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"

    postTags = []
    response = requests.get(url)
    if response.status_code == 200:

        data = response.json()

        for post in data["posts"]:

            if "attachments" in post:

                for attachment in post["attachments"]:
                    if attachment["id"] == attachment_id:
                        return attachment["title"]
    else:
        print("Error")




    return None

print(get_attachment_by_id(137))