class Node: 
def __init__(self, val): 
self.val = val 
self.sons = [] 
self.father = None 

def add_son(self, son): 
self.sons.append(son) 


class Graph: 
def __init__(self, ribs): 
self.root = None 
self.nodes = [] 
self.values = [] 
for i in ribs: 
self.add_node(int(i[0]), int(i[1])) 

def find_node_number(self, val): 
if val in self.values: 
for i in range(len(self.values)): 
if self.values[i] == val: 
return i 
else: 
return None 

def add_node(self, a, b): 
if a not in self.values and b not in self.values: 
self.root = Node(a) 
new_son = Node(b) 
new_son.father = self.root 
self.root.add_son(new_son) 
self.values.append(a) 
self.values.append(b) 
self.nodes.append(self.root) 
self.nodes.append(new_son) 
elif a not in self.values: 
new_son = Node(a) 
num = self.find_node_number(b) 
new_son.father = self.nodes[num] 
self.nodes[num].sons.append(new_son) 
self.values.append(a) 
self.nodes.append(new_son) 
elif b not in self.values: 
new_son = Node(b) 
num = self.find_node_number(a) 
new_son.father = self.nodes[num] 
self.nodes[num].sons.append(new_son) 
self.values.append(b) 
self.nodes.append(new_son) 

def dfs(self, cur_node=None): 
if not cur_node: 
cur_node = self.root 
print(cur_node.val, end=' ') 
for i in cur_node.sons: 
self.dfs(i) 
if cur_node == self.root: 
print() 

def bfs(self, cur_nodes=None): 
if not cur_nodes: 
cur_nodes = [self.root] 
print(self.root.val, end=' ') 
next_nodes = [] 
for i in cur_nodes: 
for j in i.sons: 
next_nodes.append(j) 
if j: 
print(j.val, end=' ') 
if next_nodes: 
self.bfs(next_nodes) 
else: 
print() 


gr = Graph([[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]) 
gr.dfs()
