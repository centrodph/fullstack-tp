<script>
export default {
  props: {
    status: Object,
  },
  setup() {},
  components: {},
  data() {},
  created() {},
  watch: {},
  methods: {},
  computed: {},
};
</script>
<template>
  <div
    :class="`status-interview status-${String(
      status.title
    ).toLocaleLowerCase()}`"
  >
    <span>{{ status.title }}</span>
  </div>
</template>

<style scoped>
.status-interview {
  display: flex;
  width: fit-content;
  padding: 0.1rem 0.5rem;
  background: var(--gray-dark-1);
  color: white;
  border-radius: 0.3rem;
  height: 20px;
  font-size: 13px;
  line-height: 17px;
}

.status-done {
  background: var(--green-darker);
  color: white;
}
.status-pending {
  background: orange;
  color: white;
}
.status-closed {
  background: red;
  color: white;
}
</style>
