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
    <h2>Create form</h2>
  </div>
</template>

<style scoped>
li {
  margin-bottom: 2rem;
  padding: 1rem 0.3rem;
}
</style>