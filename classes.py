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
        
    def Hello_Planet(self):
        planets = ["SATURN", "WORLD", "JUPITER", "VENUS", "NEPTUNE", "MARS", "MERCURY", "URANUS"]
        hello_planet = []
        for t in self.to_print:
            for w in t:
                for p in planets:
                    if w.upper() == p:
                        hello_planet.append(w)
        
        for i in hello_planet:
            print(f"Hello {i}")