(KEYBOARD)
	@KBD
	D=M
	@BLACK
	D;JNE
	@WHITE
	D;JEQ

(BLACK)
	@8192
	D=A
	(LOOP)
		@END		//conflict here because M changes when we do @END
		D;JLT	
		@SCREEN
		A=A+D
		M=!M
		D=D-1
		@LOOP
		0;JMP
	(END)
	@KEYBOARD
	0;JMP

(WHITE)
	@KEYBOARD
	0;JMP
//		A=D
//		M=!M
//		D=D+1	
