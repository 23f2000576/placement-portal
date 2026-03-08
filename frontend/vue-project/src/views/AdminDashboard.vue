<script setup>

import { ref, onMounted } from "vue"
import api from "../api/api"
import AdminNavbar from "../components/AdminNavbar.vue"

const companies = ref([])
const students = ref([])
const drives = ref([])
const applications = ref([])

const loadDashboard = async () => {

const res = await api.get("/admin/dashboard")

companies.value = res.data.companies
students.value = res.data.students
drives.value = res.data.drives
applications.value = res.data.applications

}

const blacklistCompany = async(id)=>{
await api.put(`/admin/company/${id}/blacklist`)
loadDashboard()
}

const blacklistStudent = async(id)=>{
await api.put(`/admin/student/${id}/blacklist`)
loadDashboard()
}

const approveCompany = async(id)=>{
await api.put(`/admin/company/${id}/approve`)
loadDashboard()
}

onMounted(loadDashboard)

</script>



<template>

<AdminNavbar />

<div class="min-h-screen bg-[#FAF7F2] p-10">

<h1 class="text-3xl font-bold text-[#4B2E2B] mb-8">
Admin Dashboard
</h1>


<!-- REGISTERED COMPANIES -->

<div class="bg-white rounded-xl shadow p-6 border border-[#F3EDE4] mb-8">

<h2 class="text-lg font-semibold mb-4">
Registered Companies
</h2>

<div
v-for="c in companies"
:key="c.id"
class="flex justify-between items-center border p-3 rounded mb-2"
>

<div class="font-medium">
{{ c.name }}
</div>

<button
@click="blacklistCompany(c.id)"
class="bg-red-200 text-red-700 px-3 py-1 rounded"
>
Blacklist
</button>

</div>

</div>



<!-- REGISTERED STUDENTS -->

<div class="bg-white rounded-xl shadow p-6 border border-[#F3EDE4] mb-8">

<h2 class="text-lg font-semibold mb-4">
Registered Students
</h2>

<div
v-for="s in students"
:key="s.id"
class="flex justify-between items-center border p-3 rounded mb-2"
>

<div class="font-medium">
{{ s.name }}
</div>

<button
@click="blacklistStudent(s.id)"
class="bg-red-200 text-red-700 px-3 py-1 rounded"
>
Blacklist
</button>

</div>

</div>



<!-- COMPANY APPLICATIONS -->

<div class="bg-white rounded-xl shadow p-6 border border-[#F3EDE4] mb-8">

<h2 class="text-lg font-semibold mb-4">
Company Applications
</h2>

<div
v-for="c in companies"
:key="c.id"
class="flex justify-between items-center border p-3 rounded mb-2"
>

<div>
{{ c.name }}
</div>

<button
@click="approveCompany(c.id)"
class="bg-green-200 text-green-700 px-3 py-1 rounded"
>
Approve
</button>

</div>

</div>



<!-- ONGOING DRIVES -->

<div class="bg-white rounded-xl shadow p-6 border border-[#F3EDE4] mb-8">

<h2 class="text-lg font-semibold mb-4">
Ongoing Drives
</h2>

<table class="w-full">

<thead class="border-b">

<tr>
<th class="text-left p-2">Drive Name</th>
<th class="text-left p-2">Action</th>
</tr>

</thead>

<tbody>

<tr
v-for="d in drives"
:key="d.id"
class="border-b"
>

<td class="p-2">
{{ d.title }}
</td>

<td class="p-2">

<button
class="bg-blue-200 px-3 py-1 rounded"
>
View Details
</button>

</td>

</tr>

</tbody>

</table>

</div>



<!-- STUDENT APPLICATIONS -->

<div class="bg-white rounded-xl shadow p-6 border border-[#F3EDE4]">

<h2 class="text-lg font-semibold mb-4">
Student Applications
</h2>

<table class="w-full">

<thead class="border-b">

<tr>
<th class="p-2 text-left">Student</th>
<th class="p-2 text-left">Drive</th>
<th class="p-2 text-left">Action</th>
</tr>

</thead>

<tbody>

<tr
v-for="a in applications"
:key="a.id"
class="border-b"
>

<td class="p-2">
{{ a.student }}
</td>

<td class="p-2">
{{ a.drive }}
</td>

<td class="p-2">

<button
class="bg-blue-200 px-3 py-1 rounded"
>
View
</button>

</td>

</tr>

</tbody>

</table>

</div>

</div>

</template>