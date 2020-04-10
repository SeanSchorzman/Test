#Functions

f = lambda x,y: x+y			#Lambda is a nameless function, 
							#where x,y are parameters, and then code to be executed (x+y)

d = lambda a: lambda b: lambda c: a*b*c		#Variable with nested functions (lambda operator = nameless function)
											#Parameters a,b, and c. With respective lambda function. 
												
e = lambda c: lambda a,b: lambda d: (c*(a+b))%d 		#Parameter c with first lamda function
														#Parameter a, b with second lamda function
														#Paramter d with final function 


print(f(2,3))								#Call variable f which call function lamda
											#that has to parameters x,y 

print(d(5)(2)(3))							#Call variable f which call function lamda
											#that has to parameters a,b, and c.

print(e(2)(4,3)(11))							#Parameters are separated by parantheses for each function
										 	#not per parameter, per function. 