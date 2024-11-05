class Human:
    def __init__(self,n ,o):
        self.name = n
        self.occcupation = o

    def do_work(self):
        if self.occcupation == "tennis player":
            print(self.name,  "plays tennis")
        elif self.occcupation == "actor":
            print(self.name , "shoots a film")

    def speaks(self):
        print(self.name , "says how are you")

tom = Human("tom cruise","actor" )
tom.do_work()
tom.speaks()

maria = Human("maria sharapova", "tennis player")
maria.do_work()
maria.speaks()