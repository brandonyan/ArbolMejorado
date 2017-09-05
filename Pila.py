class Pila(object):
	def __init__(self):
		self.items=[]
		
	def apilar(self, dato):
		self.items.append(dato)
		
	def desapilar(self):
		if self.esta_vacia():
			return None
		else:
                        return self.items.pop()
                        
			
	def esta_vacia(self):
		if len(self.items)==0:
			return True
		else:
			return False
		
	
	
