/**
 *
 * @param {number[]} nums
 * @param {number} val
 *
 * @returns {number}
 */

const nums = [ 2, 11, 11, 11, 42, -2, 15, 89, 108, 17, 11, 15, 42 ]
// const nums = []

/* ------------------------------------------------------------------------- */
function getLength ( nums, val ) {
    for ( i = nums.length - 1; i >= 0; --i ) {
        if ( val === nums[ i ] ) {
            nums.splice( i, 1 )
        }
    }
    return nums.length
}

/* ------------------------------------------------------------------------- */
/* ------------------------------------------------------------------------- */
/*                                 version 2                                 */
/* ------------------------------------------------------------------------- */
function removeAllOccurrences ( nums, val ) {
    let i = 0
    while ( i < nums.length ) {
        if ( nums[ i ] === val ) {
            nums.splice( i, 1 )
        } else {
            ++i
        }
    }
    return nums.length
}


/* ------------------------------------------------------------------------- */
let lengthArray = getLength( nums, 11 )

/* ------------------------------------------------------------------------- */
console.log( lengthArray )
/* ------------------------------------------------------------------------- */


/* ------------------------------------------------------------------------- */
lengthArray = removeAllOccurrences( nums, 11 )

/* ------------------------------------------------------------------------- */
console.log( lengthArray )
/* ------------------------------------------------------------------------- */