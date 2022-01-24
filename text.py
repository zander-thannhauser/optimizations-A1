
from stdio import printf;

from block import process_block;

from lookup import new_frame_numbering, vrtogvn;

def process_text(t, p):
	if (t.token == ".text"):
		p.printf(".text", prefix = "");
		t.next();
		p.indent();
		
		while (t.token == ".frame"):
			name = next(t);
			assert(next(t) == ',');
			framesize = next(t);
			
			args = [];
			
			while next(t) == ",":
				reg = next(t);
				printf("arg += \"%s\"\n", reg);
				assert(reg[:3] == "%vr");
				args.append(reg);
			
			new_frame_numbering(args);
			
			p.asm(".frame", [name, framesize, *(vrtogvn(a) for a in args)], prefix = "");
			
			process_block(t, p);
			
			while t.token and t.token != ".frame" and (t.token[0] == '.'):
				p.printf("%s:", t.token, prefix = "");
				assert(next(t) == ":");
				t.next();
				process_block(t, p);
		
		# assert(not "CHECK");
		
		p.unindent();



















