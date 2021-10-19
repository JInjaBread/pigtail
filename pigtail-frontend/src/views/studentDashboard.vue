<template>
 <w-app id="app" class="w-flex row">
  <aside>
    <div class="side-nav-header">

    </div>
    <div class="side-nav-icon text-center">
        <figure class="is-64x64">
        <img class="side-nav-image is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
    </figure>
    </div>
    <hr class="navbar-divider">
    <ul class="menu-list">
        <li><a>Dashboard</a></li>
        <li><a>Customers</a></li>
    </ul>
  </aside>
  <w-flex column>
    <header>
        <div class="student-header">
            <w-input class="mb2"
            label="Search"
            label-position="inside"
            inner-icon-left="wi-search">
            </w-input>
        </div>
    </header>
    <main class="grow">
        <w-flex wrap>
            <div class="xs5 pa1">
                <div class="py3">
                    <w-card class="profile text-center"  no-border>
                        <figure class="is-128x128">
                            <img class=" profile-image is-rounded" v-bind:src="student.get_photo">
                        </figure>
                        <p>
                         {{student.first_name}} {{student.last_name}}
                        </p>
                        <hr class="navbar-divider">
                        <div class="list">
                            <w-badge class="ml4 mr10" top right>
                                <template #badge>3</template>
                                <w-icon class="grey-light1" size="2.5em">mdi mdi-email</w-icon>
                            </w-badge>
                            <w-badge class="ml4 mr10" top right>
                                <template #badge>7</template>
                                <w-icon class="grey-light1" size="2.5em">mdi mdi-calendar-clock</w-icon>
                            </w-badge>
                        </div>
                    </w-card>
                </div>
            </div>
            <div class="xs7 pa1">
                <div class="py3">
                    <w-card>
                        <p></p>
                    </w-card>
                </div>
            </div>
        </w-flex>
    </main>
    <footer>Footer</footer>
  </w-flex>
</w-app>
</template>
<script>
import axios from 'axios'
export default{
    name:'studentDashboard',
    data() {
        return {
            student: {},
            subjects: [],
        }
    } ,
    mounted() {
        this.getStudent()
        this.getSubject()
        document.getElementById("page").className = "has-navbar";
        document.body.style.backgroundColor = "whitesmoke";
    },
    methods:{
    async getStudent(){
        await axios
       .get('/subject/student/', {headers: {
           Authorization: "Bearer " + localStorage.getItem('accessToken')
           } 
        })
       .then(response => {
           console.log(response.data)
           this.student = response.data
       })
       .catch(err => {
           console.log(err)
       })
    },
    async getSubject(){
        await axios
        .get('/subject/subject/', {headers: {
           Authorization: "Bearer " + localStorage.getItem('accessToken')
           } 
        })
        .then(response => {
            console.log(response.data)
            this.subjects = response.data
        })
        .catch(err => {
            console.log(err)
        })
    }
    } 
}
</script>
<style lang="scss">
.student-header{
    background-color: white;
    height: 40px;
    
}
.student-header-image{
    align-items: center;
}
.profile{
    background-color: white;
}
.profile-image{
    border-radius: 50%;
    height: 128px;
    width: 128px;
    border: 3px solid blue;
}
.side-nav-header{
    height: 40px;
    width: 100%;
    background-color: darkgreen;
}
.side-nav-image{
     border-radius: 50%;
     height: 64px;
     width: 64px;
}

</style>