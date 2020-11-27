// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
	(KEYBOARD)
		@KBD
		D=M
		@WHITE
		D;JEQ
		@BLACK
		D;JNE
	
	(BLACK)
		//maybe this approach doesn't work
		@8192
		D=A
		(LOOP)
			@END
			D;JLT
			@SCREEN
			A=A+D
			M=-1
			D=D-1
			@LOOP
			0;JMP
		(END)
		@KEYBOARD
		0;JMP
	
	(WHITE)
		@8192
		D=A
		(LOOPW)
			@ENDW
			D;JLT
			@SCREEN
			A=A+D
			M=0
			D=D-1
			@LOOPW
			0;JMP
		(ENDW)
		@KEYBOARD
		0;JMP
