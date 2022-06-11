import { defineStore } from "pinia";

export const useInterviewsStore = defineStore({
  id: "interviews",
  state: () => ({
    list: [],
  }),
  getters: {
    doubleCount: (state) => state.counter * 2,
  },
  actions: {
    list() {
      console.log("list");
    },
  },
});
