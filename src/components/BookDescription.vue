<script setup>
import {ref} from "vue";
defineProps({
  description: String,
})

const isDescriptionExpanded = ref(false)

function expandDescription(description) {
  isDescriptionExpanded.value = !isDescriptionExpanded.value
  console.log(isDescriptionExpanded.value)
}

</script>

<template>
  <p v-if="isDescriptionExpanded">
    {{description}}
    <span class="pseudoLinkStyle" @click="expandDescription()">CLOSE</span>
  </p>
  <p v-else>
    {{description.slice(0,175)}}...
    <span class="pseudoLinkStyle" @click="expandDescription()">MORE</span>
  </p>
</template>

<style scoped>
.pseudoLinkStyle {
  color: blue;
  text-decoration: underline;
}

.pseudoLinkStyle:hover {
  color: gray;
  text-decoration: underline;
}

</style>