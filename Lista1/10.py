print("""10 - Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo
(8min15s por quilômetro), então 3 quilômetros a uma passo mais rápido(7min12s por quilômetro) 
e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?\n""")
# resultado esperado= 7:30:06
total_min = ((2*8) + (3*7)) * 60 #Minutos transformados em segundos
total_seg = ((2*15) + (3*12)) + total_min #Total percorrido em segundos

saida_seg = (6*60*60) + (52*60) #Horario de saida transformado em segundos
total = total_seg + saida_seg #Soma do horario de saida com o tempo percorrido

total_seg = total%60 #Armazenando o resto da divisão 
total_min = total//60 #Armazenando o valor inteiro da divisão 
total_horas = total_min//60 #Armazenando o valor inteiro 
total_min = total_min%60 #Armazenando o resto da divisão 


print(f'{total_horas}:{total_min}:{total_seg}')


