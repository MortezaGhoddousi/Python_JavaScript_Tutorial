const print = console.log;
// var age = prompt("Enter your age: ");
// print(age);

// for (var i = 0; i < 3; i++) {
//     print(i);
// }

// print(i);
// print("The end");

// for (let i = 0; i < 3; i++) {
//     print(i);
// }

// print(i);
// print("The end");

var arr = ["Morteza", "AmirReza", "Sahar"];
for (let i of arr) {
    print(i);
}

for (let i in arr) {
    print(i);
    print(arr[i]);
}

arr.forEach(function (e) {
    print(e);
});

function sayHello(name) {
    print("hello " + name);
}

sayHello("Morteza");

const sayHello1 = (name) => {
    print("hello " + name);
};

sayHello1("Morteza");
