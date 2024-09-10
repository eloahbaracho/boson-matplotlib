import matplotlib.pyplot as plt
#temperaturas
# cidade_a = [32, 30, 27, 28, 29, 24]
# cidade_b = [27, 26, 15, 22, 22, 29]
# cidade_c = [23, 15, 19, 23, 21, 19]
datas = [5, 10, 15, 20, 25, 30]

#Homicidios
cidade_a = [5, 2, 4, 3, 10, 2]
cidade_b = [7, 6, 8, 2, 3, 9] 
cidade_c = [4, 2, 3, 5, 1, 2]

#Criar posições distintas para cada cidade
# posicoes_a = list(range(len(datas)))
# posicoes_b = [pos + 0.25 for pos in posicoes_a]
# posicoes_c = [pos + 0.50 for pos in posicoes_a]


#em posicoes_x poderiamos adicionamos a var datas antes
plt.bar(datas, cidade_a, width=0.25, color='pink', label='Cidade A')
plt.bar(datas, cidade_a, width=0.25, bottom= cidade_a, color='green', label='Cidade B')
plt.bar(datas, cidade_a, width=0.25, bottom= [a + b for a, b in zip(cidade_a, cidade_c)], color='blue', label='Cidade C')
#plt.barh(datas, cidade_a, height=0.45, color='pink', label='Cidade A')
#plt.xticks(ticks=posicoes_a, labels=datas) #agrupar dados nas datas
plt.legend()
plt.xlabel('Datas')
plt.ylabel('Homicídios')
plt.title('Homicídios nas Cidades em dias determinados')
plt.show()