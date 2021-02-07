""" Program to create and manage a list of books that the user wishes to read, and books that the user has read. """

from bookstore import Book, BookStore
from menu import Menu
import ui

store = BookStore()


def main():
    menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice == 'Q':
            break


def create_menu():
    menu = Menu()
    menu.add_option('1', 'Add Book', add_book)
    menu.add_option('2', 'Search For Book', search_book)
    menu.add_option('3', 'Show Unread Books', show_unread_books)
    menu.add_option('4', 'Show Read Books', show_read_books)
    menu.add_option('5', 'Show All Books', show_all_books)
    menu.add_option('6', 'Change Book Read Status', change_read)
    menu.add_option('7', 'Delete Book', delete_book)
    menu.add_option('Q', 'Quit', quit_program)

    return menu


def add_book():
    new_book = ui.get_book_info()
    try:
        new_book.save()
    except:
        print('This book is already in the database.')


def delete_book():
    """ Deletes book by ID """

    book_id = ui.get_book_id()
    remove_book = store.get_book_by_id(book_id)
    try:
        remove_book.delete()
    except:
        print('\nError: Book Not Found\n')


def show_read_books():
    read_books = store.get_books_by_read_value(True)
    ui.show_books(read_books)


def show_unread_books():
    unread_books = store.get_books_by_read_value(False)
    ui.show_books(unread_books)


def show_all_books():
    books = store.get_all_books()
    ui.show_books(books)


def search_book():
    search_term = ui.ask_question('Enter search term, will match partial authors or titles.')
    matches = store.book_search(search_term)
    ui.show_books(matches)


def change_read():
    book_id = ui.get_book_id()
    book = store.get_book_by_id(book_id)
    if book:  # If book ID found in db
        new_read = ui.get_read_value()
        # if else statement to determine what the state the book is in
        if new_read == False:
            read_var = '"not read"'
        else:
            read_var = '"read"'
        book.read = new_read
        book.save()
        print('Book status has changed to', read_var)
    else:  # If book ID not found in db
        print('That book is not found.')
        option = input('Return to main menu? Y for main menu. ').upper()
        if option == 'Y':
            print()
        else:
            change_read()  # restarts function for book ID input


def quit_program():
    ui.message('Thanks and bye!')


if __name__ == '__main__':
    main()
