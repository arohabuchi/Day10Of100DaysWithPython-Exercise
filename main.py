####################################### TUPLE #####################################################
#tuple is an immutable list of value, it is coma separated list of value ssometime enclosed in a parenthesis

t = 1,3,4,7,8
print(type(t))
t = (1,2,3,4)
print(type(t))
t=()
print(type(t))
#Note that single element is not a tuple unless you include a trailing coma
t=4 #not a tuple
print(type(t))
t=3, #it is a tuple
print(type(t))

#tuple are immutable
t = (1,2,3,4)
# t[2]=7 #this will throw error

# tuple function
len(t) #length
max(t) #max value
min(t) #min value

# converting list to tuple
l=[1,2,3,4]
print(tuple(l))

#concatenation of tuple
t = (1,2,3,4)
t1 = (1,2,3,4)
tt1 = t+t1
print(tt1)

#tuple indexing
t = (1,2,3,4)
print(t[3])


#########################################  BASIC I/O ##########################################################
print("hello \nit is a new day")

#input from a file
with open('hi.txt', 'w') as  fobj:
    fobj.write("hi \n friends")

with open('hi.txt', 'r') as  f:
    li1 =[]
    for i in f:
        li1.append(i)
print(li1)

#using input and raw_input
def inputNumber(msg, err_msg=None):
    while True:
        try:
            return  float(input(msg))
        except ValueError:
            if err_msg is not  None:
                print(err_msg)
    pass
uerN = inputNumber('Input a number :')
print(uerN)
#there are more to be done with file