<template>
    <div class="bg-slate-100 h-screen">
        <button v-on:click="getLeisureList">暇</button>
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