# Trouver_mot_dans_PDF

Permet de trouver et d'afficher un mot ciblé contenu dans le ou les PDF (ou TXT) dans le même dossier que le script
Ce script permet de rechercher une occurrence de texte dans tous les fichiers PDF et TXT du répertoire courant. 
Voici les étapes effectuées par le script :

1. Importation des modules os, StringIO, PDFResourceManager, PDFPageInterpreter, TextConverter, LAParams et PDFPage.
2. Définition d'une fonction "convert_pdf_to_txt" qui prend un chemin de fichier en entrée, lit le contenu du fichier PDF et renvoie le texte extrait.
3. Demande à l'utilisateur d'entrer l'occurrence de texte à rechercher.
4. Parcours de tous les fichiers du répertoire courant à l'aide de la fonction os.listdir().
5. Vérification si le fichier est un fichier PDF en vérifiant si le nom de fichier se termine par ".pdf". 
Si c'est le cas, le contenu du fichier PDF est converti en texte à l'aide de la fonction "convert_pdf_to_txt" définie précédemment.
6. Séparation du texte en lignes et itération à travers chaque ligne pour trouver l'occurrence de texte saisie par l'utilisateur. 
Si l'occurrence de texte est trouvée, le nom de fichier, le numéro de ligne et la ligne elle-même sont imprimés à l'écran.
7. Vérification si le fichier est un fichier TXT en vérifiant si le nom de fichier se termine par ".txt". 
Si c'est le cas, le contenu du fichier TXT est lu et chaque ligne est itérée pour trouver l'occurrence de texte saisie par l'utilisateur. 
Si l'occurrence de texte est trouvée, le nom de fichier, le numéro de ligne et la ligne elle-même sont imprimés à l'écran.
