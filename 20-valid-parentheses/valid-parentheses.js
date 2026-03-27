/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
     let stack = [];

    for (let i = 0; i < s.length; i++) {
        let char = s[i];

        if (char === "{" || char === "[" || char === "(") {
            stack.push(char);
        } else {
            if (stack.length === 0) {
                return false;
            }

            let top = stack.pop(); // Pop the top element to compare

            if (
                (char === "}" && top !== "{") ||
                (char === "]" && top !== "[") ||
                (char === ")" && top !== "(")
            ) {
                return false; // Mismatched brackets
            }
        }
    }
    return stack.length === 0;
};