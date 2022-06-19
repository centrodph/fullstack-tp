import { defineStore } from "pinia";
import { API_INTERVIEW_STATUS } from "../helpers/index.js";

export const useInterviewsStatusStore = defineStore({
  id: "interviewStatus",
  state: () => ({
    statuses: [],
    statusMap: {},
  }),
  getters: {
    getStatuses: (state) => state.statuses,
    getStatus: (state) => state.status,
  },
  actions: {
    async fetchStatuses() {
      console.log("Getting statuses");
      this.statuses = await (await fetch(API_INTERVIEW_STATUS)).json();
      this.statuses.forEach((status) => {
        this.statusMap[status.id] = status;
      });
    },
  },
});
