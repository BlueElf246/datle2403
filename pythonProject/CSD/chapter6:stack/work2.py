from work import ArrayStack
string="""
<body>
<center>
<h1> The Little Boat </h1>
</center>
<p> The storm tossed the little
boat like a cheap sneaker in an
old washing machine. The three
drunken fishermen were used to
such treatment, of course, but
not the tree salesman, who even as
a stowaway now felt that he
had overpaid for the voyage. </p>
<ol>
<li> Will the salesman die? </li>
<li> What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>
</body>
"""
S=ArrayStack()
start=0
def check(text):
    for index,word in enumerate(text):
        if word =='<' and string[index+1:index+2]!='/':
            k=string[index+1:string.find('>',index)]
            S.push(k)
        if word=='<' and string[index+1:index+2]=='/':
            k=string[index+2:string.find('>',index)]
            if k ==S.top():
                S.pop()
            else:
                return False
    for y in S:
        print(y)
    return True
print(check(string))


