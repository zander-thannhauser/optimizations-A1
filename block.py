
from stdio import printf;

from lookup import new_block_numbering, vrtogvn_lookup;

# Integer Arithmetic Instructions:
from instruction.process_i2i      import process_i2i;
from instruction.process_add      import process_add;
from instruction.process_sub      import process_sub;
from instruction.process_mult     import process_mult;
from instruction.process_lshift   import process_lshift;
from instruction.process_rshift   import process_rshift;
from instruction.process_mod      import process_mod;
from instruction.process_and      import process_and;
from instruction.process_or       import process_or;
from instruction.process_not      import process_not;
from instruction.process_addI     import process_addI;
from instruction.process_subI     import process_subI;
from instruction.process_multI    import process_multI;
from instruction.process_lshiftI  import process_lshiftI;
from instruction.process_rshiftI  import process_rshiftI;

# Integer Memory Operations:
from instruction.process_loadI    import process_loadI;
from instruction.process_load     import process_load;
from instruction.process_loadAI   import process_loadAI;
from instruction.process_loadAO   import process_loadAO;
from instruction.process_store    import process_store;
from instruction.process_storeAI  import process_storeAI;
from instruction.process_storeAO  import process_storeAO;

# Compare Instructions:
from instruction.process_cmp_LT   import process_cmp_LT;
from instruction.process_cmp_LE   import process_cmp_LE;
from instruction.process_cmp_GT   import process_cmp_GT;
from instruction.process_cmp_GE   import process_cmp_GE;
from instruction.process_cmp_EQ   import process_cmp_EQ;
from instruction.process_cmp_NE   import process_cmp_NE;
from instruction.process_comp     import process_comp;
from instruction.process_testeq   import process_testeq;
from instruction.process_testne   import process_testne;
from instruction.process_testgt   import process_testgt;
from instruction.process_testge   import process_testge;
from instruction.process_testlt   import process_testlt;
from instruction.process_testle   import process_testle;

# Floating-point Operations:
from instruction.process_f2i      import process_f2i;
from instruction.process_i2f      import process_i2f;
from instruction.process_f2f      import process_f2f;
from instruction.process_fadd     import process_fadd;
from instruction.process_fsub     import process_fsub;
from instruction.process_fmult    import process_fmult;
from instruction.process_fdiv     import process_fdiv;
from instruction.process_fcomp    import process_fcomp;
from instruction.process_fload    import process_fload;
from instruction.process_floadAI  import process_floadAI;
from instruction.process_floadAO  import process_floadAO;
from instruction.process_fstore   import process_fstore;
from instruction.process_fstoreAI import process_fstoreAI;
from instruction.process_fstoreAO import process_fstoreAO;

# I/O Instructions:
from instruction.process_fread    import process_fread;
from instruction.process_iread    import process_iread;
from instruction.process_fwrite   import process_fwrite;
from instruction.process_iwrite   import process_iwrite;
from instruction.process_swrite   import process_swrite;

# Branch Instructions:
from instruction.process_jumpI    import process_jumpI;
from instruction.process_jump     import process_jump;
from instruction.process_ret      import process_ret;
from instruction.process_cbr      import process_cbr;
from instruction.process_cbrne    import process_cbrne;
from instruction.process_cbr_LT   import process_cbr_LT;
from instruction.process_cbr_LE   import process_cbr_LE;
from instruction.process_cbr_GT   import process_cbr_GT;
from instruction.process_cbr_GE   import process_cbr_GE;
from instruction.process_cbr_EQ   import process_cbr_EQ;
from instruction.process_cbr_NE   import process_cbr_NE;

# Stack Operations:

# Undocumented:
from instruction.process_nop      import process_nop;
from instruction.process_call     import process_call;

