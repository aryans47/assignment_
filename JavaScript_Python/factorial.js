function factorial(n) {
    if (n === 0 || n === 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

function calculateFactorial() {
    let number = parseInt(prompt("Enter a number to calculate its factorial:"));

    if (isNaN(number)) {
        alert("Invalid input. Please enter a valid number.");
    } else {
        let result = factorial(number);

        alert("Factorial of " + number + " is " + result);
    }
}

calculateFactorial();