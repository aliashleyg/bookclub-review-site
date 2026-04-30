<script setup>
import Card from 'primevue/card'

defineProps({ book: Object })

const emit = defineEmits(['selectBookClick'])

function selectBook(book) {
  emit('selectBookClick', book)
}

</script>

<template>
  <Card style="width: 25rem; overflow: hidden">
    <template #header> {{ book.title }}</template>
    <template #title> {{ book.authors }}</template>
    <template #content>
      <img :src="book.coverImage" alt="Cover of book" style="width: 100%; margin: 1rem height: auto;"/><br />
      <p>{{book.description}}</p>
      <button @click="selectBook(book)" type="submit">Select Book</button>
    </template>
  </Card>
</template>

<style scoped>

</style>