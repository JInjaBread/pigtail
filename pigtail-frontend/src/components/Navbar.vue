<template>
      <div class="nav">
        <nav class="navbar is-fixed-top" role="navigation" aria-label="main navigation">
          <div class="navbar-brand">
        <router-link to="/">
            <a class="navbar-item"  @click="navigate">
                <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
            </a>
        </router-link>

        <a role="button" v-on:click="showNav = !showNav" class="navbar-burger" :class="{'is-active': showNav}" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu" :class="{'is-active': showNav}">
        <div class="navbar-start">
        </div>

        <div class="navbar-end has-text-centered">
            <router-link class="navbar-item" to="/">
                <fa icon="home" />
                Home
            </router-link>
            <router-link class="navbar-item" to="/about">
                <fa icon="info-circle" />
                About
            </router-link>
          <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
          <fa icon="phone-alt" />
          Contact
        </a>
        <div class="navbar-dropdown">
          <a class="navbar-item">
            Facebook
          </a>
          <a class="navbar-item">
            Twitter
          </a>
          <a class="navbar-item">
            Gmail
          </a>
          <hr class="navbar-divider">
          <a class="navbar-item">
            Report an issue
          </a>
        </div>
        </div>
      </div>
      </div>
    </nav>
    </div>
</template>
<script>
export default {
    name: 'Navbar',
    data() {
      return {
        auth:'',
        showNav: false,
      }
    },
    methods: {
    },
    computed: {
      authenticaton(){
        return auth = localStorage.getItem(auth)
      }
    }
}

</script>
<style>
@import "../../node_modules/bulma";

</style>