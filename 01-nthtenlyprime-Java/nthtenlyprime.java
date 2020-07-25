// # Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
// # and returns the nth Additive Prime, which is a prime number such that 
// # the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
// # is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


class Nthtenlyprime {

	public boolean isPrime(int n) {
		int count = 0;
		for (int i = 1; i <=n; i++) {
			if (n % i == 0) {
				count++;
			}
		}
		return count == 2;
	}

	public int fun_nthtenlyprime(int n){
		int count = -1;
		int temp = 0;
		while (count < n) {
			if (isPrime(temp)) {
				int sum = 0;
				int t = temp;
				while (t > 0) {
					sum += t % 10;
					t = t / 10;
				}
				if (isPrime(sum)) {
					count++;
				}
			}
			temp++;
		}
		return temp - 1;
	}
	public static void main(String[] args) {
	}
}