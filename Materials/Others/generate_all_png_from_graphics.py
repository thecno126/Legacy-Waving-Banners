import os
import shutil

# Dossier source (graphics) et destination (all_png)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
graphics_dir = os.path.abspath(os.path.join(SCRIPT_DIR, '../../graphics'))
dest_dir = os.path.abspath(os.path.join(SCRIPT_DIR, '../../Releases/Backup/all_png'))

# Blacklist (noms sans extension, tout en minuscules)
blacklist = {
    'hegemony',
    'persean_league',
    'luddic_church',
    'luddic_path',
    'pirates',
    'neutral_traders',
    'tritachyon',
    'sindrian_diktat',
}

# Crée le dossier de destination s'il n'existe pas
os.makedirs(dest_dir, exist_ok=True)

# Parcours récursif de graphics/
count = 0
for root, dirs, files in os.walk(graphics_dir):
    for file in files:
        if file.lower().endswith('.png'):
            name_no_ext = os.path.splitext(file)[0].lower()
            # Exclure si dans la blacklist (insensible à la casse) ou si "crest" dans le nom du fichier
            if name_no_ext not in blacklist and 'crest' not in file.lower():
                src_path = os.path.join(root, file)
                dest_path = os.path.join(dest_dir, file)
                shutil.copy2(src_path, dest_path)
                count += 1
print(f'{count} fichiers PNG copiés dans all_png.')
