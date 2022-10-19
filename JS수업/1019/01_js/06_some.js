const arr = [1, 2, 3, 4, 5]

// 1.

const result1 = arr.some(function(elem) {
  return elem % 2 === 0
})

console.log(result1)

// 2.

const result2 = arr.some((elem) => {
  return elem % 2 === 0
})

console.log(result2)

// 3. 

const result = arr.some((elem) => elem % 2 === 0)

console.log(result)