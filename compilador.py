import re

exp_valor = re.compile('[0-9]+$')
exp_operador = re.compile('[\+\*\-/=]{1,1}$')
exp_variable = re.compile('([a-z]+)([A-Z0-9_]*)$')


m = exp_variable.search('2casa')
print m.group(0)

print exp_variable.match("a")
