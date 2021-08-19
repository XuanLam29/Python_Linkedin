#
# Example file for working with classes
#
class myClass():
    def method1(self):
        print("class method1")
    def method2(self, someString):
        print("class method2", someString)

class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherclass method1")
    def method2(self, someString):
        myClass.method2(self, "string2")
        print("anotherclass method2", someString)

def main():
    c = myClass()
    c.method1()
    c.method2("this is string")
    c = anotherClass()
    c.method1()
    c.method2("lyly")
if __name__ == "__main__":
    main()
