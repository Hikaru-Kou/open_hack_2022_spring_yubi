<template>
    <!-- Left Content -->
    <div v-on:click="decideLeisure" class="absolute h-screen w-6/12 bg-orange-200 text-center">
        <button class="relative top-3/4 text-3xl">つぶす</button>
    </div>
    <!-- Right Content -->
    <div v-on:click="getLeisureList" class="absolute left-2/4 h-screen w-6/12 bg-zinc-300 text-center">
        <button class="relative top-3/4 text-3xl">つぶさない</button>
    </div>
    <!-- center content -->
    <div class="absolute top-10 bg-white drop-shadow-md rounded-md p-2 center">
        <p class="">{{ leisure.trendTop }} でつぶす？</p>
    </div>
</template>

<style>
.center {
    position: absolute;
    top: 15%;
    left: 50%;
    transform: translateY(-50%) translateX(-50%);
    -webkit-transform: translateY(-50%) translateX(-50%);
}
</style>

<script setup lang="ts">
import { leisureStore } from '~~/store/leisure';

const leisure = leisureStore()
const API_URL = 'http://127.0.0.1:8080'
const postData = {
    userId: ''
}

const decideLeisure = () => {
    const decideLeisure = useFetch(API_URL+ '/posts', {
        method: 'POST',
        body: postData,
        headers:{
        }
    })
    .then((e: any) => {
        console.log(e)
        navigateTo({
            path: '/proposalLeisure',
        })
    })
}

const getLeisureList = () => {
    const getLeisureListController = useFetch(API_URL+ '/search', {
        method: 'GET',
        headers:{
        }
    })
    .then((e: any) => {
        leisure.trendTop = e.data.value.trendtop
        leisure.keywords = e.data.value.keywords
        leisure.googleurl = e.data.value.googleurl
        navigateTo({
            path: '/proposalLeisure',
        })
    })
}
</script>