# Star pattern using loops

# 1) Left-aligned Half Pyramid
for i in range(0,5):
    for j in range(0,i):
        print("*",end="")
    print()

# 2) Inverted Left-aligned Half Pyramid
for i in range(0,5):
    for j in range(4,i-1,-1):
        print("*",end="")
    print()

# 3) Right-aligned Half Pyramid

for i in range(0,5):
    for j in range(4,i-1,-1):
        print(" ",end="")
    for k in range(0,i):
        print("*",end="")
    print()

# 4) Inverted Right-aligned Half Pyramid

for i in range(0,5):
    for j in range(0,i):
        print(" ",end="")
    for k in range(4,i-1,-1):
        print("*",end="")
    print()

# 5) Full Pyramid

for i in range(0,5):
    for j in range(4,i-1,-1):
        print(" ",end="")
    for k in range(0,2*i+1):
        print("*",end="")
    print()

# 6) Rectangle

for i in range(0,5):
    for j in range(0,5):
        print("*",end="")
    print()
