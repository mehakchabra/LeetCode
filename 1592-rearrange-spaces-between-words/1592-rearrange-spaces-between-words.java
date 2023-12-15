class Solution {
    public String reorderSpaces(String text) {
        int count=0;
        for(char a : text.toCharArray()){
            if(a == ' ')
                count++;
        }
        String arr[]= text.split(" ");
        StringBuilder str = new StringBuilder();
        int wcount=0;
        for(String sb : arr){
            if(sb.length()>0)
                wcount++;
        }
        int space;
        if(wcount-1 !=0){
            space = count /(wcount-1);
        }
        else{
            space=0;
        }
        
        String tspace="";
        for(int i=0;i<space;i++){
            tspace +=" ";
        }
        int temp=0;
        for(String sb : arr){
            if(sb.length()>0){
                 str.append(sb+tspace);
                 temp+=space;
            }      
        }
        //System.out.println(temp);
        temp -= space;
        //System.out.println(temp);
        String ans = str.toString();
        ans=ans.trim();
        if(temp<count){
            int rem = count-temp;
            //System.out.println(rem);
            for(int i=0;i<rem;i++){
                ans +=" ";
            }
        }
        return ans;
    }
}