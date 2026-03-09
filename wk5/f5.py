s1 = {1, "2", False, 3.4}  # 1, True

for v in s1:
    print(v)

s1.add(5)
if 3.4 in s1:
    s1.remove(3.4)

s2 = set(range(0, 6))

sss = set([1, "3", 4.5])
ssss = set("benblanc")
print(ssss)
print(s1, s2, sep='\n')

# common values
common = s1.intersection(s2)
print(common)
#s1.difference_update(s2)
s1.symmetric_difference_update(s2)
print(s1)
