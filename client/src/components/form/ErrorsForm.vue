<script>
export default {
  props: {
    errors: {
      type: Object,
      default: () => ({}),
    },
  },
  setup() {},
  components: {},
  data: () => ({}),
  created() {},
  watch: {},
  methods: {},
  computed: {},
};
</script>

<template>
  <div class="error-box">
    <div class="error-item" v-for="(error, key) in errors" :key="key">
      <strong>{{ key }}</strong>
      <span>{{ Array.isArray(error) ? error.join(", ") : error }}</span>
    </div>
  </div>
</template>

<style scoped>
.error-item strong {
  text-transform: capitalize;
}
.error-item {
  display: grid;
  grid-template-columns: 120px 1fr;
  margin-bottom: 0.2rem;
  color: rgb(124, 11, 11);
}
</style>