s = list(input())
a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in a:
    if i in s: 
        print(s.index(i))
    else:
        print("-1")