import java.util.*;

class test {
    public static void main(String[] args) {

        ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
        System.out.println(list);
        list.add(new ArrayList<Integer>());
        list.add(new ArrayList<Integer>());
        list.add(new ArrayList<Integer>());
        System.out.println(list);
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                list.get(i).add(3*i+j);
            }
        }
        System.out.println(list);
    }
}