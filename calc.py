def calc(text):
    ls=[["+", "sum of ","plus"], ["-","difference of",  "minus"], ["divided by","divide","/", "by"],["multiplied by", "product of ", "multiply", "into", "x"]]
    index=0
    indic=0
    tt=list(text.split())
    for i in tt:
        for ind in range(len(ls)):
            if i in ls[ind]:
                index = ind
                indic = 1
                break
    if indic ==0:
        print("INVALID STATEMENT")

    if index==0:
        ans = fun_add(text)
    elif index==1:
        ans = fun_sub(text)
    elif index==2:
        ans = fun_div(text)
    elif index==3:
        ans = fun_prod(text)
    else:
        print("INVALID STATEMENT")
    return ans

def fun_add(text):
    ans=0
    for i in text:
        try:
            ans += int(i)
        except:
            pass
    return ans

def fun_prod(text):
    ans=0
    for i in text:
        try:
            ans *= int(i)
        except:
            pass
    return ans

def fun_sub(text):
    a=0
    b=0
    for i in text:
        try:
            if a==0:
                a = int(i)
            else:
                b = int(i)
        except:
            pass
    return a-b


def fun_div(text):
    a=0
    b=0
    for i in text:
        try:
            if a==0:
                a = int(i)
            else:
                b = int(i)
        except:
            pass
    return a//b


