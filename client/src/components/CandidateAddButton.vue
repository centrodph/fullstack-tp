<script>
import { RouterLink } from "vue-router";

export default {
  setup() {},
  components: {
    RouterLink,
  },
  data() {},
  created() {},
  watch: {},
  methods: {},
  computed: {},
};
</script>
<template>
  <div class="candidate-add-button">
    <RouterLink to="/candidate/form" class="add">Add Candidate</RouterLink>
  </div>
</template>

<style scoped>
button {
  width: fit-content;
  margin-left: 1rem;
}
</style>
