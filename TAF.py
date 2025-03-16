import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Parameter
h = 5  # um, ketebalan teras
lambda0 = 1.0  # um, panjang gelombang vakum
nf = 1.5  # indeks bias teras/film
nc = 1.4  # indeks bias cladding
ns = 1.45  # indeks bias substrat
k0 = 2 * np.pi / lambda0 # bilangan gelombang vakum
nfck = (nf**2 - nc**2) * k0**2
nfsk = (nf**2 - ns**2) * k0**2
kmax = min(np.sqrt(nfck), np.sqrt(nfsk))

# Definisikan fungsi
def f1(x):
    return np.tan(x * h)

def f2(x):
    gc = np.sqrt(nfck - x**2)
    gs = np.sqrt(nfsk - x**2)
    nfns = nf**2 / ns**2
    nfnc = nf**2 / nc**2
    return x * (nfns*gs + nfnc*gc) / (x**2 - nfns * nfnc * gc * gs)

# Plot fungsi
Npoin = 100
delk = kmax / Npoin
kp = np.linspace(0, kmax, Npoin)

plt.plot(kp, f1(kp), label="Fungsi 1")
plt.plot(kp, f2(kp), label="Fungsi 2")
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.ylim(-10, 10)
plt.xlabel("κ (kappa)")
plt.ylabel("y")
plt.title(f"h={h:.1f} um, lambda={lambda0:.1f} um, nf={nf:.3f}, ns={ns:.3f}, nc={nc:.3f}")
plt.legend()
plt.show()

# Mencari semua akarnya dari 0 sampai kmax
fun = lambda x: f1(x) - f2(x)
initial_guesses = np.linspace(0, kmax, 20)  
roots = []
for x0 in initial_guesses:
    try:
        root = fsolve(fun, x0)[0]
        if 0 <= root <= kmax and all(abs(root - r) > 1e-2 for r in roots):
            roots.append(root)
    except:
        pass

roots = np.sort(roots) # Ngurutin akarnya
print("Akar K=", roots)
