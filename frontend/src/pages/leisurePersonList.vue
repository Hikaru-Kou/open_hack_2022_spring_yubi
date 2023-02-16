<template>
    <p>暇な人</p>
    <ul>
        <li>ユーザー１</li>
        <li>ユーザー２</li>
    </ul>
    <
</template>

<script setup lang="ts">
const API_URL = ''
const availableUsers: string[] = []
const postData = {
    userId: ''
}

const getAvailableUsers = () => {
    const availableUserController = useFetch(API_URL+ '/posts', {
        method: 'POST',
        body: postData,
        headers:{
        }
    })
    .then((e: any) => {
        console.log(e)
        // availableUsers = e
    })
}

const goToAddFriendPage = () => {
    navigateTo('/addFriend')
}
getAvailableUsers()
</script>