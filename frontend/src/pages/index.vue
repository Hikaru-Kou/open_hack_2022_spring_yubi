<template>
    <button v-on:click="goToRegistrationPage">新規登録</button>
    <button v-on:click="goToLoginPage">ログイン</button>
</template>

<script setup lang="ts">
const goToRegistrationPage = () => {
    navigateTo('/register')
}

const goToLoginPage = () => {
    navigateTo('/login')
}
</script>