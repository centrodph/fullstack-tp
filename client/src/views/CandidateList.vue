<script>
import InterviewStatus from "@/components/InterviewStatus.vue";
import CandidateBox from "@/components/CandidateBox.vue";
import { humanDateTime, API_CANDIDATES } from "../helpers/index.js";

export default {
  setup() {},
  components: {
    CandidateBox,
    InterviewStatus,
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