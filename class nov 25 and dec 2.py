


#tuples are the same as lists but are immutable sequences
#can make a list of data that you ARE NOT GOING TO CHANGE it is safer
#slides go over how to make a tuple and the syntax that is involved
#You can index slice the same as lists the only difference is that they cannot be changed the 
#only way to change is to make a new tuple from the old tuple and cacantinate them.
#tuples are safer to use when passing them into functions
#common use for tuples include: swapping two variables, Tuple assignment use tuples on both sides and python will automatically transfer
#Tuples can be used as a return value this allows you to return any number of values that you want at one time


#t = tuple()
#t = "a" , 1, "b", 2, 3.14
#print(t)
#print(t[1])
#print(t[1:3])


#example of a tuple swap
#tuple2 = 0.1,
#t, tuples2 = tuple2, t
#print(t)
#print(tuple2)


#t = 1, 2, 5, 17, 3

#def min_max(seq):
#    return min(seq), max(seq)

#min1, max1 = min_max(t)

#print(min1, max1)



t = tuple()

def divide( divident, divisor):
    quot = divident // divisor
    remain = (divident % divisor)
    return quot, remain

quot, remain = divide(10, 3)
#or
#t = divide(10, 3)

print(quot, remain)


t = ("a", "b", "c", "d")
def split_tuple(t):
    odd = t[::2]
    even = t[1::2]
    return odd, even

odd, even = split_tuple(t)
print(odd, even)




# object-orientated programming and the real world
#function focus ex. print(obj) versus method focus ex. obj.print
# __init__ for creating and initializing an object or __str__ for returning 
#

class Currency:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
    def get_usd(self):
        return self.dollars + self.cents * 0.01
    
    def get_euro(self):
        return round(self.get_usd() * .9, 2)

    def get_yen(self):
        return round(self.get_usd() * 108.96) 

    def get_jmd(self):
        return round(self.get_usd() * 140.56)

    def __str__ (self):
        return ("USD: $%.2f\nEuro: $%.2f\nYEN: $%d\njmd: $%.2d" %
            (self.get_usd(), self.get_euro(), self.get_yen(), self.get_jmd()))

    def __add__(self, rhs):
        sum = Currency(self.dollars + rhs.dollars, self.cents + rhs.cents )
        return sum

    def __sub__(self, rhs):
        subtraction = Currency(self.dollars - rhs.dollars, self.cents + rhs.cents)
        return subtraction


currency = Currency(5, 20)
print (currency.get_euro())

#operator overloading

currency2 = Currency(7, 91)
currency3 = Currency(100, 50)
print (currency + currency2)
print (currency - currency2)