from stack import Stack


def infix2postfix(expr):
	stack  =  Stack()
	result = ''
	operator = ['+','-','*','/']
	
	for char  in expr:
		print char
		if char == '(':
			None
		elif char in operator:
			stack.push(char)
		elif char == ')':
			result = result + ' ' +  stack.pop()
		else:
			result = result + char 
	return result


print infix2postfix('(A + B)')
