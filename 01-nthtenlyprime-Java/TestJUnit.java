/**
 * This is JUnit that tests the methods of the Clock.
 * This contains 2 testcases.
 * 
 * Please don't run this file.
 * You can add your own test cases to this file by just copy and 
 * paste the last three lines of the code (TestCase2).
 * 
 * @author: Deepak
 */

import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.beans.Transient;

public class TestJUnit {

   @Test
   public void testCase1() {
      Nthtenlyprime s = new Nthtenlyprime();
      
      assertEquals("1.", 2, s.fun_nthtenlyprime(0));
      assertEquals("2.", 3, s.fun_nthtenlyprime(1));
      assertEquals("3.", 11, s.fun_nthtenlyprime(4));
      assertEquals("3.", 61, s.fun_nthtenlyprime(10));
   }

   @Test
   public void testCase2() {
      Nthtenlyprime s = new Nthtenlyprime();
      
      assertEquals("1.", 113, s.fun_nthtenlyprime(15));
      assertEquals("2.", 157, s.fun_nthtenlyprime(20)); 
      assertEquals("2.", 197, s.fun_nthtenlyprime(25)); 
   }
}

