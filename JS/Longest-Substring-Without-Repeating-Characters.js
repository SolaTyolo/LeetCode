/*  Given a string, find the length of the longest substring without repeating characters.

 Example:
   Given "abcabcbb", the answer is "abc", which the length is 3.

   Given "bbbbb", the answer is "b", with the length of 1.

   Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 */


/**
* @param {string} s
* @return {number}
*/
var lengthOfLongestSubstring = function (s) {
    let hashTable ={};
    cur = 0;
    max_len = 0;

    for (let index = 0; index < s.length; index++) {
        const element = s[index];
        if(hashTable.hasOwnProperty(element) && cur <= hashTable[element]){
            cur = hashTable[element] + 1;
        }else{
            max_len = Math.max(max_len,index - cur + 1);
        }
        hashTable[element] = index;
    }
    return max_len;
};