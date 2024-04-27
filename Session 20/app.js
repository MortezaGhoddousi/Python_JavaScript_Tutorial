const print = console.log;

class rect1 {
    constructor(height, width) {
        this.height = height;
        this.width = width;
    }

    calArea() {
        return this.height * this.width;
    }

    calPrimeter() {
        return 2 * this.height + 2 * this.width;
    }

    showResult() {
        var area = this.calArea();
        var primeter = this.calPrimeter();
        print("Area is: " + area);
        print("Primeter is: " + primeter);
    }
}

var rec1 = new rect1(4, 3);

print(rec1.height);
print(rec1.width);

print(rec1.calArea());
print(rec1.calPrimeter());

rec1.showResult();

class rect2 extends rect1 {
    show() {
        print("Class inherited");
    }
}

var rec2 = new rect2(1, 2);

rec2.show();

print(rec2.height);
print(rec2.width);

print(rec2.calArea());
print(rec2.calPrimeter());

rec2.showResult();
