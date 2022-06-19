<script>
import { humanDate } from "../helpers/index.js";

export default {
  props: {
    candidate: Object,
  },
  methods: {
    formatDate: humanDate,
  },
};
</script>

<template>
  <div class="candidate-box" :v-if="candidate && candidate.last_name">
    <div class="head">
      <h4>Name: {{ candidate?.last_name }}, {{ candidate?.name }}</h4>
      <div class="date">Updated at {{ formatDate(candidate?.update) }}</div>
      <div class="date">
        More Info:
        <a class="link" :href="candidate?.info_link" target="_blank"
          >External Link</a
        >
      </div>
    </div>
    <div class="description">{{ candidate?.description }}</div>
    <div class="email">{{ candidate?.email }}</div>
  </div>
</template>

<style scoped>
.candidate-box {
  border: solid 1px rgba(0, 0, 0, 0.05);
  padding: 0.5rem;
}
.description {
  font-size: 0.8rem;
  line-height: 1.4;
}
.head {
  display: grid;
  grid-template-columns: 1fr auto auto;
  gap: 0.5rem;
  font-weight: bold;
}
</style>
