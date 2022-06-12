<script>
import Candidate from "@/components/Candidate.vue";
import { humanDateTime, API_INTERVIEWS } from "../helpers/index.js";

export default {
  components: {
    Candidate,
  },
  data: () => ({
    list: [],
    search: "",
    commits: null,
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
      this.list = await (await fetch(API_INTERVIEWS)).json();
    },
    formatDate: humanDateTime,
  },
};
</script>

<template>
  <div>
    <h2>Interview List</h2>
    <div class="search">
      <label :for="search">Search</label>
      <input type="text" :id="search" name="search" v-model="search" />
    </div>
    <ul>
      <li
        v-for="{
          code_access,
          date,
          description,
          id,
          interviewer,
          interviewer_username,
          candidate_data,
        } in list"
        :key="id"
      >
        <h3>
          {{ description }}
        </h3>
        <Candidate :candidate="candidate_data" />
        <p><strong>Dia y Hora: </strong>{{ formatDate(date) }}</p>
        <p>
          <strong>Entrevistador: </strong>{{ interviewer_username }}
          <RouterLink :to="'/user/' + interviewer">View</RouterLink>
        </p>
        <p><strong>Access Code: </strong>{{ code_access }}</p>
      </li>
    </ul>
  </div>
</template>

<style scoped>
a {
  text-decoration: none;
  color: #42b883;
}
li {
  line-height: 2;
  margin-bottom: 2rem;
  border-top: solid 1px #ccc;
  border-bottom: solid 1px #ccc;
  padding: 1rem 0.3rem;
}
h2 {
  margin-bottom: 2rem;
}

.search {
  display: grid;
  grid-template-columns: auto 120px;
  grid-gap: 10px;
  justify-content: flex-start;
  margin-bottom: 1rem;
}
.search label {
  font-weight: bold;
}
.search input {
  width: 100%;
}
</style>