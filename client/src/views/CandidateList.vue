<script>
import CandidateBox from "@/components/CandidateBox.vue";
import CandidateAddButton from "@/components/CandidateAddButton.vue";
import CandidateEditButton from "@/components/CandidateEditButton.vue";
import {
  humanDateTime,
  API_CANDIDATES,
  secureFetch,
} from "../helpers/index.js";

export default {
  setup() {},
  components: {
    CandidateBox,
    CandidateAddButton,
    CandidateEditButton,
  },
  data: () => ({
    list: [],
  }),

  created() {
    this.fetchData();
  },

  watch: {
    // re-fetch whenever currentBranch changes
    search: "fetchData",
  },

  methods: {
    async fetchData() {
      this.list = await (await secureFetch(API_CANDIDATES)).json();
    },
    formatDate: humanDateTime,
  },
  computed: {},
};
</script>

<template>
  <div>
    <header>
      <h2>Candidate List</h2>
      <CandidateAddButton />
    </header>
    <ul>
      <li v-for="candidate in list" :key="candidate.id">
        <CandidateBox :candidate="candidate" />
        <div class="jf-l">
          <CandidateEditButton :id="candidate.id" />
        </div>
      </li>
    </ul>
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