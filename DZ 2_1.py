s = input() 
ans = 0 
for i in range(len(s)): 
if i > 0 and (len(s) % i) == 0: 
t = s[:i] 
if s == t * (len(s) // len(t)) and (len(s) // len(t)) > ans: 
ans = (len(s) // len(t)) 
print(ans)
