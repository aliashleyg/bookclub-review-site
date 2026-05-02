<script setup>

const props = defineProps({
  populatingSelectedBook: Object,
})
</script>

<template>
  <img :src="populatingSelectedBook.coverImage" alt="Cover of book" style="width: 100%; margin: 1rem height: 150px;"/><br />
  <h2> {{populatingSelectedBook.title}}</h2>
  <h3> {{populatingSelectedBook.author}}</h3>
  <h3> {{populatingSelectedBook.description}}</h3>
</template>

<style scoped>

</style>