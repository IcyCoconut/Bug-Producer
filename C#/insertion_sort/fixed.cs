using System;

namespace InsertionSort {
    class Sort {
        static void Main(string[] args){
            int[] array = init_array(args.Length, args);
            print_array(array);
            array = insertion_sort(array);
            print_array(array);
        }

        private static int[] init_array(int argn, string[] args){
            int[] array = new int[argn];
            for (int i = 0; i < argn; i ++) {
                array[i] = Convert.ToInt32(args[i]);
            }
            return array;
        }

        private static void print_array(int[] array){
            for (int i = 0; i < array.Length; i ++){
                Console.Write("{0:d} ", array[i]);
            }
            Console.Write("\n");
        }

        private static int[] insertion_sort(int[] array){
            for (int i = 1; i < array.Length; i ++){
                int j = i;
                int k = j - 1;
                while (k >= 0){
                    if (array[k] > array[j]){
                        int temp = array[j];
                        array[j] = array[k];
                        array[k] = temp;
                        j --;
                        k --;
                    }
                    else {
                        break;
                    }
                }
            }
            return array;
        }
    }
}