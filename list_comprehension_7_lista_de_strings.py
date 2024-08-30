"""
Dada uma lista de strings que representam frases, crie uma nova lista contendo a
quantidade de palavras em cada frase.

frases = [
    "Python é uma linguagem de programação",
    "List comprehension é muito útil",
    "Aprender novas habilidades é importante",
    "Desenvolvimento de software é desafiador",
    "Exercícios ajudam a fixar o conhecimento"
]

Requisito: Utilize list comprehension para gerar a nova lista com a quantidade de
palavras em cada frase.

Dica: Para contar as palavras em cada frase, você pode usar o método split()
para dividir a frase em palavras e depois usar a função len() para contar
quantas palavras há.
"""

frases = [
    "Python é uma linguagem de programação",
    "List comprehension é muito útil",
    "Aprender novas habilidades é importante",
    "Desenvolvimento de software é desafiador",
    "Exercícios ajudam a fixar o conhecimento"
]

lista_string = [len(frase.split()) for frase in frases]

print(lista_string)