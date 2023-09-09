import re

class Pessoa:

    def __init__(self, nome, idade, altura, peso, nascimento):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso =  peso
        self.nascimento = nascimento

    def apresentar(self):
        print(f'Muito prazer!Eu me chamo {self.nome} e tenho {self.idade} anos de idade.')

    def eh_maior(self):
        return self.idade >= 18
    
    def imc(self): 
        return self.peso / (self.altura * self.altura)
    
    def imc_longo(self):
        imc= self.imc()
        if imc <18.5:
            return 'Abaixo do peso.'
        elif imc <25.0:
            return 'Peso normal.'
        elif imc <30.0:
            return 'Excesso de peso.'
        elif imc <35.0:
            return 'Obesidade 1.'
        elif imc <40.0:
            return 'Obesidade 2.'
        else:
            return 'Obesidade 3.'

    def comparar_idade(self,idade):
        if idade < self.idade:
            print(f'{self.nome} é mais velho que eu!')
        elif idade > self.idade:
            print(f'{self.nome} é mais novo que eu!')
        else:
            print(f'{self.idade} tem a mesma idade que eu!')

    def validar_nascimento(self,nascimento):
        self.nascimento = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        return re.match(self.nascimento, nascimento)
    
    def validar_nome(self,nome):
        self.nome = r'^([A-Za-z])$'
        return re.match(self.nome, nome)
    
    def validar_altura(self,altura):
        self.altura = r'^([0-90-9].[0-9])$'
        return re.match(self.altura, altura)
    
    def validar_peso(self,peso):
        self.peso = r'^([0-90-9].[0-9])$'
        return re.match(self.peso, peso)
