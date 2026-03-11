import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Incarca dataset-ul tips din Seaborn
tips = sns.load_dataset("tips")

# ================================
# 1. Informatii generale despre dataset
# ================================
print("\n=== Cerinta 1: Informatii generale despre dataset ===")
print("Dimensiune (randuri, coloane):", tips.shape)
print("\nTipuri de date ale coloanelor:")
print(tips.dtypes)
print("\nStatistici descriptive:")
print(tips.describe())

# ================================
# 2. Bacsiș mediu per zi si per sex
# ================================
print("\n=== Cerinta 2: Bacsiș mediu per zi si per sex ===")
bacsis_per_day = tips.groupby("day")["tip"].mean()
print("\nBacsis mediu per zi:")
print(bacsis_per_day.round(2))
bacsis_per_sex = tips.groupby("sex")["tip"].mean()
print("\nBacsis mediu per sex:")
print(bacsis_per_sex.round(2))

# ================================
# 3. Coloana noua procent_bacsis
# ================================
print("\n=== Cerinta 3: Coloana noua procent_bacsis ===")
tips_copy = tips.copy()
tips_copy["procent_bacsis"] = tips_copy["tip"] / tips_copy["total_bill"] * 100
print(tips_copy[["total_bill", "tip", "procent_bacsis"]].head())

# ================================
# 4. Cele mai generoase 5 mese
# ================================
print("\n=== Cerinta 4: Cele mai generoase 5 mese ===")
top5 = tips_copy.sort_values(by="procent_bacsis", ascending=False).head(5)
print(top5[["total_bill", "tip", "procent_bacsis", "day", "sex", "smoker"]].round(2))

# ================================
# 5. Numar mese per zi si per fumatori
# ================================
print("\n=== Cerinta 5: Numar mese per zi si per fumatori ===")
mese_per_zi_smoker = tips_copy.groupby(["day", "smoker"]).size().reset_index(name="numar_mese")
print(mese_per_zi_smoker)

# ================================
# 6. Vizualizare grafica
# ================================
sns.set_theme(style='whitegrid', palette='Set2')

fig, axes = plt.subplots(1, 3, figsize=(18,5))
fig.suptitle("Vizualizare bacsișuri - Tips", fontsize=16, fontweight='bold')

# Histogramă bacșiș
sns.histplot(tips_copy['tip'], bins=15, kde=True, ax=axes[0])
axes[0].set_title('Distributia bacsișurilor')
axes[0].set_xlabel('Bacsis ($)')
axes[0].set_ylabel('Numar mese')

# Boxplot bacșiș per zi
sns.boxplot(data=tips_copy, x='day', y='tip', order=['Thur','Fri','Sat','Sun'], ax=axes[1])
axes[1].set_title('Bacsis per zi')
axes[1].set_xlabel('Zi')
axes[1].set_ylabel('Bacsis ($)')

# Barplot bacșiș mediu per zi
bacsis_mediu_per_zi = tips_copy.groupby('day')['tip'].mean().reindex(['Thur','Fri','Sat','Sun'])
sns.barplot(x=bacsis_mediu_per_zi.index, y=bacsis_mediu_per_zi.values, ax=axes[2])
axes[2].set_title('Bacsis mediu per zi')
axes[2].set_xlabel('Zi')
axes[2].set_ylabel('Bacsis mediu ($)')

# Ajustare layout si salvare imagine
plt.tight_layout(rect=[0,0,1,0.95])
plt.savefig('vizualizare_bacsis_tips.png', dpi=150)
plt.show()