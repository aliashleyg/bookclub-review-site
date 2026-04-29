# User Flows for Project

## Add Book (manual form)

1. Button lives in **AddBookForm** which calls `handleSubmit`
2. **AddBookForm** emits selected book (`newBook`) via `submitBook`
3. **BooksView** receives `newBook` in `handleSaveBook`
4. Because `bookToEdit` is null, `handleSaveBook` runs create mode
5. `handleSaveBook` calls `createBook(newBook)` from **api.js**
6. Data returned from `createBook` is saved as `createdBook`
7. `createdBook` is pushed to `books`


## Edit Book

1. Button lives in **BookCard**
2. Button click → calls `handleEditClick` → emits selected book via `edit-book`
3. **BooksView** receives book in `handleEditBook`
4. **BooksView** stores it in `bookToEdit`
5. **AddBookForm** receives `editingBook` prop
6. **AddBookForm** watcher copies `editingBook` into local form state
7. Submit → emits `save-book`
8. **BooksView** runs update mode because `bookToEdit` exists
9. After successful update, `bookToEdit` is reset to `null`


## Delete Book

1. Delete button lives in **BookCard** and calls `handleDeleteClick`
2. `handleDeleteClick` emits `delete-book-click` with `book.id`
3. **BooksView** receives `id` in `handleDeletingBook`
4. `handleDeletingBook` calls `deleteBook(id)` from **api.js**
5. `books` array is updated by filtering out the deleted book


## Search Book (Google API)

1. Search input and button live in **BookSearch**
2. Search input is bound to `searchInputTitle`
3. Search button triggers `bookSearch`
4. `bookSearch` emits the query string via `search`
5. **BooksView** receives the query in `handleSearch`
6. `handleSearch` calls `searchGoogleBooks(query)` from **api.js**
7. The API response is mapped into a simplified array and stored in `searchResults`


## Select Book From Search List (populate form)

1. Select button lives in BookSearchResultCard
2. Select button triggers `selectBook(book)`
3. `selectBook(book)` emits `book` through `selectBookClick`
4. **BookSearchResultsList** receives book through `selectBookClick`
5. **BookSearchResultsList** emits `selectBookClick` through `passSelectedBook`
6. **BooksView** receives book in `handleSelectedBook`
7. 



## Select Book From Search (same as Add Book, just different source)
## Clear Search (input + results)


# API Calls

# Shared Patterns

### Add Book + Save From Search
Both use AddBookForm → submit/save → BooksView → createBook API → update books list.

### Edit Book + Select Book From Search
Both populate AddBookForm from external data.
Difference:
- Edit Book sets bookToEdit and later updates existing book
- Select From Search sets selectedSearchBook and later creates a new book

### Clear Search + Clear Add Book
Both reset local component state back to empty/default values.