import pyperclip as clipboard
import os 
cache=clipboard.paste()
temp="temporal"
# print(f"[{cache} - {temp}]")
while(1):
    cache = str(clipboard.paste())
    if cache != temp:
        temp = str(clipboard.paste())
        print(f"<{cache}> - <{temp}>")
        ext = temp[-4:]
        if ext in ['.png','.jpg','.bmp','jpeg']:
            print("Si es candidato a descargar")
            os.system("wget "+ temp)
            print("Imagen descargada")        

