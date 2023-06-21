let maxnum = 999;
let palindrome = 0;
let productChar = 0;
let productRv = 0;
let product = 0;

for (let x = 100; x < maxnum; x++) {
  for (let y = 100; y < maxnum; y++) {
    product = x * y;
    productChar = String(product);
    productRv = productChar.split("").reverse().join("");

    if (productChar == productRv && product > palindrome) {
        palindrome = product;
        console.log(palindrome);
    }
  }
}

console.log(palindrome);