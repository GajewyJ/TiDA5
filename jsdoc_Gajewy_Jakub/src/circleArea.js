/**
 * Calculates area of a circle
 * @param {number} radius Radius of a circle
 * @returns {number} Area of a circle
 * @throws {Error} If radius is lower than or equal 0
 * @author Jakub Gajewy 5D
 */
function calculateArea(radius){
    if(radius > 0){
        return Math.PI * (radius * radius)
    }
    else{
        throw Error("Radius can not be lower than or equal to zero");
    }
}