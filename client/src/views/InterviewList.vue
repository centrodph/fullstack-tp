<script>
import { mapState } from "pinia";
import InterviewStatus from "@/components/InterviewStatus.vue";
import CandidateBox from "@/components/CandidateBox.vue";
import {
  humanDateTime,
  API_INTERVIEWS,
  isDoneStatus,
} from "../helpers/index.js";
import { useInterviewsStatusStore } from "@/stores/interviewStatus";

export default {
  setup() {
    const status = useInterviewsStatusStore();
    status.fetchStatuses();
  },
  components: {
    CandidateBox,
    InterviewStatus,
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
    isDoneStatus,
  },
  computed: {
    ...mapState(useInterviewsStatusStore, ["statusMap"]),
  },
};
</script>

<template>
  <div>
    <h2>Interview List</h2>
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
          status,
        } in list"
        :key="id"
      >
        <h3>
          {{ description }} <InterviewStatus :status="statusMap[status]" />
        </h3>
        <CandidateBox :candidate="candidate_data" />
        <p><strong>Dia y Hora: </strong>{{ formatDate(date) }}</p>
        <p>
          <strong>Entrevistador: </strong>{{ interviewer_username }}
          <RouterLink :to="'/user/' + interviewer">View</RouterLink>
        </p>
        <p><strong>Access Code: </strong>{{ code_access }}</p>
        <div class="jf-l">
          <RouterLink
            v-if="!isDoneStatus(status)"
            class="btn-ir-entrevista"
            :to="'/interview/' + id"
            >Ir a la entrevista</RouterLink
          >
          <RouterLink
            v-if="isDoneStatus(status)"
            class="btn-ir-resultados"
            :to="'/interview/' + id + '/results'"
            >Ver resultados</RouterLink
          >
        </div>
      </li>
    </ul>
  </div>
</template>

<style scoped>
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
h3 {
  display: flex;
  align-items: center;
  justify-content: space-between;
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