# def sayHi():
#     print("Step1")
#     print("Step2")
#     print("Step3")

# sayHi()



# def addPrint(a,b):
#     print("Hello")
#     print(a+b)

# addPrint(3,3)

# addPrint(33,30)

# def greet(name, wish):
#     print(f"hello {name}, {wish}!")


# greet("Livin","Morning")
# greet("Sindhu","Afternoon")

# Hello Livin!, Good Moning!

# def steps():
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("Step4")
#     print("Step5")
    
# print(steps())


# def mulNum(a,b): 
#     return a*b

# print(mulNum(mulNum(3,3),5))

a=10

def func1():
    a=15
    print("The number from inside of function1: "+str(a))
    
def func2():
    print("The number from inside of function2: "+str(a))

# print("The number from outside of function: "+str(a)) 

func1()
func2()