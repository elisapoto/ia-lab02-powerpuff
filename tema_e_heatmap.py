import seaborn as sns
import matplotlib.pyplot as plt

# Încărcăm datele
iris = sns.load_dataset('iris')

# Calculăm corelația (doar pentru coloanele numerice)
corr_matrix = iris.drop(columns='species').corr()

# Desenăm heatmap-ul
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matricea de Corelație (Seaborn Heatmap)')
plt.show()