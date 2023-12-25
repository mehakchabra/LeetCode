class Solution {
    public String largestWordCount(String[] messages, String[] senders) {
        // In a hashmap, record whhich person has sent how many words
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < messages.length; i++) {
            // doing this would get us the number of words in that particular message
            int words = messages[i].split(" ").length;
            String name = senders[i];
            // update in the map
            map.put(name, words + map.getOrDefault(name, 0));
        }

        // a string 'ans' to record our final sender's name
        String ans = "";
        // variable to keep track of the maximum number of words spoken by a sender
        int max = 0;    
        // go through the senders
        for (String name : map.keySet()) {
            // number of words current sender has sent
            int words = map.get(name);  
            // if number of words > max spoken words
            if (words > max) {
                max = words;    // update max
                ans = name;     // make this sender our candidate
            } 
            // if we have a tie in the max number of words spoken
            else if (words == max) {
                // keep the name which is lexicographically greater
                int x = ans.compareTo(name);
                ans = (x > 0)? ans : name;
            }
        }

        // return the final sender's name
        return ans;
    }
}