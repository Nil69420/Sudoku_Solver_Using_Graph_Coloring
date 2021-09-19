from connections import sudoku_connections


class Solution : 
    def __init__(self) : 

        self.board = self.get_board()
        
        self.sudoku_graph = sudoku_connections()
        self.mapped_grid = self.get_mapped_matrix() 

    def get_mapped_matrix(self) : 
        matrix = [[0 for cols in range(9)] 
        for rows in range(9)]

        count = 1
        for rows in range(9) : 
            for cols in range(9):
                matrix[rows][cols] = count
                count += 1
        return matrix

    def get_board(self) : 

        board = [
            [0,0,0,4,0,0,0,0,0],
            [4,0,9,0,0,6,8,7,0],
            [0,0,0,9,0,0,1,0,0],
            [5,0,4,0,2,0,0,0,9],
            [0,7,0,8,0,4,0,6,0],
            [6,0,0,0,3,0,5,0,2],
            [0,0,1,0,0,7,0,0,0],
            [0,4,3,2,0,0,6,0,5],
            [0,0,0,0,0,5,0,0,0]
        ]
        return board

    def print_board(self) : 
        
        print("    1 2 3     4 5 6     7 8 9")
        for i in range(len(self.board)) : 
            if i%3 == 0  :
                print("  - - - - - - - - - - - - - - ")

            for j in range(len(self.board[i])) : 
                if j %3 == 0 : 
                    print(" |  ", end = "")
                if j == 8 :
                    print(self.board[i][j]," | ", i+1)
                else : 
                    print(f"{ self.board[i][j] } ", end="")
        print("  - - - - - - - - - - - - - - ")

    def graph_color(self):
        color = [0] * (self.sudoku_graph.graph.total_vertices+1)
        given = [] 
        for row in range(len(self.board)) : 
            for col in range(len(self.board[row])) : 
                if self.board[row][col] != 0 : 
                    
                    idx = self.mapped_grid[row][col]
                   
                    color[idx] = self.board[row][col] 
                    given.append(idx)
        return color, given

    def graph_algorithm(self, m =9) : 
        
        color, given = self.graph_color()
        if self.algorithm_utility(m =m, color=color, v =1, given=given) is None :
            print(":(")
            return False
        count = 1
        for row in range(9) : 
            for col in range(9) :
                self.board[row][col] = color[count]
                count += 1
        return color
    
    def algorithm_utility(self, m, color, v, given) :
        
        if v == self.sudoku_graph.graph.total_vertices+1  : 
            return True
        for c in range(1, m+1) : 
            if self.is_safe_to_color(v, color, c, given) == True :
                color[v] = c
                if self.algorithm_utility(m, color, v+1, given) : 
                    return True
            if v not in given : 
                color[v] = 0

    def is_safe_to_color(self, v, color, c, given) : 
        
        if v in given and color[v] == c: 
            return True
        elif v in given : 
            return False

        for i in range(1, self.sudoku_graph.graph.total_vertices+1) :
            if color[i] == c and self.sudoku_graph.graph.is_neighbor(v, i) :
                return False
        return True


def main() : 
    s = Solution()
    print("BEFORE SOLVING ...")
    print("\n\n")
    s.print_board()
    print("\nSolving ...")
    print("\n\n\nAFTER SOLVING ...")
    print("\n\n")
    s.graph_algorithm(m=9)
    s.print_board()

if __name__ == "__main__" : 
    main()