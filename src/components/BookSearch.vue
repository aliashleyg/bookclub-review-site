<script setup>
import {ref} from "vue";


const emit = defineEmits(['search-input'])
const searchInput = ref({
  searchInputTitle: '',
  searchInputAuthor: ''
})

function bookSearch() {
  emit('search-input', searchInput.value)
}

</script>

<template>
  <h2>Search</h2>
  <input v-model="searchInput.searchInputTitle" placeholder="Search by Book Title" />
  <input v-model="searchInput.searchInputAuthor" placeholder="Search by Author" />
  <button @click="bookSearch">Search</button>
</template>

<style scoped>

</style>