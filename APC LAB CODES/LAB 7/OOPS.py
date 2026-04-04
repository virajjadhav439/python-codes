# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def grade(self):
#         avg = sum(self.marks) / len(self.marks)
#         return "A" if avg >= 75 else "B" if avg >= 50 else "C"


# class Manager :
#     def __init__(self):
#         self.data = []

#     def add(self, s):
#         self.data.append(s)

#     def show(self):
#         for s in self.data:
#             print(f"{s.name} -> {s.marks} -> {s.grade()}")


# m = Manager()
# m.add(Student("Viraj", [80, 90, 70]))
# m.add(Student("Rahul", [40, 50, 60]))

# m.show()


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)


class Car(Vehicle):   # inheritance
    def __init__(self, brand, speed):
        super().__init__(brand)   # parent ka constructor call
        self.speed = speed

    def show_details(self):
        self.show_brand()
        print("Speed:", self.speed)


c1 = Car("BMW", 200)
c1.show_details()