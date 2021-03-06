# -*- coding: utf-8 -*-
"""chocolate_box

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d1yGign5zAXNwBXJcQp5aIbMj5WPbYQN
"""

def chocolate_distr(c, s):
  c.sort() # ordena a lista de caixas
  min_dif = max(c) - min(c) # pegando a maior diferença
  for i in range(len(c)-s+1): # p/ percorrer a lista
    dif = c[i + s-1] - c[i] #diferença entre maior e menor da sublista
    print('Dif. cx com', c[i + s-1], 'chocs. e cx com', c[i], 'chocs.' ,'=', dif) 
    min_dif = min(min_dif, dif) #atualiza a menor diferença
  return min_dif

#==== exemplo 1 ======
chocolate_box = [5, 7, 2, 8, 4, 3] # cxs de chocolate
students = 3 # qtde de estudantes
#==== exemplo 2 ======
#chocolate_bars = [2, 14, 11, 12, 17]
#students = 4

print('Menor diferença:',chocolate_distr(chocolate_box, students))