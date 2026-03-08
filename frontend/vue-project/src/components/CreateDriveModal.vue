<template>

<div class="fixed inset-0 bg-black/40 flex items-center justify-center">

<div class="bg-white p-6 w-96 rounded">

<h2>Create Drive</h2>

<input v-model="title" placeholder="Drive Name"/>

<input v-model="job_title" placeholder="Job Title"/>

<textarea v-model="desc" placeholder="Job Description"></textarea>

<input v-model="deadline" type="date"/>

<button @click="create">Save</button>

</div>

</div>

</template>

<script setup>

import { ref } from "vue"
import api from "../api/api"

const title = ref("")
const job_title = ref("")
const desc = ref("")
const deadline = ref("")

const create = async()=>{

await api.post("/company/create-drive",{

title:title.value,
description:desc.value,
deadline:deadline.value

})

}

</script>