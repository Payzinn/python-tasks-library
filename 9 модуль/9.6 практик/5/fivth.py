text_file = open('text.txt' ,'r', encoding='utf-8')
content = text_file.read().lower() 
text_file.close()
list_of_letters = [i for i in content if i.isalpha()]
result = set(list_of_letters)
dict_of_letters = dict()

for letter in result:
    frequency = round(list_of_letters.count(letter)/len(list_of_letters), 3)
    dict_of_letters[letter] = frequency

sorted_dict_of_letters = dict(sorted(dict_of_letters.items()))

analysis_file = open('analysis.txt', 'w', encoding='utf-8')

for key in sorted_dict_of_letters:
    result = (key,':', sorted_dict_of_letters[key])
    analysis_file.write(str(result)+'\n')

analysis_file.close()