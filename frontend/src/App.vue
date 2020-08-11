<template>
  <v-app>
    <v-main>
      <v-app-bar dense dark collapse-on-scroll prominent>
        <v-toolbar-title>Title</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn
          class="font-weight-bold my-3 rounded-xl"
          outlined
          :loading="!shakehand"
          dark
          >{{ shakehand }}</v-btn
        >

        <template v-slot:extension>
          <v-tabs grow>
            <template v-for="(r, index) in routes">
              <v-tab
                :key="index"
                :to="r.to"
                color="primary"
                dark
                slider-color="primary"
              >
                {{ r.label }}
              </v-tab>
            </template>
          </v-tabs>
        </template>
      </v-app-bar>

      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      routes: [
        { label: "Home", to: "/" },
        { label: "App", to: "/about" },
      ],
      shakehand: false,
    };
  },
  created() {
    this.shakehand = false;
    this.axios.get("/api/shakehand").then((response) => {
      this.shakehand = response.data.data;
    });
  },
};
</script>

<style>
#app {
  /* font-family: 'Avenir', Helvetica, Arial, sans-serif; */
  font-family: "Open Sans", sans-serif;
  /* font-family: 'Noto Sans', sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

a {
  text-decoration: none !important;
  color: inherit !important;
}

.col,
.row {
  margin: 0 !important;
}
</style>
