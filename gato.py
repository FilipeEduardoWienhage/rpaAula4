import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

url = "https://cataas.com/cat"

def baixar_imagem(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    
    except requests.RequestException as e:
        print(f"erro ao acessar a API: {e}")
        return None
    
imagem = baixar_imagem("https://cataas.com/cat")
imagem.save("cat.png")



