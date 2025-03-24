% Plot dalam satu figure dengan layout 2x5
figure; 
for id = 1:10
    subplot(2,5,id); % Membuat grid 2 baris, 5 kolom
    hold on;
    
    Epp = abs(Ep(id, :));
    plot(x, Epp);
    title(strcat('z = ', string(id))); 
    xlim([-30 30]);  
    
    % Garis batas core
    x1 = [- (Wcore/2), - (Wcore/2)]; y1 = [0, 1]; 
    x2 = [ (Wcore/2),  (Wcore/2)];  
    line(x1, y1);
    line(x2, y1);
    
    xlabel('x'); 
    hold off;
end

% Plot satu grafik
figure;  hold on
for id=1:ip
 Epp=abs(Ep(id,:));   plot(x,Epp);
 text(0,Epp(Nx/2),strcat('z',string(id)))
end
x1 = [-(a/2), -(b/2)];  
x2 = [(a/2), (b/2)];  
z1 = [0, 1];  
line(x1, z1);  
line(x2, z1);
xlabel 'x'
hold off

% Surface Plot
[X,Z] = meshgrid(linspace(-3, 3, size(Ep,2)), linspace(0, z_max, ip)); % Buat grid untuk x dan z
surf(X, Z, abs(Ep)); % Plot surface 3D
shading interp
xlabel('x');
ylabel('z');
zlabel('|E|');
title('Profil Medan Listrik dalam Propagasi');
colorbar;
