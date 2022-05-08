
"""
 * @author nhphung
"""
from cgitb import reset
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value


class GetEnv(BaseVisitor, Utils):

    def __init__(self):
        self.globalEnv = {}

    def visitProgram(self, ctx: Program, o: object):
        o = self.globalEnv
        for x in ctx.decl:
            self.visit(x, o)
        return o

    def visitClassDecl(self, ast: ClassDecl, o: object):
        name = ast.classname.name
        if o.get(name) is not None:
            raise Redeclared(Class(), name)
        o[name] = {}
        for x in ast.memlist:
            self.visit(x, o[name])

    def visitAttributeDecl(self, ast: AttributeDecl, o: object):
        if type(ast.kind) is Instance:
            self.visit(ast.decl, ('instance', o))
        if type(ast.kind) is Static:
            self.visit(ast.decl, ('static', o))

    def visitVarDecl(self, ctx: VarDecl, o: object):
        kind, env = o
        name = ctx.variable.name
        if env.get(name) is not None:
            raise Redeclared(Attribute(), name)
        env[name] = ('mutable', self.visit(ctx.varType, env), kind)
        return('mutable', self.visit(ctx.varType, env), kind)

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        kind, env = o
        
        name = ctx.constant.name
        if env.get(name) is not None:
            raise Redeclared(Attribute(), name)
        env[name] = ('immutable', self.visit(ctx.constType, env), kind)

    def visitMethodDecl(self, ctx: MethodDecl, o: object):
        if type(ctx.kind) is Instance:
            kind = 'instance'
        if type(ctx.kind) is Static:
            kind = 'static'
        if o.get(ctx.name.name) is not None:
            if len(ctx.param)!=len(o[ctx.name.name][3]):
                raise Redeclared(Method(), ctx.name.name)
        params = ctx.param
        # if ctx.returnType is not None:
        #     param = list(map(lambda x: self.visit(x, (None, {})), params))
        #     o[ctx.name.name] = ('method', self.visit(
        #         ctx.returnType, o), kind, param)
        # else:
        param = list(map(lambda x: self.visit(x, (None, {})), params))
        o[ctx.name.name] = ('method', None, kind, param)

    def visitIntType(self, ast, param):
        return IntType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitVoidType(self, ast, param):
        return VoidType()

    def visitArrayType(self, ast, param):
        return ast

    def visitClassType(self, ast, param):
        env = self.globalEnv
        if ast.classname.name in env:
            return ClassType(ast.classname)
        raise Undeclared(Class(), ast.classname.name)

class ExpUtils:
    @ staticmethod
    def isNaNType(expType):
        return type(expType) not in [IntType, FloatType]

    @ staticmethod
    def isNotConst(expType):
        return type(expType) in [CallExpr, NewExpr, ArrayCell, ArrayType]

    @ staticmethod
    def isNotAccess(expType):
        return type(expType) not in [CallExpr, FieldAccess, CallStmt]

