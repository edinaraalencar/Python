print("s=solteiro e c=casado")
eu = str(input("Meu estado civil-->"))
pessoa02= str(input("Diga o seu estado civil da segunda pessoa--> "))

def match(eu, pessoa02):
    if eu == "s" and pessoa02 == "s":
        return "Bora"
    elif eu == "s" and pessoa02 == "c":
        return "Deixa quieto"
    elif eu == "c" and pessoa02 == "s":
        return "Deixa quieto"
    elif eu == "c" and pessoa02 == "c":
        return "Deixa quieto"
    else:
        return "invalido, informe s=solteiro e c=casado"

x = match(eu, pessoa02)
print(x)