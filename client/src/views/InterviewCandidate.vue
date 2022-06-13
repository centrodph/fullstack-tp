<script>
import Candidate from "@/components/Candidate.vue";
import Question from "@/components/Question.vue";
import {
  humanDateTime,
  API_INTERVIEWS,
  API_CHALLENGES,
  API_INTERVIEW_REPORT,
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
    comments: {},
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
    onChange(e) {
      const { question, questionOption } = e.target.dataset;
      this.answer[this.getKey(question, questionOption)] = questionOption;
      this.updateSelection(question, questionOption);
    },
    onChangeComment(e) {
      const { question } = e.target.dataset;
      this.comments[question] = e.target.value;
    },
    getKey(question, questionOption) {
      return `${question}_${questionOption}`;
    },
    updateSelection(question, questionOption) {
      console.log(this.comments);
      const url = `${API_INTERVIEW_REPORT}`;
      const data = {
        comments: this.comments[question] || "-",
        interview: this.interview.id,
        candidate: this.interview.candidate_data.id,
        challenge: this.interview.challenge,
        question: question,
        question_option: questionOption,
      };
      fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json",
        },
      });
    },
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
                      :data-question="question.id"
                      :data-question-option="option.id"
                      :value="answer[getKey(question.id, option.id)]"
                    />
                    <label :for="option.id">{{ option.option }}</label>
                  </div>
                  <h5>Comentarios</h5>
                  <textarea
                    name="comment"
                    @input="onChangeComment($event)"
                    :data-question="question.id"
                  ></textarea>
                </div>
              </li>
            </ol>
          </div>
        </div>
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
textarea {
  resize: none;
  width: 100%;
  border: solid 1px #ccc;
}
</style>