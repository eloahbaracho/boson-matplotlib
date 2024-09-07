from matplotlib import pyplot as plt
#plt.style.use('seaborn-v0_8-ticks') #estilo do gráfico 
eixo_x_dias = [1, 5, 10, 15, 20, 25, 30]
eixo_y_temp_max = [28, 29, 25, 32, 34, 36, 31]
eixo_y_temp_min = [21, 22, 17, 24, 21, 24, 25]

plt.title('Temperaturas máximas e mínimas')
plt.xlabel('Datas')
plt.ylabel('Temperaturas')

plt.plot(eixo_x_dias, eixo_y_temp_max, label='Temperatura máxima', linestyle='--', marker='o', color='#5d66c9', linewidth=1)
plt.plot(eixo_x_dias, eixo_y_temp_min, label='Temperatura mínima', linestyle='--', marker='o') #ou plt.bar

plt.legend(loc='lower right') #ou lower/ left/ center / best

#print(plt.style.available) #tipos de estilos de gráficos

plt.axis([1,31, 5, 45]) #valores mínimos e máximos dos eixos

print(plt.axis()) #ou plt.xlim([1,31]) ou plt.ylim(-5, 50)

plt.grid(False)

#plt.savefig('meu_grafico.png')
plt.show()