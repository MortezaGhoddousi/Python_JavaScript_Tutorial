var print = console.log;

console.log("Hello world from JavaScript");

var fname = "Morteza";

console.log(fname);

var isMale = true;

var x = 14;
var y = 5;

console.log(x % y);

x++; // x = x+1;

console.log(5 == 5.0);
console.log(5 === 5.0);

console.log(true && true);
console.log(true && false);
console.log(false && true);
console.log(false && false);

console.log(true || true);
console.log(true || false);
console.log(false || true);
console.log(false || false);

var age = 15;

if (age > 18) {
  print("Adult");
} else if (age < 10) {
  print("Child");
} else {
  print("Teenager");
}
