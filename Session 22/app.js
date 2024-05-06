function factorial(n) {
    var a = 1;
    var x = 1;
    while (a < n) {
        x = x * a;
        a++;
    }
    return x;
}

var x = factorial(5);
console.log("The value of 5! is: ", x);
