
def process_data(t, p):
	if (t.token == ".data"):
		p.printf(".data", prefix = "");
		p.indent();
		while True:
			token = next(t);
			if token == ".string":
				label = next(t);
				assert(next(t) == ',');
				literal = next(t);
				p.printf("%8s %16s, %s", ".string", label, literal);
			elif token == ".float":
				assert(not "TODO");
			elif token == ".global":
				assert(not "TODO");
			else:
				break;
		p.unindent();
