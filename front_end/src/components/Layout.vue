<template>
  <div :id="identify.id">
    <header id="topnav">
      <top-bar></top-bar>
      <breadcrumb></breadcrumb>
    </header>
    <div class="wrapper">
      <router-view></router-view>
    </div>
  </div>
</template>
<script>
  import TopBar from '@/components/navigation/TopBar'
  import Breadcrumb from '@/components/navigation/Breadcrumb'
  export default {
    components: {
      TopBar,
      Breadcrumb
    },
    props: {
      identify: {type: Object, default () { return {id: 'layout', name: 'Layout'} }}
    }
  }
</script>
