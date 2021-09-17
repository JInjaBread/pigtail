<template>
 <NavBar></NavBar>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>
<script>
  import NavBar from '../components/Navbar';
  export default{
    name: 'About',
    components: {
      NavBar
    }
  }
</script>
