# -*- coding: utf-8 -*-
"""aula 12  curso em video 16/02/2022.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mW0yG3Bd7QPoYetb8U2Z1Hx1YJgdFTlH
"""

preço = float(input('Insira o preço do produto R$:'))
novo =preço - (preço * 5 / 100)
print('o produto  que custa R${:.2f}, na promoção com descoto de 5% vai custar  R${:.2f} é de :'.format(preço, novo))