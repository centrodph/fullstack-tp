<script>
import { mapState } from "pinia";
import { useInterviewsStore } from "@/stores/interviews";

export default {
  setup() {
    const interviewsStore = useInterviewsStore();
    return {
      logout: interviewsStore.logout,
    }
  },
  components: {},
  data() {},
  created() {},
  watch: {},
  methods: {},
  computed: {
    ...mapState(useInterviewsStore, ["user"]),
  },
};
</script>
<template>
  <div v-if="user" class="user">
    <span
      >Logged in as <em>{{ user }}</em></span
    >
    <button @click="logout()">Logout</button>
  </div>
</template>

<style scoped>
.user {
  display: flex;
}
span {
  font-weight: bold;
}
span em {
  font-size: 1.2em;
  color: var(--green);
}
button {
  margin-left: 1rem;
}
</style>
