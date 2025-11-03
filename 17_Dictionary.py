# Dictionary is a mutable and orderable, don't duplicate key and key: value pairs

info= {
    "name":"dhiraj",
    "age":17,
    "work":"student",
    "college":"LPU",
}

print(info)
print(info['name'])
print(len(info.keys()))
print(info.values())
print(info.items())

print(info.get("info"))

info.update({"city":"bettiah"})
print(info)