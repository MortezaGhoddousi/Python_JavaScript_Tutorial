var print = console.log;

function callInf(obj) {
  for (var i in obj) {
    print(i, ":", obj[i]);
  }
}

var myObj = {
  fname: "Morteza",
  lname: "Ghoddousi",
  age: 30,
  weight: 92,
  height: 1.86,
  isMale: true,
  myFunc: callInf,
};

print(myObj.fname);
print(myObj["lname"]);

print(myObj);

callInf(myObj);

myObj.myFunc(myObj);

function ParentObj(x, y, z, h, p) {
  this.firstName = x;
  this.lastName = y;
  this.age = z;
  this.weight = h;
  this.height = p;
  this.sayHello = function () {
    print("Hello");
  };
}

var morteza = new ParentObj("Morteza", "Ghoddousi", 30, 92, 1.86);
print(morteza);

var amirReza = new ParentObj("AmirReza", "Shirdel", 26, 106, 1.79);
print(amirReza);
