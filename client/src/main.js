import { createApp } from "vue";

import App from "./App.vue";
import router from "./router";
import appStore from "./stores/store";

const app = createApp(App);

app.use(appStore);
app.use(router);

app.mount("#app");
console.clear();
