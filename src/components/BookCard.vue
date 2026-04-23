<script setup>
import Card from 'primevue/card'
const emit = defineEmits(['deleteBookClick', 'editBookClick'])

defineProps({
  book: Object
})

function deleteBook(book) {
  emit('deleteBookClick', book.id)
}

function editBook(book) {
  emit('editBookClick', book)
}

</script>

<template>
  <Card style="width: 25rem; overflow: hidden">
    <template #header>  <img :src="book.coverImage" alt="Cover of The Hobbit Manuscript" style="width: 100%"></template>
    <template #title>{{ book.title }}</template>
    <template #subtitle>{{ book.author }}</template>
    <template #content><p>{{ book.genre }}</p>
      <p class="m-0">{{ book.description }}</p>
      <button @click="deleteBook(book)" style="margin-right:15px">Delete</button>
      <button @click="editBook(book)">Edit Book Details</button>
    </template>
  </Card>


</template>

<style scoped></style>

