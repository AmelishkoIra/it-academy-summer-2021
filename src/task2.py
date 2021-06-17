input_ = input(" ")
j = input_.split()
t = " "
for i in j:
    if len(i) > len(t):
     t = i
print(t)
