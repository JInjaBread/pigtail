<template>
<div class="Home">
   <Navbar />
  <div class="bod">
    <w-flex wrap>
        <div class="xs12 pa1">
          <div class="py3">
            <vueper-slides>
              <vueper-slide v-for="(slide, i) in slides" :key="i" :title="slide.title" :content="slide.content" />
            </vueper-slides>
          </div>
        </div>
        <div class="xs6 pa1">
          <div class="py3">
          </div>
        </div>
        <div class="xs6 pa1">
          <div class="py3">
            <w-button
            class="ma1"
            @click="noOverlay = false;overlayColor = 'rgba(35, 71, 129, 0.5)';showModal = !showModal"
            outline
            color="primary">
            Custom color overlay
          </w-button>
          </div>
        </div>
    </w-flex>
    <w-drawer
      v-model="showDrawer"
      top
      :no-overlay="noOverlay"
      :overlay-color="overlayColor">
      <w-button
        class="button--close"
        @click="showDrawer = false"
        sm
        outline
        absolute
        round
        color="primary"
        icon="wi-cross">
      </w-button>
    </w-drawer>
    <div class="modal" :class="{'is-active': showModal}">
              <div class="modal-background"></div>
              <div class="modal-card">
                <header class="modal-card-head text-center">
                  <p class="modal-card-title">Donsol National Comprehensive High School</p>
                  <button class="delete" v-on:click="showModal = !showModal" aria-label="close"></button>
                </header>
                <section class="modal-card-body">
                        <w-card class="white--primary" content-class="pa0">
                          <w-form 
                            @submit.prevent="login"
                            @validate="onValidate"
                            @success="onSuccess"
                            class="px8 pt2 pb12">

                            <div class="text-center"><fa class="formIcon1 text-center" icon="user" /></div>

                            <w-input class="mb2"
                              required
                              label="Username"
                              inner-icon-left="mdi mdi-account"
                              v-model="username"
                              :validators="[validators.required]">
                            </w-input>

                            <w-input class="mb2"
                              required
                              label="Password"
                              v-model="password"
                              :type="isPassword ? 'password' : 'text'"
                              :inner-icon-left="isPassword ? 'mdi mdi-eye' : 'mdi mdi-eye-off'"
                              :validators="[validators.required]"
                              @click:inner-icon-left="isPassword = !isPassword">
                            </w-input>
                            <button 
                            class="button is-link"
                            type="submit"
                            :disabled="form.valid === false"
                            :loading="form.submitted && !form.sent"
                            >Log In</button>
                          </w-form>
                           

                          <w-notification
                            v-model="form.sent"
                            error
                            transition="bounce"
                            absolute
                            plain
                            round
                            bottom>
                            Check Username or Password!
                          </w-notification>
                        </w-card>
                </section>
              </div>
            </div>
  </div>
</div>
</template>

<script>
import Navbar from '../components/Navbar'
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'
export default {
  name: 'Home',
  data: () => ({
      username:'',
      password:'',
      accountInfo: {},
      isPassword: true,
      showDrawer: false,
      noOverlay: false,
      overlayColor: '',
      showModal: false,
      form: {
        valid: null,
        submitted: false,
        sent: false,
        errorsCount: 0,
      },
      slides: [
          {
            title: 'Slide #1',
            content: 'Slide content.'
          },
          {
             title: 'Slide #2',
            content: 'Slide content.'
          }
        ],
      validators: {
        required: value => !!value || 'This field is required',
      }
    }),

    methods: {
     async login() {
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
            .catch(error => {
              this.form.sent = true
            })
        },
      onSuccess () {
        setTimeout(() => (this.form.sent = true), 2000)
      },
      onValidate () {
        this.form.sent = false
        this.form.submitted = this.form.errorsCount === 0
      }
    },
    components:{
      VueperSlides, 
      VueperSlide,
      Navbar,
    },
    computed: {
      authenticaton(){
        return this.$store.state.auth
      }
    }
  }
</script>
<style lang="scss">
@import "../../node_modules/bulma";
.formIcon1{
  color:darkcyan;
  font-size: 100px;
}
.vueperslide {
  background: linear-gradient(-45deg, #EE7752, #E73C7E, #23A6D5, #23D5AB);

  &__title {
    font-size: 7em;
    opacity: 0.6;
  }
}
.w-flex.wrap{
  flex:none;
}
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
.button{
  width: 100%;
}
</style>
