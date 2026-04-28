<script setup>
import BookSearchResultCard from "@/components/BookSearchResultCard.vue";

  defineProps({ searchResults: Object })

  </script>

  <template>
    <BookSearchResultCard
        v-for="book in searchResults"
        :key="book.title"
        :book="book"
    />
  </template>

  <style scoped>

  </style>