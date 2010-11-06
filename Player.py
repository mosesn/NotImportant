class Player:
    def __init__(self,nameStr,startHp,startAtt,startDef):
        global name
        global att
        global def
        global hp
        name=nameStr
        hp=startHp
        att=startAtt
        def=startDef

    def takeDmg(self,dmgAmt):
        hp-=(dmgAmt/def)
        if(hp<=0):
            self.die()

    def die(self):
        print("YOUR DED")

    def dealDmg(self):
        return att

    def use(self):
        print("using this damn item")

    def discard(self):
        print("you discarded the item!")

    def pickup(self):
        print("you picked up the item!")
