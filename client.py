class client:
    def __init__ (self,elm="s1",coins=0,coined=0,count=0):
        self.elm="name"
        self.coins=coins
        self.coined=coined
        self.count=count
    def moneyAdd(self,add=0):
        self.coins+=add
        return self.coins
    def moneySdd(self,sdd=0):
        self.coins-=sdd
        return self.coins
    def money(self,nothing=0):
        return self.coins