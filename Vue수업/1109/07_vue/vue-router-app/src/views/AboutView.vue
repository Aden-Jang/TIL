<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{ name: 'home' }">홈으로</router-link>
    <button @click="toHome">홈으로!</button>
  </div>
</template>

<script>
export default {
  name: "AboutView",
  methods: {
    toHome() {
      this.$router.push({ name: "home" })
    },
  },
}
</script>
