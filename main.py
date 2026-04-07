name = "Tanu"

age = "20" # BUG 1: age should be int, not string

def greet(name):

print(f"Hello, {name}!") # BUG 2: missing indentation

def check_age(age):

if age = 18: # BUG 3: = should be ==

print("You are 18")

def calculate(a, b):

result = a / 0 # BUG 4: division by zero

return result

def add(a, b):

return a + b

total = add(5) # BUG 5: missing second argumen

def count():

while i < 5:

print(i) # BUG 6: i never

def main():

greet(name)

check_age(age)

calculate(10, 2)

count()

if name == " main ":

main()
