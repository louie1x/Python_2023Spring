# class Person:
#     def __init__(self, name, age, favoritefood):
#         self.name = name
#         self.age = age
#         self.favoritefood = favoritefood

#     # 方法 Method
#     def introduce(self):
#         print("我是"+self.name+"，我今年"+str(self.age)+"歲，最喜歡吃"+self.favoritefood+"。")

#     def shout(self, content):
#         print("我大喊："+content)

# # 建立物件
# Louie = Person("Louie", 13, "Steak")
# # 呼叫行為
# Louie.introduce()
# Louie.shout("我不知道要喊什麼")


# # 人類類別
# class Person:
#     state = "healthy" #類別屬性: 屬性類別的屬性，而不是物件！

#     # 實體方法 (Instance Method)
#     def getcold(self):
#         self.__class__.state = "sick"

# print("Origin: I'm", Person.state)
# Louie=Person()
# Louie.getcold()
# print("After getcold(): I'm", Person.state)


# class Person:

#     # 建構式
#     def __init__(self, eyesColor, hairColor):
#         self.eyesColor = eyesColor
#         self.hairsColor = hairColor

#     # 美國人
#     @classmethod
#     def American(cls):
#         return cls("blue", "brown")
    
#     # 台灣人
#     @classmethod
#     def Taiwanese(cls):
#         return cls("black", "black")
    

#     def introduce(self):
#         print("My eyes are "+self.eyesColor+" and my hair are "+self.hairsColor)

# American = Person.American()
# Taiwanese = Person.Taiwanese()
# American.introduce()
# Taiwanese.introduce()


# class Person:
    
#     @staticmethod
#     def work(workinghour):
#         print("Working Hour: "+str(workinghour))

# Louie = Person()
# Louie.work(8)