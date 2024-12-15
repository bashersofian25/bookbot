def readFile(path):
    with open(path,'r') as file:
        fileContent = file.read()
        file.close()
    return fileContent


def countWords(content):
    return len(content.split())


def countChars(content):
    chars = list(content)
    uniq = {}
    for char in chars:
        if char.isalpha():
            if char.lower() not in uniq.keys():
                uniq[char.lower()] = 1
            else:
                uniq[char.lower()] += 1

    return uniq


def printBookReport(path):
    fileContent = readFile(path)
    wordCount = countWords(fileContent)
    charCount = countChars(fileContent)
    print (f"--- Begin report of {path} ---")
    print (f"{wordCount} words found in the document\n")
    keys = list(charCount.keys())
    keys.sort()
    for char in keys:
        print (f"The '{char}' character was found {charCount[char]} times")
    print ("--- End report ---")


print (printBookReport('books/Frankenstein'))