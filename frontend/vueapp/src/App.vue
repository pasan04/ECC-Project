<template>
    <HomeView/>
</template>

<script>
import HomeView from "@/views/HomeView.vue";

export default {
  name: 'App',
  components: {
      HomeView
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
@import'~bootstrap/dist/css/bootstrap.css';
@import '../src/assets/css/styles.css';

.page-title {
    font-size: 2.5em; /* Adjust the font size as needed */
}

.subtitle {
    font-size: 0.8em; /* Adjust the font size for the subtitle */
    color: #555; /* Change the color if desired */
}

.black-link {
    color: #2c3e50;
    text-decoration: none; /* Remove underline, if needed */
}
.black-link:hover {
    text-decoration: underline; /* Underline on hover */
}

</style>
