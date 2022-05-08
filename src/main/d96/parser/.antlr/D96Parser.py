# Generated from /Users/minh/Downloads/initial/src/main/d96/parser/D96.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0263\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u0088\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u008f\n\4")
        buf.write("\3\4\3\4\3\4\5\4\u0094\n\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u009c\n\5\3\6\3\6\5\6\u00a0\n\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\5\7\u00a9\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\5\b\u00b4\n\b\3\b\3\b\3\t\3\t\5\t\u00ba\n\t\3\n\3\n")
        buf.write("\3\n\3\n\5\n\u00c0\n\n\3\13\3\13\3\f\3\f\5\f\u00c6\n\f")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u00cc\n\f\5\f\u00ce\n\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u00d6\n\r\3\r\3\r\5\r\u00da\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00e6")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00ed\n\17\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\5\21\u00f5\n\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\5\23\u0102\n")
        buf.write("\23\3\23\3\23\3\24\3\24\3\24\3\24\5\24\u010a\n\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0116")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u011f\n")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u012a\n\27\3\27\3\27\3\30\3\30\3\30\3\30\5\30\u0132\n")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u013a\n\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0144\n\32\3")
        buf.write("\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u014e\n\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0159")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u0160\n\35\3\36\3")
        buf.write("\36\3\36\3\36\3\36\5\36\u0167\n\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\7\37\u016f\n\37\f\37\16\37\u0172\13\37\3 \3")
        buf.write(" \3 \3 \3 \3 \7 \u017a\n \f \16 \u017d\13 \3!\3!\3!\3")
        buf.write("!\3!\3!\7!\u0185\n!\f!\16!\u0188\13!\3\"\3\"\3\"\5\"\u018d")
        buf.write("\n\"\3#\3#\3#\5#\u0192\n#\3$\3$\3$\3$\3$\7$\u0199\n$\f")
        buf.write("$\16$\u019c\13$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5")
        buf.write("%\u01aa\n%\3%\7%\u01ad\n%\f%\16%\u01b0\13%\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\5&\u01bb\n&\3&\3&\5&\u01bf\n&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\5\'\u01c6\n\'\3\'\3\'\5\'\u01ca\n\'\3(\3")
        buf.write("(\3(\3(\3(\5(\u01d1\n(\3)\3)\3)\3)\5)\u01d7\n)\3*\3*\3")
        buf.write("*\3*\3*\5*\u01de\n*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\5,\u01ec\n,\3-\3-\3-\3-\3-\5-\u01f3\n-\3.\3.\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\5\60\u0207\n\60\3\60\3\60\3\60\3\61\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\63\3\63\3\63\5\63\u0215\n\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u021f\n\64\3\65\3")
        buf.write("\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\38\3")
        buf.write("8\39\39\59\u0230\n9\3:\3:\3:\3:\3:\3:\3:\5:\u0239\n:\3")
        buf.write(":\3:\3;\3;\3;\3;\3;\5;\u0242\n;\3<\3<\3<\3<\5<\u0248\n")
        buf.write("<\3=\3=\3=\3=\5=\u024e\n=\3>\3>\3>\3>\3>\5>\u0255\n>\3")
        buf.write("?\3?\3?\3?\3?\5?\u025c\n?\3@\3@\3@\3@\3@\3@\2\7<>@FHA")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\2\n\3\2>?")
        buf.write("\3\2-.\4\2&&(,\3\2$%\3\2\36\37\3\2 \"\3\2:;\3\2\3\4\2")
        buf.write("\u0273\2\u0080\3\2\2\2\4\u0087\3\2\2\2\6\u0089\3\2\2\2")
        buf.write("\b\u009b\3\2\2\2\n\u009f\3\2\2\2\f\u00a1\3\2\2\2\16\u00ac")
        buf.write("\3\2\2\2\20\u00b9\3\2\2\2\22\u00bf\3\2\2\2\24\u00c1\3")
        buf.write("\2\2\2\26\u00cd\3\2\2\2\30\u00d9\3\2\2\2\32\u00e5\3\2")
        buf.write("\2\2\34\u00ec\3\2\2\2\36\u00ee\3\2\2\2 \u00f0\3\2\2\2")
        buf.write("\"\u00f9\3\2\2\2$\u00fe\3\2\2\2&\u0109\3\2\2\2(\u0115")
        buf.write("\3\2\2\2*\u0117\3\2\2\2,\u0122\3\2\2\2.\u0131\3\2\2\2")
        buf.write("\60\u0133\3\2\2\2\62\u013d\3\2\2\2\64\u014d\3\2\2\2\66")
        buf.write("\u0158\3\2\2\28\u015f\3\2\2\2:\u0166\3\2\2\2<\u0168\3")
        buf.write("\2\2\2>\u0173\3\2\2\2@\u017e\3\2\2\2B\u018c\3\2\2\2D\u0191")
        buf.write("\3\2\2\2F\u0193\3\2\2\2H\u019d\3\2\2\2J\u01be\3\2\2\2")
        buf.write("L\u01c9\3\2\2\2N\u01d0\3\2\2\2P\u01d6\3\2\2\2R\u01dd\3")
        buf.write("\2\2\2T\u01df\3\2\2\2V\u01e4\3\2\2\2X\u01f2\3\2\2\2Z\u01f4")
        buf.write("\3\2\2\2\\\u01fa\3\2\2\2^\u01fd\3\2\2\2`\u020b\3\2\2\2")
        buf.write("b\u020e\3\2\2\2d\u0211\3\2\2\2f\u021e\3\2\2\2h\u0220\3")
        buf.write("\2\2\2j\u0222\3\2\2\2l\u0229\3\2\2\2n\u022b\3\2\2\2p\u022f")
        buf.write("\3\2\2\2r\u0231\3\2\2\2t\u0241\3\2\2\2v\u0247\3\2\2\2")
        buf.write("x\u024d\3\2\2\2z\u0254\3\2\2\2|\u025b\3\2\2\2~\u025d\3")
        buf.write("\2\2\2\u0080\u0081\5\4\3\2\u0081\u0082\7\2\2\3\u0082\3")
        buf.write("\3\2\2\2\u0083\u0084\5\6\4\2\u0084\u0085\5\4\3\2\u0085")
        buf.write("\u0088\3\2\2\2\u0086\u0088\5\6\4\2\u0087\u0083\3\2\2\2")
        buf.write("\u0087\u0086\3\2\2\2\u0088\5\3\2\2\2\u0089\u008e\7\22")
        buf.write("\2\2\u008a\u008f\7>\2\2\u008b\u008c\7>\2\2\u008c\u008d")
        buf.write("\7\63\2\2\u008d\u008f\7>\2\2\u008e\u008a\3\2\2\2\u008e")
        buf.write("\u008b\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0093\7\67\2")
        buf.write("\2\u0091\u0094\5\b\5\2\u0092\u0094\3\2\2\2\u0093\u0091")
        buf.write("\3\2\2\2\u0093\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\u0096\78\2\2\u0096\7\3\2\2\2\u0097\u0098\5\n\6\2\u0098")
        buf.write("\u0099\5\b\5\2\u0099\u009c\3\2\2\2\u009a\u009c\5\n\6\2")
        buf.write("\u009b\u0097\3\2\2\2\u009b\u009a\3\2\2\2\u009c\t\3\2\2")
        buf.write("\2\u009d\u00a0\5\20\t\2\u009e\u00a0\5\30\r\2\u009f\u009d")
        buf.write("\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\13\3\2\2\2\u00a1\u00a2")
        buf.write("\7\24\2\2\u00a2\u00a3\5\22\n\2\u00a3\u00a4\7\63\2\2\u00a4")
        buf.write("\u00a8\5f\64\2\u00a5\u00a6\7\'\2\2\u00a6\u00a9\5\26\f")
        buf.write("\2\u00a7\u00a9\3\2\2\2\u00a8\u00a5\3\2\2\2\u00a8\u00a7")
        buf.write("\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\7\66\2\2\u00ab")
        buf.write("\r\3\2\2\2\u00ac\u00ad\7\23\2\2\u00ad\u00ae\5\22\n\2\u00ae")
        buf.write("\u00af\7\63\2\2\u00af\u00b3\5f\64\2\u00b0\u00b1\7\'\2")
        buf.write("\2\u00b1\u00b4\5\26\f\2\u00b2\u00b4\3\2\2\2\u00b3\u00b0")
        buf.write("\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write("\u00b6\7\66\2\2\u00b6\17\3\2\2\2\u00b7\u00ba\5\f\7\2\u00b8")
        buf.write("\u00ba\5\16\b\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2")
        buf.write("\2\u00ba\21\3\2\2\2\u00bb\u00bc\t\2\2\2\u00bc\u00bd\7")
        buf.write("\65\2\2\u00bd\u00c0\5\22\n\2\u00be\u00c0\t\2\2\2\u00bf")
        buf.write("\u00bb\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0\23\3\2\2\2\u00c1")
        buf.write("\u00c2\t\2\2\2\u00c2\25\3\2\2\2\u00c3\u00c6\58\35\2\u00c4")
        buf.write("\u00c6\7\20\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3\2\2")
        buf.write("\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\7\65\2\2\u00c8\u00ce")
        buf.write("\5\26\f\2\u00c9\u00cc\58\35\2\u00ca\u00cc\7\20\2\2\u00cb")
        buf.write("\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00ce\3\2\2\2")
        buf.write("\u00cd\u00c5\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\27\3\2")
        buf.write("\2\2\u00cf\u00da\5 \21\2\u00d0\u00da\5\"\22\2\u00d1\u00d2")
        buf.write("\t\2\2\2\u00d2\u00d5\7/\2\2\u00d3\u00d6\5\32\16\2\u00d4")
        buf.write("\u00d6\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d4\3\2\2\2")
        buf.write("\u00d6\u00d7\3\2\2\2\u00d7\u00d8\7\60\2\2\u00d8\u00da")
        buf.write("\5$\23\2\u00d9\u00cf\3\2\2\2\u00d9\u00d0\3\2\2\2\u00d9")
        buf.write("\u00d1\3\2\2\2\u00da\31\3\2\2\2\u00db\u00dc\5\34\17\2")
        buf.write("\u00dc\u00dd\7\63\2\2\u00dd\u00de\5f\64\2\u00de\u00df")
        buf.write("\7\66\2\2\u00df\u00e0\5\32\16\2\u00e0\u00e6\3\2\2\2\u00e1")
        buf.write("\u00e2\5\34\17\2\u00e2\u00e3\7\63\2\2\u00e3\u00e4\5f\64")
        buf.write("\2\u00e4\u00e6\3\2\2\2\u00e5\u00db\3\2\2\2\u00e5\u00e1")
        buf.write("\3\2\2\2\u00e6\33\3\2\2\2\u00e7\u00e8\5\24\13\2\u00e8")
        buf.write("\u00e9\7\65\2\2\u00e9\u00ea\5\34\17\2\u00ea\u00ed\3\2")
        buf.write("\2\2\u00eb\u00ed\5\24\13\2\u00ec\u00e7\3\2\2\2\u00ec\u00eb")
        buf.write("\3\2\2\2\u00ed\35\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\37")
        buf.write("\3\2\2\2\u00f0\u00f1\7\30\2\2\u00f1\u00f4\7/\2\2\u00f2")
        buf.write("\u00f5\5\32\16\2\u00f3\u00f5\3\2\2\2\u00f4\u00f2\3\2\2")
        buf.write("\2\u00f4\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7")
        buf.write("\7\60\2\2\u00f7\u00f8\5$\23\2\u00f8!\3\2\2\2\u00f9\u00fa")
        buf.write("\7\31\2\2\u00fa\u00fb\7/\2\2\u00fb\u00fc\7\60\2\2\u00fc")
        buf.write("\u00fd\5$\23\2\u00fd#\3\2\2\2\u00fe\u0101\7\67\2\2\u00ff")
        buf.write("\u0102\5&\24\2\u0100\u0102\3\2\2\2\u0101\u00ff\3\2\2\2")
        buf.write("\u0101\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\7")
        buf.write("8\2\2\u0104%\3\2\2\2\u0105\u0106\5(\25\2\u0106\u0107\5")
        buf.write("&\24\2\u0107\u010a\3\2\2\2\u0108\u010a\5(\25\2\u0109\u0105")
        buf.write("\3\2\2\2\u0109\u0108\3\2\2\2\u010a\'\3\2\2\2\u010b\u0116")
        buf.write("\5*\26\2\u010c\u0116\5,\27\2\u010d\u0116\5T+\2\u010e\u0116")
        buf.write("\5V,\2\u010f\u0116\5^\60\2\u0110\u0116\5`\61\2\u0111\u0116")
        buf.write("\5b\62\2\u0112\u0116\5d\63\2\u0113\u0116\5$\23\2\u0114")
        buf.write("\u0116\5\64\33\2\u0115\u010b\3\2\2\2\u0115\u010c\3\2\2")
        buf.write("\2\u0115\u010d\3\2\2\2\u0115\u010e\3\2\2\2\u0115\u010f")
        buf.write("\3\2\2\2\u0115\u0110\3\2\2\2\u0115\u0111\3\2\2\2\u0115")
        buf.write("\u0112\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0114\3\2\2\2")
        buf.write("\u0116)\3\2\2\2\u0117\u0118\7\24\2\2\u0118\u0119\5.\30")
        buf.write("\2\u0119\u011a\7\63\2\2\u011a\u011e\5f\64\2\u011b\u011c")
        buf.write("\7\'\2\2\u011c\u011f\5\26\f\2\u011d\u011f\3\2\2\2\u011e")
        buf.write("\u011b\3\2\2\2\u011e\u011d\3\2\2\2\u011f\u0120\3\2\2\2")
        buf.write("\u0120\u0121\7\66\2\2\u0121+\3\2\2\2\u0122\u0123\7\23")
        buf.write("\2\2\u0123\u0124\5.\30\2\u0124\u0125\7\63\2\2\u0125\u0129")
        buf.write("\5f\64\2\u0126\u0127\7\'\2\2\u0127\u012a\5\26\f\2\u0128")
        buf.write("\u012a\3\2\2\2\u0129\u0126\3\2\2\2\u0129\u0128\3\2\2\2")
        buf.write("\u012a\u012b\3\2\2\2\u012b\u012c\7\66\2\2\u012c-\3\2\2")
        buf.write("\2\u012d\u012e\7>\2\2\u012e\u012f\7\65\2\2\u012f\u0132")
        buf.write("\5.\30\2\u0130\u0132\7>\2\2\u0131\u012d\3\2\2\2\u0131")
        buf.write("\u0130\3\2\2\2\u0132/\3\2\2\2\u0133\u0134\58\35\2\u0134")
        buf.write("\u0135\7\64\2\2\u0135\u0136\7>\2\2\u0136\u0139\7/\2\2")
        buf.write("\u0137\u013a\5\26\f\2\u0138\u013a\3\2\2\2\u0139\u0137")
        buf.write("\3\2\2\2\u0139\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b")
        buf.write("\u013c\7\60\2\2\u013c\61\3\2\2\2\u013d\u013e\7>\2\2\u013e")
        buf.write("\u013f\79\2\2\u013f\u0140\7?\2\2\u0140\u0143\7/\2\2\u0141")
        buf.write("\u0144\5\26\f\2\u0142\u0144\3\2\2\2\u0143\u0141\3\2\2")
        buf.write("\2\u0143\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146")
        buf.write("\7\60\2\2\u0146\63\3\2\2\2\u0147\u0148\5\60\31\2\u0148")
        buf.write("\u0149\7\66\2\2\u0149\u014e\3\2\2\2\u014a\u014b\5\62\32")
        buf.write("\2\u014b\u014c\7\66\2\2\u014c\u014e\3\2\2\2\u014d\u0147")
        buf.write("\3\2\2\2\u014d\u014a\3\2\2\2\u014e\65\3\2\2\2\u014f\u0150")
        buf.write("\7\61\2\2\u0150\u0151\58\35\2\u0151\u0152\7\62\2\2\u0152")
        buf.write("\u0153\5\66\34\2\u0153\u0159\3\2\2\2\u0154\u0155\7\61")
        buf.write("\2\2\u0155\u0156\58\35\2\u0156\u0157\7\62\2\2\u0157\u0159")
        buf.write("\3\2\2\2\u0158\u014f\3\2\2\2\u0158\u0154\3\2\2\2\u0159")
        buf.write("\67\3\2\2\2\u015a\u015b\5:\36\2\u015b\u015c\t\3\2\2\u015c")
        buf.write("\u015d\5:\36\2\u015d\u0160\3\2\2\2\u015e\u0160\5:\36\2")
        buf.write("\u015f\u015a\3\2\2\2\u015f\u015e\3\2\2\2\u01609\3\2\2")
        buf.write("\2\u0161\u0162\5<\37\2\u0162\u0163\t\4\2\2\u0163\u0164")
        buf.write("\5<\37\2\u0164\u0167\3\2\2\2\u0165\u0167\5<\37\2\u0166")
        buf.write("\u0161\3\2\2\2\u0166\u0165\3\2\2\2\u0167;\3\2\2\2\u0168")
        buf.write("\u0169\b\37\1\2\u0169\u016a\5> \2\u016a\u0170\3\2\2\2")
        buf.write("\u016b\u016c\f\4\2\2\u016c\u016d\t\5\2\2\u016d\u016f\5")
        buf.write("> \2\u016e\u016b\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e")
        buf.write("\3\2\2\2\u0170\u0171\3\2\2\2\u0171=\3\2\2\2\u0172\u0170")
        buf.write("\3\2\2\2\u0173\u0174\b \1\2\u0174\u0175\5@!\2\u0175\u017b")
        buf.write("\3\2\2\2\u0176\u0177\f\4\2\2\u0177\u0178\t\6\2\2\u0178")
        buf.write("\u017a\5@!\2\u0179\u0176\3\2\2\2\u017a\u017d\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c?\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017e\u017f\b!\1\2\u017f\u0180\5B\"\2\u0180")
        buf.write("\u0186\3\2\2\2\u0181\u0182\f\4\2\2\u0182\u0183\t\7\2\2")
        buf.write("\u0183\u0185\5B\"\2\u0184\u0181\3\2\2\2\u0185\u0188\3")
        buf.write("\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187A")
        buf.write("\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\7#\2\2\u018a")
        buf.write("\u018d\5B\"\2\u018b\u018d\5D#\2\u018c\u0189\3\2\2\2\u018c")
        buf.write("\u018b\3\2\2\2\u018dC\3\2\2\2\u018e\u018f\7\37\2\2\u018f")
        buf.write("\u0192\5D#\2\u0190\u0192\5F$\2\u0191\u018e\3\2\2\2\u0191")
        buf.write("\u0190\3\2\2\2\u0192E\3\2\2\2\u0193\u0194\b$\1\2\u0194")
        buf.write("\u0195\5H%\2\u0195\u019a\3\2\2\2\u0196\u0197\f\4\2\2\u0197")
        buf.write("\u0199\5\66\34\2\u0198\u0196\3\2\2\2\u0199\u019c\3\2\2")
        buf.write("\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019bG\3\2")
        buf.write("\2\2\u019c\u019a\3\2\2\2\u019d\u019e\b%\1\2\u019e\u019f")
        buf.write("\5J&\2\u019f\u01ae\3\2\2\2\u01a0\u01a1\f\5\2\2\u01a1\u01a2")
        buf.write("\7\64\2\2\u01a2\u01ad\7>\2\2\u01a3\u01a4\f\4\2\2\u01a4")
        buf.write("\u01a5\7\64\2\2\u01a5\u01a6\7>\2\2\u01a6\u01a9\7/\2\2")
        buf.write("\u01a7\u01aa\5\26\f\2\u01a8\u01aa\3\2\2\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01a9\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab")
        buf.write("\u01ad\7\60\2\2\u01ac\u01a0\3\2\2\2\u01ac\u01a3\3\2\2")
        buf.write("\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af")
        buf.write("\3\2\2\2\u01afI\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2")
        buf.write("\7>\2\2\u01b2\u01b3\79\2\2\u01b3\u01bf\7?\2\2\u01b4\u01b5")
        buf.write("\7>\2\2\u01b5\u01b6\79\2\2\u01b6\u01b7\7?\2\2\u01b7\u01ba")
        buf.write("\7/\2\2\u01b8\u01bb\5\26\f\2\u01b9\u01bb\3\2\2\2\u01ba")
        buf.write("\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2")
        buf.write("\u01bc\u01bf\7\60\2\2\u01bd\u01bf\5L\'\2\u01be\u01b1\3")
        buf.write("\2\2\2\u01be\u01b4\3\2\2\2\u01be\u01bd\3\2\2\2\u01bfK")
        buf.write("\3\2\2\2\u01c0\u01c1\7\25\2\2\u01c1\u01c2\7>\2\2\u01c2")
        buf.write("\u01c5\7/\2\2\u01c3\u01c6\5\26\f\2\u01c4\u01c6\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6\u01c7\3")
        buf.write("\2\2\2\u01c7\u01ca\7\60\2\2\u01c8\u01ca\5N(\2\u01c9\u01c0")
        buf.write("\3\2\2\2\u01c9\u01c8\3\2\2\2\u01caM\3\2\2\2\u01cb\u01cc")
        buf.write("\7/\2\2\u01cc\u01cd\58\35\2\u01cd\u01ce\7\60\2\2\u01ce")
        buf.write("\u01d1\3\2\2\2\u01cf\u01d1\5P)\2\u01d0\u01cb\3\2\2\2\u01d0")
        buf.write("\u01cf\3\2\2\2\u01d1O\3\2\2\2\u01d2\u01d7\7\32\2\2\u01d3")
        buf.write("\u01d7\7\20\2\2\u01d4\u01d7\5\24\13\2\u01d5\u01d7\5R*")
        buf.write("\2\u01d6\u01d2\3\2\2\2\u01d6\u01d3\3\2\2\2\u01d6\u01d4")
        buf.write("\3\2\2\2\u01d6\u01d5\3\2\2\2\u01d7Q\3\2\2\2\u01d8\u01de")
        buf.write("\5l\67\2\u01d9\u01de\7<\2\2\u01da\u01de\5n8\2\u01db\u01de")
        buf.write("\7=\2\2\u01dc\u01de\5p9\2\u01dd\u01d8\3\2\2\2\u01dd\u01d9")
        buf.write("\3\2\2\2\u01dd\u01da\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd")
        buf.write("\u01dc\3\2\2\2\u01deS\3\2\2\2\u01df\u01e0\58\35\2\u01e0")
        buf.write("\u01e1\7\'\2\2\u01e1\u01e2\58\35\2\u01e2\u01e3\7\66\2")
        buf.write("\2\u01e3U\3\2\2\2\u01e4\u01e5\7\7\2\2\u01e5\u01e6\7/\2")
        buf.write("\2\u01e6\u01e7\58\35\2\u01e7\u01e8\7\60\2\2\u01e8\u01eb")
        buf.write("\5$\23\2\u01e9\u01ec\5X-\2\u01ea\u01ec\3\2\2\2\u01eb\u01e9")
        buf.write("\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ecW\3\2\2\2\u01ed\u01ee")
        buf.write("\5Z.\2\u01ee\u01ef\5X-\2\u01ef\u01f3\3\2\2\2\u01f0\u01f3")
        buf.write("\5Z.\2\u01f1\u01f3\5\\/\2\u01f2\u01ed\3\2\2\2\u01f2\u01f0")
        buf.write("\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3Y\3\2\2\2\u01f4\u01f5")
        buf.write("\7\b\2\2\u01f5\u01f6\7/\2\2\u01f6\u01f7\58\35\2\u01f7")
        buf.write("\u01f8\7\60\2\2\u01f8\u01f9\5$\23\2\u01f9[\3\2\2\2\u01fa")
        buf.write("\u01fb\7\t\2\2\u01fb\u01fc\5$\23\2\u01fc]\3\2\2\2\u01fd")
        buf.write("\u01fe\7\n\2\2\u01fe\u01ff\7/\2\2\u01ff\u0200\t\2\2\2")
        buf.write("\u0200\u0201\7\27\2\2\u0201\u0202\58\35\2\u0202\u0203")
        buf.write("\7\33\2\2\u0203\u0206\58\35\2\u0204\u0205\7\21\2\2\u0205")
        buf.write("\u0207\58\35\2\u0206\u0204\3\2\2\2\u0206\u0207\3\2\2\2")
        buf.write("\u0207\u0208\3\2\2\2\u0208\u0209\7\60\2\2\u0209\u020a")
        buf.write("\5$\23\2\u020a_\3\2\2\2\u020b\u020c\7\5\2\2\u020c\u020d")
        buf.write("\7\66\2\2\u020da\3\2\2\2\u020e\u020f\7\6\2\2\u020f\u0210")
        buf.write("\7\66\2\2\u0210c\3\2\2\2\u0211\u0214\7\26\2\2\u0212\u0215")
        buf.write("\58\35\2\u0213\u0215\3\2\2\2\u0214\u0212\3\2\2\2\u0214")
        buf.write("\u0213\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0217\7\66\2")
        buf.write("\2\u0217e\3\2\2\2\u0218\u021f\7\f\2\2\u0219\u021f\7\r")
        buf.write("\2\2\u021a\u021f\7\16\2\2\u021b\u021f\7\17\2\2\u021c\u021f")
        buf.write("\5j\66\2\u021d\u021f\5h\65\2\u021e\u0218\3\2\2\2\u021e")
        buf.write("\u0219\3\2\2\2\u021e\u021a\3\2\2\2\u021e\u021b\3\2\2\2")
        buf.write("\u021e\u021c\3\2\2\2\u021e\u021d\3\2\2\2\u021fg\3\2\2")
        buf.write("\2\u0220\u0221\7>\2\2\u0221i\3\2\2\2\u0222\u0223\7\13")
        buf.write("\2\2\u0223\u0224\7\61\2\2\u0224\u0225\5f\64\2\u0225\u0226")
        buf.write("\7\65\2\2\u0226\u0227\5l\67\2\u0227\u0228\7\62\2\2\u0228")
        buf.write("k\3\2\2\2\u0229\u022a\t\b\2\2\u022am\3\2\2\2\u022b\u022c")
        buf.write("\t\t\2\2\u022co\3\2\2\2\u022d\u0230\5r:\2\u022e\u0230")
        buf.write("\5~@\2\u022f\u022d\3\2\2\2\u022f\u022e\3\2\2\2\u0230q")
        buf.write("\3\2\2\2\u0231\u0232\7\13\2\2\u0232\u0238\7/\2\2\u0233")
        buf.write("\u0239\5t;\2\u0234\u0239\5v<\2\u0235\u0239\5x=\2\u0236")
        buf.write("\u0239\5z>\2\u0237\u0239\3\2\2\2\u0238\u0233\3\2\2\2\u0238")
        buf.write("\u0234\3\2\2\2\u0238\u0235\3\2\2\2\u0238\u0236\3\2\2\2")
        buf.write("\u0238\u0237\3\2\2\2\u0239\u023a\3\2\2\2\u023a\u023b\7")
        buf.write("\60\2\2\u023bs\3\2\2\2\u023c\u023d\5l\67\2\u023d\u023e")
        buf.write("\7\65\2\2\u023e\u023f\5t;\2\u023f\u0242\3\2\2\2\u0240")
        buf.write("\u0242\5l\67\2\u0241\u023c\3\2\2\2\u0241\u0240\3\2\2\2")
        buf.write("\u0242u\3\2\2\2\u0243\u0244\7<\2\2\u0244\u0245\7\65\2")
        buf.write("\2\u0245\u0248\5v<\2\u0246\u0248\7<\2\2\u0247\u0243\3")
        buf.write("\2\2\2\u0247\u0246\3\2\2\2\u0248w\3\2\2\2\u0249\u024a")
        buf.write("\7=\2\2\u024a\u024b\7\65\2\2\u024b\u024e\5x=\2\u024c\u024e")
        buf.write("\7=\2\2\u024d\u0249\3\2\2\2\u024d\u024c\3\2\2\2\u024e")
        buf.write("y\3\2\2\2\u024f\u0250\5n8\2\u0250\u0251\7\65\2\2\u0251")
        buf.write("\u0252\5z>\2\u0252\u0255\3\2\2\2\u0253\u0255\5n8\2\u0254")
        buf.write("\u024f\3\2\2\2\u0254\u0253\3\2\2\2\u0255{\3\2\2\2\u0256")
        buf.write("\u0257\5r:\2\u0257\u0258\7\65\2\2\u0258\u0259\5|?\2\u0259")
        buf.write("\u025c\3\2\2\2\u025a\u025c\5r:\2\u025b\u0256\3\2\2\2\u025b")
        buf.write("\u025a\3\2\2\2\u025c}\3\2\2\2\u025d\u025e\7\13\2\2\u025e")
        buf.write("\u025f\7/\2\2\u025f\u0260\5|?\2\u0260\u0261\7\60\2\2\u0261")
        buf.write("\177\3\2\2\2;\u0087\u008e\u0093\u009b\u009f\u00a8\u00b3")
        buf.write("\u00b9\u00bf\u00c5\u00cb\u00cd\u00d5\u00d9\u00e5\u00ec")
        buf.write("\u00f4\u0101\u0109\u0115\u011e\u0129\u0131\u0139\u0143")
        buf.write("\u014d\u0158\u015f\u0166\u0170\u017b\u0186\u018c\u0191")
        buf.write("\u019a\u01a9\u01ac\u01ae\u01ba\u01be\u01c5\u01c9\u01d0")
        buf.write("\u01d6\u01dd\u01eb\u01f2\u0206\u0214\u021e\u022f\u0238")
        buf.write("\u0241\u0247\u024d\u0254\u025b")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'True'", "'False'", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Array'", 
                     "'Int'", "'Float'", "'Boolean'", "'String'", "'Null'", 
                     "'By'", "'Class'", "'Val'", "'Var'", "'New'", "'Return'", 
                     "'In'", "'Constructor'", "'Destructor'", "'Self'", 
                     "'..'", "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", 
                     "'!='", "'>'", "'>='", "'<'", "'<='", "'==.'", "'+.'", 
                     "'('", "')'", "'['", "']'", "':'", "'.'", "','", "';'", 
                     "'{'", "'}'", "'::'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ELSE", "FOREACH", "ARRAY", "INT", 
                      "FLOAT", "BOOLEAN", "STRING", "NULL", "BY", "CLASS", 
                      "VAL", "VAR", "NEW", "RETURN", "IN", "CONSTRUCTOR", 
                      "DESTRUCTOR", "SELF", "DDOTS", "WS", "COMMENT", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQ", 
                      "SET", "NE", "GT", "GTE", "LT", "LTE", "ED", "AD", 
                      "LP", "RP", "LSB", "RSB", "COLON", "DOT", "COMMA", 
                      "SEMI", "LCB", "RCB", "ACCESS", "ZEROINT", "NONZEROINT", 
                      "FLOATLIT", "STRINGLIT", "ID", "Dollar_id", "ERROR_TOKEN", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_classNormal = 2
    RULE_class_bodys = 3
    RULE_class_body = 4
    RULE_variable_decl = 5
    RULE_const_decl = 6
    RULE_attribute_decl = 7
    RULE_list_name = 8
    RULE_name_att = 9
    RULE_list_exp = 10
    RULE_method_decl = 11
    RULE_parameter = 12
    RULE_identifer_list = 13
    RULE_normal = 14
    RULE_constructor = 15
    RULE_destructor = 16
    RULE_block_stm = 17
    RULE_statements = 18
    RULE_statement = 19
    RULE_variable_declmethod = 20
    RULE_const_declmethod = 21
    RULE_list_namemethod = 22
    RULE_instance_method = 23
    RULE_static_method = 24
    RULE_member_access = 25
    RULE_index_operators = 26
    RULE_expr = 27
    RULE_expr1 = 28
    RULE_expr2 = 29
    RULE_expr3 = 30
    RULE_expr4 = 31
    RULE_expr5 = 32
    RULE_expr6 = 33
    RULE_expr7 = 34
    RULE_expr8 = 35
    RULE_expr9 = 36
    RULE_expr10 = 37
    RULE_expr11 = 38
    RULE_operand = 39
    RULE_literal = 40
    RULE_assignment_statement = 41
    RULE_if_statement = 42
    RULE_elseStmt = 43
    RULE_elif_stm = 44
    RULE_else_stm = 45
    RULE_foreach_stmt = 46
    RULE_break_stmt = 47
    RULE_cont_stmt = 48
    RULE_return_stmt = 49
    RULE_typ_var = 50
    RULE_class_type = 51
    RULE_array = 52
    RULE_intlit = 53
    RULE_boolit = 54
    RULE_arraylit = 55
    RULE_iar = 56
    RULE_aints = 57
    RULE_afloats = 58
    RULE_astrings = 59
    RULE_asbools = 60
    RULE_marraylists = 61
    RULE_mar = 62

    ruleNames =  [ "program", "decls", "classNormal", "class_bodys", "class_body", 
                   "variable_decl", "const_decl", "attribute_decl", "list_name", 
                   "name_att", "list_exp", "method_decl", "parameter", "identifer_list", 
                   "normal", "constructor", "destructor", "block_stm", "statements", 
                   "statement", "variable_declmethod", "const_declmethod", 
                   "list_namemethod", "instance_method", "static_method", 
                   "member_access", "index_operators", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "expr8", "expr9", "expr10", "expr11", "operand", "literal", 
                   "assignment_statement", "if_statement", "elseStmt", "elif_stm", 
                   "else_stm", "foreach_stmt", "break_stmt", "cont_stmt", 
                   "return_stmt", "typ_var", "class_type", "array", "intlit", 
                   "boolit", "arraylit", "iar", "aints", "afloats", "astrings", 
                   "asbools", "marraylists", "mar" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    BREAK=3
    CONTINUE=4
    IF=5
    ELSEIF=6
    ELSE=7
    FOREACH=8
    ARRAY=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    STRING=13
    NULL=14
    BY=15
    CLASS=16
    VAL=17
    VAR=18
    NEW=19
    RETURN=20
    IN=21
    CONSTRUCTOR=22
    DESTRUCTOR=23
    SELF=24
    DDOTS=25
    WS=26
    COMMENT=27
    ADD=28
    SUB=29
    MUL=30
    DIV=31
    MOD=32
    NOT=33
    AND=34
    OR=35
    EQ=36
    SET=37
    NE=38
    GT=39
    GTE=40
    LT=41
    LTE=42
    ED=43
    AD=44
    LP=45
    RP=46
    LSB=47
    RSB=48
    COLON=49
    DOT=50
    COMMA=51
    SEMI=52
    LCB=53
    RCB=54
    ACCESS=55
    ZEROINT=56
    NONZEROINT=57
    FLOATLIT=58
    STRINGLIT=59
    ID=60
    Dollar_id=61
    ERROR_TOKEN=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64
    UNTERMINATED_COMMENT=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decls(self):
            return self.getTypedRuleContext(D96Parser.DeclsContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.decls()
            self.state = 127
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classNormal(self):
            return self.getTypedRuleContext(D96Parser.ClassNormalContext,0)


        def decls(self):
            return self.getTypedRuleContext(D96Parser.DeclsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_decls




    def decls(self):

        localctx = D96Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.classNormal()
                self.state = 130
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.classNormal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassNormalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def class_bodys(self):
            return self.getTypedRuleContext(D96Parser.Class_bodysContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classNormal




    def classNormal(self):

        localctx = D96Parser.ClassNormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classNormal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(D96Parser.CLASS)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 136
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 137
                self.match(D96Parser.ID)
                self.state = 138
                self.match(D96Parser.COLON)
                self.state = 139
                self.match(D96Parser.ID)
                pass


            self.state = 142
            self.match(D96Parser.LCB)
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 143
                self.class_bodys()
                pass
            elif token in [D96Parser.RCB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 147
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodysContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def class_bodys(self):
            return self.getTypedRuleContext(D96Parser.Class_bodysContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_bodys




    def class_bodys(self):

        localctx = D96Parser.Class_bodysContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_bodys)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.class_body()
                self.state = 150
                self.class_bodys()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.class_body()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_decl(self):
            return self.getTypedRuleContext(D96Parser.Attribute_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(D96Parser.Method_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_body)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.attribute_decl()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.method_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def list_name(self):
            return self.getTypedRuleContext(D96Parser.List_nameContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ_var(self):
            return self.getTypedRuleContext(D96Parser.Typ_varContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def SET(self):
            return self.getToken(D96Parser.SET, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_decl




    def variable_decl(self):

        localctx = D96Parser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(D96Parser.VAR)
            self.state = 160
            self.list_name()
            self.state = 161
            self.match(D96Parser.COLON)
            self.state = 162
            self.typ_var()
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SET]:
                self.state = 163
                self.match(D96Parser.SET)
                self.state = 164
                self.list_exp()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 168
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def list_name(self):
            return self.getTypedRuleContext(D96Parser.List_nameContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ_var(self):
            return self.getTypedRuleContext(D96Parser.Typ_varContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def SET(self):
            return self.getToken(D96Parser.SET, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_const_decl




    def const_decl(self):

        localctx = D96Parser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(D96Parser.VAL)
            self.state = 171
            self.list_name()
            self.state = 172
            self.match(D96Parser.COLON)
            self.state = 173
            self.typ_var()
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SET]:
                self.state = 174
                self.match(D96Parser.SET)
                self.state = 175
                self.list_exp()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 179
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(D96Parser.Variable_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(D96Parser.Const_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_decl




    def attribute_decl(self):

        localctx = D96Parser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attribute_decl)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.variable_decl()
                pass
            elif token in [D96Parser.VAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.const_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def list_name(self):
            return self.getTypedRuleContext(D96Parser.List_nameContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def Dollar_id(self):
            return self.getToken(D96Parser.Dollar_id, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_list_name




    def list_name(self):

        localctx = D96Parser.List_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_name)
        self._la = 0 # Token type
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Dollar_id):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 186
                self.match(D96Parser.COMMA)
                self.state = 187
                self.list_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Dollar_id):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_attContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def Dollar_id(self):
            return self.getToken(D96Parser.Dollar_id, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_name_att




    def name_att(self):

        localctx = D96Parser.Name_attContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_name_att)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.Dollar_id):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_list_exp




    def list_exp(self):

        localctx = D96Parser.List_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_exp)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 193
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 194
                    self.match(D96Parser.NULL)
                    pass


                self.state = 197
                self.match(D96Parser.COMMA)
                self.state = 198
                self.list_exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 199
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 200
                    self.match(D96Parser.NULL)
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def Dollar_id(self):
            return self.getToken(D96Parser.Dollar_id, 0)

        def parameter(self):
            return self.getTypedRuleContext(D96Parser.ParameterContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_decl




    def method_decl(self):

        localctx = D96Parser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.destructor()
                pass
            elif token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Dollar_id):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 208
                self.match(D96Parser.LP)
                self.state = 211
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.ID, D96Parser.Dollar_id]:
                    self.state = 209
                    self.parameter()
                    pass
                elif token in [D96Parser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 213
                self.match(D96Parser.RP)
                self.state = 214
                self.block_stm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifer_list(self):
            return self.getTypedRuleContext(D96Parser.Identifer_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ_var(self):
            return self.getTypedRuleContext(D96Parser.Typ_varContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def parameter(self):
            return self.getTypedRuleContext(D96Parser.ParameterContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parameter




    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.identifer_list()
                self.state = 218
                self.match(D96Parser.COLON)
                self.state = 219
                self.typ_var()
                self.state = 220
                self.match(D96Parser.SEMI)
                self.state = 221
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.identifer_list()
                self.state = 224
                self.match(D96Parser.COLON)
                self.state = 225
                self.typ_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifer_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_att(self):
            return self.getTypedRuleContext(D96Parser.Name_attContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def identifer_list(self):
            return self.getTypedRuleContext(D96Parser.Identifer_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_identifer_list




    def identifer_list(self):

        localctx = D96Parser.Identifer_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_identifer_list)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.name_att()
                self.state = 230
                self.match(D96Parser.COMMA)
                self.state = 231
                self.identifer_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.name_att()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_normal




    def normal(self):

        localctx = D96Parser.NormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_normal)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def parameter(self):
            return self.getTypedRuleContext(D96Parser.ParameterContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 239
            self.match(D96Parser.LP)
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 240
                self.parameter()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 244
            self.match(D96Parser.RP)
            self.state = 245
            self.block_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(D96Parser.DESTRUCTOR)
            self.state = 248
            self.match(D96Parser.LP)
            self.state = 249
            self.match(D96Parser.RP)
            self.state = 250
            self.block_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stm




    def block_stm(self):

        localctx = D96Parser.Block_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(D96Parser.LCB)
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.RETURN, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.LCB, D96Parser.ZEROINT, D96Parser.NONZEROINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 253
                self.statements()
                pass
            elif token in [D96Parser.RCB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 257
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(D96Parser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statements




    def statements(self):

        localctx = D96Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statements)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.statement()
                self.state = 260
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declmethod(self):
            return self.getTypedRuleContext(D96Parser.Variable_declmethodContext,0)


        def const_declmethod(self):
            return self.getTypedRuleContext(D96Parser.Const_declmethodContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(D96Parser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(D96Parser.If_statementContext,0)


        def foreach_stmt(self):
            return self.getTypedRuleContext(D96Parser.Foreach_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def cont_stmt(self):
            return self.getTypedRuleContext(D96Parser.Cont_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def member_access(self):
            return self.getTypedRuleContext(D96Parser.Member_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_statement)
        try:
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.variable_declmethod()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.const_declmethod()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.assignment_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 268
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 269
                self.foreach_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 270
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 271
                self.cont_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 272
                self.return_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 273
                self.block_stm()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 274
                self.member_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declmethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def list_namemethod(self):
            return self.getTypedRuleContext(D96Parser.List_namemethodContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ_var(self):
            return self.getTypedRuleContext(D96Parser.Typ_varContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def SET(self):
            return self.getToken(D96Parser.SET, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_declmethod




    def variable_declmethod(self):

        localctx = D96Parser.Variable_declmethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_variable_declmethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(D96Parser.VAR)
            self.state = 278
            self.list_namemethod()
            self.state = 279
            self.match(D96Parser.COLON)
            self.state = 280
            self.typ_var()
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SET]:
                self.state = 281
                self.match(D96Parser.SET)
                self.state = 282
                self.list_exp()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 286
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declmethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def list_namemethod(self):
            return self.getTypedRuleContext(D96Parser.List_namemethodContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ_var(self):
            return self.getTypedRuleContext(D96Parser.Typ_varContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def SET(self):
            return self.getToken(D96Parser.SET, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_const_declmethod




    def const_declmethod(self):

        localctx = D96Parser.Const_declmethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_const_declmethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(D96Parser.VAL)
            self.state = 289
            self.list_namemethod()
            self.state = 290
            self.match(D96Parser.COLON)
            self.state = 291
            self.typ_var()
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SET]:
                self.state = 292
                self.match(D96Parser.SET)
                self.state = 293
                self.list_exp()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 297
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_namemethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def list_namemethod(self):
            return self.getTypedRuleContext(D96Parser.List_namemethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_namemethod




    def list_namemethod(self):

        localctx = D96Parser.List_namemethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_namemethod)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(D96Parser.ID)
                self.state = 300
                self.match(D96Parser.COMMA)
                self.state = 301
                self.list_namemethod()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_methodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instance_method




    def instance_method(self):

        localctx = D96Parser.Instance_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_instance_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.expr()
            self.state = 306
            self.match(D96Parser.DOT)
            self.state = 307
            self.match(D96Parser.ID)
            self.state = 308
            self.match(D96Parser.LP)
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.ZEROINT, D96Parser.NONZEROINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 309
                self.list_exp()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 313
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_methodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def ACCESS(self):
            return self.getToken(D96Parser.ACCESS, 0)

        def Dollar_id(self):
            return self.getToken(D96Parser.Dollar_id, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_method




    def static_method(self):

        localctx = D96Parser.Static_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_static_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(D96Parser.ID)
            self.state = 316
            self.match(D96Parser.ACCESS)
            self.state = 317
            self.match(D96Parser.Dollar_id)
            self.state = 318
            self.match(D96Parser.LP)
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.ZEROINT, D96Parser.NONZEROINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 319
                self.list_exp()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 323
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_method(self):
            return self.getTypedRuleContext(D96Parser.Instance_methodContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def static_method(self):
            return self.getTypedRuleContext(D96Parser.Static_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_access




    def member_access(self):

        localctx = D96Parser.Member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_member_access)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.instance_method()
                self.state = 326
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.static_method()
                self.state = 329
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operators




    def index_operators(self):

        localctx = D96Parser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_index_operators)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.match(D96Parser.LSB)
                self.state = 334
                self.expr()
                self.state = 335
                self.match(D96Parser.RSB)
                self.state = 336
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.match(D96Parser.LSB)
                self.state = 339
                self.expr()
                self.state = 340
                self.match(D96Parser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr1Context,i)


        def AD(self):
            return self.getToken(D96Parser.AD, 0)

        def ED(self):
            return self.getToken(D96Parser.ED, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.expr1()
                self.state = 345
                _la = self._input.LA(1)
                if not(_la==D96Parser.ED or _la==D96Parser.AD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 346
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr2Context,i)


        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def NE(self):
            return self.getToken(D96Parser.NE, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LTE(self):
            return self.getToken(D96Parser.LTE, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr1




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.expr2(0)
                self.state = 352
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ) | (1 << D96Parser.NE) | (1 << D96Parser.GT) | (1 << D96Parser.GTE) | (1 << D96Parser.LT) | (1 << D96Parser.LTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 353
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 366
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 361
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 362
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 363
                    self.expr3(0) 
                self.state = 368
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 372
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 373
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 374
                    self.expr4(0) 
                self.state = 379
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 383
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 384
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 385
                    self.expr5() 
                self.state = 390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr5




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr5)
        try:
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.match(D96Parser.NOT)
                self.state = 392
                self.expr5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.LP, D96Parser.ZEROINT, D96Parser.NONZEROINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr6




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr6)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(D96Parser.SUB)
                self.state = 397
                self.expr6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LP, D96Parser.ZEROINT, D96Parser.NONZEROINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.expr7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr7



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 404
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 405
                    self.index_operators() 
                self.state = 410
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr8



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 428
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 426
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 414
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 415
                        self.match(D96Parser.DOT)
                        self.state = 416
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 417
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 418
                        self.match(D96Parser.DOT)
                        self.state = 419
                        self.match(D96Parser.ID)
                        self.state = 420
                        self.match(D96Parser.LP)
                        self.state = 423
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.ZEROINT, D96Parser.NONZEROINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                            self.state = 421
                            self.list_exp()
                            pass
                        elif token in [D96Parser.RP]:
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 425
                        self.match(D96Parser.RP)
                        pass

             
                self.state = 430
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def ACCESS(self):
            return self.getToken(D96Parser.ACCESS, 0)

        def Dollar_id(self):
            return self.getToken(D96Parser.Dollar_id, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr9)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.match(D96Parser.ID)
                self.state = 432
                self.match(D96Parser.ACCESS)
                self.state = 433
                self.match(D96Parser.Dollar_id)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.match(D96Parser.ID)
                self.state = 435
                self.match(D96Parser.ACCESS)
                self.state = 436
                self.match(D96Parser.Dollar_id)
                self.state = 437
                self.match(D96Parser.LP)
                self.state = 440
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.ZEROINT, D96Parser.NONZEROINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                    self.state = 438
                    self.list_exp()
                    pass
                elif token in [D96Parser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 442
                self.match(D96Parser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 443
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(D96Parser.List_expContext,0)


        def expr11(self):
            return self.getTypedRuleContext(D96Parser.Expr11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr10




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr10)
        try:
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(D96Parser.NEW)
                self.state = 447
                self.match(D96Parser.ID)
                self.state = 448
                self.match(D96Parser.LP)
                self.state = 451
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.ZEROINT, D96Parser.NONZEROINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                    self.state = 449
                    self.list_exp()
                    pass
                elif token in [D96Parser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 453
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.LP, D96Parser.ZEROINT, D96Parser.NONZEROINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.expr11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def operand(self):
            return self.getTypedRuleContext(D96Parser.OperandContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr11




    def expr11(self):

        localctx = D96Parser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr11)
        try:
            self.state = 462
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(D96Parser.LP)
                self.state = 458
                self.expr()
                self.state = 459
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.ZEROINT, D96Parser.NONZEROINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def name_att(self):
            return self.getTypedRuleContext(D96Parser.Name_attContext,0)


        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_operand




    def operand(self):

        localctx = D96Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_operand)
        try:
            self.state = 468
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.ID, D96Parser.Dollar_id]:
                self.enterOuterAlt(localctx, 3)
                self.state = 466
                self.name_att()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.ZEROINT, D96Parser.NONZEROINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 467
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intlit(self):
            return self.getTypedRuleContext(D96Parser.IntlitContext,0)


        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def boolit(self):
            return self.getTypedRuleContext(D96Parser.BoolitContext,0)


        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def arraylit(self):
            return self.getTypedRuleContext(D96Parser.ArraylitContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_literal)
        try:
            self.state = 475
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ZEROINT, D96Parser.NONZEROINT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.intlit()
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 472
                self.boolit()
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 473
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 474
                self.arraylit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def SET(self):
            return self.getToken(D96Parser.SET, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assignment_statement




    def assignment_statement(self):

        localctx = D96Parser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.expr()
            self.state = 478
            self.match(D96Parser.SET)
            self.state = 479
            self.expr()
            self.state = 480
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def elseStmt(self):
            return self.getTypedRuleContext(D96Parser.ElseStmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statement




    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(D96Parser.IF)
            self.state = 483
            self.match(D96Parser.LP)
            self.state = 484
            self.expr()
            self.state = 485
            self.match(D96Parser.RP)
            self.state = 486
            self.block_stm()
            self.state = 489
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF, D96Parser.ELSE]:
                self.state = 487
                self.elseStmt()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.RETURN, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.LCB, D96Parser.RCB, D96Parser.ZEROINT, D96Parser.NONZEROINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_stm(self):
            return self.getTypedRuleContext(D96Parser.Elif_stmContext,0)


        def elseStmt(self):
            return self.getTypedRuleContext(D96Parser.ElseStmtContext,0)


        def else_stm(self):
            return self.getTypedRuleContext(D96Parser.Else_stmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseStmt




    def elseStmt(self):

        localctx = D96Parser.ElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_elseStmt)
        try:
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.elif_stm()
                self.state = 492
                self.elseStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
                self.elif_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 495
                self.else_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elif_stm




    def elif_stm(self):

        localctx = D96Parser.Elif_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_elif_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(D96Parser.ELSEIF)
            self.state = 499
            self.match(D96Parser.LP)
            self.state = 500
            self.expr()
            self.state = 501
            self.match(D96Parser.RP)
            self.state = 502
            self.block_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_stm




    def else_stm(self):

        localctx = D96Parser.Else_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_else_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(D96Parser.ELSE)
            self.state = 505
            self.block_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Foreach_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def DDOTS(self):
            return self.getToken(D96Parser.DDOTS, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def Dollar_id(self):
            return self.getToken(D96Parser.Dollar_id, 0)

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_foreach_stmt




    def foreach_stmt(self):

        localctx = D96Parser.Foreach_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_foreach_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(D96Parser.FOREACH)
            self.state = 508
            self.match(D96Parser.LP)
            self.state = 509
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.Dollar_id):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 510
            self.match(D96Parser.IN)
            self.state = 511
            self.expr()
            self.state = 512
            self.match(D96Parser.DDOTS)
            self.state = 513
            self.expr()
            self.state = 516
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 514
                self.match(D96Parser.BY)
                self.state = 515
                self.expr()


            self.state = 518
            self.match(D96Parser.RP)
            self.state = 519
            self.block_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(D96Parser.BREAK)
            self.state = 522
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cont_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_cont_stmt




    def cont_stmt(self):

        localctx = D96Parser.Cont_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_cont_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.match(D96Parser.CONTINUE)
            self.state = 525
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(D96Parser.RETURN)
            self.state = 530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.ZEROINT, D96Parser.NONZEROINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Dollar_id]:
                self.state = 528
                self.expr()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 532
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Typ_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def array(self):
            return self.getTypedRuleContext(D96Parser.ArrayContext,0)


        def class_type(self):
            return self.getTypedRuleContext(D96Parser.Class_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_typ_var




    def typ_var(self):

        localctx = D96Parser.Typ_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_typ_var)
        try:
            self.state = 540
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 534
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 535
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 536
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 537
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 538
                self.array()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 539
                self.class_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_type




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def typ_var(self):
            return self.getTypedRuleContext(D96Parser.Typ_varContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def intlit(self):
            return self.getTypedRuleContext(D96Parser.IntlitContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array




    def array(self):

        localctx = D96Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(D96Parser.ARRAY)
            self.state = 545
            self.match(D96Parser.LSB)
            self.state = 546
            self.typ_var()
            self.state = 547
            self.match(D96Parser.COMMA)
            self.state = 548
            self.intlit()
            self.state = 549
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntlitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZEROINT(self):
            return self.getToken(D96Parser.ZEROINT, 0)

        def NONZEROINT(self):
            return self.getToken(D96Parser.NONZEROINT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_intlit




    def intlit(self):

        localctx = D96Parser.IntlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_intlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            _la = self._input.LA(1)
            if not(_la==D96Parser.ZEROINT or _la==D96Parser.NONZEROINT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_boolit




    def boolit(self):

        localctx = D96Parser.BoolitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_boolit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            _la = self._input.LA(1)
            if not(_la==D96Parser.TRUE or _la==D96Parser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iar(self):
            return self.getTypedRuleContext(D96Parser.IarContext,0)


        def mar(self):
            return self.getTypedRuleContext(D96Parser.MarContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arraylit




    def arraylit(self):

        localctx = D96Parser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_arraylit)
        try:
            self.state = 557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.iar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 556
                self.mar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def aints(self):
            return self.getTypedRuleContext(D96Parser.AintsContext,0)


        def afloats(self):
            return self.getTypedRuleContext(D96Parser.AfloatsContext,0)


        def astrings(self):
            return self.getTypedRuleContext(D96Parser.AstringsContext,0)


        def asbools(self):
            return self.getTypedRuleContext(D96Parser.AsboolsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_iar




    def iar(self):

        localctx = D96Parser.IarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_iar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(D96Parser.ARRAY)
            self.state = 560
            self.match(D96Parser.LP)
            self.state = 566
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ZEROINT, D96Parser.NONZEROINT]:
                self.state = 561
                self.aints()
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.state = 562
                self.afloats()
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.state = 563
                self.astrings()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.state = 564
                self.asbools()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 568
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AintsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intlit(self):
            return self.getTypedRuleContext(D96Parser.IntlitContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def aints(self):
            return self.getTypedRuleContext(D96Parser.AintsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_aints




    def aints(self):

        localctx = D96Parser.AintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_aints)
        try:
            self.state = 575
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 570
                self.intlit()
                self.state = 571
                self.match(D96Parser.COMMA)
                self.state = 572
                self.aints()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 574
                self.intlit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AfloatsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def afloats(self):
            return self.getTypedRuleContext(D96Parser.AfloatsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_afloats




    def afloats(self):

        localctx = D96Parser.AfloatsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_afloats)
        try:
            self.state = 581
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 577
                self.match(D96Parser.FLOATLIT)
                self.state = 578
                self.match(D96Parser.COMMA)
                self.state = 579
                self.afloats()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 580
                self.match(D96Parser.FLOATLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AstringsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def astrings(self):
            return self.getTypedRuleContext(D96Parser.AstringsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_astrings




    def astrings(self):

        localctx = D96Parser.AstringsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_astrings)
        try:
            self.state = 587
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 583
                self.match(D96Parser.STRINGLIT)
                self.state = 584
                self.match(D96Parser.COMMA)
                self.state = 585
                self.astrings()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 586
                self.match(D96Parser.STRINGLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsboolsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolit(self):
            return self.getTypedRuleContext(D96Parser.BoolitContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def asbools(self):
            return self.getTypedRuleContext(D96Parser.AsboolsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_asbools




    def asbools(self):

        localctx = D96Parser.AsboolsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_asbools)
        try:
            self.state = 594
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 589
                self.boolit()
                self.state = 590
                self.match(D96Parser.COMMA)
                self.state = 591
                self.asbools()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 593
                self.boolit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MarraylistsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iar(self):
            return self.getTypedRuleContext(D96Parser.IarContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def marraylists(self):
            return self.getTypedRuleContext(D96Parser.MarraylistsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_marraylists




    def marraylists(self):

        localctx = D96Parser.MarraylistsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_marraylists)
        try:
            self.state = 601
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 596
                self.iar()
                self.state = 597
                self.match(D96Parser.COMMA)
                self.state = 598
                self.marraylists()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 600
                self.iar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def marraylists(self):
            return self.getTypedRuleContext(D96Parser.MarraylistsContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mar




    def mar(self):

        localctx = D96Parser.MarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_mar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.match(D96Parser.ARRAY)
            self.state = 604
            self.match(D96Parser.LP)
            self.state = 605
            self.marraylists()
            self.state = 606
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[29] = self.expr2_sempred
        self._predicates[30] = self.expr3_sempred
        self._predicates[31] = self.expr4_sempred
        self._predicates[34] = self.expr7_sempred
        self._predicates[35] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




