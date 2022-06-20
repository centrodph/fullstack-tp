<script>
import { RouterLink } from "vue-router";

export default {
  props: {
    id: {
      type: Number,
    },
  },
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
  <div class="candidate-edit-button">
    <RouterLink :to="`/candidate/form/${id}`" class="edit">Edit</RouterLink>
  </div>
</template>

<style scoped>
a {
  width: fit-content;
  padding: 0.2rem;
}
</style>
