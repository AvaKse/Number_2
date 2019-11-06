text = [] 
while True: 
s = input() 
text += list(s.split()) 
if s == '': 
break 
dic = {} 
for i in text: 
if i not in dic: 
dic[i] = 1 
else: 
dic[i] += 1 
maxi = 0 
ans = '-' 
for i in dic: 
if dic[i] > maxi: 
maxi = dic[i] 
ans = i 
elif dic[i] == maxi: 
ans = '-' 
print(ans)
