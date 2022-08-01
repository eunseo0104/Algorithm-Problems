import java.util.Scanner;
import java.util.Stack;

public class Main {
    private static int N;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str;
        Stack<String> stack = new Stack<String>();
        boolean f;
        while (true) {
            stack.clear();
            str = scanner.nextLine();
            f=false;
            if(str.equals(".")) break;
            for(int i=0; i<str.length(); i++){
                if(str.charAt(i) == '('){
                    stack.push("(");
                }
                else if(str.charAt(i) == '['){
                    stack.push("[");

                }
                else if(str.charAt(i) == ')'){
                    if(stack.empty()) {
                        System.out.println("no");
                        f=true;
                        break;
                    }
                    if(!stack.pop().equals("(")) {
                        System.out.println("no");
                        f=true;
                        break;
                    }

                }
                else if(str.charAt(i) == ']'){
                    if(stack.empty()) {
                        System.out.println("no");
                        f=true;
                        break;
                    }
                    if(!stack.pop().equals("[")) {
                        System.out.println("no");
                        f=true;
                        break;
                    }
                }
            }
            if(f)
                continue;
            if(stack.empty())
                System.out.println("yes");
            else
                System.out.println("no");
        }
    }

}
