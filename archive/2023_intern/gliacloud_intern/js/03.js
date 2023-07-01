function arrayChallenge(arr) {
  // Find the largest number
  const largest = Math.max(...arr);

  // Calculate the sum of all numbers except the largest
  const totalSum = arr.reduce((acc, curr) => acc + curr, 0) - largest;

  // Check if the sum is equal to the largest number
  if (totalSum === largest) {
    return "true";
  } else {
    return "false";
  }
}

console.log(arrayChallenge(prompt().split(",").map(Number)));
