<template>
  <div class="border">
    <h1>이것은 내가 만든 새로운 컴포넌트이다!</h1>
    <!-- 3. 보여주기 -->
    <MyComponentItem/>
  </div>  
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'

export default {
  name: 'MyComponent',
    // 2. 등록하기
    components: {
    MyComponentItem,
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>