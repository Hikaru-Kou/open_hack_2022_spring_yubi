<template>
    <span>メールアドレス</span>
    <input type="email" v-model="email">
    <span>パスワード</span>
    <input type="text" v-model="password">
    <span>再パスワード</span>
    <input type="text" v-model="rePassword">
    <button v-on:click="registerUser">Register</button>
    <p>{{ errorMessage }}</p>
</template>

<script setup lang="ts">
const email = ref('')
const password = ref('')
const rePassword = ref('')
const errorMessage = ref('')
const API_URL = ''

const registerUser = () => {
    if (!email.value) {
        errorMessage.value = 'メールアドレスを入力してください'
        return
    }
    if (!password.value) {
        errorMessage.value = 'パスワードを入力してください'
        return
    }
    if (!rePassword.value) {
        errorMessage.value = '再パスワードを入力してください'
        return
    }
    if (password.value !== rePassword.value) {
        errorMessage.value = 'パスワードが異なります'
        return
    }

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