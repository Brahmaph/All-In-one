sentence = input("Enter a sentence: ")

count = 0

for ch in sentence.lower():
    if ch in "aeiou":
        count +=1
print("Number of vowels: ", count)