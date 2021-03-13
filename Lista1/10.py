print("""10 - Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo
(8min15s por quilômetro), então 3 quilômetros a uma passo mais rápido(7min12s por quilômetro) 
e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?\n""")
# resultado esperado= 7:30:06
saida_hora = 6
saida_min = 52
saida_seg = 0
km = 1

if km == 1:
    saida_min += 8
    saida_seg += 15
    if saida_min >= 60:
        saida_hora += 1
        saida_min -= 60
    km += 1

while (5 > km > 1):
    saida_min += 7
    saida_seg +=12
    if saida_min >= 60:
        saida_hora += 1
        saida_min -= 60
    km += 1

if km == 5:
    saida_min += 8
    saida_seg += 15
    if saida_seg >= 60:
        saida_min += 1
        saida_seg -=60

print(f'Horario de chegada {saida_hora}:{saida_min}:{saida_seg}')