from example.vector2d import Vector2d


my_vector = Vector2d(4, 6)
print("Defining __bytes__ makes bytes() built-in work")
print(bytes(my_vector))

print("Defining __iter__ makes unpacking work")
my_set = {my_vector}
print(my_set)

