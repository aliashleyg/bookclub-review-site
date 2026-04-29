<script setup>
import BookSearchResultCard from "@/components/BookSearchResultCard.vue";

defineProps({ searchResults: Object })

const emit = defineEmits(['selectBookClick'])

function passSelectedBook(book) {
  emit('selectBookClick', book)
}
  </script>

  <template>
    <BookSearchResultCard
        v-for="book in searchResults"
        :key="book.title"
        :book="book"
        @select-book-click="passSelectedBook"
    />
  </template>

  <style scoped>

  </style>