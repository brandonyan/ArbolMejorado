from Pila import *
from Lexico import *
import re

class Nodo():
    def __init__(self, valor, izq=None, der=None):
        self.valor=valor
        self.izq=izq
        self.der=der
        
class Variable():
    def  __init__ (self, nombre, valor):
        self.Nombre=nombre
        self.Valor=valor

def evaluar(arbol):     
    if arbol.valor == "+":
        return (arbol.izq) + (arbol.der)
    elif arbol.valor == "-":
        return (arbol.izq) - (arbol.der)
    elif arbol.valor == "*":
        return (arbol.izq) * (arbol.der)
    elif arbol.valor == "/":
        return (arbol.izq) / (arbol.der)
    
    return int(arbol.valor)


    

def inicio():
    
    pila=Pila()
    pila2=Pila()
    pila3=Pila()
    token=Lex()

    exp_valor = re.compile('[0-9]+$')
    exp_operador = re.compile('[\+\*\-/=]{1,1}$')
    exp_variable = re.compile('([a-z]+)([A-Z0-9_]*)$')

    print("ingrese vacio para Terminar")
    while True:
        m=input("ingreso en post-orden:").split(" ")
        k=len(m)
        if(k<2):
            break;
        
        for j in range(0, k):
            y=m[j]
            
            if(token.operador(y)):                
                if(y=="="):
                    while len(pila2.items) != 0:
                        variable=pila2.desapilar()
                        pila3.apilar(variable)
                        print(variable.Nombre,"=",variable.Valor)
                    while len(pila3.items)!= 0:
                        variable=pila3.desapilar()
                        pila2.apilar(variable)
                                    
                else:
                    if(len(pila.items)>=2):
                        der=pila.desapilar()
                        izq=pila.desapilar()
                        nodo=Nodo(y, izq, der)
                        x=evaluar(nodo)
                        pila.apilar(x)
                    else:
                        print("estructura incorrecta")
                        
            elif(token.valor(y)):
                y=int(y)
                pila.apilar(y)
                
            elif(token.variable(y)):
                if(m[j+1]=="="): 
                    variable=Variable(y,pila.desapilar())
                    pila2.apilar(variable)
                else:
                    while len(pila2.items) != 0:
                        variable=pila2.desapilar()   
                        if(y==variable.Nombre):
                            pila.apilar(variable.Valor)
                        pila3.apilar(variable)
                                
                    while len(pila3.items)!= 0:
                        variable=pila3.desapilar()
                        pila2.apilar(variable)
            else:
                print ("entrada incorrecta para: ",y)
            

    print(pila.desapilar())
    token.tabla()
            

                
                
                
            
