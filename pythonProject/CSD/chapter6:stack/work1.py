from work import ArrayStack
def check_parenthesis(text):
    lefty='({['
    righty=')}]'
    S=ArrayStack()
    for word in text:
        if word in lefty:
            S.push(word)
        else:
            if word in righty:
                if S.is_empty():
                    return False
                elif lefty.index(S.top())==righty.index(word):
                    S.pop()
                else:
                    return False
    return True
string='dat(ele{kk)fllfl)'
print(check_parenthesis(string))



