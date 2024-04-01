import re
text = 'Even if they are djinns, I will get djinns that can outdjinn them.'
vowells_pattern = re.findall(r'\b[aeoiuAEOIU]\w*',text)
print(vowells_pattern)
vowells_pattern2 = re.findall(r'\b[^aeoiuAEOIU\W]\w*',text)
print(vowells_pattern2)