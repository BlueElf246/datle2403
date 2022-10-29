class Ceasar_Cipher:
    def __init__(self,shift):
        encoder=[None]*26
        decoder=[None]*26
        for k in range(26):
            encoder[k]=chr((k+shift)%26+ord('A'))
            decoder[k]=chr((k-shift)%26+ord('A'))
        self._forward=''.join(encoder)
        self._backward=''.join(decoder)
    def encrypt(self,message):
        message=message.upper()
        message=message.replace(' ','')
        lst=list(message)
        lst1=[]
        for k in range(0,len(lst)):
            j=ord(lst[k])-ord('A')
            lst1.append(self._forward[j])
        lst1=''.join(lst1)
        return lst1
    def decrypt(self,message):
        message=message.upper()
        message=message.replace(' ','')
        lst=list(message)
        lst1=[]
        for k in range(0,len(lst)):
            j=ord(lst[k])-ord('A')
            lst1.append(self._backward[j])
        lst1=''.join(lst1)
        return lst1
A=Ceasar_Cipher(3)
# print(A._forward)
# g='DAT'
# print(A.encrypt(g))
# print(A.decrypt(A.encrypt(g)))
doc='may be de'
print(A.encrypt(doc))
#print(A.decrypt(A.encrypt(doc)))
