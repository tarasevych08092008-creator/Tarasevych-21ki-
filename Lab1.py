class Humanity:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # інкапсуляція

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Вік не може бути від'ємним")

    def introduce(self):
        print(f"Мене звати {self.name}, мені {self.__age} років.")


class Student(Humanity):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    # Поліморфізм
    def introduce(self):
        print(f"Я студент. Мене звати {self.name}, навчаюсь у {self.university}.")


human = Humanity("Влад", 16)
human.introduce()

student = Student("Владислав", 16, "ТФК ЛНТУ")
student.introduce()