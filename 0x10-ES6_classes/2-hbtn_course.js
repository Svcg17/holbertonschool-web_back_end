export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  set name(value) {
    if (typeof (value) === 'string') this._name = value;
    else throw new Error(TypeError('name must be a String'));
  }

  get name() {
    return this._name;
  }

  set length(value) {
    if (typeof (value) === 'number') this._length = value;
    else throw new Error(TypeError('length must be a Number'));
  }

  get length() {
    return this._length;
  }

  set students(value) {
    if (Array.isArray(value)) this._students = value;
    else throw new Error(TypeError('students must be an Array'));
  }

  get students() {
    return this._students;
  }
}
