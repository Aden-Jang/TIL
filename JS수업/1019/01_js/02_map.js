const numbers = [1, 2, 3, 4, 5]

const doubleEle = function (number) {
  return number * 2
}

const newArry = numbers.map(doubleEle)

console.log(newArry)

// 2.
const newArry1 = numbers.map(function (number) {
    return number * 2
})

console.log(newArry1)

// 3.
const newArry2 = numbers.map((number) => {
    return number * 2
})

console.log(newArry2)

// 4.
const newArry3 = numbers.map((number) => number * 2)

console.log(newArry3)