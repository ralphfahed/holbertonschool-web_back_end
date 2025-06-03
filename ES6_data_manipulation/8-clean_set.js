function cleanSet(set, startString) {
  const result = [];
  for (const value of set) {
    if (value.startsWith(startString)) {
      result.push(value.slice(startString.length));
    } else {
      result.push(value);
    }
  }
  return result.join('-');
}

export default cleanSet;
