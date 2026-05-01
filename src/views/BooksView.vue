<script setup>
import { ref, onMounted } from 'vue'
import { getBooks, createBook, deleteBook, updateBook, searchGoogleBooks } from '@/services/api'
import BookCard from "@/components/BookCard.vue";
import AddBookForm from "@/components/AddBookForm.vue";
import BookSearch from "@/components/BookSearch.vue";
import BookSearchResultsList from "@/components/BookSearchResultsList.vue";

const books = ref([])
const loading = ref(true)
const error = ref(null)
const bookToEdit = ref(null)
const searchResults = ref([])
const selectedBook = ref(null)

function handleSelectedBook(book) {
  selectedBook.value = book
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
  searchResults.value = searchedBook.items.map(book => ({
    title: book.volumeInfo.title, author: book.volumeInfo.authors ? book.volumeInfo.authors[0] : "author not found",
    coverImage: book.volumeInfo.imageLinks ? book.volumeInfo.imageLinks.thumbnail + "&fife=w800-h1200" : "https://placehold.co/600x400",
    description: book.volumeInfo.description ? book.volumeInfo.description : "no description provided"}))

  return searchResults.value
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
  <AddBookForm
      @submit-book="handleSaveBook"
      :editing-book="bookToEdit"
      :populating-selected-book="selectedBook"/>
  <BookSearch @search-input="handleSearch"/>
  <BookSearchResultsList
      @select-book-click="handleSelectedBook"
      :search-results="searchResults"/>
  <BookCard
      @edit-book-click="handleEditingBook"
      @delete-book-click="handleDeletingBook"
      v-for="book in books"
      :key="book.id"
      :book="book"
  />
</template>

<style scoped></style>
