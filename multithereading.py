#multithreading:- used to perform multiple tasks concurrently(multitasking)
#good for I/O bound tasks like reading files or fetching data from APIs
#threading.Thread(target=my_function)
import threading
import time
def walk_dog(shamu):
    time.sleep(8)
    print(f"You finish walking {shamu}")
def work():
    time.sleep(5)
    print("your work is finished")
def mail():
    time.sleep(3)
    print("you get the mail")

task=threading.Thread(target=walk_dog,args=["shamu"])
task.start()
task2=threading.Thread(target=work)
task2.start()
task3=threading.Thread(target=mail)
task3.start()
task.join()
task2.join()
task3.join()
print("all task is finish")
#NOTE: threading is use to run all function at same time
# (target=) use to connect function to task
#(args=) use to pass value to the function but in list ,tuple or set