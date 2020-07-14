// # Write the function pascalsTriangleValue(row, col) 
// # that takes int values row and col, and returns the 
// # value in the given row and column of Pascal's 
// # Triangle where the triangle starts at row 0, and 
// # each row starts at column 0. If either row or col 
// # are not legal values, return None, instead of crashing. 

class pascaltrianglevalue {
	public boolean check(int row, int col) {
		return row >= 0 && col <= row;
	}

	public int fun_pascaltrianglevalue(int row, int col){
		if (check(row, col)) {
			int[] arr = {1};
			int size = 1;
			while (size <= row) {
				if (arr.length == 1) {
					arr = new int[2];
					arr[0] = arr[1] = 1;
				} else {
					int[] array = new int[size+1];
					array[0] = 1;
					int temp = 1;
					for (int i = 0; i < arr.length - 1; i++) {
						array[temp] = arr[i]+arr[i+1];
						temp++;
					}
					array[temp] = 1;
					arr = new int[array.length];
					for (int i = 0; i < arr.length; i++) {
						arr[i] = array[i];
					}
				}
				size++;
			}
			return arr[row];
		} else {
			return 0;
		}
	}
	public static void main(String[] args) {
		pascaltrianglevalue s = new pascaltrianglevalue();
		System.out.println(s.fun_pascaltrianglevalue(5, 2));
	}
}