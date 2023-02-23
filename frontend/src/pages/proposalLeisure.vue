<template>
    <p>{{ route.query.leisure }}</p>
    <button v-on:click="decideLeisure">つぶす</button>
    <button v-on:click="getLeisureList">つぶさない</button>
</template>

<script setup lang="ts">
const API_URL = ''
const route = useRoute()
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
        // leisureList = e
        navigateTo({
            path: '/proposalLeisure',
            query: {
                leisure: '暇つぶしのアプリ'
            }
        })
    })
}

const getLeisureList = () => {
    const getLeisureListController = useFetch(API_URL+ '/posts', {
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