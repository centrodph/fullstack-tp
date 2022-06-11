<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <h1>Full Stack TP</h1>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/interviews">Interviews</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
</template>

<style>
@import "@/assets/base.css";

header {
  line-height: 1.5;
  display: grid;
  background: rgba(0, 0, 0, 0.1);
  padding: 0.3rem;
  grid-template-columns: auto 1fr;
  align-items: center;
}
nav {
  padding-left: 1rem;
}

#app {
  display: grid;
  grid-template-rows: auto 1fr;
}
</style>
