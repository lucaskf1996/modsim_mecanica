import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import arange
import math

#calculando a constante do nosso problema
import math

G=6.67384e-11
M=9.982e12
#P=3.156e7
#L=1.496e11

#k=(P**2*G*M)/L**3
#print(k)

#print(4*math.pi**2)

%matplotlib inline
#constante das equações
C = 4*math.pi**2

#nossa equação diferencial
def EqDif(Solucoes,t):
    xa =Solucoes[0]
    Vxa=Solucoes[1]
    ya =Solucoes[2]
    Vya=Solucoes[3]

    dxadt = Vxa
    dVxadt = (-C*xa)/(xa**2 + ya**2)**(3/2)
    dyadt = Vya
    dVyadt = (-C*ya)/(xa**2 + ya**2)**(3/2)
    return [dxadt, dVxadt, dyadt, dVyadt]



#condições inciais
angulo =
vel_i =
xa0  = 1
ya0  = 0
Vxa0 = cos(angulo) * vel_i
Vya0 = sen(angulo) * vel_i
CI  = [xa0, Vxa0, ya0, Vya0]

#Quero fazer um circulo
circle = Circle((0,0), radius=3)
plt.show()

#lista de tempo: vamos rodar 1 anos
T = arange(0,10,0.005)
#rodando o ODEINT
SolucaoTerra = odeint(EqDif,CI,T)