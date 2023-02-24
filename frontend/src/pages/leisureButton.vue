<template>
    <div class="bg-slate-100 h-screen">
        <div class="absolute rounded-full bg-green-200/75 w-28 h-28 top-12 left-40"></div>
        <div class="absolute rounded-full bg-green-300/75 w-20 h-20 top-48 left-8"></div>
        <div class="absolute rounded-full bg-teal-200/75 w-32 h-32 top-48 left-60"></div>
        <div class="absolute rounded-full bg-cyan-200/75 w-32 h-32 top-80 left-40"></div>
        <div class="absolute rounded-full bg-teal-200/50 w-24 h-24 top-80 left-8"></div>
        <div class="absolute rounded-full bg-green-200/75 w-24 h-24 top-3/4 left-40"></div>
        <img v-on:click="getLeisureList" src="images/hima1.png" class="w-36 absolute top-20 left-10">
        <img v-on:click="getLeisureList" src="images/hima2.png" class="w-32 absolute top-32 left-56">
        <img v-on:click="getLeisureList" src="images/hima3.png" class="w-32 absolute top-60 left-16">
        <img v-on:click="getLeisureList" src="images/hima4.png" class="w-32 absolute top-96 left-8">
        <img v-on:click="getLeisureList" src="images/hima5.png" class="w-32 absolute top-80 left-52">
    </div>
</template>

<script setup lang="ts">
import { leisureStore } from '~~/store/leisure';

const API_URL = 'http://127.0.0.1:8080'
const leisure = leisureStore()
const postData = {
    userId: ''
}

const getLeisureList = () => {
    const leisureListController = useFetch(API_URL+ '/search', {
        method: 'GET',
        headers:{
        }
    })
    .then((e: any) => {
        console.log(e.data.value)
        leisure.trendTop = e.data.value.trendtop
        leisure.keywords = e.data.value.keywords
        leisure.googleurl = e.data.value.googleurl
        navigateTo({
            path: '/proposalLeisure',
        })
    })
}
</script>