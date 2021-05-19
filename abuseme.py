import random

e=input("Enter name of the target: ")
while e!='':
	apologylst=["Sorry","I am really sorry...","I am good for nothing","It was my fault","Its all my fault","Please forgive me...", "I apologize"]
	a=input("You: ")
	print(e+':',random.choice(apologylst))