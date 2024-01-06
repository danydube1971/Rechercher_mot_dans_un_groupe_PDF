# Rechercher_mots_dans_PDF

Testé dans Linux Mint Mate 21.2

Le script `Rechercher_mots_dans_PDF.py` est un programme Python pour rechercher des mots spécifiques dans des fichiers PDF. 

![Rechercher_mots_dans_PDF](https://github.com/danydube1971/Trouver_mot_dans_un_groupe_PDF/assets/74633244/499a0aab-53fa-49b5-ac43-bf029a3a63e1)

Voici un aperçu basé sur les premières lignes du script :

1. **Importation de Bibliothèques** :
   - `PySimpleGUI` : Pour créer une interface graphique utilisateur (GUI).
   - `os` : Pour interagir avec le système d'exploitation, notamment pour lister les fichiers dans un dossier.
   - `fitz` (alias de `PyMuPDF`) : Utilisé pour lire et manipuler des fichiers PDF.
   - `subprocess` : Pour exécuter des commandes système ou des programmes externes.

2. **Fonctionnalités Principales** :
   - `compter_occurrences(texte, mot)` : Fonction pour compter le nombre d'occurrences d'un mot dans un texte, indépendamment de la casse (majuscules/minuscules).
   - `rechercher_mots_dans_pdf(dossier, mots)` : Fonction pour rechercher un ou deux mots-clés dans tous les fichiers PDF d'un dossier spécifié.

Le script parcoure un dossier spécifié, ouvre chaque fichier PDF, et recherche les occurrences de mots-clés fournis. Les résultats (probablement les occurrences et/ou les emplacements des mots dans les documents) sont collectés.

### Utilisation du Script

**Prérequis** :
1. **Python** : Vous devez avoir Python installé sur votre ordinateur.
2. **Bibliothèques Python** : Assurez-vous d'avoir installé les bibliothèques nécessaires. Vous pouvez les installer via pip :
   - PySimpleGUI : `pip install PySimpleGUI`
   - PyMuPDF : `pip install PyMuPDF`

**Étapes pour Utiliser le Script** :
1. Lancez le script *Rechercher_mots_dans_PDF_GUI_1.0*. 
2. Sélectionnez un dossier contenant les PDF :
   - Le dossier contenant les fichiers PDF à analyser.
   - Un ou deux mots-clés à rechercher.
3. Le script parcourt les fichiers PDF du dossier spécifié et recherche les mots-clés.
4. Les résultats (comme le nombre d'occurrences des mots-clés) sont affichés.



