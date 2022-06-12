<script>
export default {
  props: {
    option: Object,
  },
};
</script>

<template>
  <div class="question-option">
    <span v-if="option.correct"> ✅ </span>
    <span v-else>🛑</span>
    {{ option.option }}
  </div>
</template>

<style scoped>
.question-option {
  background: rgba(0, 0, 0, 0.02);
  padding: 0.3rem;
}
</style>
