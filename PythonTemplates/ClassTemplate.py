

class TemplateClass:
    # Not needed - will be shared among all of this kind of object
    kind = 'example'
    myList = []

    # Initial set up. Define what the inputs should be.
    # Can also assign default values as shown
    def __init__(self, name, var1,  var2=0):
        self.name = name
        self.var1 = var1
        self.var2 = var2

    # Example of how to add class method. Here adding to list
    def add_list(self, item):
        self.myList.append(item)


# This just shows how to define and use the class 
bob = TemplateClass("Bob", 17, 3)
bob.add_list("Nuts")

print(bob.kind,
      bob.myList,
      bob.name,
      bob.var1,
      bob.var2)
