import java.util.*;
class Counter {
     static int count = 0;  // Shared across ALL objects

    Counter() {
        count++;  // Every new object increases same count
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.printf("%d", 42);
        System.out.printf("%f", 3.14159);
        System.out.println(in.nextLine());
        Counter a = new Counter();  // count = 1
        Counter b = new Counter();  // count = 2
        Counter c = new Counter();
        System.out.println(Counter.count);
        System.out.println(b.count);
        System.out.println(c.count);

    }
}
