import { defineStore } from 'pinia'

export const leisureStore = defineStore('leisure', () => {
    const leisureList = ref({})
    const trendTop = ref('')
    const trendUrl = ref('')
  
    return { leisureList, trendTop, trendUrl }
  })
  