<script setup>

import { ref, onMounted } from "vue"
import api from "../api/api"
import AdminNavbar from "../components/AdminNavbar.vue"

const companies = ref([])
const students = ref([])
const drives = ref([])
const applications = ref([])

const searchQuery = ref("")
const searchResults = ref([])

const showDriveModal = ref(false)
const showAppModal = ref(false)

const selectedDrive = ref({})
const selectedApp = ref({})

const loading = ref(false)

const loadDashboard = async () => {

loading.value = true

const res = await api.get("/admin/dashboard")

companies.value = res.data.companies
students.value = res.data.students
drives.value = res.data.drives
applications.value = res.data.applications

loading.value = false
}

const searchUsers = async () => {

if(!searchQuery.value){
searchResults.value=[]
return
}

const res = await api.get(`/admin/search?q=${searchQuery.value}`)
searchResults.value = res.data
}

const blacklistCompany = async(id)=>{
await api.put(`/admin/user/${id}/blacklist`)
loadDashboard()
}

const blacklistStudent = async(id)=>{
await api.put(`/admin/user/${id}/blacklist`)
loadDashboard()
}

const approveCompany = async(id)=>{
await api.put(`/admin/company/${id}/approve`)
loadDashboard()
}

const rejectCompany = async(id)=>{
await api.put(`/admin/company/${id}/reject`)
loadDashboard()
}

const generateReport = async()=>{
await api.post("/admin/generate-report")
alert("Monthly report sent to admin email")
}

const viewDrive = async(id)=>{

const res = await api.get(`/admin/drive/${id}`)

selectedDrive.value = res.data

showDriveModal.value = true
}

const viewApplication = async(id)=>{

const res = await api.get(`/admin/application/${id}`)

selectedApp.value = res.data

showAppModal.value = true
}

onMounted(loadDashboard)

</script>


<template>

<AdminNavbar/>

<div class="min-h-screen bg-[#FAF7F2] p-10">

<h1 class="text-3xl font-bold text-[#4B2E2B] mb-6 flex items-center gap-4">
Admin Dashboard

<button
@click="generateReport"
class="bg-green-100 text-green-700 px-4 py-2 rounded"
>
Generate Monthly Report
</button>

</h1>

<!-- STATISTICS -->

<div class="grid grid-cols-4 gap-6 mb-8">

<div class="bg-white p-4 rounded shadow">
<p class="text-sm text-gray-500">Companies</p>
<p class="text-2xl font-bold">{{companies.length}}</p>
</div>

<div class="bg-white p-4 rounded shadow">
<p class="text-sm text-gray-500">Students</p>
<p class="text-2xl font-bold">{{students.length}}</p>
</div>

<div class="bg-white p-4 rounded shadow">
<p class="text-sm text-gray-500">Drives</p>
<p class="text-2xl font-bold">{{drives.length}}</p>
</div>

<div class="bg-white p-4 rounded shadow">
<p class="text-sm text-gray-500">Applications</p>
<p class="text-2xl font-bold">{{applications.length}}</p>
</div>

</div>


<!-- SEARCH -->

<div class="bg-white border border-[#F3EDE4] rounded-xl p-4 mb-8 shadow">

<div class="flex gap-3">

<input
v-model="searchQuery"
@input="searchUsers"
placeholder="Search student or company"
class="border p-2 rounded w-full"
/>

<button
@click="searchUsers"
class="bg-blue-100 text-blue-700 px-4 rounded"
>
Search
</button>

</div>

<div v-if="searchResults.length" class="mt-4 space-y-2">

<div
v-for="u in searchResults"
:key="u.user_id"
class="border p-3 rounded flex justify-between"
>

<div>

<p class="font-semibold">{{u.name}}</p>

<p class="text-sm text-gray-500">
{{u.email}} • {{u.role}}
</p>

</div>

</div>

</div>

</div>


<!-- COMPANIES + STUDENTS -->

<div class="grid grid-cols-2 gap-8">


<!-- COMPANIES -->

<div class="bg-white rounded-xl shadow border border-[#F3EDE4] p-6">

<h2 class="font-semibold mb-4">
Registered Companies
</h2>

<div class="space-y-2 max-h-[250px] overflow-y-auto">

<div
v-for="c in companies"
:key="c.id"
class="border p-3 rounded flex justify-between items-center"
>

<div>

