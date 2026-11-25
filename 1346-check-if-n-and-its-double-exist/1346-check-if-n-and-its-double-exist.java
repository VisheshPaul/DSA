class Solution {
    public boolean checkIfExist(int[] arr) {
        int n = arr.length, i = 0;
        HashMap<Integer, Integer> x = new HashMap<>();
        while (i < n) {
            if (x.getOrDefault(arr[i] * 2, 0) == 1 || (arr[i] % 2 == 0 && x.getOrDefault(arr[i] / 2, 0) == 1)) return true;
            x.put(arr[i], 1);
            i++;
        }
        return false;
    }
}