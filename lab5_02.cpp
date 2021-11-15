#include <iostream>
#include <string>
using namespace std;

int main(){
    string text = "5245345";
    int leng = text.length();
    int result;
    result = stoi(text);
    /*asm(R"(
    push %eax
    mov %eax, 0
    for_loop:
    	cmp %eax, 10
    	je exit_loop
    	inc %eax
    jmp for_loop
    exit_loop:
    	mov result, %eax
    pop eax)"
    );*/
    cout << "result: " << result;
}
