const arr = [1, 2, 3, 4, 5]

// 1.

const result1 = arr.every(function(elem) {
  return elem % 2 === 0
})

console.log(result1)

// 2.

const result2 = arr.every((elem) => {
  return elem % 2 === 0
})

console.log(result2)

// 3. 

const result = arr.every((elem) => elem % 2 === 0)

console.log(result)