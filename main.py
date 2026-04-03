result = []

def divider(a, b):
    if b == 0:
        return 0
    if a < b:
        return a
    if b > 100:
        return 0
    return a / b

data = {10: 2, 2: 5, 123: 4, 18: 2, 8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)