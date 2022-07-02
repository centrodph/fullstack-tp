import { useInterviewsStatusStore } from "@/stores/interviewStatus";

export const isDoneStatus = (statusId) => {
  const store = useInterviewsStatusStore();
  return String(store.statusMap[statusId].title).toLocaleLowerCase() === "done";
};
