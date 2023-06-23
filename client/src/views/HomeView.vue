<script setup>
import TodoItem from '../components/TodoItem.vue';
const items = ["fjklsd","fsdklfj"];
</script>

<style>
/* For mobile phones: */

  .responsiveWidth{
    width: 95%;
    margin:auto
  }

  .todoItem{
    padding-left: 20px;
    margin: 0;
    padding-top: 10px;
    padding-bottom: 10px;
  }

  .circle{
    padding-right: 10px;
  }

  [class*="col-"] {
    width: 100%;
  }
  .todoItem{
    padding-left: 20px;
    margin: 0;
    padding-top: 15px;
    padding-bottom: 15px;
  }
  .round{
    border-radius: 10px
  }
  .inputBar{
    width: 100%; 
    border:none;
    background-color: rgb(42, 51, 51) ;
    background: transparent;
  }
  input:focus, input:focus{
    outline: none;
}


  .wrapper:hover{
    color:white;
    transition: 0.5s;
    transform: rotateZ(-90deg);
  }
  .wrapper{
    color: gray;
    transition: 0.9s;
    transform: rotateZ(45deg);
  }
 

  .secondaryBtn{
    text-decoration: none;
    cursor: pointer;
    color: gray;
  }
  .secondaryBtn:hover{
    color:darkcyan;
  }

  @media screen and (min-width: 576px) {
    /* For desktop: */
    .col-1 {width: 8.33%;}
    .col-2 {width: 16.66%;}
    .col-3 {width: 25%;}
    .col-4 {width: 33.33%;}
    .col-5 {width: 41.66%;}
    .col-6 {width: 50%;}
    .col-7 {width: 58.33%;}
    .col-8 {width: 66.66%;}
    .col-9 {width: 75%;}
    .col-10 {width: 83.33%;}
    .col-11 {width: 91.66%;}
    .col-12 {width: 100%;}
  }

  @media screen and (min-width: 768px) {
    /* For desktop: */
    .round{border-radius: 10px;}
    .responsiveWidth{ width: 50%; margin:auto}
    .col-1 {width: 8.33%;}
    .col-2 {width: 16.66%;}
    .col-3 {width: 25%;}
    .col-4 {width: 33.33%;}
    .col-5 {width: 41.66%;}
    .col-6 {width: 50%;}
    .col-7 {width: 58.33%;}
    .col-8 {width: 66.66%;}
    .col-9 {width: 75%;}
    .col-10 {width: 83.33%;}
    .col-11 {width: 91.66%;}
    .col-12 {width: 100%;}
  }
</style>



<template>
    <div class="text-white responsiveWidth" >
        <div class="pb-3" style="padding-left:10px;">
          <h1>TO DO</h1>
        </div>

        <form @submit.prevent="handleAddSubmit" style="background-color: rgb(42, 51, 51);" class="round">
          <div class="mb-3 d-flex flex-row ">
            <button
                type="button"
                class="btn  btn-sm m-3 "
                @click="handleAddSubmit">
                <div class="wrapper"><i class="fa fa-plus-circle" style="font-size:24px"></i></div>
                
              </button>
            <input
              autocomplete="off"
              type="text"
              class="todoItem round inputBar"
              id="addBookTitle"
              v-model="addTodoForm.item"
              placeholder="Create new to-do"
              style=" color: white;">
              
          </div>
        </form>



        <div style="background-color: rgb(42, 51, 51);" class="round">
          <div v-for="item in todoItems">
            <TodoItem :message=item></TodoItem>
          </div>


          <div class="container todoItem text-center" style="color:gray">
            <div class="row">
              <div class="col-sm">
                   <a class="secondaryBtn">4 Items</a>
              </div>
              <div class="col-sm">
                <a class="secondaryBtn">Place holder</a>
              </div>
              <div class="col-sm">
                <a class="secondaryBtn">Clear completed</a>
              </div>
            </div>
          </div>
        </div>
      
    </div>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      addTodoForm:{
        item: '',
      },
      todoItems: [],
    };
  },
  methods: {
    addTodo(payload){
      const path = 'http://localhost:5000/todo';
      axios.post(path,payload)
        .then(()=>{
          this.getTodo();
        })
        .catch((error)=>{
          console.log(error);
          this.getTodo();
        });
    },
    getTodo() {
      const path = 'http://localhost:5000/todo';
      axios.get(path)
        .then((res) => {
          this.todoItems = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handleAddSubmit(){
      if (this.addTodoForm.item !=""){
        const payload = {item: this.addTodoForm.item};
        this.addTodo(payload)
        this.initForm();
      }
    },
    initForm(){
      this.addTodoForm.item = '';
    }
    // next method

  },
  created() {
    this.getTodo();
  },
  mounted(){
    this.interval = setInterval(() => {
      this.getTodo()
    }, 30000 );
},

};



</script>
