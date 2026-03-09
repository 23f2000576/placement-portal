<script setup>

import { ref,onMounted } from "vue"
import api from "../api/api"
import StudentNavbar from "../components/StudentNavbar.vue"

const history = ref([])

const loadHistory = async()=>{

const res = await api.get("/student/history")

history.value = res.data

}

onMounted(loadHistory)

</script>


<template>

<StudentNavbar/>

<div class="min-h-screen bg-[#FAF7F2] p-10">

<h1 class="text-2xl font-bold mb-6">
Student Application History
</h1>

<table class="w-full bg-white shadow rounded">

<tr class="border-b">
<th class="p-2">Drive</th>
<th class="p-2">Result</th>
<th class="p-2">Date</th>
</tr>

<tr
v-for="h in history"
:key="h.id"
>

<td class="p-2">{{ h.drive }}</td>
<td class="p-2">{{ h.status }}</td>
<td class="p-2">{{ h.date }}</td>

</tr>

</table>

</div>

</template>