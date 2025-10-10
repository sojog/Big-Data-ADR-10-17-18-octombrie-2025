
### LISTA
#      0   1     2    3   4
x = [ 201, 301, 401, 501, 601]
print(x, type(x))

print("Primul element:",  x[0])
print("Ultimul element:", x[4])


## TUPLE
x = (201, 301, 401, 501, 601)
print(x, type(x))

print("Primul element:",  x[0])
print("Ultimul element:", x[4])

### RANGE
x = range(100)
print(x, type(x))
print(list(x))

### DICTIONAR
x = {
    "rosu": 201, "verde":301, "albastru": 401, "negru":501, "alb":601
}
print(x, type(x))
print("Primul element:", x["rosu"])
