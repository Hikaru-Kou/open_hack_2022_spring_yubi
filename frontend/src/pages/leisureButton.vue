<template>
    <button v-on:click="getLeisureList">暇</button>
</template>

<script setup lang="ts">
const API_URL = ''
const leisureList = []
const postData = {
    userId: ''
}

const getLeisureList = () => {
    const leisureListController = useFetch(API_URL+ '/posts', {
        method: 'POST',
        body: postData,
        headers:{
        }
    })
    .then((e: any) => {
        console.log(e)
        // leisureList = e
        navigateTo({
            path: '/proposalLeisure',
            query: {
                leisure: '暇つぶしのアプリ'
            }
        })
    })
}
</script>