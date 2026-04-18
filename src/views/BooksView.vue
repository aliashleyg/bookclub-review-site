<script setup>
import { ref, onMounted } from 'vue'
import { getBooks } from '@/services/api'
import BookCard from "@/components/BookCard.vue";
import { createBook } from '@/services/api'

const books = ref([])
const loading = ref(true)
const error = ref(null)
const newBook = ref({
  title: '',
  author: '',
  genre: '',
  description: '',
  coverImage: ''
})

async function handleCreateBook() {
  const createdBook = await createBook(newBook.value)
  books.value.push(createdBook)

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

  <div style="margin-bottom: 2rem;">
    <h2>Add a Book</h2>

    <input v-model="newBook.title" placeholder="Title" /><br />
    <input v-model="newBook.author" placeholder="Author" /><br />
    <input v-model="newBook.genre" placeholder="Genre" /><br />
    <input v-model="newBook.coverImage" placeholder="Cover Image URL" /><br />
    <textarea v-model="newBook.description" placeholder="Description"></textarea><br />

    <button @click="handleCreateBook()">Submit</button>
  </div>

  <BookCard
      v-for="book in books"
      :key="book.id"
      :book="book"
  />
</template>

<style scoped></style>
