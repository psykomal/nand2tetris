// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


(START2)

@8193
D = A

@i
M = D

@SCREEN
D = A
@address
M = D

(LOOP2)
	
	@i
	M = M-1
	D = M

	@END2
	D, JEQ

	@address
	A = M

	M = 0

	@address
	M = M+1

	@LOOP2
	0; JMP
	
(END2)

	
	@KBD
	D = M

	@START1
	D, JNE

	@END2
	0; JMP


(START1)

@8193
D = A

@i
M = D

@SCREEN
D = A
@address
M = D

(LOOP1)
	
	@i
	M = M-1
	D = M

	@END1
	D, JEQ

	@address
	A = M

	M = -1

	@address
	M = M+1

	@LOOP1
	0; JMP
	
(END1)


	@KBD
	D = M

	@START2
	D, JEQ

	@END1
	0; JMP


