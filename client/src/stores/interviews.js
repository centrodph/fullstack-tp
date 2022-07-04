import { defineStore } from "pinia";
import { API_LOGIN } from "../helpers/index.js";
import router from "../router";

export const useInterviewsStore = defineStore({
  id: "user",
  state: () => ({
    user: null,
    role: null,
    access: null,
    refresh: null,
    errors: {},
  }),
  getters: {
    getUser: (state) => state.user,
    getErrors: (state) => state.errors,
  },
  actions: {
    async login(username, password) {
      console.log("Getting access token", username, password);
      this.errors = null;
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
          console.log(r);
          this.errors = r;
        } else {
          this.user = username;
          this.access = r.access;
          this.refresh = r.refresh;
          router.push("/interviews");
        }
      } catch (error) {
        this.errors = { error };
      }
    },
    logout() {
      console.log("Logout user", this.user);
      this.user = null;
      this.role = null;
      this.access = null;
      this.refresh = null;
      router.push("/");
    },
  },
});
