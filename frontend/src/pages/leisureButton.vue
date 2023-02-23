<template>
    <button v-on:click="getLeisureList">暇</button>
    <p>{{ trendTop }}</p>
    <p>{{ trendUrl }}</p>
    <p v-for="(searchNum, leisure) in leisureList"> {{ leisure }}</p>
</template>

<script setup lang="ts">
const API_URL = 'http://127.0.0.1:8080'
const leisureList = ref({})
const trendTop = ref('')
const trendUrl = ref('')
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
        trendTop.value = e.data.value.trendtop
        leisureList.value = e.data.value.keywords
        trendUrl.value = e.data.value.googleurl
    })
}
</script>