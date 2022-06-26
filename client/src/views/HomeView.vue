<script>
import ErrorsForm from "@/components/form/ErrorsForm.vue";
import { useInterviewsStore } from "@/stores/interviews";
export default {
  setup() {
    const interviews = useInterviewsStore();

    return { interviews };
  },

  components: {
    ErrorsForm,
  },
  data: () => ({
    user: this,
    pass: null,
  }),
  created() {
    console.log("Created");
  },
  watch: {},
  methods: {
    save(e) {
      e.preventDefault();
      this.interviews.login(this.user, this.pass);
    },
  },
  computed: {
    // ...mapState(useInterviewsStore, ["errors"]),
  },
};
</script>

<template>
  <main>
    <ErrorsForm :errors="interviews.errors" />
    <form v-on:submit="save($event)" autocomplete="off">
      <div class="input">
        <label :for="user">User</label>
        <input type="text" id="user" v-model="user" autocomplete="off" />
      </div>
      <div class="input">
        <label :for="pass">Pass</label>
        <input type="password" id="pass" v-model="pass" autocomplete="off" />
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
