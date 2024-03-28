var print = console.log;
function sayHello() {
  print("Hello dude");
}

print("Start the script!");
sayHello();

function sumNums(x, y) {
  var z = x + y;
  print(z);
  return z;
}
var z = sumNums(4, 9);
print(z);

myInfo = ["Morteza", "Ghoddousi", 29, "Male", 1.86, 91];

print(myInfo[0]);

myInfo.push("Black");

print(myInfo);

print(myInfo.length);

yourInfo = new Array("AmirReza", "Shirdel", 26, "Male", 1.79, 105);
print(yourInfo);

// [1, 4, 7]
// [1, 8, 4, 9, 12]
function calAvg(inp) {
  var sum = 0;
  for (var i of inp) {
    sum = sum + i;
  }
  return sum / inp.length;
}
avg = calAvg([1, 4, 7]);
print(avg);

avg = calAvg([1, 8, 4, 9, 12]);
print(avg);
