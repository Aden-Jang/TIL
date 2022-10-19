const products = [
  { name: 'cucumber', type: 'vegetable' },
  { name: 'banana', type: 'fruit' },
  { name: 'carrot', type: 'vegetable' },
  { name: 'apple', type: 'fruit' },
]

const fruitFilter = function (product) {
  return product.type === 'fruit'
}

const newArry = products.filter(fruitFilter)

console.log(newArry)

// 2.


const newArry1 = products.filter(function (product) {
    return product.type === 'fruit'
})

console.log(newArry1)

// 3.

const newArry2 = products.filter((product) => {
    return product.type === 'fruit'
})

console.log(newArry2)