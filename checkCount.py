import sys


def printCheck(check):
    check.sort(reverse=True)
    totalCheck = 0
    lineLimiter = 80
    stringBuffer = ""
    for cost, item in check:
        totalCheck += cost
        newItem = str(cost) + " " + item + '\t'
        if len(stringBuffer + newItem) <= lineLimiter:
            stringBuffer += newItem
        else:
            print(stringBuffer)
            stringBuffer = ""
    print(stringBuffer)
    print("\n************")
    print("total: ", totalCheck)
    print("************\n")


lines = sys.stdin.readlines()
myOwnSpendings = list()
check = list()
while lines:
    line = lines.pop(0)
    if "." in line:
        continue
    elif line == "":
        continue
    elif "(" == line[0]:
         words = line.split()
         words[0] = words[0][1:]
         words[-1] = words.pop(-1)
         cost = int(words[0])
         item = " ".join(words[1:])
         myOwnSpendings.append((cost, item))
    else:
        words = line.split()
        cost = int(words[0])
        item = " ".join(words[1:])
        check.append((cost, item))

print("debdt:")
printCheck(check)
print("own money")
printCheck(myOwnSpendings)
