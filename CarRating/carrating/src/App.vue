<script setup lang="ts">
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div id="app" class="app-container">
    <Header />

    <main class="main-content">
      <router-view /> <!-- Home.vue, Form.vue, Result.vue will render here -->
    </main>

    <Footer />
  </div>
</template>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  padding: 20px;
  background: #f5f5f5;
  display: flex;
  justify-content: center; /* center horizontally */
  align-items: center;     /* center vertically */
}
</style>
