<script setup>
import Card from 'primevue/card'

defineProps({
  book: Object
})

</script>

<template>
  <Card style="width: 25rem; overflow: hidden">
    <template #header>  <img :src="book.coverImage" alt="Cover of The Hobbit Manuscript" style="width: 100%"></template>
    <template #title>{{ book.title }}</template>
    <template #subtitle>{{ book.author }}</template>
    <template #content><p>{{ book.genre }}</p>
      <p class="m-0">{{ book.description }}</p>
    </template>

  </Card>


</template>

<style scoped></style>

