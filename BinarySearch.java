






// Write a code to find the specific number in the array.Time complexity should be the log(n).
// we are using the  binary Search algorithm to find the specific number or target element in the array.
public class BinarySearch {
    public static void main(String[] args) {


        int[] arr={2,3,22,44,78};
        int target=22;
        System.out.println(search(arr,target));;


    }

    public static int search(int[] arr,int target)
    {

        int start = 0;
        int end = arr.length-1;

        while (start<=end)
        {
            int mid = (end-start)+start/2;

            if(target<arr[mid])
            {
                end = mid-1;
            } else if (target>arr[mid]) {
                start=mid+1;
            }else
            {
                return mid;
            }


        }


return -1;



    }


}
