#varible_scope = where a varible is visible and accessible
#scope resolution = (LEGB) Local-> Enclosed -> Global -> built-in
def func1():
    x=3
    def func2():
        x=4
        print(x)
    func2()
func1()
# here x=4 is local varible and x=3 is enclosed
def func1():
    print(x)
def func2():
    print(x)
x=13
func2()
func1()
#here x=13 is global varible
from math import e
def func1():
    print(e)
func1()
#here e is an built-in