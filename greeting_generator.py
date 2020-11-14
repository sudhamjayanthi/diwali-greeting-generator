from PIL import Image, ImageDraw
import requests
from io import BytesIO

response = requests.get("https://wallpapercave.com/wp/wp1831958.jpg")
img = Image.open(BytesIO(response.content))


