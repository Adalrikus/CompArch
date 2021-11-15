#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

int main()
{
	system("python3 vm.py");
	
	ifstream ifs;
	ifs.open("decrypted.txt");

	
	return 0;
}
