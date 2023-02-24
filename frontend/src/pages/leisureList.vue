<template>
    <p>暇リスト</p>
    <p>{{ leisure.trendTop }}</p>
    <p>{{ leisure.trendUrl }}</p>
    <ul>
        <li v-for="keyword in leisure.keywords ">{{ keyword }}</li>
    </ul>
</template>

<script setup lang="ts">
import { leisureStore } from '~~/store/leisure';

const leisure = leisureStore()

const API_URL = 'http://127.0.0.1:8080'
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
    })
}
</script>