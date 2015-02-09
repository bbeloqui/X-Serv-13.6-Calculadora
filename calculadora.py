#!/usr/bin/python

print "Introduce la funcion"
funcion= (raw_input() )
try:
	print "Introduce el primer operador"
	operando1= float(raw_input() ) 
	print "Introduce el segundo operador"
	operando2= float(raw_input() )
except ValueError:
	print "Solo numeros en los operadores"

if funcion == ('*'):
	try: 
		resultado1= operando1 * operando2
		print 'El resultado es: ' +str(resultado1)
	except :
		print "Siga las indicaciones por favor"
elif funcion == '-' :
	try: 
		resultado2= operando1 - operando2
		print 'El resultado es: '+ str(resultado2)
	except :
		print "Siga las indicaciones por favor"
elif funcion == '+' :
	try:
		resultado3= operando1 + operando2
		print 'El resultado es: '+ str(resultado3) 
	except :
		print "Siga las indicaciones por favor"
elif funcion == '/' :
	try:
		resultado4= operando1 / operando2
		print "El resultado es: "+ str(resultado4) 
	except ZeroDivisionError:
		print " Indeterminacion.No se permite la division entre 0"  
	except NameError	:
		print "Siga las indicaciones por favor"
else :
	     print "Siga las indicaciones por favor \nSolo +  -  *  /  en funcion"    
	





