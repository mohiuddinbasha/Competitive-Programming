import java.util.Arrays;

class QuickSort {

	public int partition(int[] arr, int low, int high) {
		int pivot = arr[low];
		int i = low+1;
		int j = high;
		while (i < j) {
			System.out.println("i = "+i);
			System.out.println("j = "+j);
			while (arr[i] < pivot) {
				i++;
				if (i == high) {
					break;
				}
			}
			while (pivot > arr[j]) {
				j--;
				if (j == low) {
					break;
				}
			}
			if (i >= j) {
				break;
			}
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
		int temp = arr[low];
		arr[low] = arr[j];
		arr[j] = temp;
		return j;
	}

	public void sort(int[] arr, int low, int high) {
		if (high > low) {
			int index = partition(arr, low, high);
			sort(arr, low, index-1);
			sort(arr, index+1, high);
		}
		System.out.println(Arrays.toString(arr));
	}

	public int[] quicksort(int[] arr){
		// Your code goes here
		int low = 0;
		int high = arr.length - 1;
		sort(arr, low, high);
		return arr;
	}
	public static void main(String[] args) {
		QuickSort obj = new QuickSort();
		int[] arr = {14,4,6,25,9};
		System.out.println(Arrays.toString(obj.quicksort(arr)));
	}
}