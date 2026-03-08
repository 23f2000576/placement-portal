<template>

<!-- NAVBAR -->
<Nav />

<div class="min-h-screen bg-[#FAF7F2] p-10">

<!-- HEADER -->

<div class="flex justify-between items-center mb-8">

<h1 class="text-3xl font-bold text-[#4B2E2B]">
Welcome Organization
</h1>

<div class="flex gap-4">

<button
@click="showCreateModal = true"
class="bg-green-100 text-green-700 px-4 py-2 rounded-md"
>
Create Drive
</button>

<button
@click="logout"
class="bg-red-100 text-red-600 px-4 py-2 rounded-md"
>
Logout
</button>

</div>

</div>


<!-- UPCOMING DRIVES -->

<div class="bg-white rounded-xl shadow p-6 border border-[#F3EDE4]">

<h2 class="text-lg font-semibold mb-4">
Upcoming Drives
</h2>

<table class="w-full text-sm">

<thead class="bg-gray-100">
<tr>
<th class="p-2 text-left">Sr No.</th>
<th class="p-2 text-left">Drive Name</th>
<th class="p-2 text-center">Actions</th>
</tr>
</thead>

<tbody>

<tr
v-for="(d,index) in upcomingDrives"
:key="d.id"
class="border-t"
>

<td class="p-2">{{ index + 1 }}</td>
<td class="p-2">{{ d.title }}</td>

<td class="p-2 text-center space-x-2">

<button
@click="viewDetails(d.id)"
class="bg-blue-100 text-blue-700 px-3 py-1 rounded"
>
view details
</button>

<button
@click="completeDrive(d.id)"
class="bg-green-100 text-green-700 px-3 py-1 rounded"
>
mark as complete
</button>

</td>

</tr>

</tbody>

</table>

</div>


<!-- CLOSED DRIVES -->

<div class="bg-white rounded-xl shadow p-6 border border-[#F3EDE4] mt-6">

<h2 class="text-lg font-semibold mb-4">
Closed Drives
</h2>

<table class="w-full text-sm">

<thead class="bg-gray-100">
<tr>
<th class="p-2 text-left">Sr No.</th>
<th class="p-2 text-left">Drive Name</th>
<th class="p-2 text-center">Actions</th>
</tr>
</thead>

<tbody>

<tr
v-for="(d,index) in closedDrives"
:key="d.id"
class="border-t"
>

<td class="p-2">{{ index + 1 }}</td>
<td class="p-2">{{ d.title }}</td>

<td class="p-2 text-center">

<button
@click="viewDetails(d.id)"
class="bg-blue-100 text-blue-700 px-3 py-1 rounded"
>
update
</button>

</td>

</tr>

</tbody>

</table>

</div>



<!-- CREATE DRIVE MODAL -->

<div v-if="showCreateModal" class="fixed inset-0 bg-black/40 flex items-center justify-center">

<div class="bg-white p-6 rounded w-[400px]">

<h2 class="text-xl font-bold mb-4">Create Drive</h2>

<input v-model="title" placeholder="Drive Name" class="border p-2 w-full mb-2"/>

<input v-model="location" placeholder="Location" class="border p-2 w-full mb-2"/>

<input v-model="salary" placeholder="Salary" class="border p-2 w-full mb-2"/>

<textarea v-model="description" placeholder="Job Description" class="border p-2 w-full mb-2"></textarea>

<input v-model="deadline" type="date" class="border p-2 w-full mb-4"/>

<div class="flex justify-end space-x-2">

<button @click="showCreateModal=false" class="px-3 py-1 bg-gray-200 rounded">
Cancel
</button>

<button @click="createDrive" class="px-3 py-1 bg-green-500 text-white rounded">
Save
</button>

</div>

</div>

</div>



<!-- APPLICATIONS POPUP -->

<div v-if="showApplicationsModal" class="fixed inset-0 bg-black/40 flex items-center justify-center">

<div class="bg-white p-6 rounded w-[600px]">

<h2 class="text-xl font-bold mb-2">
Update Applications for the Drive
</h2>

<p class="text-gray-500 mb-4">
Received Applications
</p>

<div class="max-h-[300px] overflow-y-auto">

<div
v-for="app in applications"
:key="app.application_id"
class="flex justify-between items-center border p-3 rounded mb-2"
>

<div>

<p class="font-semibold">
{{ app.student_name }}
</p>

<p class="text-sm text-gray-500">
{{ app.branch }} • CGPA {{ app.cgpa }}
</p>

</div>

<button
@click="reviewApplication(app)"
class="bg-blue-100 text-blue-700 px-3 py-1 rounded"
>
review application
</button>

</div>

</div>

<div class="flex justify-end mt-4">

<button
@click="showApplicationsModal=false"
class="px-3 py-1 bg-green-500 text-white rounded"
>
Save
</button>

</div>

</div>

</div>


</div>

</template>



<script setup>

import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"
import api from "../api/api"
import Nav from "../components/Nav.vue"

const router = useRouter()

const drives = ref([])
const upcomingDrives = ref([])
const closedDrives = ref([])

const showCreateModal = ref(false)
const showApplicationsModal = ref(false)

const applications = ref([])
const selectedDrive = ref(null)

const title = ref("")
const location = ref("")
const salary = ref("")
const description = ref("")
const deadline = ref("")


const logout = () => {

localStorage.removeItem("token")

router.push("/login")

}



const loadDrives = async () => {

try {

const res = await api.get("/company/drives")

drives.value = res.data

upcomingDrives.value = drives.value.filter(d => d.status !== "Closed")
closedDrives.value = drives.value.filter(d => d.status === "Closed")

}
catch(err){

console.log(err)

}

}



const createDrive = async () => {

await api.post("/company/create-drive",{

title:title.value,
location:location.value,
salary:salary.value,
description:description.value,
deadline:deadline.value

})

showCreateModal.value=false

loadDrives()

}



const completeDrive = async (id)=>{

await api.put(`/company/drive/${id}/complete`)

loadDrives()

}



const viewDetails = async (driveId)=>{

selectedDrive.value=driveId

const res = await api.get(`/company/drive/${driveId}/applications`)

applications.value=res.data

showApplicationsModal.value=true

}



const reviewApplication = (app)=>{

console.log("Review Student",app)

}



onMounted(()=>{

const token = localStorage.getItem("token")

if(!token){
router.push("/login")
return
}

loadDrives()

})

</script>