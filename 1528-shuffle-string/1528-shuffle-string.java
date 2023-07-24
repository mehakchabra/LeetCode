class Solution {
    public String restoreString(String s, int[] indices) {
        char[] ch = new char[indices.length];
        String str = "";
        for(int i = 0; i<indices.length;i++){
            ch[indices[i]] = s.charAt(i);
        }
        for(int i = 0; i<indices.length;i++){
            str+=ch[i];
        }
        return str;
    }
}