<script>
import Candidate from "@/components/Candidate.vue";
import { humanDateTime, API_QUESTIONS } from "../helpers/index.js";

export default {
  components: {
    Candidate,
  },
  data: () => ({
    list: [],
    search: "",
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
      this.list = await (await fetch(API_QUESTIONS)).json();
    },
    formatDate: humanDateTime,
  },
};
</script>

<template>
  <div>
    <h2>Question List</h2>
    <ul>
      <li v-for="{ id, title, update } in list" :key="id">
        <h3>
          {{ title }}
        </h3>
        <p><strong>Updated: </strong>{{ formatDate(update) }}</p>
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