<!--
This example fetches latest Vue.js commits data from GitHub’s API and displays them as a list.
You can switch between the two branches.
-->

<script>
import { humanDate } from "../helpers/index.js";
const API_URL = "http://localhost:8000/api/interviews/";

export default {
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
      const url = `${API_URL}`;
      this.list = await (await fetch(url)).json();
    },
    formatDate: humanDate,
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
        v-for="{ code_access, date, description, id, interviewer } in list"
        :key="id"
      >
        <h3>
          {{ description }}
        </h3>
        <p><strong>Dia y Hora: </strong>{{ formatDate(date) }}</p>
        <p><strong>Entrevistador: </strong>{{ interviewer }}</p>
        <p><strong>Access Code: </strong>{{ code_access }}</p>
      </li>
    </ul>
  </div>
</template>

<style>
a {
  text-decoration: none;
  color: #42b883;
}
li {
  line-height: 1.5em;
  margin-bottom: 20px;
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