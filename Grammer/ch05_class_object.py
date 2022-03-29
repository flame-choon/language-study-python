# 클래스, 오브젝트

# class

class Person: # 사람 클래스
    # constructor 함수
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    def sayHello(self):
        print("안녕 나는" + self.name)

    def introduce(self):
        print("나의 고향은" + self.hometown)        


p = Person("광진", "서울")
p.sayHello()
p.introduce()


# 상송 클래스
# Programmer 클래스는 Person을 상속하는 클래스
class Programmer(Person):
    def code(self):
        print("나는 코딩을 한다!!!")

# Chef 클래스는 Person을 상속하는 클래스
class Chef(Person):
    def cook(self):
        print("나는 요리를 한다!! 부글부글")


programmer = Programmer("광진", "서울")
programmer.sayHello()
programmer.code()
