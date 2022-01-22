
from stdio import printf;

from block import process_block;

from lookup import new_frame_numbering;

def process_text(t, p):
	if (t.token == ".text"):
		p.printf(".text");
		t.next();
		p.indent();
		while (t.token == ".frame"):
			new_frame_numbering();
			name = next(t);
			assert(next(t) == ',');
			framesize = next(t);
			p.asm(".frame", [name, framesize]);
			while ("%vr" == next(t)[:3]):
				assert(not "TODO");
			process_block(t, p);
			while t.token and (t.token[0] == '.'):
				p.printf("%s:", t.token);
				assert(next(t) == ":");
				t.next();
				process_block(t, p);
		p.unindent();



















