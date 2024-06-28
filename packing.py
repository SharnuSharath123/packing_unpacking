# Packing : it is used to pack the data in a secured type and send it to function designation.
# '*' operator is used to pack the single value in tuple

def sample(*a):
    print(a)
    type(a)

sample()
sample(44)
sample(12,34,56,78)