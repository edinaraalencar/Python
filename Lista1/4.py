print("4 - Escreva uma função para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, a função deverá retornar quantos dias de vida um fumante perderá. Exiba o total em dias.\n")

def tempoVida(quant, anos):
    dias = anos * 365 #Transformado anos em dias
    min_perdido = ((quant * 10) / 1440) #Tempo perdido em minutos convertido para dias
    total_perdido = min_perdido * dias
    return total_perdido
    
quant = int (input("Digite a quantidade de cigarros fumados por dia: "))
anos = int (input("Digite a quantidade de anos você já fumou: "))
print(f'Você perdeu {tempoVida(quant, anos):.2f} dias, por causa do fumo. ')