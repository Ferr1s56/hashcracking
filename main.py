import time
import hashlib
import os

print("(1) RockYou")
print("(2) Lowercase English Dictionary")
print("(3) Other")

wordlistSelection = int(input("Enter wordlist you would like to use (1-3): "))
wordlistList = ["rockyou.txt", "englishdictionary.txt"]

if wordlistSelection < 3:
    wordlistUsed = wordlistList[wordlistSelection-1]

elif wordlistSelection == 3:

    wordlistUsed = str(input("Enter custom wordlist filename: "))
    fileExists = os.path.isfile(wordlistUsed)

    if fileExists == True:
        pass
    else: 
        print("Wordlist file does not exist.")
        exit()


print("Opening wordlist...")
wordlistFile = open(wordlistUsed, "r", encoding="utf8")


encodedHash = str(input("Input hash: "))
clearText = ""

startTime = float(time.time())

for line in wordlistFile.readlines():
    readLine = line.replace("\n", "")
    hashedEntryRaw = hashlib.md5(readLine.encode())
    hashedEntry = str(hashedEntryRaw.hexdigest())
    if encodedHash == hashedEntry:
        clearText = line
        break
    else:
        pass

endTime = float(time.time())
breakingTime = str(endTime - startTime)

if clearText == "":
    print("Password could not be decoded, try a different wordlist or recheck your hash.")

else: 
    print("Decoded password is: " + clearText)

print("Decoding took approximately " + breakingTime + " seconds.")
print("Closing wordlist...")
wordlistFile.close