<script>
import { mapState, mapActions } from "pinia";
import { useInterviewsStore } from "@/stores/interviews";

export default {
  setup() {},
  components: {},
  data() {},
  created() {},
  watch: {},
  methods: {},
  computed: {
    ...mapActions(useInterviewsStore, ["logout"]),
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

<style>
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
