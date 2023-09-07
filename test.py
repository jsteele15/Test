print("hello world")

class StayClassy():
    def __init__(self, *text):
        self.to_print = [text]
    
    def Print_All(self):
        for i in self.to_print:
            for v in i:
                print(v)
            
words = StayClassy("Hello", "world", "jam", "boner")

words.Print_All()            