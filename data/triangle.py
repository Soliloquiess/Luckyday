class Triangle:
    def __init__(self, name, under, height):
        self.name = name
        self.under = under
        self.height = height

    def triangle_print(self):
        print(f'이름 = {self.name}\n밑변 = {self.under}\n높이 = {self.height}')

    def triangle_area(self):
        print('*'*40)
        print(f'삼각형의 넓이 = {(self.under * self.height)/2}')
        print('*' * 40)

    def total(self):
        self.triangle_print()
        self.triangle_area()
        print()