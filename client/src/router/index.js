import { useInterviewsStore } from "@/stores/interviews";
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
    {
      path: "/interview/:id",
      name: "interviewCandidate",
      component: () => import("../views/InterviewCandidate.vue"),
    },
  ],
});

router.beforeEach(async (to) => {
  const interviews = useInterviewsStore();
  console.log("Checking login");
  if (!interviews.user && to.path !== "/") {
    return router.push("/");
  }
});

export default router;
