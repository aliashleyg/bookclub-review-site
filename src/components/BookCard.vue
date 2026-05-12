<script setup>
import Card from 'primevue/card'
import Dialog from 'primevue/dialog';
import {ref} from "vue";
import BookDescription from "@/components/BookDescription.vue";
import ReaderRatingModal from "@/components/ReaderRatingModal.vue";

const emit = defineEmits(['deleteBookClick', 'editBookClick'])
const bookDetailsIsOpen = ref(false)
const ReaderRatingModalIsOpen = ref(false)

const props = defineProps({
  book: Object
})

function deleteBook(book) {
  emit('deleteBookClick', book.id)
}

function editBook(book) {
  emit('editBookClick', book)
}

function getMonth(book) {
  const dateSplit = props.book.monthRead.split("-")
  const month = parseInt(dateSplit[1])
  const year = parseInt(dateSplit[0])
  const newDate = new Date(year, month, 0)
  return newDate.toLocaleString('en-US', { month: 'long' });
}

function getYear(book) {
  const dateSplit = props.book.monthRead.split("-")
  const month = parseInt(dateSplit[1])
  const year = parseInt(dateSplit[0])
  const newDate = new Date(year, month, 0)
  return newDate.getFullYear()
}
</script>

<template>
  <Card style="width: 25rem; overflow: hidden">
    <template #header>
      <h2 style="text-align: right">{{ getMonth(book) }} {{ getYear(book)}}</h2>
      <h2>{{ book.title }}</h2>
      <h3>{{ book.author }}</h3>
      <img :src="book.coverImage" :alt="'Cover of ' + book.title" style="width: 150px">
    </template>

<!--    <template #title>{{ book.author }}</template>-->
<!--    <template #subtitle>{{ book.author }}</template>-->
    <template #content>
      <BookDescription :description="book.description" /><br><br>
      <button @click="editBook(book)">Edit Book Details</button><br><br>
      <button @click="ReaderRatingModalIsOpen = true">Rate Book</button><br><br>
      <button @click="bookDetailsIsOpen = true" style="margin-right:15px">Delete</button><br><br>

    </template>
  </Card>
  <Dialog v-model:visible="bookDetailsIsOpen" >
    <h2>Are you sure you want to delete this book?</h2>
    <button @click="deleteBook(book)">Yes</button>
    <button @click="bookDetailsIsOpen = false">No</button>
  </Dialog>
  <Dialog v-model:visible="ReaderRatingModalIsOpen">
    <ReaderRatingModal />
  </Dialog>
</template>

<style scoped></style>

