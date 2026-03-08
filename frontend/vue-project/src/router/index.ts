import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Signup from "../views/Signup.vue";
import Dashboard from "../views/Dashboard.vue";
import CompanyDashboard from "../views/CompanyDashboard.vue"
import AdminDashboard from "../views/AdminDashboard.vue"
const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  { path: "/signup", component: Signup },
  { path: "/dashboard", component: Dashboard },
  { path: "/company-dashboard", component: CompanyDashboard },
  { path: "/admin-dashboard", component: AdminDashboard },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
