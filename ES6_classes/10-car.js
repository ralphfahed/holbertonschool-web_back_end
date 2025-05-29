export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Clone method
  cloneCar() {
    const Constructor = this.constructor;  // ✅ Now Constructor is defined
    return new Constructor(this._brand, this._motor, this._color);
  }
}
