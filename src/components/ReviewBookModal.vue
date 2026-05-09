<script setup>
import {ref} from "vue";
import DatePicker from 'primevue/datepicker';
import {FloatLabel} from "primevue";

const emit = defineEmits(['submitBook'])
const props = defineProps({
  populatingSelectedBook: Object,
})

const monthRead = ref(null)

function submitBook(book) {
  console.log()
  const formattedDate = monthRead.value.toISOString().slice(0, 7)
  book["monthRead"] = formattedDate;
  const updatedBook = {
    ...book,
    monthRead: formattedDate
  }
  emit('submitBook', updatedBook)
}

</script>

<template>
  <h2>Add Book To Library</h2>
  <h3>Book Read:</h3>
  <FloatLabel variant="on">
    <DatePicker v-model="monthRead" view="month" dateFormat="mm/yy" showClear inputId="on_label"/>
    <label for="on_label">Select Month/Year Read</label><br>
  </FloatLabel>
    <img :src="populatingSelectedBook.coverImage" alt="Cover of book" style="margin: 1rem; height: 150px"/><br />
    <h3> {{populatingSelectedBook.title}}</h3>
    <h4> {{populatingSelectedBook.author}}</h4>
    <h4> {{populatingSelectedBook.description}}</h4>
    <button @click="submitBook(populatingSelectedBook)" type="submit">Confirm</button>
</template>

<style scoped>

</style>