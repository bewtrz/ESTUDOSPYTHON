class Television: #QUESTÃO 06 part.1
    Volume = 0
    Canal = 14
    
    def AumentarVolume(self):
        self.Volume += 1 if self.Volume != 100 else 0
        self.Volume = 100 if self.Volume > 100 else self.Volume
        
    def BaixarVolume(self):
        self.Volume -= 1 if self.Volume != 0 else 0
        self.Volume = 0 if self.Volume < 0 else self.Volume
        
    def AumentarCanal(self):
        self.Canal += 1 if self.Canal != 69 else 0
        self.Canal = 69 if self.Canal > 69 else self.Canal

    def BaixarCanal(self):
        self.Canal -= 1 if self.Canal != 14 else 0
        self.Canal = 14 if self.Canal < 14 else self.Canal
        
    def MudarCanal(self, value):
        self.Canal = value if value > 14 and value < 69 else self.Canal
