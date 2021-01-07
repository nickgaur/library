

# DEFINING THE CLASS LIBRARY
class Library:

    # LIBRARY CLASS CONSTRUCTOR
    def __init__(self, library_name, list_of_books):
        self.__library_name__ = library_name
        self.__list_of_books__ = sorted(list_of_books)
        self.__logbook__ = {}

    # IMPLEMENTING DISPLAY METHOD
    def __display_book__(self):
        for serial_number, book_name in enumerate(self.__list_of_books__, 1):
            print(f"{serial_number} - {book_name}")

    # IMPLEMENTING BORROW METHOD
    def __borrow_book__(self):

        name = input("Enter your Name: ")

        while True:
            book_to_borrow = input("Enter the name of a book to borrow: ")
            if book_to_borrow in self.__list_of_books__:
                if name in self.__logbook__:
                    temp = self.__logbook__[name]
                    temp2 = temp.append(book_to_borrow)
                    self.__logbook__[name] = temp
                else:
                    books_borrowed = []
                    pass
                    books_borrowed.append(book_to_borrow)
                    self.__logbook__[name] = books_borrowed
                print("Book Borrowed Successfully")
                break
            else:
                print("Invalid Book Name, Try Again")

    # THIS METHOD PRINTS LIBRARY LOGBOOK
    def __print_logbook__(self):
        if len(self.__logbook__) != 0:
            # print(self.logbook)
            for key, value in self.__logbook__.items():
                print(f"{key} - {value}")
        else:
            print("No Entries Yet!")

    # ADDING THE BOOK TO THE LIBRARY
    def __add_book__(self):
        book_to_add = input("Enter the Name of the Book: ")
        self.__list_of_books__.append(book_to_add)
        print("Book Added Sucessfully")

    # RETURNING THE BOOK
    def __return_book__(self):
        try:
            name = input("Enter Your Name: ")
            book_name = input("Enter the name of the book you are returning: ")
            temp = self.__logbook__[name]
            temp.remove(book_name)
            print("Book Returned Successfully")
        except ImportError:
            print("This Name Doesn't Exist")

    # DELETING THE BOOK FROM CURRENT LIBRARY
    def __delete_book__(self):
        book_name = input("Enter the name of the book you want to delete from your library: ")
        self.__list_of_books__.remove(book_name)
        print("Book Deleted")

    # OPEN METHOD TO ACCESS ALL ATTRIBUTES AND METHODS
    def open_method(self, selected_option):
        if selected_option == 1:
            self.__display_book__()
        elif selected_option == 2:
            self.__borrow_book__()
        elif selected_option == 3:
            self.__add_book__()
        elif selected_option == 4:
            self.__return_book__()
        elif selected_option == 5:
            self.__delete_book__()
        elif selected_option == 6:
            self.__print_logbook__()


# DISPLAYING HOME PAGE MENUS
def homepage():
    print("""Select your Option from below
    1: Create New Library
    2: Select Library""")


# DISPLAYING MENUS UNDER LIBRARY
def menu():
    print("""\nChoose any option from below:
    1: Display the Books
    2: Borrow Book
    3: Add the Book
    4: Return the Book
    5: Delete any Book
    6: Print LogBook
    0: Change Library""")


# SELECTING LIBRARY FROM ALL LIBRARIES
def select_library(library_names_dict):
    enumerated_list = list(enumerate(sorted(library_names_dict), 1))
    entries = []
    while True:
        print("\nAll Libraries")
        for item in enumerated_list:
            print(f"{item[0]} - {item[1]}")

            # APPENDING THE S.NO OF ENTRY TO ENTRIES LIST
            entries.append(item[0])
        selected_library = int(input("Select Library: "))
        if selected_library not in entries:
            print("Invalid Selection, Try Again")
        else:
            options_from_menu(Library(enumerated_list[selected_library-1][1],
                                      library_names_dict[enumerated_list[selected_library-1][1]]))


# SELECTING OPTIONS FROM MENU
def options_from_menu(object1):
    # LOOPING FOR DISPLAYING MENU OF SELECTED LIBRARY
    while True:
        # DISPLAYING MENU
        menu()

        # SELECTING OPTIONS FROM MENU
        selected_option = int(input("Select Option: "))
        if selected_option != 0:
            object1.open_method(selected_option)
        elif selected_option == 0:
            break


def main():
    library_names_dict = {"Nikhil": ["Harry Potter",
                                     "The Theory of Everything",
                                     "Relativity : the special and the general theory",
                                     "A Brief History of Time",
                                     "The Evolution of Physics"]}

    # LOOP FOR DISPLAYING MAIN MENU
    while True:

        homepage()
        main_menu_query = int(input("Enter your Selection: "))

        # CREATING NEW LIBRARY
        if main_menu_query == 1:
            new_name = input("Enter the Name of Library: ")
            new_library_books = []
            number_of_books = int(input("Enter number of books you want to Add: "))
            for number in range(number_of_books):
                book_name = input("Enter the book name: ")
                new_library_books.append(book_name)
            library_names_dict[new_name] = new_library_books
            print("New Library Created\n")

        # SELECTING EXISTING LIBRARY
        elif main_menu_query == 2:
            select_library(library_names_dict)

        # INVALID SELECTION FROM HOME PAGE
        else:
            print("Invalid Selection, Please select correct option from the given list")


# MAIN BLOCK
if __name__ == '__main__':
    main()
