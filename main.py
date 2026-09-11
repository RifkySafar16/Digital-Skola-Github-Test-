def jumlahkan(num_1: int, num_2: int=10):
    return num_1 + num_2


print(jumlahkan(5,15))
print(jumlahkan(5))


class Angka:
    def __init__(self, number: int):
        self.number = number  

    def add_new(self,other_num:int):
        total = jumlahkan(self.number, other_num)
        self.number = total