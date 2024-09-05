/**
 *
 * @param {number} age Age of a person
 * @returns {boolean}
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