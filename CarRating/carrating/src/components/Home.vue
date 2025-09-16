<template>
  <div class="home">
    <h1>🚗 Vehicle Rating Prediction System</h1>
    <p>Enter your vehicle details and get AI-powered ratings & recommendations.</p>
    <router-link to="/form">
      <button class="btn">Evaluate My Vehicle</button>
    </router-link>
  </div>
</template>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 70vh;
}
h1 {
  font-size: 28px;
  margin-bottom: 10px;
}
p {
  margin-bottom: 20px;
}
.btn {
  background: #1e3a8a;
  color: white;
  padding: 10px 20px;
  border-radius: 8px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}
.btn:hover {
  background: #1e40af;
}
</style>
