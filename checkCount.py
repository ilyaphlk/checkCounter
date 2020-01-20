import sys

#added a comment so it'll pop up as if the file has been changed


INPUT_FILENAME = "checkOctober.txt"


def printCheck(check, file):
    check.sort(reverse=True)
    totalCheck = 0
    lineLimiter = 40
    stringBuffer = ""
    for cost, item in check:
        totalCheck += cost
        newItem = str(cost) + " " + item + '\t'
        if len(stringBuffer + newItem) <= lineLimiter:
            stringBuffer += newItem
        else:
            file.write(stringBuffer+'\n')
            stringBuffer = ""
    file.write(stringBuffer)
    file.write("\n************\ntotal: ")
    file.write(str(totalCheck) + '\n')
    file.write("************\n")


def main():
    with open(INPUT_FILENAME, 'r') as file:
        lines = file.readlines()
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

    sys.stdout.write("debdt:\n")
    printCheck(check, sys.stdout)
    sys.stdout.write("own money:\n")
    printCheck(myOwnSpendings, sys.stdout)


main()
