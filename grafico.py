from matplotlib import pyplot as plt
#plt.style.use('seaborn-v0_8-ticks') #estilo do gráfico 
eixo_x_dias = [1, 5, 10, 15, 20, 25, 30]
eixo_y_temp_max = [28, 29, 25, 32, 34, 36, 31]
eixo_y_temp_min = [21, 22, 17, 24, 21, 24, 25]

plt.title('Temperaturas máximas e mínimas')
plt.xlabel('Datas')
plt.ylabel('Temperaturas')

plt.plot(eixo_x_dias, eixo_y_temp_max, linestyle='--', marker='o', color='#5d66c9', linewidth=1)
plt.plot(eixo_x_dias, eixo_y_temp_min, linestyle='--', marker='o')

plt.legend(['Temperatura máxima' , 'Temperatura mínima'])
#print(plt.style.available) #tipos de estilos de gráficos
plt.grid(True)
plt.show()