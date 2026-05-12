<script setup>
import {ref} from "vue";
import DatePicker from 'primevue/datepicker';
import {FloatLabel} from "primevue";
import {computed} from "vue";

const emit = defineEmits(['submitBook'])
const props = defineProps({
  populatingSelectedBook: Object,
  editingBook: Object,
})
const monthRead = ref(new Date())
monthRead.value = null

const currentBook = computed(() => {
  return props.populatingSelectedBook || props.editingBook
})

function submitBook(book) {
  let mode = ''
  if (props.populatingSelectedBook) {
    mode = 'add'
  } else {
    mode = 'edit'
  }
  const formattedDate = monthRead.value.toISOString().slice(0, 7)
  book["monthRead"] = formattedDate;
  const updatedBook = {
    ...book,
    monthRead: formattedDate
  }
  emit('submitBook', {bookPassed: updatedBook, mode: mode})
}
</script>

<template>
  <h2>Add Book To Library</h2>
  <h3>Book Read:</h3>
  <FloatLabel variant="on">
    <DatePicker v-if="editingBook" v-model="monthRead" view="month" dateFormat="MM - yy" showClear inputId="on_label" showIcon />
    <DatePicker v-else v-model="monthRead" view="month" dateFormat="MM - yy" showClear inputId="on_label" showIcon/>
    <label for="on_label">Select Month Read</label>
  </FloatLabel>
    <div v-if='monthRead'>
      <button v-if="populatingSelectedBook" @click="submitBook(populatingSelectedBook)" type="submit">Add Book</button>
      <button v-else @click="submitBook(currentBook)" type="submit">Update Book</button>
    </div>
  <br>
    <img :src="currentBook.coverImage" alt="Cover of book" style="margin: 1rem; height: 150px"/>
    <h3> {{currentBook.title}} </h3>
    <h4> {{currentBook.author}} </h4>
    <h4> {{currentBook.description}} </h4>


</template>

<style scoped>

</style>