import re
from Pila import *

exp_valor = re.compile('[0-9]+$')
exp_operador = re.compile('[\+\*\-/=]{1,1}$')
exp_variable = re.compile('([a-z]+)([A-Z0-9_]*)$')

tokens=Pila()
    
class Token():
    def  __init__ (self, tipo, valor):
        self.Valor=valor
        self.Tipo=tipo
        
class Lex(object):    

    def  __init__ (self):
        self.Valor=0

    def operador(self, dato):
        if(exp_operador.match(dato) != None):
            token=Token("ope",dato)
            tokens.apilar(token)
            return True
        else:
            return False

    def valor(self, dato):
        if(exp_valor.match(dato) != None):
            token=Token("val",dato)
            tokens.apilar(token)
            return True
        else:
            return False

    def variable(self, dato):
        if(exp_variable.match(dato) != None):
            token=Token("var",dato)
            tokens.apilar(token)
            return True
        else:
            return False

    def tabla(self):
        while len(tokens.items) != 0:
            token=tokens.desapilar()
            print(token.Tipo,"=",token.Valor)

