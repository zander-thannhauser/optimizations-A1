
def process_jumpI(ins, outs, p):
	p.casm("jumpI", ins, "->", outs);
	p.asm("jumpI", ins, "->", outs);
