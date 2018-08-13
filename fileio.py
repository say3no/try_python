f = open("hoge", mode="w")
contents = ["a", "b"]

for ele in contents:
    f.write(ele + "\n")

f.close()

f = open("hoge", mode="r")

for ele in f.readlines():
    print(ele)
