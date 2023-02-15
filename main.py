class Class1:
    def part_a(self):
        self.a = input("Item 1 - ")


class Class2:
    def part_b(self):
        self.b = input("Item 2 - ")


class Class3(Class1, Class2):
    def __init__(self):
        print("This code combines two strings from different classes together!")
        self.part_a()
        self.part_b()
        print(self.a + self.b)


object3 = Class3()
