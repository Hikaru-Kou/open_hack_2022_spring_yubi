<template>
    <span>メールアドレス</span>
    <input type="text" v-model="email">
    <span>パスワード</span>
    <input type="text" v-model="password">
    <span>再パスワード</span>
    <input type="text" v-model="rePassword">
    <button v-on:click="registerUser">Register</button>
</template>

<script setup lang="ts">
const email = ref('')
const password = ref('')
const rePassword = ref('')
const API_URL = ''

const registerUser = () => {
    const postData = {
        email: email,
        password: password,
        rePassword: rePassword
    }
    const registerController = useFetch(API_URL+ '/posts', {
        method: 'POST',
        body: postData,
        headers:{
        }
    })
    .then((e: any) => {
        console.log(e)
        navigateTo('/leisureButton')
    })
}
</script>