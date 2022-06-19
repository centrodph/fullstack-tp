<script>
import CandidateBox from "@/components/CandidateBox.vue";
import { humanDateTime, API_CANDIDATES } from "../helpers/index.js";

export default {
  setup() {},
  components: {
    CandidateBox,
  },
  data: () => ({
    form: {},
  }),

  created() {
    // fetch on init
    this.fetchData();
  },

  watch: {
    // re-fetch whenever currentBranch changes
    search: "fetchData",
  },

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
    <h2>Candidate List</h2>
    <ul>
      <li v-for="candidate in list" :key="candidate.id">
        <CandidateBox :candidate="candidate" />
        <div class="jf-l"></div>
      </li>
    </ul>
  </div>
</template>

<style scoped>
li {
  margin-bottom: 2rem;
  padding: 1rem 0.3rem;
}
</style>