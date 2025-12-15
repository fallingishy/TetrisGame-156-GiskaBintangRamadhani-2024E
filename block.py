# Import modul yang diperlukan
from colors import Colors
import pygame
from position import Position

class Block:
    # Menginisialisasi block
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()
    
    # Menggerakkan block dengan menambah offset
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns
    
    # Mengembalikan posisi absolut dari semua tiles dalam block
    def get_cell_positions(self):
        # Mengambil tiles untuk state rotasi saat ini
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        # Menambahkan offset ke setiap tile
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
    
    # Merotasi block searah jarum jam
    def rotate(self):
        self.rotation_state += 1
        # Wrap around ke state 0 jika melebihi jumlah state
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0
    
    # Membatalkan rotasi terakhir
    def undo_rotation(self):
        self.rotation_state -= 1
        # Wrap around ke state terakhir jika kurang dari 0
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1
    
    # Menggambar block ke screen
    def draw(self, screen, offset_x, offset_y):
        # Mengambil posisi semua tiles
        tiles = self.get_cell_positions()
        # Menggambar setiap tile sebagai persegi panjang
        for tile in tiles:
            # Menghitung posisi dan ukuran persegi panjang
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
                offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            # Menggambar persegi panjang dengan warna sesuai block id
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)