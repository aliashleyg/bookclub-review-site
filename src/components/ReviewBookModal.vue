<script setup>
import {ref} from "vue";
import DatePicker from 'primevue/datepicker';

const emit = defineEmits(['submitBook'])
const props = defineProps({
  populatingSelectedBook: Object,
})

const monthYearRead = ref(new Date())

function submitBook(book) {
  console.log(monthYearRead.value.toISOString().slice(0, 7))

  emit('submitBook', book)
}


</script>

<template>
  <h2>Add Book To Library</h2>
  <h3>Book Read:</h3>
  <DatePicker v-model="monthYearRead" view="month" dateFormat="mm/yy" /><br>
  <img :src="populatingSelectedBook.coverImage" alt="Cover of book" style="margin: 1rem; height: 150px"/><br />
  <h3> {{populatingSelectedBook.title}}</h3>
  <h4> {{populatingSelectedBook.author}}</h4>
  <h4> {{populatingSelectedBook.description}}</h4>
  <button @click="submitBook(populatingSelectedBook)" type="submit">Confirm</button>
</template>

<style scoped>

</style>