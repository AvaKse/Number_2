my_dict = {'1': [''], 
'2': ['a', 'b', 'c'], 
'3': ['d', 'e', 'f'], 
'4': ['g','h', 'i'], 
'5': ['j', 'k', 'l'], 
'6': ['m', 'n', 'o'], 
'7': ['p', 'q', 'r', 's'], 
'8': ['t', 'u', 'v'], 
'9': ['w', 'x', 'y', 'z'], 
'0': [' ']} 
s = input() 


def wr(s1, string): 
if len(string) == 1: 
for i in my_dict[string]: 
print(s1+i) 
else: 
for i in my_dict[string[0]]: 
s1 += i 
wr(s1, string[1:]) 
s1 = s1[:len(s1) - 1] 

wr('', s)
