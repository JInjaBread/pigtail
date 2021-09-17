<template>
<div class="Home">
  <NavBar></NavBar>
  <div class="bod">
    <h1>This is home page</h1>
  </div>
</div>
</template>

<script>
import NavBar from '../components/Navbar'
export default {
  name: 'Home',
  data(){
    return{
    }
  },
  components: {
    NavBar
  }
  
}
</script>
<style>
.bod{
  margin-top: 50px;
}
</style>
