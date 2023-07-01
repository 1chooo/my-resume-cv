function stringChallenge(strParam: string): string {
    // Remove punctuation and spaces
    return strParam.split('').reverse().join('');
}

console.log(stringChallenge(prompt()));
