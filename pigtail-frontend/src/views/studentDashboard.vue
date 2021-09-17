<template>
    <!-- START NAV -->
    <section class="hero is-fullheight">
        <div class="columns">
            <aside class="column is-2" id="sidenav" >
                <div class="menu">
                    <ul class="menu-list">
                        <li><a>Dashboard</a></li>
                        <li><a>Timeline</a></li>
                    </ul>
                    <p class="menu-label">
                        General
                    </p>
                    <ul class="menu-list">
                        <li><a>Subject</a></li>
                        <li><a>Grade Report</a></li>
                    </ul>
                    <p class="menu-label">
                        Others
                    </p>
                    <ul class="menu-list">
                        <li><a>Account</a></li>
                        <li><a>Rewards</a></li>
                    </ul>
                </div>
            </aside>
            <div class="column is-fullwidth">
                <div class="userPictures has-text-centered">
                    <figure class="image is-128x128">
                    <img class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
                    </figure>
                </div>
                <div class="exp columns">
                <div v-for="subject in subjects" :key="subject.id" class="card">
                    <div class="card-image">
                        <figure class="image is-fullwidth">
                            <img v-bind:src="subject.get_photo" alt="Placeholder image">
                     </figure>
                    </div>
                <div :class="subject.category.category" class="card-content">
                    <div class="media">
                    <div class="media-left">
                    </div>
                    <div class="media-content">
                        <p class="title is-4">{{subject.name}}</p>
                        <a class="is-6">{{subject.channel}}</a>
                    </div>
                    </div>

                    <div class="content">
                    
                    </div>
                </div>
            </div>
            </div>
            </div>
        </div>
    </section>
    
   
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
    },
    methods:{
    async getStudent(){
        axios
       .get('/student/', {headers: {
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
        axios
        .get('/subject/', {headers: {
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
<style>
.card {
    margin-right: 10px;
    margin-top: 50px;
    width: 100%;
    max-height: 50%;
}

.Filipino{
    border-color: yellow;
    background: linear-gradient(to bottom, #33ccff 0%, #999966 100%);;
}
.Science {
    border-color: green;
    background: linear-gradient(to bottom, #33ccff 0%, #cc0066 100%);
}
.ArtsaAndLetters{
    border-color: green;
    background: linear-gradient(to bottom, #33ccff 0%, #660066 100%);
}
#sidenav{
    height: 700px;
    overflow: auto;
    background-color: darkslategrey;
}
.userPictures{
    height: 100px;
    background-color: darkgrey;

}
.exp{
    margin-top:10px ;
    margin-right: 10px;
}
</style>