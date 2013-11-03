h = int(input())
a = int(input())
b = int(input())

hday = h - a
#hday1 = h - b

step = a - b

answer = 1 + hday // step + (hday % step + step - 1) // step
#answer1 = hday1 // step + (hday1 % step + step - 1) // step

#a = hday1 % step + step - 1
#b = (hday1 % step + step - 1) // step

#print("hday = ", hday)
#print("hday1 = ", hday1)
#print("step = ", step)
#print(hday1, "%", step, " + ", step, "- 1 = ", a)


print(answer)
#print(answer1)
