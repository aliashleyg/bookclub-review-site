<script setup>
import RatingForm from "@/components/RatingForm.vue";

const props = defineProps({
  bookToRate: Object
})
</script>

<template>
  <h1>{{bookToRate.title}}</h1>
  <RatingForm />

</template>

<style scoped></style>

