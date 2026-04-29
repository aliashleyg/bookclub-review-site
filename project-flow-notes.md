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
## Select Book From Search (populate form)
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