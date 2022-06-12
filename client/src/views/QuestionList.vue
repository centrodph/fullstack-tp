<script>
import QuestionOption from "@/components/QuestionOption.vue";
import { humanDateTime, API_QUESTIONS } from "../helpers/index.js";

export default {
  components: {
    QuestionOption,
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
      <li v-for="{ id, title, update, options } in list" :key="id">
        <div class="simple-header">
          <h3>
            {{ title }}
          </h3>
          <p><strong>Updated: </strong>{{ formatDate(update) }}</p>
        </div>
        <div v-for="option in options" :key="option.id">
          <QuestionOption :option="option" />
        </div>
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
</style>