class Player:
    def __init__(self,nameStr,startHp,startAtt,startDef):
        self.name=nameStr
        self.hp=startHp
        self.att=startAtt
        self.dfns=startDef

    def takeDmg(self,dmgAmt):
        self.hp-=(dmgAmt/self.dfns)
        if(self.hp<=0):
            self.die()

    def die(self):
        print("YOUR DED")

    def dealDmg(self):
        return self.att

    def use(self):
        print("using this damn item")

    def discard(self):
        print("you discarded the item!")

    def pickup(self):
        print("you picked up the item!")
