para = input("enter a paragraph:").lower()
frequency_dict = {}
for word in para.split():
    if word in frequency_dict:
        frequency_dict[word] += 1
    else:
        frequency_dict[word] = 1

print("the frequency of each word in the paragraph is:" , frequency_dict)    
print("the total number of words in the paragraph is:" , sum(frequency_dict.values()))
print("the top 5 most frequent words in the paragraph are:" , sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)[:5])