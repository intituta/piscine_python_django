#!/usr/bin/python3
def print_val_and_type(val):
	print("{0} est de type {1}".format(val, type(val)))
def my_var():
	print_val_and_type(42)
	print_val_and_type("42")
	print_val_and_type("quarante-deux")
	print_val_and_type(42.0)
	print_val_and_type(True)
	print_val_and_type([42])
	print_val_and_type({42: 42})
	print_val_and_type((42,))
	print_val_and_type(set())
if __name__ == '__main__' :
    my_var()
