function arrayChallenge(arr: number[]): number {
    if (arr.length < 2) {
      return -1;
    }
  
    let minPrice = arr[0];
    let maxProfit = 0;
  
    for (let i = 1; i < arr.length; i++) {
      const price = arr[i];
      if (price < minPrice) {
        minPrice = price;
      } else {
        const profit = price - minPrice;
        if (profit > maxProfit) {
          maxProfit = profit;
        }
      }
    }
  
    if (maxProfit === 0) {
      return -1;
    } else {
      return maxProfit;
    }
  }
  
  console.log(arrayChallenge(prompt().split(",").map(Number)));
  