/**
 * Calculates area of a circle
 * @param {number} radius Radius of a circle
 * @returns {number} Area of a circle
 * @throws {Error} If radius is lower than or equal 0
 * @author Jakub Gajewy kl. 5D
 */
function calculateArea(radius){
    if(radius > 0){
        return 3.14 * (radius * radius)
    }
    else{
        throw Error("Radius can not be lower than or equal to zero");
    }
}