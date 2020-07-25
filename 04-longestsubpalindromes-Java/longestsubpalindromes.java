// # Write the function longestSubpalindrome(s), that takes a string s and returns 
// the longest palindrome that occurs as consecutive characters (not just letters, but 
// 	any characters) in s. So:
// #    	longestSubpalindrome("ab-4-be!!!") 
// # returns "b-4-b". If there is a tie, return the lexicographically larger value -- 
// in java, a string s1 is lexicographically greater than a string s2 if (s1 > s2). So:
// #    	longestSubpalindrome("abcbce") 
// # returns "cbc", since ("cbc" > "bcb"). Note that unlike the previous functions, 
// this function is case-sensitive (so "A" is not treated the same as "a" here). Also, 
// from the explanation above, we see that longestSubpalindrome("aba") is "aba", 
// and longestSubpalindrome("a") is "a".

class Longestsubpalindromes {

	public boolean isPalindrome(String str) {
		String s = "";
		for (int i = str.length() - 1; i >= 0; i--) {
			s += str.charAt(i);
		}
		return s.equals(str);
	}

	public String fun_longestsubpalindromes(String s){
		String out = "";
		for (int i = 0; i < s.length(); i++) {
			String temp = "";
			for (int j = i; j < s.length(); j++) {
				temp += s.charAt(j);
				if (isPalindrome(temp)) {
					if (temp.length() > out.length() || (temp.length() == out.length() && temp.compareTo(out) > 0)) {
						out = temp;
					}
				}
			}
		}
		return out;
	}
	public static void main(String[] args) {
		Longestsubpalindromes obj = new Longestsubpalindromes();
		System.out.println(obj.fun_longestsubpalindromes("abcba"));
	}
}
