import requests
response=requests.get("https://filesamples.com/samples/audio/mp3/sample3.mp3")
with open("sound.mp3","wb") as file:
    file.write(response.content)