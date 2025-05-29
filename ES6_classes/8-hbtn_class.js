export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number' || typeof location !== 'string') {
      throw new TypeError('size must be a number and location must be a string');
    }

    this._size = size;
    this._location = location;
  }

  // Cast to Number
  valueOf() {
    return this._size;
  }

  // Cast to String
  toString() {
    return this._location;
  }
}
