class Human():
    """인간"""
    def __init__(self, name, weight):
        """초기화 메서드"""
        print("init 실행")
        self.name = name
        self.weight = weight
        print("이름: {}, 몸무게: {}".format(name, weight))

    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))

    def speak(self, message):
        print("{}(이)가 {}라고 말합니다.".format(self.name, message))

    def __str__(self):
        """문자열화 메서드"""
        return "{}(몸무게 {}kg)".format(self.name, self.weight)


person = Human("사람", 60.5)
print(person.name)
print(person.weight)
print(person.speak("하하호호"))
print(person)
