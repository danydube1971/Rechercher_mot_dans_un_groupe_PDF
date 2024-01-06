import PySimpleGUI as sg
import os
import fitz  # PyMuPDF
import subprocess

def compter_occurrences(texte, mot):
    return texte.lower().count(mot.lower())

def rechercher_mots_dans_pdf(dossier, mots):
    if not 1 <= len(mots) <= 2:
        raise ValueError("Un ou deux mots-clés doivent être fournis")

    resultats = []
    for filename in os.listdir(dossier):
        if filename.endswith('.pdf'):
            with fitz.open(os.path.join(dossier, filename)) as pdf_file:
                pdf_text = ''
                for page in pdf_file:
                    pdf_text += page.get_text()
                occurrences = [compter_occurrences(pdf_text, mot) for mot in mots]
                if all(occ > 0 for occ in occurrences):
                    resultats.append((filename, occurrences))
                    if len(resultats) == 50:
                        break

    return resultats

def open_pdf_file(path):
    try:
        subprocess.Popen(['xdg-open', path])
    except Exception as e:
        screen_size = sg.Window.get_screen_size()
        error_window_size = (300, 100)  # Estimate
        error_window_location = ((screen_size[0] - error_window_size[0]) // 2, 
                                 (screen_size[1] - error_window_size[1]) // 2)
        sg.popup_error(f"Erreur lors de l'ouverture du fichier: {e}", location=error_window_location)

# Création de l'interface graphique
layout = [
    [sg.Button('Effacer les mots-clés', key='-CLEAR-')],
    [sg.Text('Sélectionnez le dossier contenant les PDF :')],
    [sg.InputText(), sg.FolderBrowse(key='-FOLDER-')],
    [sg.Text('Entrez le mot clé (ou deux mots clés séparés par un espace) :')],
    [sg.InputText(key='-KEYWORD-')],
    [sg.Button('Rechercher'), sg.Button('Quitter')],
    [sg.Text('Résultats de la recherche :')],
    [sg.Listbox(values=[], enable_events=True, size=(120, 20), key='-LISTBOX-', auto_size_text=True)]
]

window = sg.Window('Recherche de mots dans les fichiers PDF', layout, resizable=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quitter':
        break
    if event == '-CLEAR-':
        window['-LISTBOX-'].update(values=[])
        window['-KEYWORD-'].update('')
    if event == 'Rechercher':
        try:
            dossier = values['-FOLDER-']
            mots = values['-KEYWORD-'].split()
            resultats = rechercher_mots_dans_pdf(dossier, mots)
            # Trier les résultats par nombre d'occurrences décroissantes
            resultats_tries = sorted(resultats, key=lambda x: sum(x[1]), reverse=True)
            resultats_affichage = [f"{nom_fichier} - Occurrences: {sum(occ)}" for nom_fichier, occ in resultats_tries]
            window['-LISTBOX-'].update(values=resultats_affichage)
        except ValueError as e:
            sg.popup_error(str(e))
    if event == '-LISTBOX-':  # Gestion des événements pour les résultats cliquables
        selected_file = values['-LISTBOX-'][0].split(' - ')[0]
        if selected_file:
            full_path = os.path.join(dossier, selected_file)
            open_pdf_file(full_path)

window.close()

