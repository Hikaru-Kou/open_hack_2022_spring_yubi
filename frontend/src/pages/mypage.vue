<template>
    <img src={{ userInfo.userIcon }}>
    <span>ユーザー名</span>
    <span>{{ userInfo.userName }}</span><br>
    <span>行った暇つぶし</span>
    <ul>
        <li v-for="leisure in userInfo.leisureList">{{ leisure }}</li>
        <li>あああ</li>
    </ul>
</template>

<script setup lang="ts">
const API_URL = ''
const userInfo = {
    userName: '',
    userIcon: '',
    leisureList: []
}
const postData = {
    userId: ''
}

const getUserInformation = () => {
    const userInfoController = useFetch(API_URL+ '/posts', {
        method: 'POST',
        body: postData,
        headers:{
        }
    })
    .then((e: any) => {
        console.log(e)
        // userInfo = e
    })
}

getUserInformation()
</script>