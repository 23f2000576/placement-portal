<script setup>

import { ref, onMounted } from "vue"
import api from "../api/api"
import StudentNavbar from "../components/StudentNavbar.vue"

const profile = ref({})

const resume = ref(null)

const loadProfile = async () => {

  const res = await api.get("/student/profile")

  profile.value = res.data
}

const handleFile = (e)=>{

  resume.value = e.target.files[0]

}

const updateProfile = async () => {

  const formData = new FormData()

  formData.append("roll_number", profile.value.roll_number)
  formData.append("branch", profile.value.branch)
  formData.append("year", profile.value.year)
  formData.append("cgpa", profile.value.cgpa)
  formData.append("phone", profile.value.phone)
  formData.append("skills", profile.value.skills)

  if(resume.value){
    formData.append("resume", resume.value)
  }

  await api.put("/student/profile", formData)

  alert("Profile Updated")
}

onMounted(loadProfile)

</script>

<template>

<StudentNavbar/>

<div class="min-h-screen bg-[#FAF7F2] p-10">

<h1 class="text-2xl font-bold text-[#4B2E2B] mb-6">
Edit Profile
</h1>

<div class="bg-white p-6 rounded-xl border border-[#F3EDE4] w-[500px]">

<input v-model="profile.roll_number" placeholder="Roll Number" class="border p-2 w-full mb-3"/>

<input v-model="profile.branch" placeholder="Branch" class="border p-2 w-full mb-3"/>

<input v-model="profile.year" placeholder="Year" class="border p-2 w-full mb-3"/>

<input v-model="profile.cgpa" placeholder="CGPA" class="border p-2 w-full mb-3"/>

<input v-model="profile.phone" placeholder="Phone" class="border p-2 w-full mb-3"/>

<textarea v-model="profile.skills" placeholder="Skills" class="border p-2 w-full mb-3"></textarea>

<!-- Resume Upload -->

<div class="mb-4">

<label class="font-semibold">
Upload Resume
</label>

<input
type="file"
@change="handleFile"
class="border p-2 w-full mt-2"
/>

<div v-if="profile.resume" class="mt-2">

<a
:href="'http://127.0.0.1:5000/'+profile.resume"
target="_blank"
class="text-blue-600"
>
View Current Resume
</a>

</div>

</div>

<button
@click="updateProfile"
class="bg-green-500 text-white px-4 py-2 rounded"
>
Save
</button>

</div>

</div>

</template>