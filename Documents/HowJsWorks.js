//program allocates memory, parse and executes
//There is JavaScript Engine in every browser
// Chrome has the V8 engine that reads the JS that we write and changes 
// into machine executable instruction for the Browser
// the engine consists memory heap and call stack

//Memory heap just holds the variables and consts that we created
// it has limited size so we can encounter memory size errors
const a = 1;
const b = 10;
const c = 100;

//call stack runs the line of the code in order and remove if it executed
//you can only do one thing at a time, first in last out.
//other languages can have multiple steps, and these are called multithreaded
// JS is single threaded, only one statement is executed at a time and non blocking
//Multithreaded environment can have deadlocks
// Sync programming because of the call stack
// Stack overflows happen when call stack over flowed
// In sync programming if a line takes so much time, browser can freeze and the left line will not be executed before.
// Async programming comes to help
// JavaScript Run-Time Environment is a part of a browser
// Web APIs (DOM, AJAX, Timeout), CallBack and Event Loop 
// setTimeout goes to call stack first, after that it goes to web api part and web api set the timeout
// and then it goes to callback and event loop checks if there is some callbacks.
// if the timeout 0, it still goes to the process

console.log('1');
console.log('2');
console.log('3');

setTimeout(() => {console.log('async')}, 1000)

const one = () => {
    const two = () => {
        console.log('4');
    }

    two();
}

console.log('4') // --> After executed its going to be removed
two() // --> goes on top and after execution will be removed
one() // Same

//Call stack
//Stack overflow with recursion
function foo(){
    foo()
}

foo()
//Stack overflow


//The order -->
// Call stack
// web api
// callback
// event loop

