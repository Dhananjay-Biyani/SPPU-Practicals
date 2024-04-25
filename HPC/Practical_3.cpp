#include <iostream>
#include <vector>
#include <algorithm>
#include <omp.h>

using namespace std;

void parallel_reduction(const vector<int> &data, int &min_value, int &max_value, int &sum_value, float &avg_value) {
    int size = data.size();
    min_value = data[0];
    max_value = data[0];
    sum_value = 0;

    #pragma omp parallel for reduction(min:min_value) reduction(max:max_value) reduction(+:sum_value)
    for (int i = 0; i < size; i++) {
        if (data[i] < min_value) {
            min_value = data[i];
        }
        if (data[i] > max_value) {
            max_value = data[i];
        }
        sum_value += data[i];
    }
    avg_value = static_cast<float>(sum_value) / size;
}

int main() {
    vector<int> data;
    int num;
    char choice;

    do {
        cout << "Enter a number: ";
        cin >> num;
        data.push_back(num);

        cout << "Do you want to continue (y/n): ";
        cin >> choice;
    } while (choice == 'Y' || choice == 'y');

    int min_value, max_value, sum_value;
    float avg_value;

    parallel_reduction(data, min_value, max_value, sum_value, avg_value);

    cout << "Minimum value is: " << min_value << endl;
    cout << "Maximum value is: " << max_value << endl;
    cout << "Summation is: " << sum_value << endl;
    cout << "Average value is: " << avg_value << endl;

    return 0;
}
