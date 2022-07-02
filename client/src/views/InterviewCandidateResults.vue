<script>
import debounce from "lodash.debounce";
import CandidateBox from "@/components/CandidateBox.vue";
import QuestionItem from "@/components/QuestionItem.vue";
import QuestionOption from "@/components/QuestionOption.vue";
import {
  humanDateTime,
  API_INTERVIEWS,
  API_CHALLENGES,
  API_INTERVIEW_REPORT,
  calculateScore,
} from "../helpers/index.js";

export default {
  components: {
    CandidateBox,
    QuestionItem,
    QuestionOption,
  },
  data: () => ({
    interview: {},
    challenge: {},
    answer: {},
    comments: {},
  }),

  created() {
    this.fetchData();
    this.fetchLatestReport();
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
    async fetchLatestReport() {
      const id = this.$route.params.id;
      const url = `${API_INTERVIEW_REPORT}?interview=${id}`;
      const reports = await (await fetch(url)).json();
      if (reports.length > 0) {
        reports.forEach(({ comments, question, question_option }) => {
          this.answer[this.getKey(question)] = `${question_option}`;
          this.comments[this.getKey(question)] = comments;
        });
      }
    },
    calculateScore,
    formatDate: humanDateTime,
    onChange(e) {
      const { question, questionOption } = e.target.dataset;
      this.answer[this.getKey(question)] = questionOption;
      this.updateSelection(question);
    },
    onChangeComment(e) {
      const { question } = e.target.dataset;
      this.comments[question] = e.target.value;
      this.updateSelection(question);
    },
    onChangeDebounce: debounce(function (e) {
      this.onChangeComment(e);
    }, 600),
    getKey(question) {
      return `${question}`;
    },
    save() {
      Object.keys(this.answer).forEach(this.updateSelection);
    },
    updateSelection(question) {
      if (!this.answer[this.getKey(question)]) return;

      const url = `${API_INTERVIEW_REPORT}save_question_answer/`;
      const data = {
        comments: this.comments[question],
        interview: this.interview.id,
        candidate: this.interview.candidate_data.id,
        challenge: this.interview.challenge,
        question: question,
        question_option: this.answer[this.getKey(question)],
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
      <div class="interview-candidate">
        <h3>Candidato</h3>
        <div>
          <CandidateBox :candidate="interview.candidate_data" />
        </div>
      </div>
      <div class="interview-candidate">
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
                    <QuestionItem :question="question" />
                  </div>
                  <div
                    v-for="option in question.options"
                    :key="option.id"
                    :class="{
                      'option-radio': true,
                      selected:
                        String(option.id) === answer[getKey(question.id)],
                      correct:
                        String(option.id) === answer[getKey(question.id)] &&
                        option.correct,
                      wrong:
                        String(option.id) === answer[getKey(question.id)] &&
                        !option.correct,
                    }"
                  >
                    <QuestionOption :option="option" />
                  </div>
                  <h5>Comentarios</h5>
                  {{ comments[getKey(question.id)] }}
                </div>
              </li>
            </ol>
          </div>
        </div>
        <div class="floating-btn">
          <div class="jf-l">
            <div class="results">
              Total: {{ calculateScore(challenge.questions, answer) }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.interview-main {
  padding-bottom: 90px;
}
.floating-btn {
  position: fixed;
  bottom: 0;
  right: 0;
  width: 100%;
  z-index: 9999;
  padding: 1rem;
  background: #ccc;
}
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
.option-radio.selected {
  border: solid 1px gray;
}
.option-radio.selected.correct {
  background: var(--green);
}
.option-radio.selected.wrong {
  background: rgb(255, 186, 186);
}
.option-radio input {
  margin-top: 5px;
}
textarea {
  resize: none;
  width: 100%;
  border: solid 1px #ccc;
}

.results {
  font-size: 2rem;
}
</style>