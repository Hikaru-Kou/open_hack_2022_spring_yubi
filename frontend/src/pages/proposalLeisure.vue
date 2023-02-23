<template>
    <p>{{ leisure.trendTop }}</p>
    <button v-on:click="decideLeisure">つぶす</button>
    <button v-on:click="getLeisureList">つぶさない</button>
</template>

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