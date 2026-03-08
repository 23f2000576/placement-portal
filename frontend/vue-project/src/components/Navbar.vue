<template>
  <nav class="w-full bg-[#4B2E2B] text-white shadow-md">
    <div class="w-full px-10 py-4 flex justify-between items-center">
      <h1 class="text-2xl font-bold">Placement Portal</h1>

      <div class="space-x-4">
        <RouterLink to="/" class="hover:text-[#EADBC8]">Home</RouterLink>
        <RouterLink
          to="/login"
          class="bg-[#C8A27A] text-[#4B2E2B] px-4 py-2 rounded-md font-medium hover:bg-[#d6b593]"
        >
          Login
        </RouterLink>
        <RouterLink
          to="/signup"
          class="border border-[#EADBC8] px-4 py-2 rounded-md hover:bg-[#EADBC8] hover:text-[#4B2E2B]"
        >
          Signup
        </RouterLink>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>
