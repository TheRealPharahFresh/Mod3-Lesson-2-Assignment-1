# Task 1: 
# Library System Enhancement
#  Sharpen your skills in managing and modifying data within tuples and lists.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_books(library):
    new_book_input = input("Book Name","Book Author"("Please Separate book title and author"))
    title,author = [item.strip() for item in new_book_input.split(',')]
    new_book = (title,author)
    if new_book in library:
        print("Book Already Found Try Another Entry")
    else:
        print(f"Book {title} by {author} now added to the library")
        return library.append(new_book)

    