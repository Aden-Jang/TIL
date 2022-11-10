import Vue from "vue"
import VueRouter from "vue-router"
import IndexView from "@/views/IndexView.vue"
import CreateView from "@/views/CreateView.vue"
import DetailView from "@/views/DetailView.vue"
import NotFound404 from "@/views/NotFound404.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "index",
    component: IndexView,
  },
  {
    path: "/create",
    name: "create",
    component: CreateView,
  },
  {
    path: "/404-not-found",
    name: "NotFound404",
    component: NotFound404,
  },
  {
    path: "/:id",
    name: "detail",
    component: DetailView,
  },
  {
    path: "*",
    redirect: { name: "NotFound404" },
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
