import re
deep_ocean = """
oCeAn Marlin OcEaN oceAN ocEAN OCEAN NEMO NEMP nemaa nemo Nemo nemo0
"""

nemo_pattern = r'[Nn]em\w{0,2}'
full_search = re.findall(nemo_pattern, deep_ocean)
print(full_search)

nemo_matched = re.search('Nemo', deep_ocean)
print('Немо в тексте: {}'.format(nemo_matched.group(0)))

transparent = re.sub(r'[Oo]\w{4}\s+', '', deep_ocean)
print('Всё что заменилось: {}'.format(transparent))