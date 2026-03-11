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

const resumeFile = ref(null)
const exporting = ref(false)

/* ---------------- LOAD COMPANIES ---------------- */

const loadCompanies = async () => {

  try {

    const res = await api.get("/student/companies")

    companies.value = res.data

  } catch (err) {

    console.error("Error loading companies", err)

  }

}


/* ---------------- VIEW COMPANY DRIVES ---------------- */

const viewCompany = async (company) => {

  try {

    selectedCompany.value = company

    const res = await api.get(`/student/company/${company.id}/drives`)

    drives.value = res.data

    showCompanyPopup.value = true

  } catch (err) {

    console.error(err)

  }

}


/* ---------------- VIEW DRIVE ---------------- */

const viewDrive = (drive) => {

  selectedDrive.value = drive

  showDrivePopup.value = true

}


/* ---------------- HANDLE RESUME FILE ---------------- */

const handleResume = (e)=>{

  resumeFile.value = e.target.files[0]

}


/* ---------------- APPLY FOR DRIVE ---------------- */

const apply = async () => {

  try {

    const formData = new FormData()

    if(resumeFile.value){
      formData.append("resume", resumeFile.value)
    }

    await api.post(
      `/student/apply/${selectedDrive.value.id}`,
      formData
    )

    alert("Applied Successfully")

    showDrivePopup.value = false

  } catch (err) {

    console.error(err)

  }

}


/* ---------------- EXPORT APPLICATIONS ---------------- */

const exportApplications = async () => {

  try{

    exporting.value = true

    await api.post("/student/export")

    alert("Export started. CSV will be emailed to you.")

  }
  catch(err){

    console.error(err)

  }
  finally{

    exporting.value = false

  }

}

onMounted(loadCompanies)

</script>



<template>

<StudentNavbar/>

<div class="min-h-screen bg-[#FAF7F2] p-10">

<h1 class="text-3xl font-bold text-[#4B2E2B] mb-6">
Student Dashboard
</h1>


<!-- EXPORT BUTTON -->

<div class="mb-6">

<button
@click="exportApplications"
class="bg-[#4B2E2B] text-white px-4 py-2 rounded shadow"
>

{{ exporting ? "Exporting..." : "Export My Applications (CSV)" }}

</button>

</div>



<!-- ORGANIZATIONS -->

<div class="bg-white p-6 rounded-xl shadow border border-[#F3EDE4]">

<h2 class="text-lg font-semibold mb-4">
Organizations
</h2>

<div
v-for="c in companies"
:key="c.id"
class="flex justify-between border p-3 mb-2 rounded hover:bg-gray-50"
>

<span class="font-medium">
{{ c.name }}
</span>

<button
@click="viewCompany(c)"
class="bg-blue-200 px-3 py-1 rounded"
>
View Drives
</button>

</div>

</div>

</div>



<!-- COMPANY POPUP -->

<div v-if="showCompanyPopup" class="fixed inset-0 bg-black/40 flex justify-center items-center">

<div class="bg-white p-6 w-[500px] rounded shadow-lg">

<h2 class="text-xl font-bold mb-4">
{{ selectedCompany.name }}
</h2>

<div
v-for="d in drives"
:key="d.id"
class="flex justify-between border p-3 mb-2 rounded"
>

<span>{{ d.title }}</span>

<button
@click="viewDrive(d)"
class="bg-blue-200 px-3 py-1 rounded"
>
View Details
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

<div class="bg-white p-6 w-[450px] rounded shadow-lg">

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


<!-- RESUME UPLOAD -->

<div class="mt-3">

<input
type="file"
@change="handleResume"
class="border p-2 w-full"
/>

</div>


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