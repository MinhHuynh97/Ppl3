import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
#     def test_undeclared_function(self):
#         """Simple program: int main() {} """
#         input = Program(
#     [
#         ClassDecl(
#             Id("Program"),
#             [
#                 MethodDecl(
#                     Static(),
#                     Id("main"),
#                     [],
#                     Block([])
#                 ),
#                 AttributeDecl(
#                     Instance(),
#                     VarDecl(
#                         Id("myVar"),
#                         StringType(),
#                         StringLiteral("Hello World")
#                     )
#                 ),
#                 AttributeDecl(
#                     Instance(),
#                     VarDecl(
#                         Id("myVar"),
#                         IntType()
#                     )
#                 )
#             ]
#         )
#     ]
# )
        
#         expect = "Redeclared Attribute: myVar"
#         self.assertTrue(TestChecker.test(input,expect,400))

#     def test_diff_numofparam_stmt(self):
#         """More complex program"""
#         input = Program(
#     [
#         ClassDecl(
#             Id("Program"),
#             [
#                 MethodDecl(
#                     Static(),
#                     Id("main"),
#                     [],
#                     Block(
#                         [
#                             Assign(
#                                 Id("myVar"),
#                                 IntLiteral(10)
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#     ]
# )
#         expect = "Undeclared Identifier: myVar"
#         self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """
                Class Program{
                    Var k:Float=1.1;
                    main(m,b:Int){
                        
                    }
                    main(x,y : Int) {
                        Var x :Int=1;
                    }
                }
                Class notAProgram{
                    main() {}
                }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(myVar),IntLit(10))"
        self.assertTrue(TestChecker.test(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],IntType(),Block([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([ClassDecl(Id("myCla46"),[MethodDecl(Id("myMetd46"),Instance,[],Block([ConstDecl(Id("x"),IntType,IntLit(1))]))])])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    