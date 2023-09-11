import classp1
import re

next = True

while next:
    while True:
        nome = input('Digite seu nome: ')
        if  re.match(r'^[A-Za-zÀ-Úà-ú\s\.]+$', nome):
            break
        else:
            print('Nome invalido!Digite apenas letras maiusculas e minusculas e espacos.')
    while True:
        idade = input('Digite sua idade: ')
        if re.match(r'^[0-9]+$', idade):
            break
        else:
            print('Idade invalida!Digite apenas numeros positivos.')

    while True:
        altura = input('Digite sua altura: ')
        if re.match(r'^\d{1}\.\d{2}$', altura):
            break
        else:
            print('Altura invalida!Digite no formato: 0.00')

    while True:
        peso = input('Digite seu peso: ')
        if re.match(r'^\d{2}\.\d{1}$', peso):
            break
        else:
            print('Peso invalida!Digite no formato: 00.0')
    while True:
        nascimento = input('Digite sua data de nasciment,(dd/mm/aaaa): ')
        if re.match(r'^(0[1-9|[12][0-9]|1[0-2])/\d{4}$', nascimento):
            break
        else:
            print('Data de nascimento invalida!Digite no formato: dd/mm/aaaa')
            
#adicionarei funcoes em breve
#user = Pessoa(nome, idade, altura, peso, nascimento)


    