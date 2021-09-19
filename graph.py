class Node:

    #constructor
    def __init__(self, idx, data=0):
        self.id = idx
        self.data = data
        self.connectedto = dict()

    def add_neighbor(self, neighbor, weight=0):
        if neighbor.id not in self.connectedto.keys():
            self.connectedto[neighbor.id] = weight     

    #setter
    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    #getter
    def get_connections(self):
        return self.connectedto.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connectedto[neighbor.id]

    def _str_(self):
        return str(self.data) + " Connected to : "+ \
            str([x.data for x in self.connectedto])


class Graph:

    total_vertices = 0

    def __init__(self):
        self.all_nodes = dict()

    def add_node(self, idx):
        if idx in self.all_nodes:
            return None

        Graph.total_vertices += 1
        node = Node(idx=idx)
        self.all_nodes[idx] = node
        return node

    def add_node_data(self, idx, data):
        if idx in self.all_nodes:
            node = self.all_nodes[idx]
            node.set_data(data)
        else:
            print("No ID to add to the data")

    def add_edge(self, start_edge, end_edge, wt=0):
        self.all_nodes[start_edge].add_neighbor(self.all_nodes[end_edge], wt)
        self.all_nodes[end_edge].add_neighbor(self.all_nodes[start_edge], wt)

    def is_neighbor(self, u, v):
        if u>=1 and u<=81 and v>=1 and v<=81 and u!=v:
            if v in self.all_nodes[u].get_connections():
                return True

        return False

    def print_edges(self):
        for idx in self.all_nodes:
            node = self.all_nodes[idx]
            for con in node.get_connections():
                print(node.get_id(), "-->", 
                self.all_nodes[con].get_id())

    #getter
    def get_node(self, idx):
        if idx in self.all_nodes:
            return self.all_nodes[idx]
        return None

    def get_all_nodes_ids(self):
        return self.all_nodes.keys()