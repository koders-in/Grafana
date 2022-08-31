import requests


def check():
    CAT_API_KEY = 'c7523607ed9cb408ab106017be05b30c8796e8e8'

    headers = {
        "X-Redmine-API-Key": CAT_API_KEY
    }

    temp = requests.get(
        "http://localhost:8080/operations.json?page=1.json",
        headers=headers)
    tempContent = temp.json()
    count = 0
    for check1, check2 in tempContent.items():
        if check1 == "total_count":
            count = check2

    pages = int(count / 25)
    leftPages = int(count % 25)
    if leftPages > 0:
        pages = pages + 1
    url = []
    for i in range(pages):
        url.append("http://localhost:8080/operations.json?page=" + str(i + 1) + ".json")

    # ans = []
    res = []
    for i in range(pages):
        response = requests.get(
            url[i],
            headers=headers)
        jsonContent = response.json()
        # ans.append(func(jsonContent))
        res.append(jsonContent)
    return {'val': res}


# check()
