# CONTAGEM DE FREQUÊNCIA
import numpy as np

def findshift(dic,texto):
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dicti={}
    for i in range(len(alfabeto)):
        dicti[alfabeto[i]]=i
    key_list = list(dicti.keys()) 
    val_list = list(dicti.values())

    for i in dicti:
        if i in dic:
            shifted=dicti[i]
            letter=dicti[dic[i]]
    
    for k in range(1,27):
        if (k+letter)%26==shifted:
            shift=k

    base_26=np.array([dicti[i] for i in texto])
    recoverd_text=(base_26+shift)%26

    recoverd_text=[key_list[val_list.index(i)] for i in recoverd_text]





alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dicti={}
for i in range(len(alfabeto)):
    dicti[alfabeto[i]]=i
key_list_a = list(dicti.keys()) 
val_list_a = list(dicti.values())

texto = 'MXPQYAGOEVFANEOXKPKXJSONFONKVAKFFPQSKVQOXEVZAXEKNOMVQXAPCJAKPEUQVZQXRONGKVQOXQVUKXVEYAFVEASNAVRONJASKJAEADAXEOUAEZOMPJKPPROPPOUVZAXEKEPAKJKXJVNKXEQVQOXOMNOUXECEVAGEVOWMKXVMGNAEQEVKXVKPIONQVZGEODANVZAXALVJASKJAONEOFOEEQBPCADAXEOOXANVZAXEKQEKSVQXIPQYAFNKSVQSKPWMKXVMGSOGFMVANEUQPPALQEVPOXIBARONAVZAXKXJQKGJARANNQXIVOVZAQNALFANVQEA'

dic={}

for k in texto:
    if k not in dic:
        dic[k] = 1
    elif k in dic:
        dic[k] = dic[k] + 1
key_list = list(dic.keys()) 
val_list = list(dic.values())

print(dic)
solution={}
for i in dic:
    if dic[i]==max(val_list):
        solution[i]='E'
        val_list.pop()
    else:
        ...


findshift(solution,texto)

# outra abordagem

texto_temp=np.array([dicti[i] for i in texto])

rec=[key_list_a[val_list_a.index(i)] for i in (((texto_temp)*23)+4)%26]
rec="".join(rec)
print(rec)