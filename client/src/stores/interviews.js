import { defineStore } from "pinia";
import router from "../router";

export const useInterviewsStore = defineStore({
  id: "user",
  state: () => ({
    user: "user",
    role: "user",
  }),
  getters: {
    getUser: (state) => state.user,
  },
  actions: {
    login(user, pass) {
      console.log("login", user, pass);
      if (user === "user" && pass === "pass") {
        console.log("login success");
        this.user = user;
        this.role = "user";
        router.push("/interviews");
      } else if (user === "admin" && pass === "pass") {
        console.log("login success");
        this.user = user;
        this.role = "admin";
        router.push("/interviews");
      }
    },
    logout() {
      console.log("Logout user", this.user);
    },
  },
});
