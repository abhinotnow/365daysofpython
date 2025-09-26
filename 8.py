#string analyzer tool
print("Enter a sentence: ")
sentence = input()
print(f"\n Number of characters: {len(sentence.strip())}")
print(f"\n Number of words: {len(sentence.split())}")
print("\n" + sentence.upper())
print("\n" + sentence.lower())
print(f"Reversed sentence is: ", end="")
for i in range(len(sentence)):
    print(sentence[-(i+1)], end="")

search = input("\nEnter the search keyword: ")
if search in sentence:
    print(f"The word {search} is present in the sentence.")
else:
    print(f"The word {search} is not present in the sentence.")

split = sentence.split()
revsentence = []
for i in range(len(split)):
    revsentence.append(split[-(i+1)])

if split == revsentence:
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
print("Word frequency: ")

frequency = {}
for i in range(len(split)):
    count = 0
    for n in range(len(split)):
        if split[i]==split[n]:
            count+=1
        frequency[split[i]] = count
print(frequency)





