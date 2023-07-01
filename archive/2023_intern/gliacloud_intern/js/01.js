function stringChallenge(strParam) {
  // Remove punctuation and spaces
  return strParam.split('').reverse().join('');
}

console.log(stringChallenge(prompt()));
