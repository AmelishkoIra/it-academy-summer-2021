input_ = input(" ")
t = ""
n = ""
for i in range(len(input_)):
    if input_[i].islower() and input_[i] != " ":
        t = t + input_[i]
    elif input_[i].isupper() and input_[i] != " ":
        n = n + input_[i]
print(len(t), " - строчные")
print(len(n), " - прописные ")
