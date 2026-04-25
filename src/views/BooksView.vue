<script setup>
import { ref, onMounted } from 'vue'
import { getBooks, createBook, deleteBook, updateBook } from '@/services/api'
import BookCard from "@/components/BookCard.vue";
import AddBookForm from "@/components/AddBookForm.vue";

const books = ref([])
const loading = ref(true)
const error = ref(null)
const bookToEdit = ref(null)

async function handleSaveBook(newBook) {
  if (bookToEdit.value) {
    const updatedBook = await updateBook(bookToEdit.value.id, newBook)
    getUpdatedBookList(updatedBook)
    bookToEdit.value = null
  } else {
    const createdBook = await createBook(newBook)
    books.value.push(createdBook)
  }
}
function getUpdatedBookList(updatedBook) {
  books.value = books.value.map(function(book) {
    if (book.id === bookToEdit.value.id) {
      return updatedBook
    }
    return book
  })
}
async function handleDeletingBook(id) {
  const deletedBook = await deleteBook(id)
  books.value = books.value.filter(book => book.id !== id)
}

async function handleEditingBook(book) {
  bookToEdit.value = book
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
  <AddBookForm @submit-book="handleSaveBook"
    :editing-book="bookToEdit"/>
  <BookCard
      @edit-book-click="handleEditingBook"
      @delete-book-click="handleDeletingBook"
      v-for="book in books"
      :key="book.id"
      :book="book"
  />
</template>

<style scoped></style>
