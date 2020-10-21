import hashlib #lib for work with hash
print("***************** sha256 generator ******************")
entry = input("Enter : ")
while entry != "cancel":
    res = hashlib.sha256(entry.encode('ASCII')).hexdigest() #converting input to sha256 hash
    print(res)
    print("-----------------for canecelling just type cancel after \"Enter : \" -------------------")
    entry = input("Enter : ")
