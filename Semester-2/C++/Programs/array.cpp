#include <iostream>
using namespace std;

class Array {
private:
    int item[100];
    int size;
    int capacity;

public:
    Array() {
        size = 0;
        capacity = 100;
    }

    void insertA(int index, int value) {
        if (size >= capacity || index < 0 || index > size) {
            cout << "Invalid Position";
            return;
        }

        for (int i = size; i > index; i--) {
            item[i] = item[i - 1];
        }

        item[index] = value;
        size++;
    }

    void display() {
        for (int i = 0; i < size; i++) {
            cout << item[i] << " ";
        }
    }
};

int main() {
    Array arr;
    arr.insertA(0, 10);
    arr.insertA(1, 20);
    arr.insertA(1, 15);

    arr.display();
    return 0;
}
        // Find Another Way to enter an element to a specific position.
