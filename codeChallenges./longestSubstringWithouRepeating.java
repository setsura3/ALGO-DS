class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0, j = 0, maxLen = 0;
        int [] counts = new int[256];
        for(; i < s.length(); i ++){
            for(; j < s.length(); j ++){
                if(counts[s.charAt(j)] != 0 ) break;
                counts[s.charAt(j)] += 1;
            }
            maxLen = Math.max(maxLen, j - i);
            counts[s.charAt(i)] -= 1;
    
        }
        return maxLen;
    }
}
