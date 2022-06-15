<script>
import { mapState } from "pinia";
import { RouterLink, RouterView } from "vue-router";
import { useInterviewsStore } from "@/stores/interviews";

export default {
  setup() {},
  components: {
    RouterLink,
    RouterView,
  },
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
  <div>
    <header>
      <h1>Entrevistas</h1>
      <div class="wrapper">
        <nav v-if="user">
          <RouterLink to="/interviews">Interviews</RouterLink>
          <RouterLink to="/questions">Questions</RouterLink>
          <RouterLink to="/challenges">Challenges</RouterLink>
        </nav>
        <div v-if="user" class="user">
          <span>{{ user }}</span>
          <button @click="user.logout()">Logout</button>
        </div>
      </div>
    </header>
    <div id="main-content">
      <RouterView />
    </div>
  </div>
</template>

<style>
@import "@/assets/base.css";

header {
  line-height: 1.5;
  display: grid;
  background: rgba(0, 0, 0, 0.1);
  padding: 0.3rem 1rem;
  grid-template-columns: auto 1fr;
  align-items: center;
}
nav {
  padding-left: 1rem;
}
nav a {
  padding: 0.1rem 0.3rem;
}

#app {
  display: grid;
  grid-template-rows: auto 1fr;
}
#main-content {
  padding: 1rem;
}
.wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>
