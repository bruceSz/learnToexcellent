def analyser(arg):
	if len(arg) == 1:
		return arg
	if arg[0] != '(':
		return arg.pop(0)
	L = []
	while arg[0] != ')':
		arg.pop(0)
		L.append(analyser(arg[0]))
	if arg[0]==')':
		arg.pop(0)
	return L
		
		
	

if __name__ == "__main__":
	str = raw_input("please input your parentheis string")
	parsed =str.replace('(',' ( ').replace(')',' ) ').split() 
	print analyser(parsed)
	
		
