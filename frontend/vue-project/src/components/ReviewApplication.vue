<template>

<div class="modal">

<h3>Student Details</h3>

<p>Branch {{ student.branch }}</p>
<p>CGPA {{ student.cgpa }}</p>

<a :href="student.resume">View Resume</a>

<select v-model="status">

<option>Shortlist</option>
<option>Waiting</option>
<option>Reject</option>

</select>

<button @click="update">Save</button>

</div>

</template>

<script setup>

import { ref } from "vue"
import api from "../api/api"

const status = ref("Waiting")

const update = async()=>{

await api.put(`/company/application/${id}/status`,{
status:status.value
})

}

</script>