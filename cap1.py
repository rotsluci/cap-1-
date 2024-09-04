#5) Use a função filter para selecionar apenas as palavras que começam com a letra "a" na
#lista ["apple", "banana", "avocado", "cherry"].

lista = ["apple", "banana", "avocado", "cherry"]
print(list(filter(lambda s: s.endswith('a'),lista))) #  o codigo x.endswith() serve como se fse um if para diser termina com
print(list(filter(lambda s: s.startswith('a'),lista))) #  o codigo x.endswith() serve como se fse um if para diser comessa com

#Utilize a função map para converter todas as palavras da lista ["hello", "world"] em
#maiúsculas.

lista = ["HELLO", "world"]
print(list(map(lambda s: s.lower(),lista))) #o codigo x.lower() serve paras deichar todo os string em minusculo
print(list(map(lambda s: s.upper(),lista))) #o codigo x.lower() serve paras deichar todo os string em maiuscula

#7) Crie uma função lambda que receba uma lista de números e retorne a soma deles.
#Teste com a lista [1, 2, 3, 4].

d = lambda s: sum(s)
print(d([int(o) for o in input().split()]))

#8) Utilize a função filter para remover todos os elementos None da lista [1, None, 2, None,
#3, None].

l = [1, None, 2, None, 3, None]
print(list(filter(lambda s: s != None,l)))

#9) Use a função map para adicionar 5 a cada elemento da lista [10, 20, 30].

l = [10, 20, 30]
print(list(map(lambda s:s+5,l)))

#10) Crie uma função lambda que receba uma lista de números e retorne a lista ordenada
#em ordem decrescente. Teste com a lista [3, 1, 4, 2].
l = [3, 1, 4, 2]
g = lambda f: sorted(f)
print(g([int(o) for o in input().split()[:3]]))
