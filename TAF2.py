import numpy as np
import matplotlib.pyplot as plt

def f1(x, gc):# untuk x >= 0
    return np.exp(-gc * x)  

def f2(x, kappa, gc): # untuk -h < x < 0
    return np.cos(kappa * x) - (gc / kappa) * np.sin(kappa * x)  

def f3(x, gs, kappa, gc, h): # untuk x <= -h
    prec = np.cos(kappa * h) + gc / kappa * np.sin(kappa * h)
    return prec * np.exp(gs * (x + h))  

# Parameter
h = 5.0  # um, ketebalan core
lambda0 = 1.0  # um, panjang gelombang vakum
nf = 1.5  # indeks bias core
nc = 1.4  # indeks bias cladding
ns = 1.45  # indeks bias substrate
k0 = 2 * np.pi / lambda0 # bilangan gelombang vakum
kf = nf * k0
kc = nc * k0
ks = ns * k0
kappa_values = np.array([0.55595303, 1.10800766, 1.65046806, 2.16939757, 2.39893996, 2.41310311])

# Buat dx untuk plot profile E(x)
Npoin = 100
xmin = -1.5 * h
xmax = 0.5 * h
delx = (xmax - xmin) / Npoin
x = np.arange(xmin, xmax, delx)

colors = ['b', 'r', 'g', 'c', 'm', 'y']  
plt.figure()

# Untuk ngeplot seluruh grafiknya
for i, kappa in enumerate(kappa_values):
    beta = np.sqrt(kf**2 - kappa**2)
    gs = np.sqrt((kf**2 - ks**2) - kappa**2)
    gc = np.sqrt((kf**2 - kc**2) - kappa**2)
    
    Ey = np.where(x > 0, f1(x, gc), 
                  np.where((-h < x) & (x <= 0), f2(x, kappa, gc), 
                           f3(x, gs, kappa, gc, h)))

    plt.plot(x, Ey, colors[i], label=f'kappa = {kappa:.6f}')

# Buat garis untuk ngebedain antar medium
plt.axvline(0, color='k', linestyle='--')
plt.axvline(-h, color='k', linestyle='--')

title = f"h = {h:.1f} um, lambda = {lambda0:.1f} um, nf = {nf:.3f}, ns = {ns:.3f}, nc = {nc:.3f}"
plt.title(title)
plt.xlabel('x')
plt.ylabel('Ey')
plt.legend()
plt.show()
