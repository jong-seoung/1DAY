word = input().upper()
cnt = []
word_list = list(set(word))

for i in word_list:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[cnt.index(max(cnt))])