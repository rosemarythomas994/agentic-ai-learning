import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import VehicleForm from '../components/VehicleForm.vue'
import Result from '../components/Result.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/form', name: 'VehicleForm', component: VehicleForm },
  { 
    path: '/result', 
    name: 'Result', 
    component: Result, 
    props: route => ({ resultData: route.state?.resultData }) 
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
