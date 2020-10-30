tst ="Hello my name is python, your name is blue ?"
words = tst.lower().split()
unique_words = list(set(words))
count =[0]*len(unique_words)
freq = dict(zip(unique_words,count))
for word in unique_words:
    freq[word]+=tst.lower().count(word)
print(freq)