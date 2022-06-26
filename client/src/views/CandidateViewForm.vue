<script>
import CandidateForm from "@/components/form/CandidateForm.vue";

export default {
  setup() {},
  components: {
    CandidateForm,
  },
  data() {},
  created() {},
  watch: {},
  methods: {},
  computed: {},
};
</script>

<template>
  <div class="main-form">
    <CandidateForm :id="$route.params.id" />
  </div>
</template>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  background: none;
}
li {
  margin-bottom: 2rem;
  padding: 1rem 0.3rem;
}
</style>