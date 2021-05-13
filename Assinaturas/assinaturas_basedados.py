#coding: utf-8

import tkinter as tk
from tkinter import messagebox 

## Make a database for annual subscriptions storage and warning about the ending

## Possible storage types: Lists, Dictionaries, Tuples (Lists would be hard, Dictionaries or Tuples should be implemented)

## furthermore i want this data to be acessible through txt file

## in a dictionary we add values to a key ellement, but we need to add several values to a single key, which would mean a list for each key. 
## is there is existent data on the file. it should be read and uploaded to the dictionary, in the exact same format it will be saved.
def dataLoad():
    dic={}
    file2read=open("assinaturas.txt",'r',encoding="utf-8")
    lines=file2read.readlines()
    file2read.close

    newlines=[]
    for line in lines:
        line=line.split(',')
        newlines.append(line)


    for line in newlines:
        dic[line[0]]=[line[1],line[2],line[3],line[4]]
    return dic

def dataWrite(dic):

    file2write=open("assinaturas.txt",'a+')
    for i in dic:
        file2write.write(i)
        file2write.write(", ")
        for j in dic[i]:
            if dic[i].index(j) == 3:
                file2write.write(j)
            else:
                file2write.write(j)
                file2write.write(", ")
        file2write.write('\n')

    file2write.close()

def displayInfo():
    dic = dataLoad()
    key_list = list(dic.keys()) 
    val_list = list(dic.values())

    for i in dic:
        lista = dic[i]
        nome.config(text=i)
        numero.config(text=lista[0])
        morada.config(text=lista[1])
        codigopostal.config(text=lista[2])
        pagamento.config(text=lista[3])
        labelRodape.config(text=('Assinante numero ' + numero.cget('text') + ' de ' + str(len(dic)-1)))

def add():
    dic = dataLoad()
    ## for the key value we use the name of the person
    name=entryNome.get()
    ## we also need to store address and membership number, aswell as pay dates

    number=entryNA.get()
    address=entryMorada.get()
    postalcode=entryCodigopostal.get()
    payment=entryPagamento.get()

    tempdic={}
    if name not in dic:
        tempdic[name]=[number,address,postalcode,payment]
        dataWrite(tempdic)


########################################################################################################################################################
# GUI implementation #

W=700
H=500

root= tk.Tk()
dic = dataLoad()
key_list = list(dic.keys()) 
val_list = list(dic.values())

canvas = tk.Canvas(root,height=H,width=W, bg='black')
canvas.pack()
#criar as divisões para as secções do GUI
frame1 = tk.Frame(root, bg='#DFDEDF')
frame1.place(relx=0.25,rely=0.005,relwidth=0.49,relheight=0.985,anchor='n')

frame2 = tk.Frame(root, bg='#DFDEDF')
frame2.place(relx=0.746,rely=0.005,relwidth=0.49,relheight=0.555,anchor='n')

frame3 = tk.Frame(root,bg='#DFDEDF')
frame3.place(relx=0.746,rely=0.565,relwidth=0.49,relheight=0.425,anchor='n')



assinantes =  tk.Label(frame1,text='Assinantes do Horizonte',width=25,height=3)
assinantes.pack()

labelNome = tk.Label(frame1,text='Nome do Assinante:',height=2,width=20)
labelNome.place(relx=0,rely=0.15)

labelNA = tk.Label(frame1,text='Número de Assinante:',height=2,width=20)
labelNA.place(relx=0,rely=0.25)

labelMorada = tk.Label(frame1,text='Morada do Assinante:',height=2,width=20)
labelMorada.place(relx=0,rely=0.35)

labelPostal = tk.Label(frame1, text='Código Postal:',height=2,width=20)
labelPostal.place(relx=0,rely=0.45)

labelPagamento = tk.Label(frame1, text='Assinatura paga até:',height=2,width=20)
labelPagamento.place(relx=0,rely=0.55)

labelProcurar = tk.Label(frame1,text='Procurar por:',width=20,height=2)
labelProcurar.place(relx=0,rely=0.7)

labelRodape = tk.Label(frame1, text=('Assinante numero ' + dic[key_list[0]][0] + ' de ' + str(len(dic)-1)))
labelRodape.place(relx=0.5,rely=0.65,anchor='n')

nome = tk.Label(frame1,text=key_list[0],width=27)
nome.place(relx=0.43,rely=0.165)

numero = tk.Label(frame1,text=dic[key_list[0]][0],width=27)
numero.place(relx=0.43,rely=0.265)

morada = tk.Label(frame1,text=dic[key_list[0]][1],width=27)
morada.place(relx=0.43,rely=0.365)

codigopostal = tk.Label(frame1,text=dic[key_list[0]][2],width=27)
codigopostal.place(relx=0.43,rely=0.465)

pagamento = tk.Label(frame1,text=dic[key_list[0]][3],width=27)
pagamento.place(relx=0.43,rely=0.565)

adicionarAssinante = tk.Label(frame2,text='Adicionar novo assinante',width=25,height=2)
adicionarAssinante.pack()

labelNome = tk.Label(frame2,text='Nome do Assinante:',height=2,width=20)
labelNome.place(relx=0,rely=0.14)

entryNome = tk.Entry(frame2,width=30)
entryNome.place(relx=0.43,rely=0.18)

labelNA = tk.Label(frame2,text='Número de Assinante:',height=2,width=20)
labelNA.place(relx=0,rely=0.28)

entryNA = tk.Entry(frame2,width=30)
entryNA.place(relx=0.43,rely=0.32)

labelMorada = tk.Label(frame2,text='Morada do Assinante:',height=2,width=20)
labelMorada.place(relx=0,rely=0.42)

entryMorada = tk.Entry(frame2,width=30)
entryMorada.place(relx=0.43,rely=0.45)

labelCodigopostal = tk.Label(frame2,text='Código Postal',height=2,width=20)
labelCodigopostal.place(relx=0,rely=0.56)

entryCodigopostal = tk.Entry(frame2,width=30)
entryCodigopostal.place(relx=0.43,rely=0.59)

labelPagamento = tk.Label(frame2, text='Assinatura paga até:',height=2,width=20)
labelPagamento.place(relx=0,rely=0.7)

entryPagamento = tk.Entry(frame2,width=30)
entryPagamento.place(relx=0.43,rely=0.73)

addAssinante = tk.Button(frame2,text='Adicionar à base de dados',height=2,width=20,command=add)
addAssinante.place(relx=0.5, rely=0.84, anchor='n')

search = tk.Button(frame1,text='Procurar',command=displayInfo)
search.place(relx=0.59,rely=0.75)

choices=['Nome','Numero de Assinante','Morada']
experiment = tk.StringVar(root)
experiment.set('Método de procura')
exps = tk.OptionMenu(frame1,experiment,*choices)
exps.place(relx=-0.01,rely=0.75,relwidth=0.435) 

searchtext = tk.Entry(frame1,width=25)
searchtext.place(relx=0.45,rely=0.71)

root.mainloop()