# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#decls.
    def visitDecls(self, ctx:D96Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classNormal.
    def visitClassNormal(self, ctx:D96Parser.ClassNormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_bodys.
    def visitClass_bodys(self, ctx:D96Parser.Class_bodysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_body.
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_decl.
    def visitVariable_decl(self, ctx:D96Parser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#const_decl.
    def visitConst_decl(self, ctx:D96Parser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_decl.
    def visitAttribute_decl(self, ctx:D96Parser.Attribute_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_name.
    def visitList_name(self, ctx:D96Parser.List_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#name_att.
    def visitName_att(self, ctx:D96Parser.Name_attContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_exp.
    def visitList_exp(self, ctx:D96Parser.List_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_decl.
    def visitMethod_decl(self, ctx:D96Parser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter.
    def visitParameter(self, ctx:D96Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifer_list.
    def visitIdentifer_list(self, ctx:D96Parser.Identifer_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#normal.
    def visitNormal(self, ctx:D96Parser.NormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stm.
    def visitBlock_stm(self, ctx:D96Parser.Block_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statements.
    def visitStatements(self, ctx:D96Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_declmethod.
    def visitVariable_declmethod(self, ctx:D96Parser.Variable_declmethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#const_declmethod.
    def visitConst_declmethod(self, ctx:D96Parser.Const_declmethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_namemethod.
    def visitList_namemethod(self, ctx:D96Parser.List_namemethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_method.
    def visitInstance_method(self, ctx:D96Parser.Instance_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_method.
    def visitStatic_method(self, ctx:D96Parser.Static_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_access.
    def visitMember_access(self, ctx:D96Parser.Member_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operators.
    def visitIndex_operators(self, ctx:D96Parser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx:D96Parser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr11.
    def visitExpr11(self, ctx:D96Parser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operand.
    def visitOperand(self, ctx:D96Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignment_statement.
    def visitAssignment_statement(self, ctx:D96Parser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_statement.
    def visitIf_statement(self, ctx:D96Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseStmt.
    def visitElseStmt(self, ctx:D96Parser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elif_stm.
    def visitElif_stm(self, ctx:D96Parser.Elif_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_stm.
    def visitElse_stm(self, ctx:D96Parser.Else_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#foreach_stmt.
    def visitForeach_stmt(self, ctx:D96Parser.Foreach_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#cont_stmt.
    def visitCont_stmt(self, ctx:D96Parser.Cont_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typ_var.
    def visitTyp_var(self, ctx:D96Parser.Typ_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array.
    def visitArray(self, ctx:D96Parser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#intlit.
    def visitIntlit(self, ctx:D96Parser.IntlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#boolit.
    def visitBoolit(self, ctx:D96Parser.BoolitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arraylit.
    def visitArraylit(self, ctx:D96Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#iar.
    def visitIar(self, ctx:D96Parser.IarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#aints.
    def visitAints(self, ctx:D96Parser.AintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#afloats.
    def visitAfloats(self, ctx:D96Parser.AfloatsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#astrings.
    def visitAstrings(self, ctx:D96Parser.AstringsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#asbools.
    def visitAsbools(self, ctx:D96Parser.AsboolsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#marraylists.
    def visitMarraylists(self, ctx:D96Parser.MarraylistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mar.
    def visitMar(self, ctx:D96Parser.MarContext):
        return self.visitChildren(ctx)



del D96Parser