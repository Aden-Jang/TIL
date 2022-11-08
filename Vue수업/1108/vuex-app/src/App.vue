<template>
  <div id="app">
    <!-- <h1>{{ $store.state.message }}</h1> -->
    <h1>{{ message }}</h1>
    <!-- <h3>{{ $store.getters.messageLength }}</h3> -->
    <h3>{{ messagelength }}</h3>
    <h3> X2 : {{ doublelength }}</h3>
    <input 
      type="text"
      @keyup.enter="changeMessage"
      v-model="inputData"
      >
  </div>
</template>

<script>

export default {
  name: 'App',
  data: function() {
    return{
      inputData: null
    }
  },
  computed: {
    message() {
      return this.$store.state.message
    },
    messagelength() {
      return this.$store.getters.messageLength
    },
    doublelength() {
      return this.$store.getters.doubleLength
    },
  },
  components: {

  },
  methods: {
    changeMessage() {
      // console.log(event.target.value)
      // this.inputData = event.target.value
      this.$store.dispatch('changeMessage', this.inputData)
      this.inputData = null
    }
  },
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
</style>
