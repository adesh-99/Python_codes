def word_count(str):
    counts=dict()
    words=str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word]=1

    counts_x=sorted(counts.items(), key=lambda kv: kv[1])
    return counts_x[-2]
string=input("Enter any String:-")
print(word_count(string))