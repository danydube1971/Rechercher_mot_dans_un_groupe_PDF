"""Ce script permet d'afficher dans le terminal, à partir d'un mot ciblé, toutes les occurrences trouvées dans les fichier TXT et PDF 
situés dans le dossier courant. Le script doit être dans le même dossier que les fichiers TXT ou PDF. Vous devez également avoir 
installé la librairie python pdfminer""" 

"""This script is used to display in the terminal, from a targeted word, all the occurrences found in the TXT and PDF files located 
in the current folder. The script must be in the same folder as the TXT or PDF files. You must also have installed the pdfminer python library"""

import os
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

# demander à l'utilisateur de saisir l'occurrence à rechercher
occurrence = input("Entrez l'occurrence à rechercher : ")

# parcourir tous les fichiers dans le dossier courant
for filename in os.listdir():
    # vérifier si le fichier est un fichier PDF
    if filename.endswith(".pdf"):
        pdf_text = convert_pdf_to_txt(filename)
        lines = pdf_text.split("\n")
        for i, line in enumerate(lines):
            if occurrence in line:
                print("{} (ligne {}) : {}".format(filename, i+1, line))
    # vérifier si le fichier est un fichier TXT
    elif filename.endswith(".txt"):
        # ouvrir le fichier TXT
        with open(filename, "r") as txt_file:
            # lire le contenu du fichier TXT
            lines = txt_file.readlines()
            for i, line in enumerate(lines):
                if occurrence in line:
                    print("{} (ligne {}) : {}".format(filename, i+1, line))
