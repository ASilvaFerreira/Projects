#Vigenere
import numpy as np
# Encriptar um texto em português



def encriptar(texto,chave):
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic={}
    for i in range(len(alfabeto)):
        dic[alfabeto[i]]=i
    key_list = list(dic.keys()) 
    val_list = list(dic.values())

    base26=[dic[i] for i in texto]
    chave = [dic[i] for i in chave]
    n = len(chave)
    index=0
    cripta=list()
    for i in range(len(base26)):
        cripta.append((base26[i]+chave[index])%26)
        index+=1
        if index==n:
            index=0

    cripta=[key_list[val_list.index(i)] for i in cripta]
    encriptado="".join(cripta)
    return encriptado

def detetar_tamanho(dic):
    # lista_indice={'Português':0.0738,'Inglês':0.0661,'Random':0.0385}
    # para um primeiro teste vamos usar um simples check de range + ou - 0.005
    linguagem=[]
    for i in dic:
        if 0.0685<dic[i] and dic[i]<0.082:
            linguagem.append('Português')
        elif 0.06<dic[i] and dic[i]<0.0685:
            linguagem.append('Inglês')
        elif dic[i]<0.06 or dic[i]>0.08:
            linguagem.append('Random')
        else:
            linguagem.append('N/A')
    
    k=0
    for i in linguagem:
        if i == 'Random':
            k+=1
    if k<=len(linguagem)/2 and len(linguagem) !=1:
        return 'Key'
    else:
        ...

def freq(lista):
    dic={}
    c=1
    if type(lista[0]) != type(list()):
        for i in lista:
            if i not in dic:
                dic[i] = 1
            elif i in dic:
                dic[i] = dic[i] + 1
        return dic

    else:
        for i in lista:
            
            dic[c]={}
            for k in i:
                if k not in dic[c]:
                    dic[c][k] = 1
                elif k in dic[c]:
                    dic[c][k] = dic[c][k] + 1
            c+=1
        return dic

def coincidencia(lista):
    # conta a frequencia de letras em cada linha da lista e guarda num dicionario

    dic=freq(lista)

    coincidencia=list()
    for i in dic:
        kek=list()
        
        for k in dic[i]:
            kek.append(dic[i][k]*((dic[i][k])-1))
        coincidencia.append(sum(kek))

    indice_coincidencia={}
    for i in dic:
        indice_coincidencia[i]=(sum([dic[i][k]*((dic[i][k])-1) for k in dic[i]]))/((len(lista[i-1]))*(len(lista[i-1])-1))
        
    return indice_coincidencia

def coincidencia_mutuo(blocos_afins):
    # calcular a diferença entre os shifts dde cada bloco
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic={}
    for i in range(len(alfabeto)):
        dic[alfabeto[i]]=i

    for i in blocos_afins:
        for k in range(len(i)):
            i[k] = dic[i[k]]
    key_list = list(dic.keys()) 
    val_list = list(dic.values())
    blocos = {}
    c=1
    for i in blocos_afins:
        blocos[c]=np.array(i)
        c+=1    

    mutuo={}
    c=1
    for i in blocos:
        # calcular freq do bloco i
        freq_yi=freq([key_list[val_list.index(letra)] for letra in blocos[i]])
        for j in range(i+1,8):
            if i != j:
                for g in range(26):
                    # fazer o shift e calcular as freqs
                    if i+1 == (len(blocos)+1):
                        break
                    freq_yj=([key_list[val_list.index(i)] for i in list((blocos[j]-g)%26)])
                    mutuo[str(i)+str(j)]='aqui'
            else:
                ...
    print(mutuo)

            
    
    


def decifrar(encriptado):
    r=1
    key_size = list()
    while r<11:
        encriptadito=[i for i in encriptado]
        multiple_row=[list() for i in range(r)]
        
        for i in range(len(encriptado)):
            for k in range(r):
                if encriptadito == list():
                    break 
                multiple_row[k].append(encriptadito.pop(0))
            if encriptadito == list():
                break  
        indices=coincidencia(multiple_row)
        if detetar_tamanho(indices)=='Key':
            key_size.append(r)
        r+=1
    blocos=[list() for i in range(key_size[0])]
    encriptado=[i for i in encriptado]
    for i in range(len(encriptado)):
        for k in range(key_size[0]):
            if encriptado == list():
                break 
            blocos[k].append(encriptado.pop(0))
        if encriptado == list():
            break  

    coincidencia_mutuo(blocos)


chave='MAINHE'
tpc='LSYPEUDIFLYSZWXCYEOHXPBEFMIHHWDEAEWPZRZRZWWADTNKKTBZETFRSWDEAEWUIEFRVEPGPOOEHMDPCIVQRSTYDVSACJTNXVJWEPBNHWOGPDVWTFXTNVGICDEAIWEZLYNZQVOYOCFPBIYTCRWXBRPAIONOMZUKWWSFACFPXBRERRQHWETOEWDEFLNKXBFPDIJWPBELLXRGWESMJRJFFWTZPPHPROROXGEZPIRKWOPCFVISQQETWXJPDETXGWEJAXDXBDEAGRISYEIROFILYTLPRCXAUKHGKPLRVZDFVTNXZXHSAAIWCSCDATUDGDEHVXHUGPNURGGLYDJWPBOLRUVQCOTEJWDSYDUIHIVPCEZVPQWPAISAOYQOIJTHETNXDCSHDUZWTCQLLXRGWESMJWOWELRVGTJPWOGHSWYLNFSTBLYDKUPBDAAIHCHXLNEHGHSLTNLAZQZRDWWSQZUEGPHTZNFIDICYEOWHITEEFIRFJATFJGOASITDAUZCIKKBG'
texto='ATUAMAINHEGOSTADEESTARDEQUATROENQUANTOEULHEFACOUMABEITACAPODREEHEHEOHBELHINHOAPARTIRDAQUIPARAAFRENTEJANAOTEMPIADAPORQUEESTOUSOAESCREVERPARATERLETRASSUFICIENTESPARAAESTATISTICA'
texto1='ramalheteaindaqueacrescentavaelenumafrasemeditadaatemeenvergonhodemencionartaisfrioleirasnesteseculodevoltaireguisoteoutrosfilosofosliberaisaonsoriumuitodabastariaabrirdeparemparasjanelasedeixarentrarosolsexmandavaecomoesseinvernoiasecoasobrascomecaramlogosobadireccaodumestevesarquitectopoliticoecompadredevilacasteartistaentusiasmaraoprocuradorcomumprojectodeescadaaparatosaflanqueadaporduasfigurassimbolizandoasconquistasdaguineedaindiaeestavaideandoetambemumacascatadeloucanasaladejantarquando'
oupa='TMHPPLTCWUMEPLHABUKAAYHPPOEOHIIOGKNETFXSCUHSPVXMRIFOSYVIULTRTMMAHWHIHULTDXTSTKNACXHCDHLEVOBRTMWERCYRPLBSIIWIOGXACXKEHIIAGUFEIYKNDDHATFXS'

texto_encriptado=encriptar(texto,chave)

decifrar(oupa)

