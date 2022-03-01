food = [[["pie1", "pie2"], ["pie3", "pie4"], ["pie5", "pie6"]], [["cake1", "cake2"], ["cake3", "cake4"], ["cake5", "cake6"]]]
w = 1
printt = ["is"]

for i in range(w):
    printt.append("a")
    printt.append("list")
    printt.insert(2, "3d")
    printt.insert(0, "this")

#prints 'this is a 3d list'
print(" ".join(printt))

#prints last 'cake' in list
print(food[1][2][1])

