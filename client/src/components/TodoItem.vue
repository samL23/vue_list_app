<style>
  p{
    border-color: gray;
    cursor: pointer;
  }
  .done{
    text-decoration: line-through;
    color:gray
  }
</style>

<template>
    <p onclick="if (this.classList.contains('done')){
      this.classList.remove('done')
    }else{
      this.classList.add('done');
    }" class=" todoItem border-bottom border-secondary"><i class="fa fa-circle-o circle" style="font-size:24px"></i>{{ message }}</p>
</template>

<script>
export default {
  props: ['message'],
};


</script>