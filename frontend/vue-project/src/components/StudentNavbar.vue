<script setup>
import { useRouter } from "vue-router"

const router = useRouter()

const logout = () => {
  localStorage.removeItem("token")
  router.push("/login")
}
</script>

<template>
<nav class="flex justify-between items-center bg-[#4B2E2B] text-white px-8 py-4">

<div class="text-xl font-bold">
Placement Portal
</div>

<div class="flex gap-6">

<button @click="$router.push('/student-dashboard')">
Dashboard
</button>

<button @click="$router.push('/student-history')">
History
</button>

<button @click="$router.push('/student-profile')">
Edit Profile
</button>

<button
@click="logout"
class="bg-red-200 text-red-700 px-3 py-1 rounded"
>
Logout
</button>

</div>

</nav>
</template>