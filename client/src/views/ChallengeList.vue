<script>
import Question from "@/components/Question.vue";
import { humanDate, API_CHALLENGES } from "../helpers/index.js";

export default {
  components: {
    Question,
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
      this.list = await (await fetch(API_CHALLENGES)).json();
    },
    formatDate: humanDate,
  },
};
</script>

<template>
  <div>
    <h2>Challenge List</h2>
    <ul>
      <li
        v-for="{ id, description, title, update, questions } in list"
        :key="id"
      >
        <div class="simple-header">
          <h3>
            {{ title }}
          </h3>
          <p><strong>Updated: </strong>{{ formatDate(update) }}</p>
        </div>
        <p class="description">{{ description }}</p>
        <ol>
          <li v-for="question in questions" :key="question.id">
            <Question :question="question" />
          </li>
        </ol>
      </li>
    </ul>
  </div>
</template>

<style scoped>
a {
  text-decoration: none;
  color: #42b883;
}
.description {
  color: var(--blue-dark);
}
ol {
  list-style: none;
  counter-reset: my-awesome-counter;
  padding-left: 1rem;
}
ol li {
  counter-increment: my-awesome-counter;
  display: flex;
  padding: 0.2rem 0;
  font-size: 0.8rem;
}
ol li::before {
  content: counter(my-awesome-counter) ". ";
  color: var(--blue-darker);
  font-weight: bold;
  margin-right: 0.5rem;
}

h2 {
  margin-bottom: 2rem;
}
</style>