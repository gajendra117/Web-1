public class Solution {
    public String reverseWords(String s) {
    
        if (s == null || s.equals("")){
            return s;
        }
        StringBuffer buffer = new StringBuffer();
        s = s.trim();//取出两边的空格
        /*把相邻的空格去除掉*/
        for (int i=0; i<s.length(); ++i){
        	if (s.charAt(i) == ' ' && buffer.toString().charAt(buffer.toString().length()-1) == ' '){
        		;
        	}else{
        		buffer.append(s.charAt(i));
        	}
        }
        /*存储逆序的字符串*/
        StringBuilder reverseStr = new StringBuilder("");
        /*根据空格来做分割*/
        String[] arrays = buffer.toString().split(" ");
        
        for (int i=arrays.length-1; i>=0; --i){
            if (!reverseStr.toString().equals("")){
                reverseStr.append(" ");
            }
            reverseStr.append(arrays[i]);
        }
        return reverseStr.toString();
    }
}
