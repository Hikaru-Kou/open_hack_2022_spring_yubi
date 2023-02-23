<template>
    <button v-on:click="goToRegistrationPage">新規登録</button>
    <button v-on:click="goToLoginPage">ログイン</button>
</template>

<script setup lang="ts">
const goToRegistrationPage = () => {
    test()
    navigateTo('/register')
}

const goToLoginPage = () => {
    navigateTo('/login')
}

const API_URL = 'http://127.0.0.1:8080'
const test = async () => {
    await useFetch(API_URL+ '/test', {
        method: 'GET',
        // body: postData,
        headers:{
        }
    })
    .then((e: any) => {
        console.log(e.data.value)
    })
}
</script>