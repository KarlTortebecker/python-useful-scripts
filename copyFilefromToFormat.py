# @Author : Karl Tortebecker
# @Role : This code copies some images from a directory to another one according to some format


import os
import shutil
import re

# Dossier source contenant les images
src_folder = '/chemin/vers/dossier/src'

# Dossier de destination pour les images copiées
dst_folder = "/chemin/vers/dossier/dst"


# Obtenir la liste des fichiers dans le dossier source
files = os.listdir(src_folder)

# Triez les fichiers par ordre alphabétique
files.sort()

# Compteur pour générer la nouvelle syntaxe de nom de fichier
counter = 0

# Copier chaque fichier dans le dossier de destination
for filename in files:
    # Vérifiez si le fichier est un fichier JPG
    if filename.endswith(".jpg"):

        # Générer le nouveau nom de fichier
        new_filename = "image" + str(counter).zfill(2) + ".jpg"

        # Copier le fichier dans le dossier de destination avec le nouveau nom de fichier
        shutil.copy(os.path.join(src_folder, filename), os.path.join(dst_folder, new_filename))

        # Incrémenter le compteur
        counter += 1
