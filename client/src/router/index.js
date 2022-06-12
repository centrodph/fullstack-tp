import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/interviews",
      name: "interviewsList",
      component: () => import("../views/InterviewList.vue"),
    },
    {
      path: "/questions",
      name: "questionList",
      component: () => import("../views/QuestionList.vue"),
    },
    {
      path: "/challenges",
      name: "challengeList",
      component: () => import("../views/ChallengeList.vue"),
    },
  ],
});

export default router;
