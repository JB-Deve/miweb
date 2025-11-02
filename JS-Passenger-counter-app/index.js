//document.getElementById("count").innerText = 5
//cmd+k+c

/*let countEl = document.getElementById("count-el")
let count = 0
let saveEl = document.getElementById("save-el")

function increment() {
    count += 1
    countEl.textContent = count 
}

function save() {
    let countStr = count + " - "
    saveEl.textContent += countStr
    countEl.textContent = 0
    count = 0
}
*/
let myPoints = 3

function add3Points() {
    myPoints += 3
}

function removelPoint() {
    myPoints -= 1
}
add3Points()
add3Points()
add3Points()
removelPoint()
removelPoint()

console.log(`My points: ${myPoints + 10 -3}`)
console.log("My points: " + myPoints + 2)
