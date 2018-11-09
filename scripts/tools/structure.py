# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 13:50:29 2018

@author: 245_01
"""

import matplotlib.pyplot as plt

a = 5.43

path = r'C:\Users\245_01\Desktop\Si\structure_1.dat'
with open(path, 'r') as file:
    datas = file.readlines()

L_A = []
L_E = []

for data in datas:
    A, e = [float(i) for i in data.strip().split(' ')]
    L_A.append(A)
    L_E.append(e)
    
plt.plot(L_A, L_E, color='r', markerfacecolor='blue', marker='o')
for a, b in zip(L_A, L_E):  
    plt.text(a, b, (b), ha='center', va='bottom', fontsize=8)
plt.xlabel(r'$A/\AA$')
plt.ylabel(r'$E/eV$')

plt.tight_layout()
plt.savefig(r'C:\Users\245_01\Desktop\structure_1.png',dpi=300)
plt.show()