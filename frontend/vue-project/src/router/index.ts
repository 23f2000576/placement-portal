import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Signup from "../views/Signup.vue";
import Dashboard from "../views/Dashboard.vue";
import CompanyDashboard from "../views/CompanyDashboard.vue"
import AdminDashboard from "../views/AdminDashboard.vue"
import StudentDashboard from "../views/StudentDashboard.vue"
import StudentHistory from "../views/StudentHistory.vue"
import StudentProfile from "../views/StudentProfile.vue"

const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  { path: "/signup", component: Signup },
  { path: "/dashboard", component: Dashboard },
  { path: "/company-dashboard", component: CompanyDashboard },
  { path: "/admin-dashboard", component: AdminDashboard },
  { path: "/student-dashboard", component: StudentDashboard },
  { path: "/student-history", component: StudentHistory },
  {
    path: "/student-profile",
    component: StudentProfile
    }
];
  
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
