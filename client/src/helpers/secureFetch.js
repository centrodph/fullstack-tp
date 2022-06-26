import { useInterviewsStore } from "@/stores/interviews";

export const secureFetchPUT = (url, data) => {
  return secureFetch(url, data, "PUT");
};

export const secureFetchPOST = (url, data) => {
  return secureFetch(url, data, "POST");
};

export const secureFetch = (url, data, method = "GET") => {
  const store = useInterviewsStore();

  return fetch(url, {
    method,
    body: method === "GET" ? undefined : JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${store.access}`,
    },
  });
};
