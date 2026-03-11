import seaborn as sns

import matplotlib.pyplot as plt

# Incarcam dataset-ul Iris

df = sns.load_dataset("iris")



# 1. Pairplot complet cu hue='species' si diag_kind='kde'


pairplot_fig = sns.pairplot(df, hue="species", diag_kind="kde", palette="Set2")

pairplot_fig.figure.suptitle("Pairplot - Dataset Iris (dupa Species)", y=1.02, fontsize=15, fontweight="bold")

plt.savefig("iris_pairplot.png", dpi=150, bbox_inches="tight")

print("Pairplot salvat ca 'iris_pairplot.png'")

plt.show()


# 2. Figura separata cu 4 subploturi (1x4) - Violinplot

#    pentru fiecare variabila numerica


variables = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

fig, axes = plt.subplots(1, 4, figsize=(18, 6))

fig.suptitle("Violinplot - Distributia Variabilelor Iris pe Species",

             fontsize=14, fontweight="bold")

for ax, var in zip(axes, variables):

    sns.violinplot(data=df, x="species", y=var,

                   hue="species", split=False,

                   palette="Set2", ax=ax, legend=False)

    ax.set_title(var.replace("_", " ").title())

    ax.set_xlabel("Species")

    ax.set_ylabel(var.replace("_", " ").title())

plt.tight_layout()

plt.savefig("iris_violinplots.png", dpi=150, bbox_inches="tight")

print("Violinplots salvate ca 'iris_violinplots.png'")

plt.show()