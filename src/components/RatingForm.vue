<script setup>
import Rating from 'primevue/rating';

const props = defineProps({
  bookToRate: Object
})
</script>

<template>
  <h1>Rate</h1>
  <Rating />
</template>

<style scoped></style>

