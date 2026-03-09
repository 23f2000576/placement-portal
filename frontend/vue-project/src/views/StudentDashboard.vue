<script setup>

import { ref, onMounted } from "vue"
import api from "../api/api"
import StudentNavbar from "../components/StudentNavbar.vue"

const companies = ref([])
const drives = ref([])

const selectedCompany = ref(null)
const selectedDrive = ref(null)

const showCompanyPopup = ref(false)
const showDrivePopup = ref(false)


/* ---------------- LOAD COMPANIES ---------------- */

const loadCompanies = async () => {

  try {

    console.log("Calling API: /student/companies")

    const res = await api.get("/student/companies")

    console.log("Companies API response:", res.data)

    companies.value = res.data

  } catch (err) {

    console.error("Error loading companies", err)

  }

}


/* ---------------- VIEW COMPANY DRIVES ---------------- */

const viewCompany = async (company) => {

  try {

    selectedCompany.value = company

    console.log("Calling API:", `/student/company/${company.id}/drives`)

    const res = await api.get(`/student/company/${company.id}/drives`)

    console.log("Drives response:", res.data)

    drives.value = res.data

    showCompanyPopup.value = true

  } catch (err) {

    console.error("Error loading drives", err)

  }

}


/* ---------------- VIEW DRIVE ---------------- */

const viewDrive = (drive) => {

  selectedDrive.value = drive

  showDrivePopup.value = true

}


/* ---------------- APPLY ---------------- */

const apply = async () => {

  try {

    await api.post(`/student/apply/${selectedDrive.value.id}`)

    alert("Applied Successfully")

    showDrivePopup.value = false

  } catch (err) {

    console.error(err)

  }

}


onMounted(loadCompanies)

</script>



<template>

<StudentNavbar/>

<div class="min-h-screen bg-[#FAF7F2] p-10">

<h1 class="text-3xl font-bold text-[#4B2E2B] mb-6">
Students Dashboard
</h1>


<!-- ORGANIZATIONS -->

<div class="bg-white p-6 rounded-xl shadow border border-[#F3EDE4]">

<h2 class="text-lg font-semibold mb-4">
Organizations
</h2>

<div
v-for="c in companies"
:key="c.id"
class="flex justify-between border p-3 mb-2 rounded"
>

<span class="font-medium">
{{ c.name }}
</span>

<button
@click="viewCompany(c)"
class="bg-blue-200 px-3 py-1 rounded"
>
view details
</button>

</div>

</div>

</div>



<!-- COMPANY POPUP -->

<div v-if="showCompanyPopup" class="fixed inset-0 bg-black/40 flex justify-center items-center">

<div class="bg-white p-6 w-[500px] rounded">

<h2 class="text-xl font-bold mb-4">
{{ selectedCompany.name }}
</h2>

<div
v-for="d in drives"
:key="d.id"
class="flex justify-between border p-3 mb-2"
>

<span>{{ d.title }}</span>

<button
@click="viewDrive(d)"
class="bg-blue-200 px-3 py-1 rounded"
>
view details
</button>

</div>

<button
@click="showCompanyPopup=false"
class="mt-4 bg-gray-200 px-3 py-1 rounded"
>
Close
</button>

</div>

</div>



<!-- DRIVE DETAILS POPUP -->

<div v-if="showDrivePopup" class="fixed inset-0 bg-black/40 flex justify-center items-center">

<div class="bg-white p-6 w-[450px] rounded">

<h2 class="text-xl font-bold mb-3">
{{ selectedDrive.title }}
</h2>

<p class="mb-2">
{{ selectedDrive.description }}
</p>

<p>
Salary: {{ selectedDrive.salary }}
</p>

<p>
Location: {{ selectedDrive.location }}
</p>

<div class="flex gap-3 mt-4">

<button
@click="apply"
class="bg-green-500 text-white px-3 py-1 rounded"
>
Apply
</button>

<button
@click="showDrivePopup=false"
class="bg-gray-200 px-3 py-1 rounded"
>
Go Back
</button>

</div>

</div>

</div>

</template>