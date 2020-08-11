<template>
  <v-container>
    <v-row class="text-center d-flex justify-center align-center">
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        shakehand : false
      }
    },
    created() {
      this.shakehand = false
       this.axios.get('/api/shakehand').then(response =>{
        this.shakehand = response.data
      })
    },
  }
</script>
