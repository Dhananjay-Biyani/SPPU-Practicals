#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <omp.h>

using namespace std;
using namespace std::chrono;

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    bool swapped = true;

    while (swapped) {
        swapped = false;
        #pragma omp parallel for
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                swap(arr[i], arr[i + 1]);
                swapped = true;
            }
        }
    }
}

void merge(vector<int>& arr, int l, int m, int r) {
    vector<int> temp;
    int left = l;
    int right = m + 1;

    while (left <= m && right <= r) {
        if (arr[left] <= arr[right]) {
            temp.push_back(arr[left]);
            left++;
        }
        else {
            temp.push_back(arr[right]);
            right++;
        }
    }

    while (left <= m) {
        temp.push_back(arr[left]);
        left++;
    }

    while (right <= r) {
        temp.push_back(arr[right]);
        right++;
    }

    for (int i = l; i <= r; i++) {
        arr[i] = temp[i - l];
    }
}

void mergeSort(vector<int>& arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        #pragma omp parallel sections
        {
            #pragma omp section
            mergeSort(arr, l, m);
            #pragma omp section
            mergeSort(arr, m + 1, r);
        }
        merge(arr, l, m, r);
    }
}

int main() {
    int n = 1000; // Number of elements
    vector<int> arr(n);

    // Generate random numbers and store them in the array
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 1000); // Range of random numbers

    for (int i = 0; i < n; ++i) {
        arr[i] = dis(gen);
    }

    // Measure execution time for Bubble Sort
    auto start_bubble = high_resolution_clock::now();
    bubbleSort(arr);
    auto stop_bubble = high_resolution_clock::now();
    auto duration_bubble = duration_cast<microseconds>(stop_bubble - start_bubble);

    cout << "Bubble Sort Execution Time: " << duration_bubble.count() << " microseconds" << endl;

    // Measure execution time for Merge Sort
    auto start_merge = high_resolution_clock::now();
    mergeSort(arr, 0, n - 1);
    auto stop_merge = high_resolution_clock::now();
    auto duration_merge = duration_cast<microseconds>(stop_merge - start_merge);

    cout << "Merge Sort Execution Time: " << duration_merge.count() << " microseconds" << endl;

    return 0;
}
