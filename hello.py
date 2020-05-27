print("Hello, World!")

thistuple = ("apple", "banana", "cherry")
print(thistuple)

x = 5
y = "John"
print(x)
print(y)

x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

thislist = ["apple", "banana", "cherry"]
print(thislist)

def my_function():
  print("Hello from a function")

my_function()

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
