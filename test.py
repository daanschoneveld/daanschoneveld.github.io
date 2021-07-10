getallen = []

for i in range(10):
    if i > 6:
        getallen.append(i)

print(getallen)

getallen = [i for i in range(10) if i > 6]

print(getallen)
