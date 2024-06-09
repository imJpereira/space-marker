def salvarDados(estrelas):
    try:
        baseDeDados = open("baseDeDados.txt", "w", encoding="utf8")
        baseDeDados.write(str(estrelas))
        baseDeDados.close()
    except:
        print("Ocorreu um erro ao salvar os dados")

def carregarDados():
    try:
        baseDeDados = open("baseDeDados.txt", "r", encoding="utf8")
        text = baseDeDados.read()
        baseDeDados.close()
        return eval(text)
    except:
        print("Ocorreu um erro ao carregar os dados")
        return {}

def deletarDados():
    try:
        baseDeDados = open("baseDeDados.txt", "w", encoding="utf8")
        baseDeDados.write("")
        baseDeDados.close()
    except:
        print("Ocorreu um erro ao deletar os dados")