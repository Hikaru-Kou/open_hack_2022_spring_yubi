<template>
    <p>暇リスト</p>
    <ul>
        <li v-for="leisure in leisureList">{{ leisure }}</li>
        <li>暇つぶし２</li>
    </ul>
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
    })
}

getLeisureList()
</script>