class A:

    def __init__(self):
        self.title = "A"

    def print(self):
        print(self.title)


class B:

    def __init__(self):
        self.title = "B"
        self.listOfA = []

    def print(self):
        print(self.title)
        for item in self.listOfA:
            item: A
            item.print()


testB = B()
testA1 = A()
testA2 = A()
testB.listOfA.append(testA1)
testB.listOfA.append(testA2)
testB.print()
