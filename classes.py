class StayClassy():
    def __init__(self, *text):
        self.to_print = [text]
    
    def Print_All(self):
        for i in self.to_print:
            for v in i:
                print(v)
                
    def Sponge_Case(self):
        result = ""
        for i in self.to_print:
            for v in i:
                for q in range(len(v)):
                    if q % 2 == 0:
                        result += v[q].upper()
                    else:
                        result += v[q].lower()
                        
        print(result)  