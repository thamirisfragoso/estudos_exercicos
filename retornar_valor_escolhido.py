# -*- coding: utf-8 -*-
"""retornar valor escolhido.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BdFfJdOVlqX_ywzW0BW-A2Lf54BSX6u2
"""

numero_secreto = 42
chute_str = input('Digite o seu numero:')
print('Você digitou', chute_str)
chute= int(chute_str)
if(numero_secreto == chute):
  print('você acertou!')
else :
    print('Você errou!')
    print('-----Fim do jogo-----')