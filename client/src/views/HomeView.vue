<script>
/**
 * https://pinia.vuejs.org/core-concepts/actions.html#with-setup
 */
import { useInterviewsStore } from "@/stores/interviews";
export default {
  setup() {
    const interviews = useInterviewsStore();

    return { interviews };
  },
  components: {},
  data: () => ({}),

  created() {
    console.log("Created");
  },

  watch: {},
  methods: {
    save(e) {
      e.preventDefault();
      this.interviews.login();
    },
  },
};
</script>

<template>
  <main>
    <form v-on:submit="save($event)">
      <div class="input">
        <label :for="search">User</label>
        <input type="text" :id="user" name="user" v-model="user" />
      </div>
      <div class="input">
        <label :for="search">Pass</label>
        <input type="password" :id="pass" name="pass" v-model="pass" />
      </div>
      <div class="input">
        <button class="btn-ir-entrevista">Login</button>
      </div>
    </form>
  </main>
</template>

<style scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: calc(100vh - 200px);
}
form {
  padding: 2rem;
  max-width: 400px;
}
button {
  width: 100%;
}
</style>