word = input()

letra = input()

count= 0

for lettter in word:
    if letra.toupper() == lettter.toupper():
        count+=1
print(count) 