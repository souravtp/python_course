sampledict = {
    "class": {
        "student": {
            "name2": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }, "medium": "english"
}

L = [sampledict]  # [{a:{b:{}}}]
keys = []
while L:
    D = L.pop()
    for i in D.keys():
        keys.append(i)
        if isinstance(D[i], dict):
            L.append(D[i])
print(keys)
