a = 30
b = 0

try:
    c=a/b
    print(c)
except:
    print("error, b value can't be zero")
# else:
#      print("try block is working")

finally:
    print("this finally block")