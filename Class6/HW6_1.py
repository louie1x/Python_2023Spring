class Class:

    # 建構式
    def __init__(self, teacher, time):
        self.teacher = teacher
        self.time = time

    @classmethod
    def Math(cls):
        return cls("Emma", "Monday")
    
    @classmethod
    def Englush(cls):
        return cls("Peter", "Thursday")
    

    def summary(self):
        print("This Lesson is taught by "+self.teacher+" on "+self.time)

Math = Class.Math()
English = Class.Englush()
Math.summary()
English.summary()