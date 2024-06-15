from datetime import datetime
import functools
import time

def logging(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        for method in dir(instance):
            if method.startswith('__') is False:
                with open('log.txt', 'a', encoding= 'utf-8') as file:
                    file.write("Время создания: {} \nИмя метода: {} \nДокументация метода: {}".format(datetime.utcnow(), method, getattr(instance, method).__doc__))
                    file.write("\n\n")
        return cls(*args, **kwargs)
    return wrapper

@logging
class MyClass:
    def first_method(self):
        """
        This function does something.

        Parameters:
            self (object): The object that called the function.

        Returns:
            None
        """
        print("first method")

    def second_method(self):
        """
        This function does something.

        Parameters:
            self (object): The object that called the function.

        Returns:
            None
        """
        print("second method")

    def third_method(self):
        """
        This function does something.
        """
        print("third method")


my_class = MyClass()
my_class.first_method()
time.sleep(1)
my_class.second_method()
time.sleep(1)
my_class.third_method()