
try:
    num=int(input("Enter a number: "))
    if(num%2==0):
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Enter Valid Number!")
finally:
    print("Executed Sccessfully!")



# try:
#     a=3/0
#     print(a)
# except TypeError:
#     print("String cannot be attached to an integer")
# except ZeroDivisionError:
#     print("Number cannot be divided by 0")
