'''class Square:  #QUESTÃO 01
    SideSize = 0.00
    def __init__(self, size):
        self.SideSize = size
    def ChangeSizeSide(self, size):
        self.SideSize = size
    def CalcSquareArea(self):
        return self.SideSize ** 2
    def SideSizeValue(self):
        return f"O Lado do quadrado tem: {self.SideSize}"
    def AreaSquare(self):
        return f"A area do quadrado e de: {self.CalcSquareArea()}"
    
quadrado = Square(2)
print(quadrado.AreaSquare())
print(quadrado.SideSizeValue())
quadrado.ChangeSizeSide(4)
print(quadrado.SideSizeValue())
print(quadrado.AreaSquare())
'''
#--------------------------------------------------------------
'''
class Ball:  #QUESTÃO 02
    Color = ""
    Circle = 0.00
    Material = ""
    def __init__(self, color, circle, material):
        self.Color = color
        self.Circle = circle
        self.Material = material
    
    def ShowColor(self):
        return f"Ball is from color: {self.Color}"
    def ChangeColor(self, color):
        self.Color = color
        
futballBall = Ball("Blue", 23.5, "Leather")
print(futballBall.ShowColor())
futballBall.ChangeColor("Red")
print(futballBall.ShowColor())
'''
#------------------------------------------------------------
'''
class Rectangle:  #QUESTÃO 03
    SideA = 0.00
    SideB = 0.00
    
    def __init__(self, sideA, sideB):
        self.SideB = sideB
        self.SideA = sideA
        
    def ChangeSideA(self,newSize):
        self.SideA = newSize
    
    def ChangeSideB(self,newSize):
        self.SideA = newSize
        
    def CalcRectangleArea(self):
        return self.SideA * self.SideB
        
    def CalcRectanglePerimeter(self):
        return (self.SideA * 2) + (self.SideB * 2)
    
    def ShowSideSize(self):
        return f"Side A has a size: {self.SideA} and Side B has a size: {self.SideB}"
    
    def ShowPerimeter(self):
        return f"Rectangle has a perimeter of: {self.CalcRectanglePerimeter()}"
        
    def ShowArea(self):
        return f"Rectangle has a area of: {self.CalcRectangleArea()}"

teste = Rectangle(12,3)
print(teste.ShowSideSize())
print(teste.ShowPerimeter())
print(teste.ShowArea()) 
'''
#---------------------------------------------
'''
class Human:  #QUESTÃO 04
    nome = ""
    idade = 0
    peso = 0.00
    altura = 0.00
    
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, anos):
        self.idade += anos
        self.altura += (0.05 * anos)
        
    def engordar(self, novoPeso):
        self.peso += novoPeso
        
    def emagrecer(self, novoPeso):
        self.peso -= novoPeso

    def alto(self, novoAlto):
        self.altura += novoAlto
        
    def mostrarAtributos(self):
        return f"nome: {self.nome} \n idade: {self.idade} \n peso: {self.peso} \n altura: {self.altura}"
    
pessoa1 = Human('beatriz', 24, 53.0, 1.65)es
pessoa1.envelhecer(4)
print(pessoa1.mostrarAtributos())
pessoa1.engordar(3.5)
print(pessoa1.peso)
pessoa1.emagrecer(3)
print(pessoa1.peso)
pessoa1.alto(1.0)
print(pessoa1.altura)
print(pessoa1.mostrarAtributos())
'''
#-------------------------------------------------- 
''''
class checkingBanco: #QUESTÃO 05
    numeroConta = ""
    nomeConta = ""
    saldoConta = 0.00
    
    def __init__(self, nome, numero, saldo = 0.00):
        self.nomeConta = nome
        self.numeroConta = numero
        self.saldoConta = saldo
    
    def mudarNome(self, nome):
        self.nomeConta = nome
    
    def retirar(self, value):
        self.saldoConta -= value
    
    def depositar(self, value):
        self.saldoConta += value

    def mostrarAtributos(self):
     return f" Nome: {self.nomeConta} \n Account Balance: {self.saldoConta} \n Account Number: {self.numeroConta}"


cliente1 = checkingBanco('beatriz', 00000, 250.00)
cliente1.mudarNome('joao')
print(cliente1.nomeConta) 
cliente1.retirar(150)
print(cliente1.saldoConta)
cliente1.depositar(1000)
print(cliente1.saldoConta)
'''
#------------------------------------------------------------
'''
class BichoVirtual:  #QUESTÃO 07
    Nome = ""
    Fome = 100
    Saude = 100
    Idade = 0 
    
    def SetNome(self,value):
        self.Nome = value
    def SetFome(self, value):
        self.Fome = value
    def SetSaude(self, value):
        self.Saude = value
    def SetIdade(self, value):
        self.Idade = value
    def GetNome(self):
        return self.Nome
    
    def GetFome(self):
        return self.Fome
    
    def GetSaude(self):
        return self.Saude
    
    def GetIdade(self):
        return self.Idade
    
    def GetHumor(self):
        return self.Saude + self.Fome
    

bichinho = BichoVirtual()

bichinho.SetFome(10)
print(bichinho.GetFome())
bichinho.SetNome('olavo')
print(bichinho.GetNome())
bichinho.SetIdade(3)
print(bichinho.GetIdade())
'''

