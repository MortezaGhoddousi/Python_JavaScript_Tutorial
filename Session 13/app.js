var print = console.log;
var myList = [0, 1, 2];

print("For of loop");
for (var i of myList) {
  print(i);
}

print("For loop");
for (var i = 0; i < 3; i++) {
  print(i);
}

// Task

var text = "Learning is fun";

for (var i = 0; i < 3; i++) {
  print(text);
}

for (var i of myList) {
  print(text);
}

print("While loop");
var i = 0;
while (i < 3) {
  print(i);
  i++;
}

var client = 6;
while (client >= 0) {
  print(--client);
}

for (var i = 0; i < 5; i++) {
  print(i);
  if (i == 3) {
    break;
  }
}
