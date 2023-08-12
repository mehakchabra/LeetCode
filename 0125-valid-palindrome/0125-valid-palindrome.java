class Solution {
    public boolean isPalindrome(String s) {
        s = s.trim().toLowerCase();
        String s1 ="", s2="";
        for(int i=0; i<s.length();i++){
            if(s.charAt(i) >= 97 && s.charAt(i) <= 122 || s.charAt(i)>=48 && s.charAt(i)<=57){
                s1= s1+s.charAt(i);
            }
        }
        for (int i=0; i<s1.length(); i++)
      {
        char ch= s1.charAt(i); 
        s2= ch+s2; 
      }
        if(s1.equals(s2)) return true;
        else return false;
    }
}