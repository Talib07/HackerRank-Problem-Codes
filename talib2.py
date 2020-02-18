s = list(input())
s = [1,2,3] + s + [4,5]
# print(s)
stack = []
mid = '{'
rmid = '}'
sq = '['
rsq = ']'
para = '('
rpara = ')'
balanced = True
i = 3
bcount = 0

while i < len(s)-2:
    # print(s[i])
    if s[i] == rmid:
        star = 0
        del s[i]
        # print(s)
        rcount = 0
        for j in range(i-1,-1,-1):
            if s[j] == '[' or s[j] == '{' or s[j] == '(':
                if s[j] == mid and star >= 2:
                    bcount += 1
                    rcount += 1
                    del s[j]
                    break
                del s[j]
                balanced = False
                break
            else:
                rcount += 1
                if s[j] == '*':
                    star += 1
                    del s[j]
                else:
                    del s[j]
            if s[j] == s[0]:
                if s[j] != '[' or s[j] != '{' or s[j] != '(':
                    balanced = False
        i = i - rcount



    elif s[i] == rsq:
        star = 0
        del s[i]
        # print(s)
        rcount = 0
        for j in range(i - 1, -1, -1):
            if s[j] == '[' or s[j] == '{' or s[j] == '(':
                if s[j] == sq and star >= 2:
                    bcount += 1
                    rcount += 1
                    del s[j]
                    break
                del s[j]
                balanced = False
                break
            else:
                # print('in else')
                rcount += 1
                if s[j] == '*':
                    star += 1
                    del s[j]
                else:
                    del s[j]
            if s[j] == s[0]:
                if s[j] != '[' or s[j] != '{' or s[j] != '(':
                    balanced = False
        i = i-rcount



    elif s[i] == rpara:
        star = 0
        del s[i]
        # print(s)
        rcount = 0
        for j in range(i - 1, -1, -1):
            if s[j] == '[' or s[j] == '{' or s[j] == '(':
                if s[j] == para and star >= 2:
                    bcount += 1
                    rcount += 1
                    del s[j]
                    break
                del s[j]
                balanced = False
                break
            else:
                rcount += 1
                if s[j] == '*':
                    star += 1
                    del s[j]
                else:
                    del s[j]
            if s[j] == s[0]:
                if s[j] != '[' or s[j] != '{' or s[j] != '(':
                    balanced = False
        i = i - rcount

    else:
        i += 1
# print(s)
if bcount == 0:
    balanced = False
if balanced == True:
    print('Yes',bcount)
else:
    print('No',bcount)
