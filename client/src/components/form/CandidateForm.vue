<script>
import ErrorsForm from "@/components/form/ErrorsForm.vue";
import BackBtn from "@/components/form/BackBtn.vue";
import SaveBtn from "@/components/form/SaveBtn.vue";
import { humanDateTime, API_CANDIDATES } from "../../helpers/index.js";
undefined;
undefined;
undefined;

export default {
  setup() {},
  components: { SaveBtn, BackBtn, ErrorsForm },
  data: () => ({
    form: {},
    errors: {},
  }),
  created() {},
  watch: {},
  methods: {
    isEdit() {
      console.log("isEdit", this.$route.params.id ? true : false);
      return this.$route.params.id ? true : false;
    },
    handleBack() {
      this.$router.push("/candidates");
    },
    async onSubmit() {
      console.log("Submit");
      if (this.isEdit()) {
        await this.update();
      } else {
        await this.create();
      }
    },
    async update() {
      const url = `${API_CANDIDATES}`;
      fetch(url, {
        method: "UPDATE",
        body: JSON.stringify(this.form),
        headers: {
          "Content-Type": "application/json",
        },
      });
    },
    async create() {
      const url = `${API_CANDIDATES}`;
      try {
        const response = await fetch(url, {
          method: "POST",
          body: JSON.stringify(this.form),
          headers: {
            "Content-Type": "application/json",
          },
        });
        const r = await response.json();
        if (response.status > 300) {
          this.errors = r;
        } else {
          this.$router.push(`/candidates`);
        }
      } catch (error) {
        this.errors = { error };
      }
    },
    formatDate: humanDateTime,
  },
  computed: {},
};
</script>

<template>
  <div>
    <h2 v-if="isEdit()">Edit form</h2>
    <h2 v-else>Create Candidate</h2>
    <ErrorsForm :errors="errors" />
    <form @submit.prevent="onSubmit">
      <div class="input">
        <label for="name">First name</label>
        <input type="text" name="name" v-model="form.name" />
      </div>
      <div class="input">
        <label for="name">Last Name</label>
        <input type="text" name="last_name" v-model="form.last_name" />
      </div>
      <div class="input">
        <label for="name">LinkedIn</label>
        <input type="text" name="name" v-model="form.info_link" />
      </div>
      <div class="input">
        <label for="name">Description</label>
        <textarea
          name="description"
          v-model="form.description"
          rows="8"
        ></textarea>
      </div>
      <div class="form-footer">
        <BackBtn @back="handleBack" />
        <SaveBtn />
      </div>
    </form>
  </div>
</template>

<style scoped>
li {
  margin-bottom: 2rem;
  padding: 1rem 0.3rem;
}
</style>