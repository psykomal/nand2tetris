// Bootstrap
	@256
	D=A
	@SP
	M=D
	@Sys.init
	0;JMP
// function Main.fibonacci 0
(Main.fibonacci)
	@Main.fibonacci.locals
	M=0
(Main.fibonacci.locals_loop)
	@0
	D=A
	@Main.fibonacci.locals
	D=D-M
	@Main.fibonacci.end_locals_loop
	D;JEQ
	@SP
	M=M+1
	A=M-1
	M=0
	@Main.fibonacci.locals
	M=M+1
	@Main.fibonacci.locals_loop
	0;JMP
(Main.fibonacci.end_locals_loop)
// push ARG 0

	@ARG
	D=M
	@0
	A=A+D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
// push constant 2

	@2
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
// lt
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	D=M-D
	@LT_0
	D;JLT
	@SP
	A=M
	M=0
	@CONTINUE_0
	0;JMP
(LT_0)
	@SP
	A=M
	M=-1
(CONTINUE_0)
	@SP
	M=M+1
// if-goto Main.fibonacci$IF_TRUE
	@SP
	AM = M-1
	D = M
	@Main.fibonacci$IF_TRUE
	D; JNE
// goto Main.fibonacci$IF_FALSE
	@Main.fibonacci$IF_FALSE
	0; JMP
// label Main.fibonacci$IF_TRUE
(Main.fibonacci$IF_TRUE)
// push ARG 0

	@ARG
	D=M
	@0
	A=A+D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
// return
	@LCL
	D = M
	@R14
	M = D
	@5
	A = D - A
	D = M
	@R15
	M = D
	@SP
	M = M-1
	A = M
	D = M
	@ARG
	A = M
	M = D
	D = A + 1
	@SP
	M = D
	@R14
	AM = M - 1
	D = M
	@THAT
	M = D
	@R14
	AM = M - 1
	D = M
	@THIS
	M = D
	@R14
	AM = M - 1
	D = M
	@ARG
	M = D
	@R14
	A = M - 1
	D = M
	@LCL
	M = D
	@R15
	A = M
	0; JMP
// label Main.fibonacci$IF_FALSE
(Main.fibonacci$IF_FALSE)
// push ARG 0

	@ARG
	D=M
	@0
	A=A+D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
// push constant 2

	@2
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
// sub
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	D=M-D
	@SP
	A=M
	M=D
	@SP
	M=M+1
// call Main.fibonacci 1
	@Main.fibonacci_return_2
	D = A
	@SP
	M = M+1
	A = M-1
	M = D
	@LCL
	D = M
	@SP
	M = M+1
	A = M-1
	M = D
	@ARG
	D = M
	@SP
	M = M+1
	A = M-1
	M = D
	@THIS
	D = M
	@SP
	M = M+1
	A = M-1
	M = D
	@THAT
	D = M
	@SP
	M = M+1
	A = M-1
	M = D
	@SP
	D = M
	@6
	D = D - A
	@ARG
	M = D
	@SP
	D = M
	@LCL
	M = D
	@Main.fibonacci
	0; JMP
(Main.fibonacci_return.2)
// push ARG 0

	@ARG
	D=M
	@0
	A=A+D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
// push constant 1

	@1
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
// sub
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	D=M-D
	@SP
	A=M
	M=D
	@SP
	M=M+1
// call Main.fibonacci 1
	@Main.fibonacci_return_4
	D = A
	@SP
	M = M+1
	A = M-1
	M = D
	@LCL
	D = M
	@SP
	M = M+1
	A = M-1
	M = D
	@ARG
	D = M
	@SP
	M = M+1
	A = M-1
	M = D
	@THIS
	D = M
	@SP
	M = M+1
	A = M-1
	M = D
	@THAT
	D = M
	@SP
	M = M+1
	A = M-1
	M = D
	@SP
	D = M
	@6
	D = D - A
	@ARG
	M = D
	@SP
	D = M
	@LCL
	M = D
	@Main.fibonacci
	0; JMP
(Main.fibonacci_return.4)
// add
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	D=M+D
	@SP
	A=M
	M=D
	@SP
	M=M+1
// return
	@LCL
	D = M
	@R14
	M = D
	@5
	A = D - A
	D = M
	@R15
	M = D
	@SP
	M = M-1
	A = M
	D = M
	@ARG
	A = M
	M = D
	D = A + 1
	@SP
	M = D
	@R14
	AM = M - 1
	D = M
	@THAT
	M = D
	@R14
	AM = M - 1
	D = M
	@THIS
	M = D
	@R14
	AM = M - 1
	D = M
	@ARG
	M = D
	@R14
	A = M - 1
	D = M
	@LCL
	M = D
	@R15
	A = M
	0; JMP
// function Sys.init 0
(Sys.init)
	@Sys.init.locals
	M=0
(Sys.init.locals_loop)
	@0
	D=A
	@Sys.init.locals
	D=D-M
	@Sys.init.end_locals_loop
	D;JEQ
	@SP
	M=M+1
	A=M-1
	M=0
	@Sys.init.locals
	M=M+1
	@Sys.init.locals_loop
	0;JMP
(Sys.init.end_locals_loop)
// push constant 4

	@4
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
// call Main.fibonacci 1
	@Main.fibonacci_return_6
	D = A
	@SP
	M = M+1
	A = M-1
	M = D
	@LCL
	D = M
	@SP
	M = M+1
	A = M-1
	M = D
	@ARG
	D = M
	@SP
	M = M+1
	A = M-1
	M = D
	@THIS
	D = M
	@SP
	M = M+1
	A = M-1
	M = D
	@THAT
	D = M
	@SP
	M = M+1
	A = M-1
	M = D
	@SP
	D = M
	@6
	D = D - A
	@ARG
	M = D
	@SP
	D = M
	@LCL
	M = D
	@Main.fibonacci
	0; JMP
(Main.fibonacci_return.6)
// label Sys.init$WHILE
(Sys.init$WHILE)
// goto Sys.init$WHILE
	@Sys.init$WHILE
	0; JMP
