<script setup>
import {ref} from "vue";


const emit = defineEmits(['searchInputTitle', 'searchInputAuthor'])
const searchInputTitle = ref('')
const searchInputAuthor = ref('')

function bookSearch() {
  emit('searchInputTitle', searchInputTitle.value, 'searchInputAuthor', searchInputAuthor.value)
  searchInputTitle.value = ''
}

</script>

<template>
  <h2>Search</h2>
  <input v-model="searchInputTitle" placeholder="Search by Book Title" />
  <input v-model="searchInputAuthor" placeholder="Search by Author" />
  <button @click="bookSearch">Search</button>
</template>

<style scoped>

</style>