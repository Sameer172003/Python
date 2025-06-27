# Chapter 5 – Dictionary & Sets

# Dictionary is a collection of key-value pairs. It is mutable. It is unordered. It is indexed. Cannot contains duplicate values.

a={"name":"Sameer",
   "from":"Bihar",
   "marks":[92,79,85]}

# Methods in dictionary

# 1) Items
print(a.items())

# 2) Keys
print(a.keys())

# 3) values
print(a.values())

# 4) Get
print(a.get("name"))

# 5) Update
a.update({"friend":"Harry"})
print(a)

# 6) Clear

a.clear()

# 7) Copy

b=a.copy()
print(b)


# Set - Set is a collection of non repetitive elements. They are unordered. They are unindexed. Cannot contain duplicate elements. There is no way to change items in set.

# Operations on Set

# 1) add
s=set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)

print(s)

# 2) len()
print(len(s))

# 3) remove
s.remove(2)
print(s)

# 4) pop
s.pop()
print(s)

# 5) union
s1=set()
s2=set()

s1.add(1)
s1.add(2)
s1.add(3)

s2.add(3)
s2.add(4)

print(s1.union(s2))

# 6) Intersection

print(s1.intersection(s2))

# 7) Clear

s.clear()
print(s)


