d ={"tom": 57348758934, "robin":  48593579348 , "joe": 934578453}

print(d["tom"])

d["sam"] = 349523478

print(d)

del d["sam"]

print(d)

for key in d:
    print("key:", key, "value:", d[key])

"tom" in d