import { createRouter, createWebHistory } from 'vue-router'
import BooksView from '../views/BooksView.vue'

const routes = [
    {
        path: '/',
        component: BooksView
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router