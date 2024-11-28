// src/com/example/Calculator.java
package com.example;

public class Calculator {
    public static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 20;
        System.out.println("Сума " + num1 + " і " + num2 + " дорівнює: " + add(num1, num2));
    }
}
