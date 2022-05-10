#include <iostream>
#include <cmath>
#include <string>
using namespace std;

void hanoi(int start, int goal, int remain, int n) {
   if (n == 2) {
      printf("%d %d\n", start, remain); // 1 3
      printf("%d %d\n", start, goal); // 1 2
      printf("%d %d\n", remain, goal); // 3 2
   }
   else {
      hanoi(start, remain, goal, n - 1);
      printf("%d %d\n", start, goal); // 1 3
      hanoi(remain, goal, start, n - 1); //2 1 // 2 3 // 1 3
   }
}

int main() {
   int n;
   cin >> n;
   string count = to_string(pow(2, n));
   int idx = count.find('.');
   count = count.substr(0, idx);
   count[count.length() - 1] = count[count.length() - 1] - 1;
   cout << count << endl;
   if (n <= 20) hanoi(1, 3, 2, n);
   return 0;
}


// 오류 해결 2가지
// 2의 100승 처리위해 문자열로 해결해줘야함
// cout --> printf 로 시간초과 해결

//int solve_remain(int s, int g) {
//   
//   bool inThree= ((s - 3 + 1) > 0 || (g - 3 + 1) > 0);
//   bool inOne= !((s - 2 + 1) > 0 && (g - 2 + 1) > 0);
//   
//   if(inThree == false) return 3;
//   else if(inOne == false) return 1;
//   else return 2;
//}