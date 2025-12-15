# Class sederhana untuk merepresentasikan posisi koordinat 2D dan menyimpan posisi setiap tile dari block
class Position:
    # Constructor untuk membuat object Position
    def __init__(self, row, column):
        self.row = row
        self.column = column