<template>

<div class="modal">

<div v-for="app in apps">

{{ app.branch }} - {{ app.cgpa }}

<button @click="review(app)">Review</button>

</div>

</div>

</template>

<script setup>

import { ref } from "vue"
import api from "../api/api"

const apps = ref([])

const load = async(id)=>{

const res = await api.get(`/company/drive/${id}/applications`)

apps.value = res.data

}

const review = (app)=>{

console.log(app)

}

</script>