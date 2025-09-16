<template>
  <div id="app" class="container">
    <Chat />
  </div>
</template>

<script setup>
import Chat from "./components/Chat.vue"
</script>

<style>
body {
  font-family: Arial, sans-serif;
  background: #f4f4f4;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>
