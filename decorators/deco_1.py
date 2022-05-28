#!/usr/bin/python3

class Myclass:
    def __init__(self, func):
        self.func = func
        self.numcalls = 0

    def __call__(self, *args, **kwargs):
        self.numcalls += 1
        print("start")
        print(f"execut {self.numcalls} times")
        return self.func(*args, **kwargs)

@Myclass
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()
