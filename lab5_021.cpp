#include <iostream>
#include <string>
using namespace std;

int main()
{
	string c;
	int result = 0;
	cout << "Input a string: ";
	cin >> c;
	int len = c.length();
	/*asm(
	"StrToDec:\n\t\t"
	"movb (c),%cl\n\t\t"
	"cmpq $10,%rcx\n\t\t"
	"je end\n\t\t"
	"imulq $10,%rax\n\t\t"
	"subq $48,%rcx\n\t\t"
	"addq %rcx,%rax\n\t\t"
	"incq %rbx\n\t\t"
	"jmp StrToDec\n"
	"end:\n\t"
	"movq %rax,%rbx\n\t"
	: "=rax" (result)
	: "rax" (result)
	);*/
	asm(R"(
.lcomm %buf, $8
movq $3,%rax
xorq %rbx,%rbx
movq $buf, %rcx
movq $8,%rdx
int $0x80

xorq %rax,%rax
movq $buf, %rbx
xorq %rcx,%rcx

StrToDec:
        movb (%rbx),%cl
        cmpq $0,%rcx
        cmpq $10,%rcx
        je end
        imulq $10,%rax
	subq $48,%rcx
        addq %rcx,%rax
        incq %rbx
        jmp StrToDec

end:
    movq %rax,%rbx
    movq $1,%rax
    int $0x80
	)"
	);
	cout << result << endl;
}
/*
.global _start
_start:
    movq $3,%rax
    xorq %rbx,%rbx
    movq $buf, %rcx
    movq $8,%rdx
    int $0x80

    xorq %rax,%rax
    movq $buf, %rbx
    xorq %rcx,%rcx

StrToDec:
        movb (%rbx),%cl
        cmpq $0,%rcx
        cmpq $10,%rcx
        je end
        imulq $10,%rax
	subq $48,%rcx
        addq %rcx,%rax
        incq %rbx
        jmp StrToDec

end:
    movq %rax,%rbx
    movq $1,%rax
    int $0x80*/
