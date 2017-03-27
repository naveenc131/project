from Stack import *
def postfix(strn):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    s = Stack()
    lst = []
    str = strn.split()
    for token in str :
        if token in "QWERTYUIOPASDFGHJKLZXCVBNM" or token in "1234567890" :
            lst.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            top = s.pop()
            while top != ')':
                lst.append(top)
                top = s.pop()
        else:
            while (not s.is_empty()) and (prec[s.peek()] >= prec[token]):
                lst.append(s.pop())
            s.push(token)
    while not s.is_empty():
        lst.append(s.pop)
    print(lst)
postfix("(A+B)*(C+D)")
    