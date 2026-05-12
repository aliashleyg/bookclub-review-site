<script setup>
import RatingForm from "@/components/RatingForm.vue";

const props = defineProps({
  bookToRate: Object
})
</script>

<template>
  <h1>My Rating for:<br>{{bookToRate.title}}</h1>
  <img :src="bookToRate.coverImage" alt="Cover of book" style="margin: 1rem; height: 150px"/><br>
  <RatingForm />

</template>

<style scoped></style>

