# Import modul yang diperlukan
import pygame
from colors import Colors

# Class untuk merepresentasikan papan permainan Tetris
class Grid:
    # Constructor untuk menginisialisasi grid dan membuat grid 20x10 (standard Tetris size)
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()
    
    # Debug method untuk print grid ke console
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()
    
    # Mengecek apakah posisi (row, column) berada di dalam grid
    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False
    
    # Mengecek apakah cell di posisi (row, column) kosong
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    # Mengecek apakah sebuah baris penuh (tidak ada cell kosong)
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    
    # Menghapus sebuah baris (set semua cell ke 0)
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0
    
    # Memindahkan baris ke bawah sejumlah num_rows
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row+num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0
    
    # Mencari dan menghapus semua baris yang penuh
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed
    
    # Mereset grid ke kondisi awal (semua cell kosong)
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0
    
    # Menggambar grid ke screen
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11, 
                self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)