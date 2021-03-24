books = []
books.append('Learn C')
books.append('Javascript')
books.append('Python')
print(books)

books.pop()
print(books)

books.pop()
print('Now the top book is: ',books[-1]) 
books.pop()
if not books:
    print('No Books Left')