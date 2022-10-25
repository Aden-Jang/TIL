// let cat = {
//   name: '고양이',
//   age: 5,
//   attack: function() {
//     console.log(`${this.name} 냥냥펀치`)
//   }
// }

// let munchkin = {
//   name: '키티',
//   age: 2
// }

// munchkin.__proto__ = cat
// munchkin.attack()

// function Cat(name, age){
//   this.name = name
//   this.age = age
// }

// Cat.prototype.attack = function() {
//   console.log(`${this.name} 냥냥펀치`)
// }
// let myCat = new Cat('키티', 3)
// myCat.attack()

// class Cat {
//   constructor(name, age) {
//     this.name = name
//     this.age = age
//   }
// }

Cat.prototype.attack = function() {
  console.log(`${this.name} 냥냥펀치`)
}
let myCat = new Cat('키티', 3)
myCat.attack()

const myPrice = {
  exchangeRate: 1432,
  prices: [10, 50, 100],

  printPrices: function() {
    this.prices.forEach(function (price) {
      console.log(price * this.exchangeRate)
    }.bind(this)
    )
  }
}
myPrice.printPrices()

