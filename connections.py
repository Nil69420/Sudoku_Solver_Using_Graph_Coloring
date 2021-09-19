from graph import Graph

class sudoku_connections:

    def __init__(self):
        self.graph = Graph()
        self.rows = 9
        self.cols = 9
        self.grid = self.rows*self.cols
        self.generate_nodes() #generates nodes
        self.connect_nodes() #connects all nodes
        self.all_ids = self.graph.get_all_nodes_ids() #stores ids in list

    def generate_nodes(self):
        for idx in range(1, self.grid + 1):
            _=self.graph.add_node(idx)

    def connect_nodes(self):
        matrix = self.get_grid_matrix()
        head_connections = dict()

        for row in range(9):
            for col in range(9):
                head = matrix[row][col]
                connections = self.what_to_connect(matrix, row, col)
                head_connections[head] = connections

        #connect all edges
        self.connect_those(head_connections = head_connections)                


    def connect_those(self, head_connections):
        for head in head_connections.keys():
            connections = head_connections[head]

            for key in connections:
                for v in connections[key]:
                    self.graph.add_edge(start_edge=head, end_edge=v)

    def get_grid_matrix(self):
        matrix = [[0 for cols in range(self.cols)]
        for rows in range(self.rows)]

        count = 1
        for rows in range(9):
            for cols in range(9):
                matrix[rows][cols] = count
                count += 1
        return matrix            

    def what_to_connect(self, matrix, rows, cols):
        connections = dict()
        row = []
        col = []
        grid = []

        #rows
        for i in range(cols+1, 9):
            row.append(matrix[rows][i])

        connections["rows"] = row

        #columns
        for j in range(rows+1, 9):
            col.append(matrix[j][cols])

        connections["cols"] = col

        #grid
        if rows % 3 == 0:

            if cols % 3 == 0:
                grid.append(matrix[rows+1][cols+1])
                grid.append(matrix[rows+1][cols+2])
                grid.append(matrix[rows+2][cols+1])
                grid.append(matrix[rows+2][cols+2])

            elif cols % 3 == 1:
                grid.append(matrix[rows+1][cols-1])
                grid.append(matrix[rows+1][cols+1])
                grid.append(matrix[rows+2][cols-1])
                grid.append(matrix[rows+2][cols+1])

            elif cols % 3 == 2:
                grid.append(matrix[rows+1][cols-2])
                grid.append(matrix[rows+1][cols-1])
                grid.append(matrix[rows+2][cols-2])
                grid.append(matrix[rows+2][cols-1])    

        elif rows % 3 == 1:

            if cols % 3 == 0:
                grid.append(matrix[rows-1][cols+1])
                grid.append(matrix[rows-1][cols+2])
                grid.append(matrix[rows+1][cols+1])
                grid.append(matrix[rows+1][cols+2])

            elif cols % 3 == 1:
                grid.append(matrix[rows-1][cols-1])
                grid.append(matrix[rows-1][cols+1])
                grid.append(matrix[rows+1][cols-1])
                grid.append(matrix[rows+1][cols+1])

            elif cols % 3 == 2:
                grid.append(matrix[rows-1][cols-2])
                grid.append(matrix[rows-1][cols-1])
                grid.append(matrix[rows+1][cols-2])
                grid.append(matrix[rows+1][cols-1])

        elif rows % 3 == 2:

            if cols % 3 == 0:
                grid.append(matrix[rows-2][cols+1])
                grid.append(matrix[rows-2][cols+2])
                grid.append(matrix[rows-1][cols+1])
                grid.append(matrix[rows-1][cols+2])

            elif cols % 3 == 1:
                grid.append(matrix[rows-2][cols-1])
                grid.append(matrix[rows-2][cols+1])
                grid.append(matrix[rows-1][cols-1])
                grid.append(matrix[rows-1][cols+1])

            elif cols % 3 == 2:
                grid.append(matrix[rows-2][cols-2])
                grid.append(matrix[rows-2][cols-1])
                grid.append(matrix[rows-1][cols-2])
                grid.append(matrix[rows-1][cols-1])    

        connections["grids"] = grid
        return connections

    