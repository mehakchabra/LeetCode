class Solution {
    public String truncateSentence(String s, int k) {
        String arr[] =s.split(" ");
        // String arr1[] = new String[k];
        String str = "";
        for(int i=0; i<k; i++){
            // arr1[i] = arr[i];
            str = str+arr[i]+" ";
        }
        return str.trim();
        // return String.join(" ",arr1);
    }
}