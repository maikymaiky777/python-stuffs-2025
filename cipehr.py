d = ["the","a","an","is","was","it","in","on","at","to","for","of","and","that","this","with","from","but","not","are","be","have","has","had","do","does","did","will","can","may","all","one","two","no","yes","if","or","so","up","out",
"he","she","we","they","you","my","his","her","its","our","what","which","who","how","when","where","why","there","here","then","than","more","most","some","any","very","just","about","into","over","after","before","between","through",
"during","without","only","other","new","old","first","last","long","great","little","right","own","same","big","high","small","large","next","early","young","important","few","public","good","best","still","world","life","hand","part",
"child","place","case","week","company","system","program","question","work","number","night","point","home","water","room","mother","area","money","story","fact","month","lot","day","way","man","woman","time"]

alphabet = "abcdefghijklmnopqrstuvwxyz"

def decode(msg,shift):
    newmsg = ""
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
    return newmsg


msg = input("message: ")
shif = input("shift (decode): ")

print(decode(msg,26-int(shif)))