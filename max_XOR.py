#!/bin/python

# Complete the function below.

def XOR(num1, num2):
	num1 = bin(num1)[2::][::-1]
	num2 = bin(num2)[2::][::-1]
	len1 = len(num1)
	len2 = len(num2)
	result = ''
	for i in range(max(len1,len2)):
		if i < min(len1,len2):
			if num1[i] == num2[i]:
				result =  result + '0'
			else :
				result = result + '1'
		elif len1 > len2:
			if num1[i] == '0':
				result = result + '0'
			else:
				result = result + '1'
		else:
			if num2[i] == '0':
				result = result + '0'
			else:
				result = result + '1'
	return result[::-1]


def maxXOR():
    L = int(raw_input())
    R = int(raw_input())
    a = []
    if L == R:
        return 0
    count = 0
    for A in range(L,R+1):
        for i in range(A+1, R+1):
            num = '0b' + XOR(A,i)
            a.append(int(num,2))
    return sorted(a)[len(a)-1]


print maxXOR()
