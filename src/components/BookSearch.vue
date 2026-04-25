<script setup>
import {ref} from "vue";


const emit = defineEmits(['searchInputTitle'])
const searchInputTitle = ref('')

function bookSearch() {
  emit('searchInputTitle', searchInputTitle.value)
}

</script>

<template>
  <h2>Search</h2>
  <input v-model="searchInputTitle" placeholder="Search by Book Title" />
  <button @click="bookSearch">Search</button>
</template>

<style scoped>

</style>