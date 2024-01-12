def add_new_tile(self, number: int = 2):
        empty_cells = list(zip(*np.where(self.matrix == 0)))
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.matrix[row, col] = number