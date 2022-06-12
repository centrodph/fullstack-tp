<script>
import Candidate from "@/components/Candidate.vue";
import Question from "@/components/Question.vue";
import {
  humanDateTime,
  API_INTERVIEWS,
  API_CHALLENGES,
} from "../helpers/index.js";

export default {
  components: {
    Candidate,
    Question,
  },
  data: () => ({
    interview: {},
    challenge: {},
    answer: {},
  }),

  created() {
    this.fetchData();
  },

  watch: {
    answer: console.log,
  },
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
        <div>
          <h4>{{ challenge.title }}</h4>
          <p>{{ challenge.description }}</p>
          <div>
            <h4 style="color: var(--gray-dark-1)">Preguntas</h4>
            <ol>
              <li v-for="question in challenge.questions" :key="question.id">
                <div>
                  <div class="option-question">
                    <Question :question="question" />
                  </div>
                  <div
                    v-for="option in question.options"
                    :key="option.id"
                    class="option-radio"
                  >
                    <input
                      :name="'question_' + question.id"
                      type="radio"
                      :id="option.id"
                      @change="onChange($event)"
                    />
                    <label :for="option.id">{{ option.option }}</label>
                  </div>
                </div>
              </li>
            </ol>
          </div>
        </div>
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
.option-question {
  font-weight: bold;
}
.option-radio {
  display: grid;
  padding: 0.3rem;
  grid-template-columns: auto 1fr;
  align-items: flex-start;
  gap: 0.5rem;
}
.option-radio input {
  margin-top: 5px;
}
</style>