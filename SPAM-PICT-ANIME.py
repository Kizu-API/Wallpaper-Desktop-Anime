import requests, shutil, json, os , urllib.request, random


def downloadcuk():
    url = "https://www.nekos.life/api/v2/img/wallpaper"
    response = requests.get(url).text
    responsess = json.loads(response)
    responsesss = responsess["url"]
    name=random.randrange(1,10000000000)
    filename=str(name)+".jpg"
    img_data = requests.get(responsesss).content
    with open(filename, 'wb') as handler:
        haha = handler.write(img_data)
    return haha
  
while True:
    downloadcuk()