<script setup>
import { ref, onMounted } from 'vue'
import { getBooks, createBook, deleteBook, updateBook, searchGoogleBooks } from '@/services/api'
import Dialog from 'primevue/dialog';
import BookCard from "@/components/BookCard.vue";
import AddBookForm from "@/components/AddBookForm.vue";
import BookSearch from "@/components/BookSearch.vue";
import BookSearchResultsList from "@/components/BookSearchResultsList.vue";
import ReviewBookModal from "@/components/ReviewBookModal.vue";

const books = ref([])
const loading = ref(true)
const error = ref(null)
const bookToEdit = ref(null)
const searchResults = ref([])
const selectedBook = ref(null)
const bookReviewModalIsOpen = ref(false)

function handleSelectedBook(book) {
  selectedBook.value = book
  bookReviewModalIsOpen.value = true
}

function getUpdatedBookList(updatedBook) {
  books.value = books.value.map(function(book) {
    if (book.id === bookToEdit.value.id) {
      return updatedBook
    }
    return book
  })
}

async function handleSaveBook(newBook) {
  if (bookToEdit.value) {
    const updatedBook = await updateBook(bookToEdit.value.id, newBook)
    getUpdatedBookList(updatedBook)
    bookToEdit.value = null
  } else {
    const createdBook = await createBook(newBook)
    books.value.push(createdBook)
    selectedBook.value = null
    searchResults.value = null
  }
}

async function handleDeletingBook(id) {
  const deletedBook = await deleteBook(id)
  books.value = books.value.filter(book => book.id !== id)
}

async function handleEditingBook(book) {
  bookToEdit.value = book
}

async function handleSearch(searchInput) {
  let query = ''
  if (searchInput.searchInputTitle && searchInput.searchInputAuthor) {
    query = `intitle:${searchInput.searchInputTitle} inauthor:${searchInput.searchInputAuthor}`
  } else {
    query = `intitle:${searchInput.searchInputTitle}`
  }
  const searchedBook = await searchGoogleBooks(query)
  searchResults.value = searchedBook.items.map(formatBook)
  return searchResults.value
}

function formatBook(book) {
  const industryIdentifier = book.volumeInfo.industryIdentifiers
  let isbn
  if (industryIdentifier) {
    const isbn_13 = book.volumeInfo.industryIdentifiers.find(item => item.type === 'ISBN_13')
    const isbn_10 = book.volumeInfo.industryIdentifiers.find(item => item.type === 'ISBN_10')
    if (isbn_13) {
      isbn = isbn_13.identifier
    } else if (isbn_10) {
      isbn = isbn_10.identifier
    } else {
      isbn = "No ISBN available."
    }
  } else {
    isbn = "No ISBN available"
  }

  return {
    title: book.volumeInfo.title,
    author: book.volumeInfo.authors ? book.volumeInfo.authors[0] : "author not found",
    description: book.volumeInfo.description ? book.volumeInfo.description : "no description provided",
    coverImage: book.volumeInfo.imageLinks ? book.volumeInfo.imageLinks.thumbnail + "&fife=w800-h1200" : "https://placehold.co/600x400",
    isbn: isbn
  }
}

onMounted(async () => {
  try {
    books.value = await getBooks()
  } catch (err) {
    error.value = 'Failed to load books'
  } finally {
    loading.value = false
  }

})
</script>

<template>
  <p v-if="loading">Loading...</p>
  <p v-else-if="error">{{ error }}</p>
  <BookSearch @search-input="handleSearch"/>
  <BookSearchResultsList
      @select-book-click="handleSelectedBook"
      :search-results="searchResults"/>
  <BookCard
      @edit-book-click="handleEditingBook"
      @delete-book-click="handleDeletingBook"
      v-for="book in books"
      :key="book.id"
      :book="book"/>

<!--  Not using this anymore so can delete when ready, but keeping for now-->
<!--  <AddBookForm-->
<!--      @submit-book="handleSaveBook"-->
<!--      :editing-book="bookToEdit"-->
<!--      :populating-selected-book="selectedBook"/>-->

  <Dialog v-model:visible="bookReviewModalIsOpen">
    <ReviewBookModal
      :populating-selected-book="selectedBook"/>
  </Dialog>
</template>

<style scoped></style>
