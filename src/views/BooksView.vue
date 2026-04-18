<script setup>
import { ref, onMounted } from 'vue'
import { getBooks } from '@/services/api'
import BookCard from "@/components/BookCard.vue";

const books = ref([])
const loading = ref(true)
const error = ref(null)

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

  <BookCard
      v-else
      v-for="book in books"
      :key="book.id"
      :book="book"
  />
</template>

<style scoped></style>

<!--<script setup>-->
<!--import { ref, onMounted } from 'vue'-->
<!--import Button from 'primevue/button'-->
<!--import BookCard from '../components/BookCard.vue'-->
<!--import { getBooks } from '../services/api'-->

<!--const books = ref([])-->

<!--onMounted(async () => {-->
<!--  books.value = await getBooks()-->
<!--})-->
<!--</script>-->

<!--<template>-->
<!--  <div style="max-width: 800px; margin: 2rem auto; padding: 1rem;">-->
<!--    <h1>Book Club Books</h1>-->

<!--    <Button label="PrimeVue is working 😄" style="margin-bottom: 1rem;" />-->

<!--    <BookCard-->
<!--        v-for="book in books"-->
<!--        :key="book.id"-->
<!--        :book="book"-->
<!--    />-->
<!--  </div>-->
<!--</template>-->