class StaticChecker(BaseVisitor, Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self,ast):
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast:Program, o): 
        env = GetEnv().visit(ast, None)
        print(env)
        result=[self.visit(x, env) for x in ast.decl]
        
        return result
        
        

    def visitId(self,ast:Id,o):
        if type(o) is tuple:
            checkConst, env = o
        else:
            env = o
        if env.get('local') is not None:
            for local in env['local']:
                if ast.name in local:
                    return local[ast.name]
        if ast.name in env['global'][env['current']]:
            return env['global'][env['current']][ast.name]
        if env['parent'] is not None:
            if ast.name in env['global'][env['parent']]:
                return env['global'][env['parent']][ast.name]
        raise Undeclared(Identifier(), ast.name)

    def visitBinaryOp(self,ast:BinaryOp,c):
        pass

    def visitUnaryOp(self,ast:UnaryOp,c):
        pass
    

    def visitCallExpr(self, ast:CallExpr, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype

    def visitNewExpr(self,ast:NewExpr,c):
        pass

    def visitArrayCell(self,ast:ArrayCell,c):
        pass

    def visitFieldAccess(self,ast:FieldAccess,c):
        pass

    def visitIntLiteral(self, ast, param):
        return (None, IntType(), None)

    def visitFloatLiteral(self, ast, param):
        return (None, FloatType(), None)

    def visitBooleanLiteral(self, ast, param):
        return (None, BoolType(), None)

    def visitStringLiteral(self, ast, param):
        return (None, StringType(), None)

    def visitNullLiteral(self, ast, param):
        return (None, NullLiteral(), None)

    def visitSelfLiteral(self, ast, param):
        return (None, SelfLiteral(), None)  


    def visitAssign(self,ast, o): 
        inLoop, env = o
        lhs = self.visit(ast.lhs, env)
        exp = self.visit(ast.exp, env)

        kindlhs = lhs[0]
        typeLhs = lhs[1]
        typeExp = exp[1]
        if kindlhs == 'const' or kindlhs == 'immutable':
            raise CannotAssignToConstant(ast)
        if lhs[0] == 'mutable' or lhs[0] == 'immutable' or lhs[0] == 'method':
            if ExpUtils.isNotAccess(ast.lhs):
                raise Undeclared(Identifier(), ast.lhs.name)
        if exp[0] == 'mutable' or exp[0] == 'immutable' or exp[0] == 'method':
            if ExpUtils.isNotAccess(ast.exp):
                raise Undeclared(Identifier(), ast.exp.name)
        if type(typeLhs) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(typeLhs) is ArrayType and type(typeExp) is ArrayType:
            if typeLhs.size != typeExp.size:
                raise TypeMismatchInStatement(ast)
            if type(typeLhs.eleType) is not type(typeExp.eleType):
                if not (type(typeLhs.eleType) is FloatType and type(typeExp.eleType) is IntType):
                    raise TypeMismatchInStatement(ast)
        if not ((type(typeLhs) is type(typeExp)) or (type(typeLhs) is FloatType and type(typeExp) is IntType)):
            raise TypeMismatchInStatement(ast)

    def visitIf(self,ast, c): 
        pass

    def visitFor(self,ast, c): 
        pass

    def visitBreak(self,ast, o): 
        inLoop, env = o
        if not inLoop:
            raise MustInLoop(ast)

    def visitContinue(self,ast, c): 
        pass

    def visitReturn(self,ast, c): 
        pass

    def visitCallStmt(self,ast, c): 
        pass

    def visitVarDecl(self,ast:VarDecl, o:object): 
        kind, env = o
        name = ast.variable.name
        
        typeOfVar = self.visit(ast.varType, env)
        if ast.varInit is not None:
            value = self.visit(ast.varInit, env)
            if value[0] == 'mutable' or value[0] == 'immutable' or value[0] == 'method':
                if ExpUtils.isNotAccess(ast.varInit):
                    raise Undeclared(Identifier(), ast.varInit.name)
        if env.get('local') is not None:
            if env['local'][0].get(name) is not None:
                raise Redeclared(kind, name)
            env['local'][0][name] = ('var', typeOfVar, None)

    def visitBlock(self,ast, o): 
        inLoop, env1 = o
        env = {}
        env['global'] = env1['global']
        env['local'] = [{}]+env1['local']
        env['current'] = env1['current']
        env['parent'] = env1['parent']
        inst = ast.inst
        
        for decl in inst:

            if type(decl) is VarDecl:
                print(123)
                self.visit(decl, (Variable(), env))
            elif type(decl) is ConstDecl:
                self.visit(decl, (Constant(), env))
            else:

                [self.visit(stmt, (inLoop, env)) for stmt in decl]

    def visitConstDecl(self,ast, o): 
        kind, env = o
        name = ast.constant.name
        if ast.value is None:
            raise IllegalConstantExpression(ast.value)
        if ExpUtils.isNotConst(ast.value):
            raise IllegalConstantExpression(ast.value)
        
        valueCheck = self.visit(ast.value, (True, env))
        
        if valueCheck[0] == 'mutable' or valueCheck[0] == 'immutable' or valueCheck[0] == 'method':
            if ExpUtils.isNotAccess(ast.value):
                raise Undeclared(Identifier(), ast.value.name)
        if valueCheck[0] == 'var' or valueCheck[0] == 'mutable':
            raise IllegalConstantExpression(ast.value)
        value = self.visit(ast.value, env)[1]
        typeOfConst = self.visit(ast.constType, o)
        if env.get('local') is not None:
            if env['local'][0].get(name) is not None:

                raise Redeclared(kind, name)
        if type(typeOfConst) is ArrayType and type(value) is ArrayType:
            if typeOfConst.size != value.size:
                raise TypeMismatchInConstant(ast)
            if type(typeOfConst.eleType) is not type(value.eleType):
                if not (type(typeOfConst.eleType) is FloatType and type(value.eleType) is IntType):
                    raise TypeMismatchInConstant(ast)
        if type(value) is not type(typeOfConst):
            if not (type(typeOfConst) is FloatType and type(value) is IntType):
                raise TypeMismatchInConstant(ast)
        if env.get('local') is not None:
            env['local'][0][name] = ('const', typeOfConst, None)

    def visitClassDecl(self,ast:ClassDecl, o): 
        env = {}
        env['current'] = ast.classname.name
        env['global'] = o
        # env['local'] = [{}]
        if ast.parentname is not None:
            if env['global'].get(ast.parentname.name) is not None:
                env['parent'] = ast.parentname.name
            else:
                raise Undeclared(Class(), ast.parentname.name)
        else:
            env['parent'] = None
        for x in ast.memlist:
            self.visit(x, env)
    def visitMethodDecl(self,ast:MethodDecl, o): 
        env = {}
        env['global'] = o['global']
        env['local'] = [{}]
        env['current'] = o['current']
        env['parent'] = o['parent']
        print(ast.param)
        [self.visit(param, (Parameter(), env)) 
            for param in ast.param]
        inst = ast.body.inst

        # stmts = ast.body.stmt
        for x in inst:
            
            if type(x) is VarDecl:
                self.visit(x, (Variable(), env))
            elif type(x) is ConstDecl:
                
                self.visit(x, (Constant(), env))
        # for stmt in stmts:
            elif type(x) is not Return:
                self.visit(x, (False, env))
            else:
                typeMethod = self.visit(ast.returnType, o)
                self.visit(x, (typeMethod, env))

    def visitAttributeDecl(self,ast, c): 
        pass

    def visitIntType(self, ast, param):
        return IntType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitVoidType(self, ast, param):
        return VoidType()

    def visitArrayType(self, ast, param):
        return ast

    def visitClassType(self,ast, o): 
        env = o
        if ast.classname.name in env['global']:
            return ast
        raise Undeclared(Class(), ast.classname.name)


