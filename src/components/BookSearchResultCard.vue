<script setup>
import Card from 'primevue/card'
defineProps({ book: Object })

</script>

<template>
  <Card>
    <template #header> {{ book.title }}</template>
    <template #title> {{ book.authors }}</template>
    <template #content><img :src="book.thumbnail" alt="Description" />
    </template>
  </Card>
</template>

<style scoped>

</style>