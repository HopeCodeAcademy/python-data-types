#numbers
print("0->",bool(0))
print("0.0->",bool(0.0))
print("1->",bool(1))
print("5->",bool(5))

#strings
print("''->",bool(''))
print("'False'->",bool('False'))

#lists
print("[]->",bool([]))
print("[1, 2, 3]->",bool([1, 2, 3]))

#tuples
print("()->",bool(()))
print("(1, 2, 3)->",bool((1, 2, 3)))

#sets
print("{}->",bool({}))
print("{1, 2, 3}->",bool({1, 2, 3}))

#none
print("None->",bool(None))