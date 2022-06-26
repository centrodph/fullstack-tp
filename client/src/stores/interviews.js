import { defineStore } from "pinia";
import { API_LOGIN } from "../helpers/index.js";
import router from "../router";

export const useInterviewsStore = defineStore({
  id: "user",
  state: () => ({
    user: null,
    role: null,
    errors: {},
  }),
  getters: {
    getUser: (state) => state.user,
    getErrors: (state) => state.user,
  },
  actions: {
    async login(username, password) {
      console.log("Getting access token", username, password);
      try {
        const response = await fetch(API_LOGIN, {
          method: "POST",
          body: JSON.stringify({
            username,
            password,
          }),
          headers: {
            "Content-Type": "application/json",
          },
        });
        const r = await response.json();
        if (response.status > 300) {
          this.errors = r;
        } else {
          console.log("LOGIN OK", r);
        }
      } catch (error) {
        this.errors = { error };
      }
      console.log(this.errors);
      // if (user === "user" && pass === "pass") {
      //   console.log("login success");
      //   this.user = user;
      //   this.role = "user";
      //   router.push("/interviews");
      // } else if (user === "admin" && pass === "pass") {
      //   console.log("login success");
      //   this.user = user;
      //   this.role = "admin";
      //   router.push("/interviews");
      // }
    },
    logout() {
      console.log("Logout user", this.user);
      this.user = null;
      this.role = null;
      router.push("/");
    },
  },
});
