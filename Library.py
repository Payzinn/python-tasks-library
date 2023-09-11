#Library
books_ID=[50, 34, -1, -1, 2, 23, -1 ]
new_books_id=[]
returned=0

for _ in range (10):
    id=int(input('Введите ID книги: '))
    books_ID.append(id)

for id in books_ID:
    if id==-1:
        returned+=1
    else:
        new_books_id.append(id)

print(f'Новый список выданных книг: {new_books_id}')
print(f'Вернули за день: {returned}')