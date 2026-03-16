t = input("encrypt or decrypt: ")

msg = input("message: ")
newmsg = ""
shift = int(input("shift: "))

if t == "decrypt":
    shift = 26 - shift

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(msg)):
    letter = msg[i].lower()
    if alphabet.find(letter) >= 0:
        new = alphabet[(alphabet.find(letter)+shift)%len(alphabet)]
        if msg[i].islower():
            newmsg = newmsg + new
        else:
            newmsg = newmsg + new.upper()
    else:
        newmsg = newmsg + letter
print(newmsg)