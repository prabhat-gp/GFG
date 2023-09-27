#include <iostream>
using namespace std;

int binarySearch(int arr[], int n, int key) {
    int low = 0;
    int high = n - 1;

    while (low <= high) {
        int mid = low + (high - low) // 2
        if (arr[mid] == key) {
            return mid;
        } else if (arr[mid] > key) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }

    }
    return -1
}

int main(){
    int arr[] = {2, 4, 6, 8, 10};
    int n = sizeof(arr);
    int key = 10;

    int result = binarySearch(int arr, int n, int key);
    if result != -1 {
        cout << "Element found at index " << result << endl;
    } else {
        cout << "Element not found" << endl;
    }
    return 0;
}
