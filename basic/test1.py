sentence = input("enter a sentense: ")

count=0

for ch in sentence.lower():
    if ch in "aeiou":
        count +=1
print("Vovels count: ", count)