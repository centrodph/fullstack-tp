<script>
import CandidateForm from "@/components/form/CandidateForm.vue";
import { humanDateTime, API_CANDIDATES } from "../helpers/index.js";

export default {
  setup() {},
  components: {
    CandidateForm,
  },
  data: () => ({
    list: [],
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
    async fetchData() {
      this.list = await (await fetch(API_CANDIDATES)).json();
    },
    formatDate: humanDateTime,
  },
  computed: {},
};
</script>

<template>
  <div class="main-form">
    <CandidateForm :id="$route.params.id" />
  </div>
</template>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  background: none;
}
li {
  margin-bottom: 2rem;
  padding: 1rem 0.3rem;
}
</style>