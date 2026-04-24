<script setup>
import {ref} from "vue";
import { watch } from 'vue'

const emit = defineEmits(['submitBook'])

const newBook = ref({
  title: '',
  author: '',
  genre: '',
  description: '',
  coverImage: ''
})

const props = defineProps({
  editingBook: Object
})

watch(() => props.editingBook, (newVal) => {
  if (newVal) {
    newBook.value = { ...newVal }
    console.log("new book: ", newVal)
  }
})

function handleSubmit() {
  emit('submitBook', newBook.value)
  resetForm()
}

function resetForm() {
  newBook.value = {
    title: '',
    author: '',
    genre: '',
    description: '',
    coverImage: ''
  }

}

</script>

<template>
  <form @submit.prevent="handleSubmit">
    <h2>Add a Book</h2>

    <input v-model="newBook.title" placeholder="Title" required/><br />
    <input v-model="newBook.author" placeholder="Author" /><br />
    <input v-model="newBook.genre" placeholder="Genre" /><br />
    <input v-model="newBook.coverImage" placeholder="Cover Image URL" /><br />
    <textarea v-model="newBook.description" placeholder="Description"></textarea><br />

    <button type="submit">Submit</button>
  </form>
</template>

<style scoped>

</style>