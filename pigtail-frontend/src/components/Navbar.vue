<template>
    <div class="nav">
        <nav class="navbar is-link is-fixed-top" role="navigation" aria-label="main navigation">
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
                Home
            </router-link>
            <router-link class="navbar-item" to="/about">
                About
            </router-link>
          <div class="navbar-item">
            <div class="buttons">
              <a class="button is-success" v-on:click="showModal = !showModal" :class="{'is-active': showModal}">
                Log in
              </a>
              <div class="modal" :class="{'is-active': showModal}">
              <div class="modal-background"></div>
              <div class="modal-card">
                <header class="modal-card-head">
                  <p class="modal-card-title">Donsol National Comprehensive High School</p>
                  <button class="delete" v-on:click="showModal = !showModal" aria-label="close"></button>
                </header>
                <section class="modal-card-body">
                    <form @submit.prevent="login">
                        <div class="field">
                      <p class="control has-icons-left has-icons-right">
                        <input class="input" v-model="username" type="username" placeholder="Email/Username">
                        <span class="icon is-small is-left">
                          <fa icon="envelope" />
                        </span>
                        <span class="icon is-small is-right">
                          <fa icon="check" />
                        </span>
                      </p>
                    </div>
                    <div class="field">
                      <p class="control has-icons-left">
                        <input class="input" v-model="password" type="password" placeholder="Password">
                        <span class="icon is-small is-left">
                          <fa icon="lock" />
                        </span>
                      </p> <br>
                      <div :class="{'is-active notification is-danger': alert}">
                      <button id="contextalert" class="contextalert" :class="{'delete': alertB}" v-on:click="alert = !alert"></button>
                      Check Username & Password
                    </div>
                      <button class="button is-link">Log In</button>
                  <hr>
                   <br />
                    </div>
                    </form>
                    
                    <button v-on:click="showModal = !showModal" class="button is-danger">Cancel</button>
                </section>
              </div>
            </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
    </div>
</template>
<script>
export default {
    name: 'NavBar',
    data() {
      return {
        accountInfo: {},
        showNav: false,
        showModal: false,
        alert: false,
        alertB: false,
        username: '',
        password: '',
      }
    },
    methods: {
         login() {
           if(this.username == "" || this.password == ""){
             document.getElementById("contextalert").innerHTML = Usernam;
           }
            this.$store.dispatch('userLogin', {
              username: this.username,
              password: this.password
            })
          .then(() => {
              if(this.$store.state.accGroup == 'Students'){
                this.$router.push('/studentDashboard')
              }else if(this.$store.state.accGroup == 'Parents'){
                this.$router.push('/about')
              }
            }
            )
            .catch(err => 
              this.alert = true
            )
        }
    },
    computed: {
      authenticaton(){
        return this.$store.state.auth
      }
    }
}

</script>
<style>
@import "../../node_modules/bulma";

.modal-card-head{
  background-color: lightblue;
}
.modal-card {
  width: 350px;
}
.modal-card-head {
  height: 30px;
}
.modal-card-title {
  font-size: 15px;
}
.contextalert {
  border: 0px;
}
</style>