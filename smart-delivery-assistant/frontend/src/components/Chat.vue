<template>
  <div class="chat">
    <h2>Smart Delivery Assistant</h2>
    <div v-for="(m, idx) in messages" :key="idx" class="msg">{{ m }}</div>
    <input v-model="query" @keyup.enter="send" placeholder="Ask about order or driver..." />
    <button @click="send">Send</button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const query = ref("");
const messages = ref([]);

const send = async () => {
  if (!query.value) return;
  messages.value.push("You: " + query.value);
  try {
    const res = await axios.post("http://localhost:8000/ask", { query: query.value });
    messages.value.push("AI: " + res.data.answer);
  } catch (err) {
    messages.value.push("Error: " + err.message);
  }
  query.value = "";
};
</script>

<style scoped>
.chat {
  max-width: 600px;
  margin: auto;
}
.msg {
  padding: 10px;
  background: #eaeaea;
  margin: 5px 0;
  border-radius: 5px;
}
</style>
