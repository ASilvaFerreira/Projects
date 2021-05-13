# Cifra Playfair
# Gerar a tabela 5*5
def tabela(chave_secreta):
    alfabeto='ABCDEFGHIKLMNOPQRSTUVWXYZ'
    chave_publica=[i for i in chave_secreta]

    for i in range(len(chave_publica)):
        if chave_publica[i]=='I' or chave_publica[i]=='J':
            chave_publica[i]='IJ'

    for i in range(len(alfabeto)):
        if alfabeto[i]=='I' and 'IJ' not in chave_publica:
            chave_publica.append('IJ')
        elif alfabeto[i] not in chave_publica and alfabeto[i] != 'I':
            chave_publica.append(alfabeto[i])

    public_key=list()

    for i in range(5):
        lista=list()
        for i in range(5):
            lista.append(chave_publica.pop(0))
        public_key.append(lista)

    return public_key

def cifrar(mensagem):
    l=len(mensagem)
    if l%2==1:
        mensagem=mensagem+'X'
        l+=1
    mensagem=[i for i in mensagem]
    new_m=list()
    for i in range(int(l/2)):
        lista=list()
        for i in range(2):
            lista.append(mensagem.pop(0))
        new_m.append(lista)
    



chave='MAINHE'
mensagem='ATUAMAINHEEHEHOHBELHINHO'
cifrar(mensagem)

table = tabela(chave)

