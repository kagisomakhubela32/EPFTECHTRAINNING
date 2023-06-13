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

    if (productChar === productRv && product > palindrome) {
      palindrome = product;
    }
  }
}

console.log(palindrome);

/*This JavaScript code will find the largest palindrome number that is the product of two three-digit numbers 
within the given range (100 to maxnum). The result will be printed to the console.*/






