# Import base class dan Position
from block import Block
from position import Position

# Block berbentuk huruf L yang memiliki 4 state rotasi
class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        # Definisi 4 state rotasi dengan posisi relatif dari origin (0,0)
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],    # Rotasi 0°
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],    # Rotasi 90°
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],    # Rotasi 180°
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]     # Rotasi 270°
        }
        # Set posisi awal di tengah atas grid
        self.move(0, 3)

# Block berbentuk huruf J (mirror dari L) yang memiliki 4 state rotasi
class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        # Definisi 4 state rotasi
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.move(0, 3)

# Block berbentuk huruf I yang memiliki 4 state rotasi
class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        # Definisi 4 state rotasi
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(1, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        # I Block spawn sedikit lebih tinggi karena bentuknya panjang
        self.move(-1, 3)

# Block berbentuk huruf O atau kotak dan hanya memiliki 1 state rotasi (tidak berubah saat dirotasi)
class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        # Hanya 1 state rotasi karena bentuknya symmetrical
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        self.move(0, 4)

# Block berbentuk huruf S yang memiliki 4 state rotasi
class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        # Definisi 4 state rotasi
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

# Block berbentuk huruf T yang memiliki 4 state rotasi
class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        # Definisi 4 state rotasi
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

# Block berbentuk huruf Z (mirror dari S) yang memiliki 4 state rotasi
class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        # Definisi 4 state rotasi
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        self.move(0, 3)
