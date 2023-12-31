class Solution {
    public int rearrangeCharacters(String s, String target) {
        
        int[] freqS = new int[26];
        int[] freqTarget = new int[26];
        int count = 0;
        for(char ch : s.toCharArray()) {
            freqS[ch-'a']++;
        }
        
        for(char ch : target.toCharArray()) {
            freqTarget[ch-'a']++;
        }

        int temp = 0;
        int min = Integer.MAX_VALUE;
        for(char ch : target.toCharArray()) {
            int x = freqS[ch-'a'];
            int y = freqTarget[ch-'a'];
            if(x >= y) {
                min = Math.min(min, x/y);
                temp++;
            }
            else{
                break;
            }
        }
        return temp==target.length() ? min : 0;
    }
}