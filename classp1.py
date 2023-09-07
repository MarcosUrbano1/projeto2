class Pessoa:

    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso =  peso


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

pessoa1=Pessoa('Gallye', 21, 1.78, 33.6)

pessoa1.apresentar()

if pessoa1.eh_maior():
    print('É maior de idade!')
else:
    print('É menor de idade!')
print(pessoa1.imc())

print(pessoa1.imc_longo())

pessoa1.comparar_idade(17)

print('   ')

Herina=Pessoa('Herina', 17, 1.63, 27.9)

Herina.apresentar()

if Herina.eh_maior():
    print('É maior de idade!')
else:
    print('É menor de idade!')
print(Herina.imc())
Herina.comparar_idade(21)

print(Herina.imc_longo())