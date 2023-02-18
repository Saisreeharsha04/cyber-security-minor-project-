
def encripted(string,shift):
    ciper=''
    for char in string:
        if char==' ':
            ciper=ciper+char
        elif char.isupper():
            ciper=ciper+chr((ord(char)+shift-65)%26+65)
        else:
            ciper=ciper+chr((ord(char)+shift-97)%26+97)
    return ciper



text=input("enter the text : ")
s=int(input("enter the shift key : "))
print("the original string is :",text)
print("the encripted msg is :",encripted(text,s))