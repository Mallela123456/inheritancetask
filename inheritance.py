#inheritance:
class Animals():
    def p(self):
        print("thisis lion")
class child(Animals):
    def c(self):                       #inheritance
        print("this is tiger")
inheritance = child()
inheritance.p()
inheritance.c()
        
class Lion():
    def king(slef):
        print("i am king of forest")
class Tiger(Lion):
    def younger(self):
        print("i am younger of this forest")     #multilevel inheritance
class monkey(Tiger):
    def smaller(self):
        print("i am gamer of the forest")

multi = monkey()
multi.king()
multi.younger()
multi.smaller()


class Elephant():
    def king(slef):
        print("i am elder of the forest")
class Elphant2():
    def younger(self):
        print("i am Elder1 of the forest")     #multiple inheritance
class small_elephant(Elephant,Elphant2):
    def smaller(self):
        print("i are childerns of Elephant")
        
multiple = small_elephant()
multiple.king()
multiple.younger()
multiple.smaller()
        
        
class officer():
    def police(self):
        print("i am the officer of the forest")
class conistable(officer):
    def cons(self):
        print("i am the conistable of the forest")
class conistable2(officer):
    def cons2(self):
        print("i am second conistable forest")


inheritance = child()
inheritance.p()
inheritance.c()
multi = monkey()
multi.king()
multi.younger()
multi.smaller()
multiple = small_elephant()
multiple.king()
multiple.younger()
multiple.smaller()     
hie = conistable()
hie2 = conistable2()
hie.police()
hie.cons()
hie2.police()
hie2.cons2()