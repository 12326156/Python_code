words = ["apple","guava","orange","grapes"]
n = int(input("Enter the length: "))

big_words = list()

for word in words:
        if(len(word)>n):
              big_words.append(word)
              
print(f"word longer than {n} characters: {big_words} ")
        
