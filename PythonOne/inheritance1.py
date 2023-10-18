class Phone:

    def __init__(self):
        print("I am Phone class")

    def call(self):
        print("You can call.")

    def message(self):
        print("You can Message.")


class Samsung(Phone):

    def __init__(self):
        super().__init__()
        print("I am Samsung class")

    def photo(self):
        print("You can click photo.")


sph1 = Samsung()
sph1.call()
sph1.message()
sph1.photo()

print(issubclass(Samsung,Phone))