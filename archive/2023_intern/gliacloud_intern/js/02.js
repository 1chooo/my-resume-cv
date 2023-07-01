function stringChallenge(str) {
  // Remove punctuation and spaces
  const cleanStr = str.replace(/[^A-Za-z]/g, '');

  // Reverse the clean string
  const reversedStr = cleanStr.split('').reverse().join('');

  // Compare the clean string with its reversed version
  if (cleanStr === reversedStr) {
    return "true";
  } else {
    return "false";
  }
}

console.log(stringChallenge(prompt()));
