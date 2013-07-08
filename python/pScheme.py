DEBUG = False 
isa = isinstance
Symbol = str

class Env(dict):

	"an environment : a dict of {'var':val} pairs,with an outer Env"
	def __init__(self,parms=(),args=(),outer=None):
		self.update(zip(parms,args))	
		self.outer=outer

	def find(self,var):
		"find the innermost Env where var appears"
		return self if var in self else self.outer.find(var)

def add_globals(env):
	"add some scheme standard procedures to an environment"
	import math,operator as op
	env.update(vars(math))
	env.update(
		{'+':op.add,'-':op.sub,'*':op.mul,'/':op.div,'not':op.not_,
		'>':op.gt,'<':op.lt}
		)
	return env

global_env = add_globals(Env())

def eval(x,env=global_env):
	"evaluate an expression in an 	environment."
	method_name = 'eval'	

	if DEBUG :
		print '[DEBUG--',method_name,']::',x

	if isa(x,Symbol):
		return env.find(x)[x]
	elif not isa(x,list):
		return x
	elif x[0] == 'quote':
		(_,exp) = x 
		return exp
	elif x[0] == 'if':
		(_,test,conseq,alt) = x
		return eval((conseq if eval(test,env) else alt),alt)
	elif x[0] == 'set!':
		(_,var,exp) = x
		env.find(var)[var] = eval(exp,env)
	elif x[0] == 'define':
		(_,var,exp) = x
		env[var] = eval(exp,env)
	elif x[0] == 'lambda':
		(_,vars,exp) = x
		return lambda *args:eval(exp,Env(vars,args,env))
	elif x[0] == 'begin':
		for exp in x[1:]:
			val = eval(exp,env)
		return val
	else:
		exps = [eval(exp,env) for exp in x]
		proc = exps.pop(0)
		return proc(*exps)


def read(s):
	"read a scheme expression from a string"
	return read_from(tokenize(s))

def tokenize(s):
	"convert a string into a list of tokens"
	return s.replace('(',' ( ').replace(')',' ) ').split()

def read_from(tokens):
	"read an expression from  a sequence of tokens"

	if DEBUG:
		print  '[DEBUG] ::',tokens

	if len(tokens) == 0:
		raise SyntaxError('unexpected EOF while reading')
	token = tokens.pop(0) 
	if '(' == token:
		L=[]
		while tokens[0] != ')' :
			L.append(read_from(tokens))
		tokens.pop(0)
		return L
	elif ')' == token:
		raise SyntaxError('unexpected )')
	else:
		return atom(token)

def atom(token):
	"numbers become numbers;every other token is a symbol"
	t1 = 'hello'
	try: return int(token)
	except ValueError:
		try : return float(token)
		except ValueError:
			return Symbol(token)


def to_string(exp):
	"convert a python object back into a lisp-readable string"
	return '(' + ' '.join(map(to_string,exp))+')' if isa(exp,list) else str(exp)


def repl(propmt='lis.py>'):
	"a propmt-read-eval-print loop"
	while True:
		val = eval(parse(raw_input(propmt)))
		if val is not None : print to_string(val)
if __name__ == '__main__':

	parse = read
	repl()



