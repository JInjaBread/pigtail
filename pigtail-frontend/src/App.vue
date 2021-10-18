<template>
  <div id="app">
    <w-app>
      <router-view/>
  </w-app>
  </div>
</template>

<script>
  export default{
    name: 'App',
    mounted(){
      document.getElementById("page").className = "has-navbar-fixed-top";
      document.body.style.backgroundImage = "url('~@/assets/backgroundHomepage.jpg')";
    },
    methods:{
    },
  }


</script>

<style lang="scss">
@import "../node_modules/bulma";

</style>
