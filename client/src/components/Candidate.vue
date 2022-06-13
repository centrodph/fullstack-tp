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
      <h4>{{ candidate?.last_name }}, {{ candidate?.name }}</h4>
      <div class="date">{{ formatDate(candidate?.update) }}</div>
      <a class="link" :href="candidate?.info_link" target="_blank"
        >Ver link externo</a
      >
    </div>
    <div class="description">{{ candidate?.description }}</div>
    <div class="email">{{ candidate?.email }}</div>
  </div>
</template>

<style scoped>
.candidate-box {
  background: rgba(0, 0, 0, 0.02);
  padding: 0.3rem;
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
