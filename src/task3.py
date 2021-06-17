input_ = input()
t = ''
for i in range(len(input_)):
    if t.find(input_[i]) == -1 and input_[i] != ' ':
        t = t + input_[i]
print(t)