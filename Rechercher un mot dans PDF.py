# Installer le module PyMuPDF avec la commande pip3 install PyMuPDF
# Installer le module frontend avec la commande pip3 install frontend

"""Ce script recherche un mot ciblé dans tous les fichiers PDF du dossier courant en utilisant la bibliothèque fitz. 
Pour chaque occurrence du mot ciblé, le script affiche le nom du fichier PDF, le numéro de page et un extrait de texte autour du mot ciblé."""

import os
import fitz

target_word = input("Entrez le mot ciblé : ")
current_directory = os.getcwd()

for filename in os.listdir(current_directory):
    if filename.endswith('.pdf'):
        with fitz.open(os.path.join(current_directory, filename)) as pdf_file:
            for page_num, page in enumerate(pdf_file):
                page_text = page.get_text()
                if target_word in page_text:
                    start_index = page_text.find(target_word)
                    end_index = start_index + len(target_word)
                    excerpt_start = max(start_index - 50, 0)
                    excerpt_end = min(end_index + 50, len(page_text))
                    excerpt = page_text[excerpt_start:excerpt_end]
                    print(f"Le mot ciblé '{target_word}' a été trouvé dans le fichier PDF \033[1m'{filename}'\033[0m à la page {page_num+1} : '{excerpt}'")

