cdef class Fruit(object):
    cdef char* name 
    cdef double qty 
    cdef double price

    def __init__(self, nm, qt, pc):
        self.name = nm
        self.qty = qt
        self.price = pc

    def amount(self):
        return self.qty * self.price


def display_amount():
    cdef Fruit apple = Fruit(b"apple", 10, 2.5)
    print(f"The amount of {apple.name} is {apple.amount()}")
