<template>
  <div class="form-page">
    <div class="form-card">
      <h2 class="form-title">Enter Vehicle Details</h2>
      <form @submit.prevent="evaluateVehicle" @reset.prevent="resetForm">
        <div class="form-group">
          <label>Brand</label>
          <input v-model="vehicle.brand" placeholder="e.g. Toyota" required />
        </div>
        <div class="form-group">
          <label>Model</label>
          <input v-model="vehicle.model" placeholder="e.g. Corolla" required />
        </div>
        <div class="form-group">
          <label>Year</label>
          <input type="number" v-model.number="vehicle.year" required />
        </div>
        <div class="form-group">
          <label>Mileage (km)</label>
          <input type="number" v-model.number="vehicle.mileage" required />
        </div>
        <div class="form-group">
          <label>Fuel Type</label>
          <select v-model="vehicle.fuel">
            <option>Petrol</option>
            <option>Diesel</option>
            <option>Electric</option>
            <option>Hybrid</option>
          </select>
        </div>
        <div class="form-group">
          <label>Transmission</label>
          <select v-model="vehicle.transmission">
            <option>Manual</option>
            <option>Automatic</option>
            <option>CVT</option>
          </select>
        </div>
        <div class="form-group">
          <label>Exterior Condition</label>
          <div class="range-wrapper">
            <input type="range" v-model.number="vehicle.exterior" min="1" max="5" />
            <span>{{ vehicle.exterior }}/5</span>
          </div>
        </div>
        <div class="form-group">
          <label>Interior Condition</label>
          <div class="range-wrapper">
            <input type="range" v-model.number="vehicle.interior" min="1" max="5" />
            <span>{{ vehicle.interior }}/5</span>
          </div>
        </div>
        <div class="form-group">
          <label>Accident History</label>
          <select v-model="vehicle.accident">
            <option>No</option>
            <option>Yes</option>
          </select>
        </div>
        <div class="form-group">
          <label>Upload Images</label>
          <input type="file" @change="handleFileUpload" />
        </div>
        <div class="button-row">
          <button type="submit" class="btn btn-primary">Evaluate</button>
          <button type="reset" class="btn btn-secondary">Cancel</button>
        </div>
      </form>
      <div style="margin-top:1rem;">
        <h3>Current Form Data:</h3>
        <pre>{{ JSON.stringify(vehicle, null, 2) }}</pre>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, watch } from 'vue';
import { useRouter } from 'vue-router';
import api from "../api";

const router = useRouter();

const vehicle = reactive({
  brand: '',
  model: '',
  year: null,
  mileage: null,
  fuel: 'Petrol',
  transmission: 'Manual',
  exterior: 3,
  interior: 3,
  accident: 'No',
  image: null
});

// Log live changes (optional)
watch(vehicle, (newVal) => {
  console.log("Vehicle form data changed:", newVal);
}, { deep: true });

function handleFileUpload(event) {
  vehicle.image = event.target.files[0];
  console.log("File selected:", vehicle.image);
}

async function evaluateVehicle() {
  try {
    if (!vehicle.year || vehicle.year <= 0) {
      alert("Please enter a valid Year");
      return;
    }
    if (!vehicle.mileage || vehicle.mileage < 0) {
      alert("Please enter valid Mileage");
      return;
    }
    const payload = {
      brand: vehicle.brand,
      model: vehicle.model,
      year: vehicle.year,
      mileage: vehicle.mileage,
      fuel: vehicle.fuel,
      transmission: vehicle.transmission,
      exterior: vehicle.exterior,
      interior: vehicle.interior,
      accident: vehicle.accident
    };
    console.log("Sending payload:", payload);
    const response = await api.post("/evaluate", payload);
    console.log("Response from backend:", response.data);

    router.push({
      name: "Result",
      query: { result: JSON.stringify(response.data) }
    });
  } catch (err) {
    console.error("Evaluation failed:", err);
    alert("Something went wrong while evaluating vehicle.");
  }
}

function resetForm() {
  Object.assign(vehicle, {
    brand: '',
    model: '',
    year: null,
    mileage: null,
    fuel: 'Petrol',
    transmission: 'Manual',
    exterior: 3,
    interior: 3,
    accident: 'No',
    image: null
  });
}
</script>

<style scoped>
/* Your existing CSS here */
</style>
