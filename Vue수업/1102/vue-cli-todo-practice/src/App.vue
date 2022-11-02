<template>
  <div id="app">
    <TodoList :todos="todos" @delete-todo="deleteTodo" />
    <TodoForm @create-todo="createTodo" />
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  data: function () {
    return {
      todos: [],
    }
  },
  methods: {
    createTodo: function (todoTitle) {
      const todo = {
        title: todoTitle
      }
      this.todos.push(todo)
    },
    deleteTodo: function (todo) {
      // 인덱스 저장하는 코드
      const index = this.todos.indexOf(todo)
      // 해당 인덱스만 빼고 todos를 새로 만드는 코드
      this.todos.splice(index, 1)
    }
  }
}
</script>
  
<style>

</style>
