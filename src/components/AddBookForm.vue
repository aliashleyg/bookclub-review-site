<script setup>
import {ref} from "vue";
const emit = defineEmits(['addNewBookClick'])

const newBook = ref({
  title: '',
  author: '',
  genre: '',
  description: '',
  coverImage: ''
})

function handleSubmit() {
  emit('addNewBookClick', newBook.value)
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
    <h2>Add a Book From Book Form Component!</h2>

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