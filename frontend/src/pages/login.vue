<template>
    <span>メールアドレス</span>
    <input type="email" v-model="email">
    <span>パスワード</span>
    <input type="text" v-model="password">
    <button v-on:click="loginUser">Login</button>
    <p>{{ errorMessage }}</p>
</template>

<script setup lang="ts">
const email = ref('')
const password = ref('')
const errorMessage = ref('')
const API_URL = ''

const loginUser = () => {
    if (!email.value) {
        errorMessage.value = 'メールアドレスを入力してください'
        return
    }
    if (!password.value) {
        errorMessage.value = 'パスワードを入力してください'
        return
    }

    const postData = {
        email: email,
        password: password
    }
    const loginController = useFetch(API_URL+ '/posts', {
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