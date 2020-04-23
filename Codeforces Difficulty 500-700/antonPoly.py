shapes = {"Tetrahedron": 4,
            "Cube": 6,
            "Octahedron" : 8,
            "Dodecahedron": 12,
            "Icosahedron" : 20}
count = 0
n = int(input())
for _ in range(n):
    count += shapes[input()]
print(count)