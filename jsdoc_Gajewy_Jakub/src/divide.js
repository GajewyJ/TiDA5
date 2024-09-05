/**
 * Divides number a by number b
 * @param {number} a Numerator
 * @param {number} b Denominator
 * @returns {number} Divided number
 * @example
 * a = 6
 * b = 3
 * console.log(divide(a, b))
 * //Logs 2
 * @throws {Error} If 'b' is 0
 * @author Jakub Gajewy kl. 5D
 */

function divide(a, b) {
    if(b === 0){
        throw Error("Dividing by zero is not possible")
    }
    else{
        return a / b;
    }
}