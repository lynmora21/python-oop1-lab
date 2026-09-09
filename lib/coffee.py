#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        # Store the coffee size and price.
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Only allow Small, Medium, or Large coffee sizes.
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Print a thank-you message and increase the price by $1.
        print("This coffee is great, here’s a tip!")
        self.price += 1

