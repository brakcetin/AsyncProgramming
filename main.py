import time


def my_function1():
    print("1st function is running")
    time.sleep(5)
    print("1st function ended")
    return 5


def my_function2():
    print("2nd function is running")
    time.sleep(5)
    print("2nd function ended")
    return 10


if __name__ == "__main__":
    x = my_function1()
    y = my_function2()

    print(f"Value of x is {x}, after calling my_function1")
    print(f"Value of y is {y}, after calling my_function2")
