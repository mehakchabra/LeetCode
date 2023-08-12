class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        int index = s.lastIndexOf(" ");
        int len = s.length() - index -1;
        return len;
    }
}