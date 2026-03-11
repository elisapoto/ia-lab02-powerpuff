import numpy as np

np.random.seed(42)





A = np.random.randint(1, 11, size=(4, 3))

B = np.random.randint(1, 11, size=(3, 5))

print("=" * 50)

print("Matricea A (4x3):")

print(A)

print("\nMatricea B (3x5):")

print(B)


C = A @ B

print("\n" + "=" * 50)

print("Produsul matriceal C = A @ B (4x5):")

print(C)


print("\n" + "=" * 50)

print("Statistici pe matricea C:")

suma_totala = np.sum(C)

print(f"  Suma tuturor elementelor din C: {suma_totala}")

media_pe_coloane = np.mean(C, axis=0)

print(f"  Media pe fiecare coloana (axis=0): {media_pe_coloane}")

valoarea_maxima = np.max(C)

print(f"  Valoarea maxima globala din C: {valoarea_maxima}")




print("\n" + "=" * 50)

print("BONUS - Matrice patratica M (3x3):")

M = np.random.randint(1, 11, size=(3, 3)).astype(float)

print("Matricea M:")

print(M)

det_M = np.linalg.det(M)

print(f"\nDeterminantul lui M: {det_M:.4f}")

if abs(det_M) > 1e-10:

    M_inv = np.linalg.inv(M)

    print("\nInversa lui M:")

    print(M_inv)

    produs = M @ M_inv

    print("\nM @ inv(M) (ar trebui sa fie aproape de matricea identitate):")

    print(produs)

    este_identitate = np.allclose(produs, np.eye(3))

    print(f"\nM @ inv(M) este aproape de matricea identitate? {este_identitate}")

else:

    print("Matricea M este singulara (det = 0), nu se poate calcula inversa.")