package CTCI;
// URLify: Write a method to replace all spaces in a string with '%20'. 
// You may assume that the string has sufficient space at the end to 
// hold the additional characters,and that you are given the "true" 
// length of the string. (Note: If implementing in Java,please use a 
// character array so that you can perform this operation in place.
// EXAMPLE
// Input: "Mr John Smith ", 13 Output: "Mr%20John%20Smith"

import java.util.Enumeration;
import java.util.Hashtable;
import java.util.HashMap;

class ch1 {
    public static void main(String args[]) {
        char[] testInput = {'M','r',' ','J','o','h','n',' ','S','m','i','t','h',' '};
        replaceChars(testInput);
        
    }
    
    public static void replaceChars(char[] input) {
        StringBuilder test = new StringBuilder();

        for (int i = 0; i < input.length; i++) {
            if (input[i] == ' ') {
                test.append("%20");
            } else {
                test.append(input[i]);
            }
        }
        System.out.println(test);
    }
    
    // problem 1.4
    public static boolean palindromePermutation(String word) {
        HashMap<String, Integer> hashmap = new HashMap<>();
        int i = 0;
        while (i < word.length()) {
            char letter = word.charAt(i);
            if (hashmap.containsKey(letter)) {
                hashmap.put(letter) = hashmap[letter] + 1;
            } else {
                hashmap[letter] = 1;
            }

            i += 1;
        }
        return true;
    }
}