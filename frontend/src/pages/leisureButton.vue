<template>
    <button v-on:click="getLeisureList">暇</button>
</template>

<script setup lang="ts">
const API_URL = 'http://127.0.0.1:8080'
const leisureList = []
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
        console.log(e)
        // navigateTo({
        //     path: '/proposalLeisure',
        //     query: {
        //         leisure: '暇つぶしのアプリ'
        //     }
        // })
        console.log(e.data.value)
    })
}
</script>