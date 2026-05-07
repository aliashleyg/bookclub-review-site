<script setup>
import Card from 'primevue/card'
import BookDescription from "@/components/BookDescription.vue";

defineProps({ book: Object })

const emit = defineEmits(['selectBookClick'])

function selectBook(book) {
  emit('selectBookClick', book)
}

</script>

<template>
  <Card style="width: 25rem; overflow: hidden">
    <template #header> {{ book.title }}</template>
    <template #title> {{ book.author }}</template>
    <template #content>
      <img :src="book.coverImage" :alt="'Cover of ' + book.title" style="width: 20rem; margin: 1rem; height: auto;"/><br />
      <BookDescription :description="book.description" />
      <p>{{book.isbn}}</p>
      <button @click="selectBook(book)" type="submit">Select Book</button>
    </template>
  </Card>
</template>

<style scoped>

</style>