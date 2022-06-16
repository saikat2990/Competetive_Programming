def coreProject(convertedString):
    newConvertedString = ""
    sameCharacter = 1
    letter = convertedString[0]
    for i in range(1,len(convertedString)):
        if convertedString[i]==letter:
            sameCharacter+=1
        else:
            newConvertedString+=(str(sameCharacter)+letter)
            letter = convertedString[i]
            sameCharacter=1
    newConvertedString += (str(sameCharacter) + letter)
    return  newConvertedString

def countAndSay(n):
    if n==1:
        return "1"
    convertedString = "1"
    for i in range(2,n+1):
        convertedString = coreProject(convertedString)
    return convertedString
print(countAndSay(1))