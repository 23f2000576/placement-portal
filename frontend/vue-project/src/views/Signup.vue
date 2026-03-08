<template>
  <div class="min-h-screen flex items-center justify-center bg-[#FAF7F2] relative overflow-hidden">

    <!-- Background Effects -->
    <div class="absolute w-96 h-96 bg-[#C8A27A] opacity-20 rounded-full blur-3xl top-10 right-10"></div>
    <div class="absolute w-96 h-96 bg-[#8B6F5A] opacity-20 rounded-full blur-3xl bottom-10 left-10"></div>

    <!-- Card -->
    <div class="bg-white shadow-xl rounded-xl p-10 w-full max-w-md z-10 border border-[#F3EDE4]">

      <!-- Logo -->
      <div class="text-center mb-6">
        <img
          src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
          class="w-16 mx-auto mb-2"
        />
        <h2 class="text-2xl font-bold text-[#4B2E2B]">Create Account</h2>
        <p class="text-sm text-[#8B6F5A]">Join the Placement Portal</p>
      </div>

      <!-- Form -->
      <form @submit.prevent="signup">
        <input
          v-model="name"
          placeholder="Full Name"
          class="w-full mb-3 p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#C8A27A]"
        />

        <input
          v-model="email"
          type="email"
          placeholder="Email"
          class="w-full mb-3 p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#C8A27A]"
        />

        <input
          v-model="password"
          type="password"
          placeholder="Password"
          class="w-full mb-4 p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#C8A27A]"
        />

        <!-- Role -->
        <select
          v-model="role"
          class="w-full mb-6 p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#C8A27A]"
        >
          <option value="">Select Role</option>
          <option value="STUDENT">Student</option>
          <option value="COMPANY">Company</option>
        </select>

        <button
          class="w-full bg-[#4B2E2B] text-white py-3 rounded-lg hover:bg-[#6B4F4B] transition"
        >
          Signup
        </button>
      </form>

      <p class="text-center text-sm mt-4 text-[#6B4F4B]">
        Already have an account?
        <RouterLink to="/login" class="text-[#4B2E2B] font-semibold">
          Login
        </RouterLink>
      </p>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { RouterLink, useRouter } from "vue-router";
import api from "../api/api";   // IMPORTANT

const router = useRouter();

const name = ref("");
const email = ref("");
const password = ref("");
const role = ref("");

const signup = async () => {
  try {

    const res = await api.post("/auth/signup", {
      name: name.value,
      email: email.value,
      password: password.value,
      role: role.value
    });

    console.log("Signup response:", res.data);

    alert("Signup successful");

    router.push("/login");

  } catch (err) {
    console.error(err);
    alert(err.response?.data?.error || "Signup failed");
  }
};
</script>