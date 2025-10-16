class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            print("Object created")
        else:
            print("Object exists")
        return cls._instance

# Test
a = Singleton()
b = Singleton()
c = Singleton()

print(a is b is c)  # True

