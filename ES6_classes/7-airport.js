export default class Airport {
  constructor(name, code) {
    if (typeof name !== 'string' || typeof code !== 'string') {
      throw new TypeError('Both name and code must be strings');
    }

    this._name = name;
    this._code = code;
  }

  // Override default string tag
  get [Symbol.toStringTag]() {
    return this._code;
  }
}
