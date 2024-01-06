speakers_file = open('speakers.txt', 'r', encoding='utf-8')
sym_count = []
for i_line in speakers_file:
    print(i_line, end='')
    sym_count.append(str(len(i_line)))

sym_str = '\n'.join(sym_count)
speakers_file.close()

counts_file = open('sym_count.txt', 'w')
counts_file.write(sym_str)
counts_file.close()