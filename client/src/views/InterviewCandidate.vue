<script>
import Candidate from "@/components/Candidate.vue";
import {
  humanDateTime,
  API_INTERVIEWS,
  API_CHALLENGES,
} from "../helpers/index.js";

export default {
  components: {
    Candidate,
  },
  data: () => ({
    interview: {},
    challenge: {},
  }),

  created() {
    this.fetchData();
  },

  watch: {},
  methods: {
    async fetchData() {
      const id = this.$route.params.id;
      const url = `${API_INTERVIEWS}${id}`;
      this.interview = await (await fetch(url)).json();
      const urlChallenge = `${API_CHALLENGES}${this.interview.challenge}`;
      this.challenge = await (await fetch(urlChallenge)).json();
    },
    formatDate: humanDateTime,
  },
};
</script>

<template>
  <div>
    <h2>Interview [{{ $route.params.id }}]</h2>
    <h4 class="description">{{ interview.description }}</h4>
    <div class="interview-main">
      <div class="inteview-candidate">
        <h3>Candidato</h3>
        <Candidate :candidate="interview.candidate_data" />
      </div>
      <div class="inteview-candidate">
        <h3>Challenge</h3>

        <h3>Comments</h3>
      </div>
    </div>
  </div>
</template>

<style scoped>
.description {
  font-weight: normal;
  color: var(--gray-dark-1);
}
h3 {
  color: var(--blue-dark);
}
.interview-main {
  margin-top: 1rem;
  display: grid;
  grid-auto-flow: row;
  gap: 1rem;
}
</style>