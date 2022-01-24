
from lookup import vrtovn, after_call, mkvn, avrwvn;

def process_icall(ops, ins, outs):
	# p.casm("call", ins);
	
	out = outs[0];
	
	new = mkvn(None);
	
	ops.append(("icall", [ins[0]] + [vrtovn(i) for i in ins[1:]], "=>", [new]));
	
	# the only register you can rely on now is %vr{0,1,2,3} (not even the registers
	# from moves)
	after_call();
	
	avrwvn(out, new);
	
