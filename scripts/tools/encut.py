# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 12:25:58 2018

@author: 245_01
"""

import matplotlib.pyplot as plt

path = r'C:\Users\245_01\Desktop\Si\encut.dat'
with open(path, 'r') as file:
    datas = file.readlines()

L_Encut = []
L_E = []

for data in datas:
    encut, e = [float(i) for i in data.strip().split(' ')]
    L_Encut.append(encut)
    L_E.append(e)
    
plt.plot(L_Encut, L_E, color='r', markerfacecolor='blue', marker='o')
for a, b in zip(L_Encut, L_E):  
    plt.text(a, b, (b), ha='center', va='bottom', fontsize=8)
plt.xlabel(r'$Encut/eV$')
plt.ylabel(r'$E/eV$')

plt.tight_layout()
plt.savefig(r'C:\Users\245_01\Desktop\encut.png',dpi=300)
plt.show()