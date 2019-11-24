class Rib: 
    def __init__(self, beg, end, val): 
        self.beg = beg 
        self.end = end 
        self.val = val 


class Node: 
    def __init__(self, val): 
        self.val = val 
        self.nei = [] 

    def add_nei(self, nei, rib_val): 
        self.nei.append((nei, rib_val)) 

    def __str__(self): 
        return self.val 


class Graph: 
    """ 
      values - названия вершин 
      nodes - сами вершины 
    """ 
    def __init__(self, ribs): 
        self.nodes = [] 
        self.values = [] 
        for i in ribs: 
            self.add_node(i) 

    def find_num_of_node(self, val): 
        for i in range(len(self.values)): 
            if self.values[i] == val: 
                return i 

    def add_node(self, rib): 
      """ 
        добавление вершины в граф 
      """ 
        if rib[0] not in self.values and rib[1] not in self.values: 
            new_node_1 = Node(rib[0]) 
            new_node_2 = Node(rib[1]) 
            new_node_1.add_nei(new_node_2, rib[2]) 
            self.nodes.append(new_node_1) 
            self.nodes.append(new_node_2) 
            self.values.append(rib[0]) 
            self.values.append(rib[1]) 
            elif rib[0] not in self.values: 
            new_node = Node(rib[0]) 
            num_of_node = self.find_num_of_node(rib[1]) 
            new_node.add_nei(self.nodes[num_of_node], rib[2]) 
            self.nodes.append(new_node) 
            self.values.append(rib[0]) 
        elif rib[1] not in self.values: 
            new_node = Node(rib[1]) 
            num_of_node = self.find_num_of_node(rib[0]) 
            self.nodes[num_of_node].add_nei(new_node, rib[2]) 
            self.nodes.append(new_node) 
            self.values.append(rib[1]) 
        else: 
            node1 = self.nodes[self.find_num_of_node(rib[0])] 
            node2 = self.nodes[self.find_num_of_node(rib[1])] 
            node1.add_nei(node2, rib[2]) 

    def max_path(self, nodeStart): 
    """ 
      адгоритм Дейкстры 
    """ 
        u = set() 
        dist = {} 
        for i in self.values: 
            dist[i] = float('inf') 
        dist[nodeStart] = 0 
        while len(u) < len(self.values): 
            cur_node = None 
            cur_min = float('inf') 
            for i in dist: 
                if i not in u and dist[i] < cur_min: 
                    cur_node = self.nodes[self.find_num_of_node(i)] 
                    cur_min = dist[i] 
            if cur_min == float('inf'): 
                return -1 
            u.add(cur_node.val)
            for i in cur_node.nei: 
                if i[1] + dist[cur_node.val] < dist[i[0].val]: 
                    dist[i[0].val] = i[1] + dist[cur_node.val] 
        return dist[max(dist, key=lambda x: dist[x])] 


gr = Graph([[2, 1, 1], [2, 3, 1], [3, 4, 1]]) 
print(gr.max_path(2))