lookup = {
	# Integer Arithmetic Instructions:
	"i2i":     process_i2i,
	"add":     process_add,
	"sub":     process_sub,
	"mult":    process_mult,
	"lshift":  process_lshift,
	"rshift":  process_rshift,
	"mod":     process_mod,
	"and":     process_and,
	"or":      process_or,
	"not":     process_not,
	"addI":    process_addI,
	"subI":    process_subI,
	"multI":   process_multI,
	"lshiftI": process_lshiftI,
	"rshiftI": process_rshiftI,
	
	# Integer Memory Operations:
	"loadI":   process_loadI,
	"load":    process_load,
	"loadAI":  process_loadAI,
	"loadAO":  process_loadAO,
	"store":   process_store,
	"storeAI": process_storeAI,
	"storeAO": process_storeAO,
	
	# Compare Instructions:
	"cmp_LT": process_cmp_LT,
	"cmp_LE": process_cmp_LE,
	"cmp_GT": process_cmp_GT,
	"cmp_GE": process_cmp_GE,
	"cmp_EQ": process_cmp_EQ,
	"cmp_NE": process_cmp_NE,
	"comp": process_comp,
	"testeq": process_testeq,
	"testne": process_testne,
	"testgt": process_testgt,
	"testge": process_testge,
	"testlt": process_testlt,
	"testle": process_testle,
	
	# Floating-point Operations:
	"f2i": process_f2i,
	"i2f": process_i2f,
	"f2f": process_f2f,
	"fadd": process_fadd,
	"fsub": process_fsub,
	"fmult": process_fmult,
	"fdiv": process_fdiv,
	"fcomp": process_fcomp,
	"fload": process_fload,
	"floadAI": process_floadAI,
	"fstore": process_fstore,
	"fstoreAI": process_fstoreAI,
	"fstoreAO": process_fstoreAO,
	
	# I/O Instructions:
	"fread": process_fread,
	"iread": process_iread,
	"fwrite": process_fwrite,
	"iwrite": process_iwrite,
	"swrite": process_swrite,
	
	# Branch Instructions:
	"jumpI": process_jumpI,
	"jump": process_jump,
	"ret": process_ret,
	"cbr": process_cbr,
	"cbrne": process_cbrne,
	"cbr_LT": process_cbr_LT,
	"cbr_LE": process_cbr_LE,
	"cbr_GT": process_cbr_GT,
	"cbr_GE": process_cbr_GE,
	"cbr_EQ": process_cbr_EQ,
	"cbr_NE": process_cbr_NE,
	
	# Stack Instructions:
	
	# Undocumented:
	"nop": process_nop,
	"call": process_call,
}

def process_block(t, p):
	new_block_numbering();
	
	# (cmd[, ins[, arrow[, outs]])
	
	operations = []
	
	while t.token in lookup:
		ins = []
		outs = []
		operation = t.token;
		printf("operation == \"%s\"\n", operation);
		t.next();
		if operation not in ["ret", "nop"]:
			ins.append(t.token);
			t.next();
			while t.token == ',':
				t.next();
				ins.append(t.token);
				t.next();
			if operation not in ["iwrite", "fwrite", "swrite", "call"]:
				# printf("t.token == \"%s\"\n", t.token);
				assert(t.token in ["->", "=>"]);
				t.next();
				outs.append(t.token);
				t.next();
				while t.token == ',':
					t.next();
					outs.append(t.token);
					t.next();
		print(operation, ins, outs);
		lookup[operation](operations, ins, outs);
	
	#for o in operations:
	#	print(o);
	#assert(not "CHECK");
	
	vns = set();
	
	print("vrtogvn_lookup.values() ==", vrtogvn_lookup.values());
	
	# (prefix, operation)
	outgoing_operations = []
	
	for operation in operations[::-1]:
		print(operation);
		print(vns);
		
		def clean(a):
			for i, s in enumerate(a):
				if type(s) is int:
					a[i] = str(s);
				elif ":" in s:
					a[i] = a[i][:a[i].index(":")];
		
		clean(operation[1]);
		
		clean(operation[3]);
		
		# if your arrow is a '->': you stay
		# or if you're one of the stores: you stay
		# or if any of your outs is in vrtogvn.values(): you stay
		# or if one of your outs is in list of used value numbers: you stay
		if operation[0].startswith("store"):
			prefix = "  "
			for i in operation[1]:
				vns.add(i);
			for i in operation[3]:
				vns.add(i);
			# assert(not "CHECK");
		elif False \
			or (operation[2] != "=>") \
			or (any(out in vrtogvn_lookup.values() for out in operation[3])) \
			or (any(out in vns for out in operation[3])):
			prefix = "  "
			
			# all of your ins (that are strings) are added to vns:
			for i in operation[1]:
				vns.add(i);
			
			print("kept");
		else:
			prefix = "# "
			print("skipped");
		
		# print(prefix, operation);
		outgoing_operations.insert(0, (prefix, operation))
	
	for o in outgoing_operations:
		print(o[1]);
		p.asm(*o[1], prefix = o[0]);
	
	# assert(not "CHECK");

























