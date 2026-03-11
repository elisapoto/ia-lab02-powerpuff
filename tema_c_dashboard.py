"""
Laborator #02 - Inteligență Artificială
Cerința C: Grafice de bază cu Matplotlib (Subploturi)
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1. Încărcare date
try:
    data = sns.load_dataset('iris')
except Exception as e:
    print(f"Eroare la încărcarea datelor: {e}")
    # Fallback în caz că nu ai internet pentru load_dataset
    exit()

# 2. Creare figură conform arhitecturii Figure/Axes (Lab 2.3)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Analiza Dataset Iris - Cerința C', fontsize=14)

# --- Subplot 1: Scatter Plot (Relația lungime/lățime) ---
ax[0].scatter(data['sepal_length'], data['sepal_width'], color='purple', alpha=0.7)
ax[0].set_title('Lungime vs Lățime Sepală')
ax[0].set_xlabel('Lungime Sepală (cm)')
ax[0].set_ylabel('Lățime Sepală (cm)')
ax[0].grid(True, linestyle=':', alpha=0.6)

# --- Subplot 2: Bar Plot (Distribuția speciilor) ---
species_count = data['species'].value_counts()
ax[1].bar(species_count.index, species_count.values, color=['#ff9999','#66b3ff','#99ff99'])
ax[1].set_title('Număr de mostre per Specie')
ax[1].set_xlabel('Specie')
ax[1].set_ylabel('Count')

# Ajustare automată pentru a nu se suprapune elementele
plt.tight_layout()

# Afișare
print("Se generează graficele... (dacă e prima rulare, poate dura câteva secunde)")
plt.show()