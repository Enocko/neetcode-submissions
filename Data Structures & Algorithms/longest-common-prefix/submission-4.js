class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs) {
        strs.sort()
        const first = strs[0]
        const last = strs[strs.length - 1]
        let minn = Math.min(first.length, last.length)

        let res = ''
        for (let i=0; i < minn; i++){
            if (first[i] != last[i]){
                break 
            }
            else {
                res += first[i]
            }
        }

        return res
    }
}
