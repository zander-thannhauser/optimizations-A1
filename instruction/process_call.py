
from lookup import vrtovn, after_call;

def process_call(ops, ins, _):
	# p.casm("call", ins);
	ops.append(("call", [ins[0]] + [vrtovn(i) for i in ins[1:]]));
	# the only register you can rely on now is %vr{0,1,2,3} (not even the registers
	# from moves)
	after_call();
