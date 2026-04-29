<script setup>
import {ref} from "vue";
import { watch } from 'vue'

const emit = defineEmits(['submitBook'])

const newBook = ref({
  title: '',
  author: '',
  description: '',
  coverImage: ''
})

const props = defineProps({
  editingBook: Object,
  populatingSelectedBook: Object,
})

watch(() => props.editingBook, (newVal) => {
  if (newVal) {
    newBook.value = { ...newVal }
  }
})

watch(() => props.populatingSelectedBook, (newVal) => {
  if (newVal) {
    newBook.value = { ...newVal }
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
    description: '',
    coverImage: ''
  }

}

</script>

<template>
  <form @submit.prevent="handleSubmit">
    <h2>{{ editingBook ? 'Update Book' : 'Add a Book' }}</h2>

    <input v-model="newBook.title" placeholder="Title" required/><br />
    <input v-model="newBook.author" placeholder="Author" /><br />
    <textarea v-model="newBook.description" placeholder="Description"></textarea><br />

    <button type="submit">Submit</button>
  </form>
</template>

<style scoped>

</style>