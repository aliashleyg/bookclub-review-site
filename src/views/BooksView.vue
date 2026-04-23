<script setup>
import { ref, onMounted } from 'vue'
import { getBooks, createBook, deleteBook } from '@/services/api'
import BookCard from "@/components/BookCard.vue";
import AddBookForm from "@/components/AddBookForm.vue";

const books = ref([])
const loading = ref(true)
const error = ref(null)

async function handleCreateBook(newBook) {
  const createdBook = await createBook(newBook)
  books.value.push(createdBook)
  console.log("created book: ", createdBook)
}

async function handleDeletedBook(id) {
  const deletedBook = await deleteBook(id)
  books.value = books.value.filter(book => book.id !== id)
  console.log("deleted book: ", id)
  console.log("books: ", books)
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
  <AddBookForm @add-new-book-click="handleCreateBook" />
  <BookCard
      @delete-book-click="handleDeletedBook"
      v-for="book in books"
      :key="book.id"
      :book="book"
  />
</template>

<style scoped></style>
