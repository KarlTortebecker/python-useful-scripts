# @Author : Karl Tortebecker
# @Use : This code download some images from a list of urls (of the images) in the file "image_urls.txt"

import requests
import os

# Définir le nom du dossier où stocker les images
output_folder = "Scrapped_images"

# Vérifier si le dossier de sortie existe, sinon le créer
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Ouvrir le fichier image_urls.txt et lire les URL
with open("image_urls.txt", "r") as f:
    image_urls = f.read().splitlines()

# Télécharger les images et les enregistrer dans le dossier de sortie
for i, url in enumerate(image_urls):
    response = requests.get(url)
    img_data = response.content
    # Extraire le nom de fichier à partir de l'URL
    filename = os.path.join(output_folder, f"image{i}.jpg")
    # Écrire les données de l'image dans le fichier
    with open(filename, "wb") as f:
        f.write(img_data)
    print(f"Téléchargé {filename}")
