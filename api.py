import requests
from PIL import Image
from io import BytesIO


def GetDomainLogo(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img
