class Library:
    def __init__(self, listOfBooks):  #constructor will receive a list containing book names
        self.books = listOfBooks

    def displayAvailableBooks(self):  #this function will display available books in the library
        print('Books present in this library are: ')
        for book in self.books:
            print(' *'  + book)

    def borrowBook(self, bookName):  
        if bookName in self.books:
            print(f'You have been issued {bookName} for a timeperiod of 7 days')
            self.books.remove(bookName)
            
        else:
            print('Sorry, this book is not available at present')
            
    def returnBook(self, bookName):
        self.books.append(bookName)
        print('Thanks for returning the book')
        
class Student:
    def requestBook(self):  #we can request book using this function
        self.book = input('Enter the name of the book you want to borrow: ') 
        return self.book
    def returnBook(self):  #we can return book using this function
        self.book = input('Enter the name of the book you want to return: ')
        return self.book


if __name__ == '__main__':
    cityLibrary = Library(['Python', 'Javascript', 'HTML', 'SQL'])
    student = Student()
    while True:
        msg = '''\n ***Welcome to City Library***
        Please choose an option:
        1. List of available books
        2. Request a book
        3. Add or Return a book
        4. Exit the library
        '''
        print(msg)
        ch = int(input('Enter a choice: '))
        if ch == 1:
            cityLibrary.displayAvailableBooks()
        elif ch == 2:
            cityLibrary.borrowBook(student.requestBook())
        elif ch ==3:
            cityLibrary.returnBook(student.returnBook())
        elif ch == 4:
            print('Thanks for choosing City Library. Have a nice day')
            exit()
        else:
            print('Invalid choice')