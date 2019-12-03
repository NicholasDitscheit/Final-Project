


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
#function focus versus method focus
# __init__ or str

#
    
