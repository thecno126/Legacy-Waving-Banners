import os
import sys
from PIL import Image

# --- CONFIGURATION PAR DÉFAUT ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SUBDIR = 'all_png'
DEFAULT_PATH = os.path.abspath(os.path.join(SCRIPT_DIR, f'../../Releases/Backup/{DEFAULT_SUBDIR}'))

# --- INTERACTION TERMINAL ---
print("--- Générateur de Planche de Drapeaux ---")
user_input = input(f"Appuyez sur [ENTRÉE] pour le dossier par défaut ({DEFAULT_SUBDIR})\nou collez le CHEMIN complet du dossier source : ").strip()

if user_input == "":
    png_dir = DEFAULT_PATH
    source_name = DEFAULT_SUBDIR
else:
    # Nettoyage des guillemets
    png_dir = user_input.replace('"', '').replace("'", "")
    source_name = os.path.basename(os.path.normpath(png_dir))

# --- NETTOYAGE DU NOM DE SORTIE ---
# Si le dossier s'appelle 'all_png', on enlève le '_png' ou '.png' pour le nom final
clean_name = source_name.replace('_png', '').replace('.png', '')
out_path = os.path.abspath(os.path.join(SCRIPT_DIR, f'../Display/display_{clean_name}.png'))

# --- PARAMÈTRES GRAPHIQUES ---
cols = 5
TEMPLATE_WIDTH = 1353
margin_x, margin_y = 30, 30
space_x, space_y = 30, 30

blacklist = {
    'hegemony', 'hegemony_alt', 'persean_league', 'luddic_church',
    'luddic_path', 'pirates', 'neutral_traders', 'tritachyon', 'sindrian_diktat',
}

# --- TRAITEMENT ---
if not os.path.exists(png_dir):
    print(f"❌ Erreur : Le dossier '{png_dir}' est introuvable.")
    sys.exit(1)

all_pngs = sorted([
    f for f in os.listdir(png_dir)
    if (f.lower().endswith('.png') 
        and os.path.splitext(f)[0].lower() not in blacklist 
        and 'crest' not in f.lower())
])

nb_flags = len(all_pngs)
if nb_flags == 0:
    print(f"⚠️ Aucun drapeau valide trouvé dans : {png_dir}")
    sys.exit(0)

rows = (nb_flags + cols - 1) // cols
flag_w = (TEMPLATE_WIDTH - (2 * margin_x) - (cols - 1) * space_x) // cols
flag_h = int(flag_w * 0.6)
total_h = (2 * margin_y) + (rows * flag_h) + ((rows - 1) * space_y)

out = Image.new('RGBA', (TEMPLATE_WIDTH, total_h), (0, 0, 0, 0))

print(f"🚀 Traitement de {nb_flags} images depuis '{source_name}'...")

for idx, fname in enumerate(all_pngs):
    try:
        with Image.open(os.path.join(png_dir, fname)).convert('RGBA') as img:
            img = img.resize((int(flag_w), int(flag_h)), Image.Resampling.LANCZOS)
            col = idx % cols
            row = idx // cols
            x = margin_x + col * (flag_w + space_x)
            y = margin_y + row * (flag_h + space_y)
            out.paste(img, (int(x), int(y)), img)
    except Exception as e:
        print(f"Impossible de traiter {fname}: {e}")

os.makedirs(os.path.dirname(out_path), exist_ok=True)
out.save(out_path)

print("-" * 40)
print(f"✅ Terminé ! Grille de {cols}x{rows}")
print(f"🖼️ Sortie : display_{clean_name}.png")
print("-" * 40)