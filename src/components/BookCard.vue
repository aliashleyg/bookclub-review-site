<script setup>
import Card from 'primevue/card'
import Dialog from 'primevue/dialog';
import {ref} from "vue";
import BookDescription from "@/components/BookDescription.vue";
const emit = defineEmits(['deleteBookClick', 'editBookClick'])
const isOpen = ref(false)

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
    <template #header>  <img :src="book.coverImage" :alt="'Cover of ' + book.title" style="width: 100%"></template>

    <template #title>{{ book.title }} - {{ book.monthRead }}</template>
    <template #subtitle>{{ book.author }}</template>
    <template #content>
      <BookDescription :description="book.description" />
      <button @click="isOpen = true" style="margin-right:15px">Delete</button>
      <button @click="editBook(book)">Edit Book Details</button>
    </template>
  </Card>
  <Dialog v-model:visible="isOpen" >
    <h2>Are you sure you want to delete this book?</h2>
    <button @click="deleteBook(book)">Yes</button>
    <button @click="isOpen = false">No</button>
  </Dialog>

</template>

<style scoped></style>

