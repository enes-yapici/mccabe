import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel('xy_data.xlsx')

x_eql=data['x'].tolist()
y_eql=data['y'].tolist()

x1=np.linspace(0,1,1000)
y1=x1

xd=np.linspace(0.103962054,0.566879097,1000)
yd= 0.648 * xd + 0.199
def yd_func(xd):
    yd= 0.648 * xd + 0.199
    return yd

xb=np.linspace(0.001625712, 0.103962054)
yb= 2.591 * xb - 0.0026
def yb_func(xb):
    yb= 2.591 * xb - 0.0026
    return yb

xf=np.linspace(0.073612492, 0.103962054)
yf = 6.364 * xf - 0.395

# x noktsı kesişimi geçene kadar d ile eql arasında sonra b ile eql arasında
xd_0 = 0.566879097 # başlangıç noktası x = y  dist
kesisim= 0.103962054
tray=0
x= xd_0

mccabe_x=[]
mccabe_y= []

while x >0.001625712:
    if x >kesisim:
        target = yd_func(x)
        mccabe_x.append(x)
        mccabe_y.append(target)
    else:
        target = yb_func(x)
        mccabe_x.append(x)
        mccabe_y.append(target)

    # Her eleman için mutlak farkı hesapla ve (fark, index) tuple'ları olarak sakla
    diffs = [(abs(x - target), i) for i, x in enumerate(y_eql)]

    # Farka göre sırala ve ilk 3 elemanın indexlerini al
    closest_three_indexes = [i for _, i in sorted(diffs)[:3]]

    # array2'den bu indekslere karşılık gelen elemanları al
    y_3 = [y_eql[i] for i in closest_three_indexes]
    x_3 = [x_eql[i] for i in closest_three_indexes]


    # İkinci dereceden polinom fiti yap
    coefficients = np.polyfit(x_3, y_3, 2)

    # Polinom katsayıları (a, b, c)
    a, b, c = coefficients

    target_y = target  # Önceden hesapladığınız target değeri

    # Denklemin köklerini bul
    coeffs_for_roots = [a, b, (c - target_y)]
    roots = np.roots(coeffs_for_roots)

    x = [i for i in roots if i <x][-1]

    tray+=1

    mccabe_x.append(x)
    mccabe_y.append(target_y)

print(tray)

plt.figure(figsize=(10, 6))
plt.plot(x_eql, y_eql, label='McCabe-Thiele Method')
plt.plot(x1, y1, '--', label='Equilibrium Line')
plt.plot(mccabe_x,mccabe_y)
plt.plot(xd,yd , label='Enriching Section Operating Line')
plt.plot(xb,yb , label='Stripping Section Operating Line')
plt.plot(xf,yf , label='Feed Section Operating Line')
plt.title('McCabe-Thiele Method vs. Equilibrium Line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()