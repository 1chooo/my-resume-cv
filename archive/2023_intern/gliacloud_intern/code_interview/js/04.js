function searchingChallenge(str) {
  const stack = [];

  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    if (char === '(') {
      stack.push(char);
    } else if (char === ')') {
      if (stack.length === 0) {
        return 0;
      } else {
        stack.pop();
      }
    }
  }

  if (stack.length === 0) {
    return 1;
  } else {
    return 0;
  }
}

console.log(searchingChallenge(prompt()));
