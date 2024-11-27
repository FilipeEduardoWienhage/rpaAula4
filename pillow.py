from PIL import Image, ImageFilter

# Abrir uma imagem
img = Image.open('imagem.jpeg')
# Redimensionar a imagem para 400x200
img_resized = img.resize((400, 200))
# salvar a image
img_resized.save('imagem_redimensionada.jpeg')
# Mostrar a imagem 
img_resized.show()

# aplicar o filtro de desfoque
img_blur = img.filter(ImageFilter.BLUR)
# salvar a imagem
img_blur.save('imagem_desfocada.jpeg')
# mostrar a imagem
img_blur.show()
# converte o tipo da imagem
img.convert('RGB').save('imagem.png', 'png')
img.show()
