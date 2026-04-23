# Edit Book Flow

## Decisions

- Editing will use the same form as AddBookForm
- Form will stay at the top of the page
- When edit is triggered, form will populate with selected book data
- After saving:
    - form resets
    - returns to add mode

## Flow

1. User clicks Edit on a BookCard
2. Parent receives selected book
3. Form populates with book data
4. User updates fields
5. User clicks submit
6. Backend updates book
7. UI updates
8. Form resets

## State to track
- bookToEdit: The book currently being edited
- this value lives in the parent component