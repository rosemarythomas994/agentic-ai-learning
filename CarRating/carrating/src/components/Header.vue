<script setup lang="ts">
import logo from '../images/revv.png'
</script>

<template>
  <header class="header">
    <img :src="logo" alt="Logo" class="logo" />
  </header>
</template>

<style scoped>
.header {
  background-color: #ffffff;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  padding: 12px 24px;
  display: flex;
  align-items: center;
}
.logo {
  height: 50px;
  width: auto;
}
</style>
