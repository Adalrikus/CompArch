#include <iostream>
#include <string>

using namespace std;

int main(int argc, char** argv)
{ /*
string a = "543";
char input[] = { '5','4','3' };
int output;
int lengthy;
char* argv1 = argv[1];



//cout << "Enter string of numbers: ";
//cin >> input;

lengthy = a.length();

asm {
push eax
push ebx
push ecx
push edx
//mov ebx, 1
mov ecx, argv1
// xor ecx, ecx
xor eax, eax
xor ebx, ebx

for_loop:

xor eax,eax
mov al, byte ptr[ecx]//input[ebx] // 1 2 3
   cmp al, 0
je exit_loop
sub al, '0'
imul ebx, 10
add ebx, eax
inc ecx
jmp for_loop
exit_loop:
mov output, ebx

pop eax
pop ebx
pop ecx
pop edx



}
cout << '\n'<<input << " into output is: " << output;
cout << "\n input[0] is: "<<input[0] << "\n input[1] is: " << input[1];
*/
//pytagorian numbers program
float x [4];
float y[4];
float z[4];


for (int i = 1; i <= 1000; i += 4) {
x[0] = i;
x[1] = i + 1;
x[2] = i + 2;
x[3] = i + 3;
for (int j = i+1; j <= 1000; j ++) {
y[0] = j;
y[1] = j + 1;
y[2] = j + 2;
y[3] = j + 3;
asm(R"(
movups %xmm0, x
movups %xmm1, y
mulps %xmm0, %xmm0
mulps %xmm1, %xmm1
addps %xmm0, %xmm1
movups %xmm3, %xmm0
sqrtps %xmm0, %xmm0
roundps %xmm0, %xmm0, $1
mulps %xmm0, %xmm0
subps %xmm0, %xmm3
movups z, %xmm0
)");
if (z[0] == 0) {
cout << "\nFound: " << x[0] << " and " << y[0];
}
if (z[1] == 0) {
cout << "\nFound: " << x[1] << " and " << y[1];
}
if (z[2] == 0) {
cout << "\nFound: " << x[2] << " and " << y[2];
}
if (z[3] == 0) {
cout << "\nFound: " << x[3] << " and " << y[3];
}
}
}



// load 1-4 try 5-1000
// load 5-8 try 9-1000
// load 9-12 try 13-1000 ect.
// int x[1000] = {1,2... 1000}
// for (int i=0;i<1000;i+=4)
// for(int j=i+4;j<1000;j++)
// asm_ shit{ load x[i] test against x[j]}
/*

mov eax, x[i]
move ebx, x[j]
imulps eax, eax
imulps ebx, ebx
sum eax, ebx
mov ecx, eax
imulps eax, eax
cmp eax, ecx
je found
jmp out

found:
mov eax, result
out:


*/
}