<p class="font-semibold">{{c.name}}</p>

<p class="text-xs text-gray-500">
Status: {{c.approval_status}}
</p>

</div>

<div class="flex gap-2">

<button
@click="approveCompany(c.id)"
class="bg-green-100 text-green-700 px-2 py-1 rounded"
>
Approve
</button>

<button
@click="rejectCompany(c.id)"
class="bg-yellow-100 text-yellow-700 px-2 py-1 rounded"
>
Reject
</button>

<button
@click="blacklistCompany(c.id)"
class="bg-red-100 text-red-600 px-2 py-1 rounded"
>
Blacklist
</button>

</div>

</div>

</div>

</div>


<!-- STUDENTS -->

<div class="bg-white rounded-xl shadow border border-[#F3EDE4] p-6">

<h2 class="font-semibold mb-4">
Registered Students
</h2>

<div class="space-y-2 max-h-[250px] overflow-y-auto">

<div
v-for="s in students"
:key="s.id"
class="flex justify-between border p-3 rounded"
>

{{s.name}}

<button
@click="blacklistStudent(s.id)"
class="bg-red-100 text-red-600 px-3 py-1 rounded"
>
Blacklist
</button>

</div>

</div>

</div>

</div>


<!-- DRIVES -->

<div class="bg-white rounded-xl shadow border border-[#F3EDE4] p-6 mt-8">

<h2 class="font-semibold mb-4">
Ongoing Drives
</h2>

<table class="w-full">

<thead class="border-b">

<tr>
<th class="p-2 text-left">Drive</th>
<th>Status</th>
<th>Action</th>
</tr>

</thead>

<tbody>

<tr
v-for="d in drives"
:key="d.id"
class="border-b"
>

<td class="p-2">{{d.title}}</td>

<td>{{d.status}}</td>

<td>

<button
@click="viewDrive(d.id)"
class="bg-blue-100 px-3 py-1 rounded"
>
View Details
</button>

</td>

</tr>

</tbody>

</table>

</div>


<!-- APPLICATIONS -->

<div class="bg-white rounded-xl shadow border border-[#F3EDE4] p-6 mt-8">

<h2 class="font-semibold mb-4">
Student Applications
</h2>

<table class="w-full">

<thead class="border-b">

<tr>
<th class="p-2 text-left">Student</th>
<th>Drive</th>
<th>Status</th>
<th>Action</th>
</tr>

</thead>

<tbody>

<tr
v-for="a in applications"
:key="a.id"
class="border-b"
>

<td class="p-2">{{a.student}}</td>

<td>{{a.drive}}</td>

<td>{{a.status}}</td>

<td>

<button
@click="viewApplication(a.id)"
class="bg-blue-100 px-3 py-1 rounded"
>
View
</button>

</td>

</tr>

</tbody>

</table>

</div>


<!-- DRIVE MODAL -->

<div v-if="showDriveModal" class="fixed inset-0 bg-black/40 flex items-center justify-center">

<div class="bg-white p-6 rounded-xl w-[500px] shadow">

<h2 class="text-xl font-bold mb-3">
{{selectedDrive.title}}
</h2>

<p class="mb-3">{{selectedDrive.description}}</p>

<p><b>Salary:</b> {{selectedDrive.salary}}</p>
<p><b>Location:</b> {{selectedDrive.location}}</p>

<button
@click="showDriveModal=false"
class="mt-4 bg-gray-200 px-3 py-1 rounded"
>
Close
</button>

</div>

</div>


<!-- APPLICATION MODAL -->

<div v-if="showAppModal" class="fixed inset-0 bg-black/40 flex items-center justify-center">

<div class="bg-white p-6 rounded-xl w-[500px] shadow">

<h2 class="text-xl font-bold mb-3">
Student Application
</h2>

<p><b>Name:</b> {{selectedApp.student_name}}</p>
<p><b>Department:</b> {{selectedApp.branch}}</p>
<p><b>Drive:</b> {{selectedApp.drive}}</p>

<a
:href="'http://127.0.0.1:5000/'+selectedApp.resume"
download
class="bg-blue-100 text-blue-700 px-3 py-1 rounded inline-block mt-4"
>
Download Resume
</a>

<br>

<button
@click="showAppModal=false"
class="mt-4 bg-gray-200 px-3 py-1 rounded"
>
Back
</button>

</div>

</div>

</div>

</template>