<script setup>
import { useRouter } from "vue-router"

const router = useRouter()

const logout = () => {
  localStorage.removeItem("token")
  router.push("/login")
}
</script>

<template>

<nav class="flex justify-between items-center px-8 py-4 bg-[#4B2E2B] text-white">

<div class="text-xl font-bold">
Placement Portal
</div>

<div class="flex gap-4">

<button
@click="$router.push('/company-dashboard')"
class="hover:underline"
>
Dashboard
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