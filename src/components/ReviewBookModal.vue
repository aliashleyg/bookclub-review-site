<script setup>
const emit = defineEmits(['submitBook'])
const props = defineProps({
  populatingSelectedBook: Object,
})
function submitBook(book) {
  emit('submitBook', book)
}

</script>

<template>
  <h2>Add Book To Library?</h2>
  <img :src="populatingSelectedBook.coverImage" alt="Cover of book" style="margin: 1rem; height: 150px"/><br />
  <h3> {{populatingSelectedBook.title}}</h3>
  <h4> {{populatingSelectedBook.author}}</h4>
  <h4> {{populatingSelectedBook.description}}</h4>
  <button @click="submitBook(populatingSelectedBook)" type="submit">Confirm</button>
</template>

<style scoped>

</style>