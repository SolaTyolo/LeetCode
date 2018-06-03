
//  Given a 32 - bit signed integer, reverse digits of an integer.
// 
//  Example:
//    Input: 123
//    Output: 321
// 
//    Input: -123
//    Output: -321
// 
//    Input: 120
//    Output: 21
// 
//   Assume we are dealing with an environment which could only store integers within the 32 - bit signed integer range: [−231, 231 − 1].For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

// #####################
// #
// # TIP:
// #   将整数转为字符串，再进行倒序(对首位进行判别)
// #
// #   Accepted  Runtime: 80 ms
// #
// #####################
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
        flag = new Array(1,-1)[Number(x < 0)];
        x_str = Math.abs(x).toString();
        x_str = x_str.split('').reverse().join('');
        res = flag * Number(x_str);
        if(res > Math.pow(2,31) - 1  || res < -1 * Math.pow(2,31)){
            res = 0;
        }
        return res;
};
