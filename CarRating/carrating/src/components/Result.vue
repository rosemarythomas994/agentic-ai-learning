<template>
  <div class="p-6 max-w-3xl mx-auto">
    <h1 class="text-2xl font-bold mb-6">Vehicle Evaluation Result</h1>

    <div v-if="resultData && resultData.success" class="bg-white shadow-md rounded p-6 space-y-4">
     

      <div>
        <p><strong>Rating:</strong> {{ resultData.rating }}</p>
        <p><strong>Condition:</strong> {{ resultData.condition }}</p>
        <p><strong>Confidence:</strong> {{ (resultData.confidence * 100).toFixed(1) }}%</p>
        <p><strong>Message:</strong> {{ resultData.message }}</p>
      </div>

      <div>
        <h2 class="text-xl font-semibold mb-2">Recommended Companies</h2>
        <ul class="list-disc list-inside">
          <li v-for="company in resultData.recommended_companies" :key="company.name">
            <strong>{{ company.name }}</strong> ({{ company.type }}) -
            <a :href="company.website" target="_blank" rel="noopener noreferrer" class="text-blue-600 underline">
              Visit Website
            </a>
          </li>
        </ul>
      </div>
    </div>

    <div v-else class="text-red-600 font-semibold">
      No result data found. Please go back and evaluate a vehicle.
    </div>

    <div class="mt-6">
      <button
        class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
        @click="$router.push('/form')"
      >
        Go Back
      </button>
    </div>
  </div>
</template>

<script>
import { useRoute } from 'vue-router';

export default {
  name: "Result",
  setup() {
    const route = useRoute();
    const rawResult = route.query.result || null;
    let parsedResult = null;

    try {
      if (rawResult) {
        parsedResult = JSON.parse(rawResult);
        console.log("Parsed result from query param:", parsedResult);
      }
    } catch (error) {
      console.error("Failed to parse result query param:", error);
    }

    return { resultData: parsedResult };
  },
};
</script>

<style scoped>
/* Optional: Your existing styles */
</style>
