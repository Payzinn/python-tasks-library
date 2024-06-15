import re
text = 'AV is largest Analytics community of India'

result = re.findall(r'\b[aeiouAEIOU]\w+', text)
print(result)