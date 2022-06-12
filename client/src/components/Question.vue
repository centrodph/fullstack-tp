<script>
export default {
  props: {
    question: Object,
  },
};
</script>

<template>
  <div class="question">
    {{ question.title }}
  </div>
</template>

<style scoped>
.question-option {
  color: rgba(60, 60, 60, 0.7);
  margin: 0.3rem;
}
</style>
