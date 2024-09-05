/**
 *
 * @param {number} age Age of a person
 * @returns {boolean} True if person is an adult, false if person is under 18 years old
 * @throws {Error} If age is lower than or equal zero
 * @author Jakub Gajewy 5D
 */
function isAdult(age){
    if(age <= 0){
        throw Error("Age can not be lower than 1");
    }
    else if(age < 18){
        return false
    }
    else if (age >= 18){
        return true
    }
}