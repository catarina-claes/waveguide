clc; clear; close all;

% Parameter
wavelength = 1.5; % Panjang Gelombang Vakum
k0 = 2 * pi / wavelength; % Nomor gelombang vakum
n0 = 1.49; % Indeks biar referensi
z_max = 50; % Nilai maks dari z
a = 1; % Nilai tebal core awal
b = 8; % Nilai tebal core akhir

% Koordinat Sistem
dz = 0.1; % Nilai diskritisasi 
Nx = 500; % Total grid x-nya
Lebar = 1000;
dx= Lebar/Nx;
x = (-Nx/2:Nx/2-1) * dx;

% Definisikan Kx dan H untuk Transformasi
kx= (2 * pi / dx) * ([0:Nx/2-1 -Nx/2:-1] / Nx);
H = exp((-1i * (kx.^2 )/ (2 * k0 * n0) + (kx.^4)/ (4 * k0^3 * n0^3)) * dz * 0.5); 

% Definisikan profil awal medan
psi = exp(-(x.^2) / a^2);

% Beam Propagation Loop
z_values = 0:dz:z_max;
st=0; ip=0;
for z = z_values
 Wcore = a + ((b-a)/z_max) * z ; % Definisikan width core berdasarkan z
 n= n0+0.01*((x>=-(Wcore/2))&(x<=(Wcore/2))); % Definisi Indeks bias
 psi = ifft(fft(psi).*H); % Koreksi untuk ½ step 
 % Koreksi fasa krn indeks bias
 psi = psi .* exp(1i * 0.5*k0/n0 * (n.^2 - n0^2) * dz); 
 psi = ifft(fft(psi) .* H); % Koreksi untuk ½ step
 st=st+1;
 if mod(st,floor(length(z_values)/10))==1 
  ip=ip+1;
  Ep(ip,:)=psi;
 end
end

% Surface Plot
[X,Z] = meshgrid(x, linspace(0, z_max, ip)); % Buat grid untuk x dan z
surf(X, Z, abs(Ep)); % Plot surface 3D
shading interp
xlabel('x');
ylabel('z');
zlabel('|E|');
title('Profil Medan Listrik dalam Propagasi');
colorbar;
