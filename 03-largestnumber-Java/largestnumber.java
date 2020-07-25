// # largestNumber: Write the function largestNumber(text) that takes a string of text and 
// # returns the largest int value that occurs within that text, or 0 if no such value occurs. 
// # You may assume that the only numbers in the text are non-negative integers and 
// # that numbers are always composed of consecutive digits (without commas, for example). For example:
// #     	largestNumber("I saw 3 dogs, 17 cats, and 14 cows!")
// # returns 17 (the int value 17, not the string "17"). And
// #     	largestNumber("One person ate two hot dogs!")
// # returns None (the value None, not the string "None").


class largestnumber {
	public int fun_largestnumber(String s){
		int out = 0;
		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			String str = "";
			if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9') {
				str += c;
				i++;
				while (i < s.length()) {
					c = s.charAt(i);
					if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9') {
						str += c;
					}
					i++;
				}
				int value = Integer.parseInt(str);
				if (out == 0) {
					out = value;
				} else if (value > out) {
					out = value;
				}
			}
		}
		return out;
	}
	public static void main(String[] args) {
		
	}
}
	