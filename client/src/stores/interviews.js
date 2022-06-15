import { defineStore } from "pinia";

export const useInterviewsStore = defineStore({
  id: "user",
  state: () => ({
    user: null,
  }),
  getters: {
    getUser: (state) => state.user,
  },
  actions: {
    login() {
      console.log("login", this.getUser());
    },
  },
});
