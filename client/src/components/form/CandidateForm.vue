<script>
import { humanDateTime, API_CANDIDATES } from "../../helpers/index.js";

export default {
  setup() {},
  components: {},
  data: () => ({
    form: {},
  }),
  created() {},
  watch: {},
  methods: {
    isEdit() {
      console.log("isEdit", this.$route.params.id ? true : false);
      return this.$route.params.id ? true : false;
    },
    async update() {
      const url = `${API_CANDIDATES}`;
      fetch(url, {
        method: "UPDATE",
        body: JSON.stringify(this.form),
        headers: {
          "Content-Type": "application/json",
        },
      });
    },
    async create() {
      const url = `${API_CANDIDATES}`;
      fetch(url, {
        method: "POST",
        body: JSON.stringify(this.form),
        headers: {
          "Content-Type": "application/json",
        },
      });
    },
    formatDate: humanDateTime,
  },
  computed: {},
};
</script>

<template>
  <div>
    <h2 v-if="isEdit()">Edit form</h2>
    <h2 v-else>Create Candidate</h2>
    das
  </div>
</template>

<style scoped>
li {
  margin-bottom: 2rem;
  padding: 1rem 0.3rem;
}
</style>