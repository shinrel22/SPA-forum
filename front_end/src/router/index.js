import Vue from 'vue'
import Router from 'vue-router'

import Layout from '@/components/Layout'

import Home from '@/components/home/Home'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Layout',
      component: Layout,
      children: [
        {
          path: 'home',
          name: 'Home',
          component: Home
        }
      ]
    }
  ]
})
