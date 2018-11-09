# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 13:05:59 2018

@author: 245_01
"""

import matplotlib.pyplot as plt

path = r'C:\Users\245_01\Desktop\Si\kpoints.dat'
with open(path, 'r') as file:
    datas = file.readlines()

L_Kpoints = []
L_E = []

for data in datas:
    kpoints, e = [float(i) for i in data.strip().split(' ')]
    L_Kpoints.append(kpoints)
    L_E.append(e)
    
plt.plot(L_Kpoints, L_E, color='r', markerfacecolor='blue', marker='o')
for a, b in zip(L_Kpoints, L_E):  
    plt.text(a, b, (b), ha='center', va='bottom', fontsize=8)
plt.xlabel(r'$Kpoints$')
plt.ylabel(r'$E/eV$')

plt.tight_layout()
plt.savefig(r'C:\Users\245_01\Desktop\kpoints.png',dpi=300)
plt.show()