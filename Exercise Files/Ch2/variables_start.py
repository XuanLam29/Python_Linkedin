# 
# Example file for variables
#

# Declare a variable and initialize it
#f="abc"
#print(f)


# re-declaring the variable works

f=0

# ERROR: variables of different types cannot be combined
#print("this is a string "+ str(123))


# Global vs. local variables in functions

def someFuntion():
    global f
    f= "def"
    print(f)

someFuntion()
print(f)


