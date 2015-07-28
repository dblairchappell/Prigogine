# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .PrigogineListener import PrigogineListener
    from .PrigogineVisitor import PrigogineVisitor
else:
    from PrigogineListener import PrigogineListener
    from PrigogineVisitor import PrigogineVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\62\u01c0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\3\2\6\2@\n\2\r\2\16\2A\3\2")
        buf.write(u"\7\2E\n\2\f\2\16\2H\13\2\3\3\3\3\3\3\3\3\7\3N\n\3\f\3")
        buf.write(u"\16\3Q\13\3\3\3\3\3\3\3\6\3V\n\3\r\3\16\3W\3\3\3\3\3")
        buf.write(u"\4\3\4\3\4\3\4\3\4\3\5\7\5b\n\5\f\5\16\5e\13\5\3\6\3")
        buf.write(u"\6\3\6\3\6\6\6k\n\6\r\6\16\6l\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write(u"\3\7\3\7\3\7\7\7x\n\7\f\7\16\7{\13\7\3\7\3\7\3\7\7\7")
        buf.write(u"\u0080\n\7\f\7\16\7\u0083\13\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write(u"\7\7\7\u008b\n\7\f\7\16\7\u008e\13\7\5\7\u0090\n\7\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u009a\n\b\f\b\16\b")
        buf.write(u"\u009d\13\b\3\b\3\b\3\b\7\b\u00a2\n\b\f\b\16\b\u00a5")
        buf.write(u"\13\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00ae\n\b\f\b\16")
        buf.write(u"\b\u00b1\13\b\5\b\u00b3\n\b\3\t\3\t\3\t\3\t\7\t\u00b9")
        buf.write(u"\n\t\f\t\16\t\u00bc\13\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write(u"\7\n\u00c5\n\n\f\n\16\n\u00c8\13\n\3\n\3\n\3\n\3\n\3")
        buf.write(u"\13\3\13\3\13\7\13\u00d1\n\13\f\13\16\13\u00d4\13\13")
        buf.write(u"\3\13\3\13\3\f\3\f\3\f\7\f\u00db\n\f\f\f\16\f\u00de\13")
        buf.write(u"\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write(u"\3\16\3\16\5\16\u00ee\n\16\3\16\3\16\3\16\3\16\5\16\u00f4")
        buf.write(u"\n\16\7\16\u00f6\n\16\f\16\16\16\u00f9\13\16\7\16\u00fb")
        buf.write(u"\n\16\f\16\16\16\u00fe\13\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\5\16\u0105\n\16\3\17\3\17\3\17\3\17\5\17\u010b\n\17")
        buf.write(u"\3\17\3\17\3\17\3\17\5\17\u0111\n\17\7\17\u0113\n\17")
        buf.write(u"\f\17\16\17\u0116\13\17\7\17\u0118\n\17\f\17\16\17\u011b")
        buf.write(u"\13\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3")
        buf.write(u"\23\3\23\3\23\3\23\7\23\u012a\n\23\f\23\16\23\u012d\13")
        buf.write(u"\23\3\23\3\23\3\23\6\23\u0132\n\23\r\23\16\23\u0133\3")
        buf.write(u"\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\26\5\26\u0157\n\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0168")
        buf.write(u"\n\26\f\26\16\26\u016b\13\26\3\27\3\27\3\27\7\27\u0170")
        buf.write(u"\n\27\f\27\16\27\u0173\13\27\3\27\3\27\3\30\3\30\3\31")
        buf.write(u"\3\31\3\31\5\31\u017c\n\31\3\31\3\31\3\31\5\31\u0181")
        buf.write(u"\n\31\3\31\3\31\3\32\3\32\3\33\7\33\u0188\n\33\f\33\16")
        buf.write(u"\33\u018b\13\33\3\33\3\33\3\33\3\33\7\33\u0191\n\33\f")
        buf.write(u"\33\16\33\u0194\13\33\3\33\3\33\7\33\u0198\n\33\f\33")
        buf.write(u"\16\33\u019b\13\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write(u"\7\36\u01a4\n\36\f\36\16\36\u01a7\13\36\3\36\3\36\3\36")
        buf.write(u"\7\36\u01ac\n\36\f\36\16\36\u01af\13\36\7\36\u01b1\n")
        buf.write(u"\36\f\36\16\36\u01b4\13\36\3\36\7\36\u01b7\n\36\f\36")
        buf.write(u"\16\36\u01ba\13\36\3\36\3\36\3\37\3\37\3\37\3c\3* \2")
        buf.write(u"\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write(u"\64\668:<\2\t\3\2\7\b\4\2\30\30&&\3\2*+\3\2,-\3\2\34")
        buf.write(u"!\4\2\"\"..\3\2&\'\u01e5\2?\3\2\2\2\4I\3\2\2\2\6[\3\2")
        buf.write(u"\2\2\bc\3\2\2\2\nf\3\2\2\2\f\u008f\3\2\2\2\16\u00b2\3")
        buf.write(u"\2\2\2\20\u00b4\3\2\2\2\22\u00c0\3\2\2\2\24\u00cd\3\2")
        buf.write(u"\2\2\26\u00d7\3\2\2\2\30\u00e1\3\2\2\2\32\u0104\3\2\2")
        buf.write(u"\2\34\u0106\3\2\2\2\36\u011e\3\2\2\2 \u0120\3\2\2\2\"")
        buf.write(u"\u0123\3\2\2\2$\u0131\3\2\2\2&\u0135\3\2\2\2(\u0137\3")
        buf.write(u"\2\2\2*\u0156\3\2\2\2,\u016c\3\2\2\2.\u0176\3\2\2\2\60")
        buf.write(u"\u0178\3\2\2\2\62\u0184\3\2\2\2\64\u0189\3\2\2\2\66\u019c")
        buf.write(u"\3\2\2\28\u019e\3\2\2\2:\u01a0\3\2\2\2<\u01bd\3\2\2\2")
        buf.write(u">@\5\4\3\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2BF")
        buf.write(u"\3\2\2\2CE\5\6\4\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3")
        buf.write(u"\2\2\2G\3\3\2\2\2HF\3\2\2\2IJ\7\3\2\2JK\7(\2\2KO\7\4")
        buf.write(u"\2\2LN\5\24\13\2ML\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2")
        buf.write(u"\2\2PR\3\2\2\2QO\3\2\2\2RS\5\26\f\2SU\5\n\6\2TV\5\22")
        buf.write(u"\n\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2XY\3\2\2")
        buf.write(u"\2YZ\7\5\2\2Z\5\3\2\2\2[\\\7\6\2\2\\]\7\4\2\2]^\5\b\5")
        buf.write(u"\2^_\7\5\2\2_\7\3\2\2\2`b\n\2\2\2a`\3\2\2\2be\3\2\2\2")
        buf.write(u"cd\3\2\2\2ca\3\2\2\2d\t\3\2\2\2ec\3\2\2\2fg\7\t\2\2g")
        buf.write(u"j\7\4\2\2hk\5\f\7\2ik\5\16\b\2jh\3\2\2\2ji\3\2\2\2kl")
        buf.write(u"\3\2\2\2lj\3\2\2\2lm\3\2\2\2mn\3\2\2\2no\7\5\2\2o\13")
        buf.write(u"\3\2\2\2pq\7(\2\2qr\7\n\2\2rs\7\13\2\2sy\5*\26\2tu\7")
        buf.write(u"\f\2\2uv\7\r\2\2vx\5\64\33\2wt\3\2\2\2x{\3\2\2\2yw\3")
        buf.write(u"\2\2\2yz\3\2\2\2z\u0090\3\2\2\2{y\3\2\2\2|\u0081\7(\2")
        buf.write(u"\2}~\7\16\2\2~\u0080\7(\2\2\177}\3\2\2\2\u0080\u0083")
        buf.write(u"\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write(u"\u0084\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0085\7\n\2")
        buf.write(u"\2\u0085\u0086\7\13\2\2\u0086\u008c\5*\26\2\u0087\u0088")
        buf.write(u"\7\f\2\2\u0088\u0089\7\r\2\2\u0089\u008b\5\64\33\2\u008a")
        buf.write(u"\u0087\3\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a\3\2\2")
        buf.write(u"\2\u008c\u008d\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c")
        buf.write(u"\3\2\2\2\u008fp\3\2\2\2\u008f|\3\2\2\2\u0090\r\3\2\2")
        buf.write(u"\2\u0091\u0092\7(\2\2\u0092\u0093\7\n\2\2\u0093\u0094")
        buf.write(u"\7\17\2\2\u0094\u0095\7\13\2\2\u0095\u009b\5*\26\2\u0096")
        buf.write(u"\u0097\7\f\2\2\u0097\u0098\7\r\2\2\u0098\u009a\5\64\33")
        buf.write(u"\2\u0099\u0096\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099")
        buf.write(u"\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u00b3\3\2\2\2\u009d")
        buf.write(u"\u009b\3\2\2\2\u009e\u00a3\7(\2\2\u009f\u00a0\7\16\2")
        buf.write(u"\2\u00a0\u00a2\7(\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a5")
        buf.write(u"\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write(u"\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7\7\n\2")
        buf.write(u"\2\u00a7\u00a8\7\17\2\2\u00a8\u00a9\7\13\2\2\u00a9\u00af")
        buf.write(u"\5*\26\2\u00aa\u00ab\7\f\2\2\u00ab\u00ac\7\r\2\2\u00ac")
        buf.write(u"\u00ae\5\64\33\2\u00ad\u00aa\3\2\2\2\u00ae\u00b1\3\2")
        buf.write(u"\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b3")
        buf.write(u"\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u0091\3\2\2\2\u00b2")
        buf.write(u"\u009e\3\2\2\2\u00b3\17\3\2\2\2\u00b4\u00ba\7(\2\2\u00b5")
        buf.write(u"\u00b6\7\16\2\2\u00b6\u00b9\7(\2\2\u00b7\u00b9\5$\23")
        buf.write(u"\2\u00b8\u00b5\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\u00bc")
        buf.write(u"\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write(u"\u00bd\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00be\7\13\2")
        buf.write(u"\2\u00be\u00bf\5*\26\2\u00bf\21\3\2\2\2\u00c0\u00c1\7")
        buf.write(u"\20\2\2\u00c1\u00c2\7(\2\2\u00c2\u00c6\7\4\2\2\u00c3")
        buf.write(u"\u00c5\5\24\13\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8\3\2")
        buf.write(u"\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9")
        buf.write(u"\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\5\26\f\2\u00ca")
        buf.write(u"\u00cb\5\n\6\2\u00cb\u00cc\7\5\2\2\u00cc\23\3\2\2\2\u00cd")
        buf.write(u"\u00ce\7\21\2\2\u00ce\u00d2\7\4\2\2\u00cf\u00d1\5\"\22")
        buf.write(u"\2\u00d0\u00cf\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0")
        buf.write(u"\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4")
        buf.write(u"\u00d2\3\2\2\2\u00d5\u00d6\7\5\2\2\u00d6\25\3\2\2\2\u00d7")
        buf.write(u"\u00d8\7\22\2\2\u00d8\u00dc\7\4\2\2\u00d9\u00db\5\36")
        buf.write(u"\20\2\u00da\u00d9\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da")
        buf.write(u"\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00df\3\2\2\2\u00de")
        buf.write(u"\u00dc\3\2\2\2\u00df\u00e0\7\5\2\2\u00e0\27\3\2\2\2\u00e1")
        buf.write(u"\u00e2\7\4\2\2\u00e2\u00e3\5*\26\2\u00e3\u00e4\7\23\2")
        buf.write(u"\2\u00e4\u00e5\7(\2\2\u00e5\u00e6\7\24\2\2\u00e6\u00e7")
        buf.write(u"\5*\26\2\u00e7\u00e8\7\5\2\2\u00e8\31\3\2\2\2\u00e9\u00fc")
        buf.write(u"\7\4\2\2\u00ea\u00ee\7(\2\2\u00eb\u00ee\5<\37\2\u00ec")
        buf.write(u"\u00ee\5\62\32\2\u00ed\u00ea\3\2\2\2\u00ed\u00eb\3\2")
        buf.write(u"\2\2\u00ed\u00ec\3\2\2\2\u00ee\u00f7\3\2\2\2\u00ef\u00f3")
        buf.write(u"\7\f\2\2\u00f0\u00f4\7(\2\2\u00f1\u00f4\5<\37\2\u00f2")
        buf.write(u"\u00f4\5\62\32\2\u00f3\u00f0\3\2\2\2\u00f3\u00f1\3\2")
        buf.write(u"\2\2\u00f3\u00f2\3\2\2\2\u00f4\u00f6\3\2\2\2\u00f5\u00ef")
        buf.write(u"\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7")
        buf.write(u"\u00f8\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2")
        buf.write(u"\2\u00fa\u00ed\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa")
        buf.write(u"\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe")
        buf.write(u"\u00fc\3\2\2\2\u00ff\u0105\7\5\2\2\u0100\u0101\7\4\2")
        buf.write(u"\2\u0101\u0102\5\32\16\2\u0102\u0103\7\5\2\2\u0103\u0105")
        buf.write(u"\3\2\2\2\u0104\u00e9\3\2\2\2\u0104\u0100\3\2\2\2\u0105")
        buf.write(u"\33\3\2\2\2\u0106\u0119\7\25\2\2\u0107\u010b\7(\2\2\u0108")
        buf.write(u"\u010b\5<\37\2\u0109\u010b\5\62\32\2\u010a\u0107\3\2")
        buf.write(u"\2\2\u010a\u0108\3\2\2\2\u010a\u0109\3\2\2\2\u010b\u0114")
        buf.write(u"\3\2\2\2\u010c\u0110\7\f\2\2\u010d\u0111\7(\2\2\u010e")
        buf.write(u"\u0111\5<\37\2\u010f\u0111\5\62\32\2\u0110\u010d\3\2")
        buf.write(u"\2\2\u0110\u010e\3\2\2\2\u0110\u010f\3\2\2\2\u0111\u0113")
        buf.write(u"\3\2\2\2\u0112\u010c\3\2\2\2\u0113\u0116\3\2\2\2\u0114")
        buf.write(u"\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0118\3\2\2")
        buf.write(u"\2\u0116\u0114\3\2\2\2\u0117\u010a\3\2\2\2\u0118\u011b")
        buf.write(u"\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a")
        buf.write(u"\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011d\7\26\2")
        buf.write(u"\2\u011d\35\3\2\2\2\u011e\u011f\7(\2\2\u011f\37\3\2\2")
        buf.write(u"\2\u0120\u0121\7(\2\2\u0121\u0122\5$\23\2\u0122!\3\2")
        buf.write(u"\2\2\u0123\u0124\7(\2\2\u0124#\3\2\2\2\u0125\u0126\7")
        buf.write(u"\4\2\2\u0126\u012b\5&\24\2\u0127\u0128\7-\2\2\u0128\u012a")
        buf.write(u"\7&\2\2\u0129\u0127\3\2\2\2\u012a\u012d\3\2\2\2\u012b")
        buf.write(u"\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e\3\2\2")
        buf.write(u"\2\u012d\u012b\3\2\2\2\u012e\u012f\7\5\2\2\u012f\u0132")
        buf.write(u"\3\2\2\2\u0130\u0132\7\27\2\2\u0131\u0125\3\2\2\2\u0131")
        buf.write(u"\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0131\3\2\2")
        buf.write(u"\2\u0133\u0134\3\2\2\2\u0134%\3\2\2\2\u0135\u0136\t\3")
        buf.write(u"\2\2\u0136\'\3\2\2\2\u0137\u0138\7\4\2\2\u0138\u0139")
        buf.write(u"\5\62\32\2\u0139\u013a\7\5\2\2\u013a)\3\2\2\2\u013b\u013c")
        buf.write(u"\b\26\1\2\u013c\u013d\7\31\2\2\u013d\u0157\5*\26\17\u013e")
        buf.write(u"\u0157\5\20\t\2\u013f\u0157\5\60\31\2\u0140\u0141\7\31")
        buf.write(u"\2\2\u0141\u0157\5\62\32\2\u0142\u0143\7\31\2\2\u0143")
        buf.write(u"\u0144\5\62\32\2\u0144\u0145\7\f\2\2\u0145\u0157\3\2")
        buf.write(u"\2\2\u0146\u0157\5\32\16\2\u0147\u0157\5\34\17\2\u0148")
        buf.write(u"\u0157\5\62\32\2\u0149\u0157\5<\37\2\u014a\u0157\5:\36")
        buf.write(u"\2\u014b\u0157\5\30\r\2\u014c\u0157\7(\2\2\u014d\u0157")
        buf.write(u"\7\32\2\2\u014e\u0157\5 \21\2\u014f\u0157\5&\24\2\u0150")
        buf.write(u"\u0151\5\66\34\2\u0151\u0152\5*\26\2\u0152\u0153\58\35")
        buf.write(u"\2\u0153\u0157\3\2\2\2\u0154\u0155\7\33\2\2\u0155\u0157")
        buf.write(u"\7(\2\2\u0156\u013b\3\2\2\2\u0156\u013e\3\2\2\2\u0156")
        buf.write(u"\u013f\3\2\2\2\u0156\u0140\3\2\2\2\u0156\u0142\3\2\2")
        buf.write(u"\2\u0156\u0146\3\2\2\2\u0156\u0147\3\2\2\2\u0156\u0148")
        buf.write(u"\3\2\2\2\u0156\u0149\3\2\2\2\u0156\u014a\3\2\2\2\u0156")
        buf.write(u"\u014b\3\2\2\2\u0156\u014c\3\2\2\2\u0156\u014d\3\2\2")
        buf.write(u"\2\u0156\u014e\3\2\2\2\u0156\u014f\3\2\2\2\u0156\u0150")
        buf.write(u"\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u0169\3\2\2\2\u0158")
        buf.write(u"\u0159\f\27\2\2\u0159\u015a\7\16\2\2\u015a\u0168\5*\26")
        buf.write(u"\30\u015b\u015c\f\26\2\2\u015c\u015d\7/\2\2\u015d\u0168")
        buf.write(u"\5*\26\27\u015e\u015f\f\25\2\2\u015f\u0160\t\4\2\2\u0160")
        buf.write(u"\u0168\5*\26\26\u0161\u0162\f\24\2\2\u0162\u0163\t\5")
        buf.write(u"\2\2\u0163\u0168\5*\26\25\u0164\u0165\f\23\2\2\u0165")
        buf.write(u"\u0166\7.\2\2\u0166\u0168\5*\26\24\u0167\u0158\3\2\2")
        buf.write(u"\2\u0167\u015b\3\2\2\2\u0167\u015e\3\2\2\2\u0167\u0161")
        buf.write(u"\3\2\2\2\u0167\u0164\3\2\2\2\u0168\u016b\3\2\2\2\u0169")
        buf.write(u"\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a+\3\2\2\2\u016b")
        buf.write(u"\u0169\3\2\2\2\u016c\u0171\7\4\2\2\u016d\u0170\5.\30")
        buf.write(u"\2\u016e\u0170\5\60\31\2\u016f\u016d\3\2\2\2\u016f\u016e")
        buf.write(u"\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171")
        buf.write(u"\u0172\3\2\2\2\u0172\u0174\3\2\2\2\u0173\u0171\3\2\2")
        buf.write(u"\2\u0174\u0175\7\5\2\2\u0175-\3\2\2\2\u0176\u0177\5*")
        buf.write(u"\26\2\u0177/\3\2\2\2\u0178\u017b\7\23\2\2\u0179\u017c")
        buf.write(u"\7(\2\2\u017a\u017c\5&\24\2\u017b\u0179\3\2\2\2\u017b")
        buf.write(u"\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u0180\7\24\2")
        buf.write(u"\2\u017e\u0181\7(\2\2\u017f\u0181\5:\36\2\u0180\u017e")
        buf.write(u"\3\2\2\2\u0180\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write(u"\u0183\7\32\2\2\u0183\61\3\2\2\2\u0184\u0185\7\60\2\2")
        buf.write(u"\u0185\63\3\2\2\2\u0186\u0188\5\66\34\2\u0187\u0186\3")
        buf.write(u"\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189")
        buf.write(u"\u018a\3\2\2\2\u018a\u018c\3\2\2\2\u018b\u0189\3\2\2")
        buf.write(u"\2\u018c\u018d\5*\26\2\u018d\u018e\t\6\2\2\u018e\u0192")
        buf.write(u"\5*\26\2\u018f\u0191\58\35\2\u0190\u018f\3\2\2\2\u0191")
        buf.write(u"\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2")
        buf.write(u"\2\u0193\u0199\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u0196")
        buf.write(u"\t\7\2\2\u0196\u0198\5\64\33\2\u0197\u0195\3\2\2\2\u0198")
        buf.write(u"\u019b\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2")
        buf.write(u"\2\u019a\65\3\2\2\2\u019b\u0199\3\2\2\2\u019c\u019d\7")
        buf.write(u"\25\2\2\u019d\67\3\2\2\2\u019e\u019f\7\26\2\2\u019f9")
        buf.write(u"\3\2\2\2\u01a0\u01a1\7(\2\2\u01a1\u01a5\7\25\2\2\u01a2")
        buf.write(u"\u01a4\5\66\34\2\u01a3\u01a2\3\2\2\2\u01a4\u01a7\3\2")
        buf.write(u"\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01b2")
        buf.write(u"\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01ad\5*\26\2\u01a9")
        buf.write(u"\u01aa\7\f\2\2\u01aa\u01ac\5*\26\2\u01ab\u01a9\3\2\2")
        buf.write(u"\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae")
        buf.write(u"\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0")
        buf.write(u"\u01a8\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2")
        buf.write(u"\2\u01b2\u01b3\3\2\2\2\u01b3\u01b8\3\2\2\2\u01b4\u01b2")
        buf.write(u"\3\2\2\2\u01b5\u01b7\58\35\2\u01b6\u01b5\3\2\2\2\u01b7")
        buf.write(u"\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2")
        buf.write(u"\2\u01b9\u01bb\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc")
        buf.write(u"\7\26\2\2\u01bc;\3\2\2\2\u01bd\u01be\t\b\2\2\u01be=\3")
        buf.write(u"\2\2\2\60AFOWcjly\u0081\u008c\u008f\u009b\u00a3\u00af")
        buf.write(u"\u00b2\u00b8\u00ba\u00c6\u00d2\u00dc\u00ed\u00f3\u00f7")
        buf.write(u"\u00fc\u0104\u010a\u0110\u0114\u0119\u012b\u0131\u0133")
        buf.write(u"\u0156\u0167\u0169\u016f\u0171\u017b\u0180\u0189\u0192")
        buf.write(u"\u0199\u01a5\u01ad\u01b2\u01b8")
        return buf.getvalue()
		

class PrigogineParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'model'", u"'['", u"']'", u"'simulation'", 
                     u"'\n'", u"'\r'", u"'equations'", u"'[t+1]'", u"'='", 
                     u"','", u"'where'", u"'.'", u"'[n]'", u"'population'", 
                     u"'parameters'", u"'variables'", u"'for'", u"'in'", 
                     u"'('", u"')'", u"'[:]'", u"'t'", u"'print'", u"':'", 
                     u"'return'", u"'<'", u"'>'", u"'>='", u"'<='", u"'=='", 
                     u"'!='", u"'&'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'*'", u"'/'", u"'+'", u"'-'", u"'|'", u"'^'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"LineComment", u"NEWLINE", u"ML_COMMENT", 
                      u"INT", u"FLOAT", u"ID", u"WS", u"MUL", u"DIV", u"ADD", 
                      u"SUB", u"PIPE", u"POWER", u"STRING", u"ESC", u"SPACE" ]

    RULE_filestart = 0
    RULE_model = 1
    RULE_simulation = 2
    RULE_codeinsert = 3
    RULE_equationlist = 4
    RULE_elementwiseEquation = 5
    RULE_mapEquation = 6
    RULE_assignment = 7
    RULE_population = 8
    RULE_parameterlist = 9
    RULE_variablelist = 10
    RULE_listcomp = 11
    RULE_listdef = 12
    RULE_tupledef = 13
    RULE_variable = 14
    RULE_indexedvariable = 15
    RULE_parameter = 16
    RULE_timeindex = 17
    RULE_timevar = 18
    RULE_dictindex = 19
    RULE_expression = 20
    RULE_codeblock = 21
    RULE_codeline = 22
    RULE_pyforloop = 23
    RULE_string = 24
    RULE_conditional = 25
    RULE_lparen = 26
    RULE_rparen = 27
    RULE_func = 28
    RULE_number = 29

    ruleNames =  [ u"filestart", u"model", u"simulation", u"codeinsert", 
                   u"equationlist", u"elementwiseEquation", u"mapEquation", 
                   u"assignment", u"population", u"parameterlist", u"variablelist", 
                   u"listcomp", u"listdef", u"tupledef", u"variable", u"indexedvariable", 
                   u"parameter", u"timeindex", u"timevar", u"dictindex", 
                   u"expression", u"codeblock", u"codeline", u"pyforloop", 
                   u"string", u"conditional", u"lparen", u"rparen", u"func", 
                   u"number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    LineComment=33
    NEWLINE=34
    ML_COMMENT=35
    INT=36
    FLOAT=37
    ID=38
    WS=39
    MUL=40
    DIV=41
    ADD=42
    SUB=43
    PIPE=44
    POWER=45
    STRING=46
    ESC=47
    SPACE=48

    def __init__(self, input):
        super(PrigogineParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class FilestartContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.FilestartContext, self).__init__(parent, invokingState)
            self.parser = parser

        def model(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ModelContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ModelContext,i)


        def simulation(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.SimulationContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.SimulationContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_filestart

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterFilestart(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitFilestart(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitFilestart(self)
            else:
                return visitor.visitChildren(self)




    def filestart(self):

        localctx = PrigogineParser.FilestartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_filestart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60 
                self.model()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrigogineParser.T__0):
                    break

            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__3:
                self.state = 65 
                self.simulation()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModelContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.ModelContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def variablelist(self):
            return self.getTypedRuleContext(PrigogineParser.VariablelistContext,0)


        def equationlist(self):
            return self.getTypedRuleContext(PrigogineParser.EquationlistContext,0)


        def parameterlist(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ParameterlistContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ParameterlistContext,i)


        def population(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.PopulationContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.PopulationContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_model

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterModel(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitModel(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitModel(self)
            else:
                return visitor.visitChildren(self)




    def model(self):

        localctx = PrigogineParser.ModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(PrigogineParser.T__0)
            self.state = 72
            self.match(PrigogineParser.ID)
            self.state = 73
            self.match(PrigogineParser.T__1)

            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__14:
                self.state = 74 
                self.parameterlist()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80 
            self.variablelist()
            self.state = 81 
            self.equationlist()
            self.state = 83 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 82 
                self.population()
                self.state = 85 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrigogineParser.T__13):
                    break

            self.state = 87
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimulationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.SimulationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def codeinsert(self):
            return self.getTypedRuleContext(PrigogineParser.CodeinsertContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_simulation

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterSimulation(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitSimulation(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitSimulation(self)
            else:
                return visitor.visitChildren(self)




    def simulation(self):

        localctx = PrigogineParser.SimulationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simulation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(PrigogineParser.T__3)
            self.state = 90
            self.match(PrigogineParser.T__1)
            self.state = 91 
            self.codeinsert()
            self.state = 92
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CodeinsertContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.CodeinsertContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PrigogineParser.RULE_codeinsert

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterCodeinsert(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitCodeinsert(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitCodeinsert(self)
            else:
                return visitor.visitChildren(self)




    def codeinsert(self):

        localctx = PrigogineParser.CodeinsertContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_codeinsert)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 94
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==PrigogineParser.T__4 or _la==PrigogineParser.T__5:
                        self._errHandler.recoverInline(self)
                    self.consume() 
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EquationlistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.EquationlistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def elementwiseEquation(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ElementwiseEquationContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ElementwiseEquationContext,i)


        def mapEquation(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.MapEquationContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.MapEquationContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_equationlist

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterEquationlist(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitEquationlist(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitEquationlist(self)
            else:
                return visitor.visitChildren(self)




    def equationlist(self):

        localctx = PrigogineParser.EquationlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_equationlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(PrigogineParser.T__6)
            self.state = 101
            self.match(PrigogineParser.T__1)
            self.state = 104 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 102 
                    self.elementwiseEquation()
                    pass

                elif la_ == 2:
                    self.state = 103 
                    self.mapEquation()
                    pass


                self.state = 106 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrigogineParser.ID):
                    break

            self.state = 108
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementwiseEquationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.ElementwiseEquationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i=None):
            if i is None:
                return self.getTokens(PrigogineParser.ID)
            else:
                return self.getToken(PrigogineParser.ID, i)

        def expression(self):
            return self.getTypedRuleContext(PrigogineParser.ExpressionContext,0)


        def conditional(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ConditionalContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_elementwiseEquation

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterElementwiseEquation(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitElementwiseEquation(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitElementwiseEquation(self)
            else:
                return visitor.visitChildren(self)




    def elementwiseEquation(self):

        localctx = PrigogineParser.ElementwiseEquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elementwiseEquation)
        self._la = 0 # Token type
        try:
            self.state = 141
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(PrigogineParser.ID)
                self.state = 111
                self.match(PrigogineParser.T__7)
                self.state = 112
                self.match(PrigogineParser.T__8)
                self.state = 113 
                self.expression(0)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 114
                    self.match(PrigogineParser.T__9)
                    self.state = 115
                    self.match(PrigogineParser.T__10)
                    self.state = 116 
                    self.conditional()
                    self.state = 121
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.match(PrigogineParser.ID)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__11:
                    self.state = 123
                    self.match(PrigogineParser.T__11)
                    self.state = 124
                    self.match(PrigogineParser.ID)
                    self.state = 129
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 130
                self.match(PrigogineParser.T__7)
                self.state = 131
                self.match(PrigogineParser.T__8)
                self.state = 132 
                self.expression(0)
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 133
                    self.match(PrigogineParser.T__9)
                    self.state = 134
                    self.match(PrigogineParser.T__10)
                    self.state = 135 
                    self.conditional()
                    self.state = 140
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MapEquationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.MapEquationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i=None):
            if i is None:
                return self.getTokens(PrigogineParser.ID)
            else:
                return self.getToken(PrigogineParser.ID, i)

        def expression(self):
            return self.getTypedRuleContext(PrigogineParser.ExpressionContext,0)


        def conditional(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ConditionalContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_mapEquation

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterMapEquation(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitMapEquation(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitMapEquation(self)
            else:
                return visitor.visitChildren(self)




    def mapEquation(self):

        localctx = PrigogineParser.MapEquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mapEquation)
        self._la = 0 # Token type
        try:
            self.state = 176
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(PrigogineParser.ID)
                self.state = 144
                self.match(PrigogineParser.T__7)
                self.state = 145
                self.match(PrigogineParser.T__12)
                self.state = 146
                self.match(PrigogineParser.T__8)
                self.state = 147 
                self.expression(0)
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 148
                    self.match(PrigogineParser.T__9)
                    self.state = 149
                    self.match(PrigogineParser.T__10)
                    self.state = 150 
                    self.conditional()
                    self.state = 155
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(PrigogineParser.ID)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__11:
                    self.state = 157
                    self.match(PrigogineParser.T__11)
                    self.state = 158
                    self.match(PrigogineParser.ID)
                    self.state = 163
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 164
                self.match(PrigogineParser.T__7)
                self.state = 165
                self.match(PrigogineParser.T__12)
                self.state = 166
                self.match(PrigogineParser.T__8)
                self.state = 167 
                self.expression(0)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 168
                    self.match(PrigogineParser.T__9)
                    self.state = 169
                    self.match(PrigogineParser.T__10)
                    self.state = 170 
                    self.conditional()
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.AssignmentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i=None):
            if i is None:
                return self.getTokens(PrigogineParser.ID)
            else:
                return self.getToken(PrigogineParser.ID, i)

        def expression(self):
            return self.getTypedRuleContext(PrigogineParser.ExpressionContext,0)


        def timeindex(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.TimeindexContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.TimeindexContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_assignment

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterAssignment(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitAssignment(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = PrigogineParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(PrigogineParser.ID)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__11) | (1 << PrigogineParser.T__20))) != 0):
                self.state = 182
                token = self._input.LA(1)
                if token in [PrigogineParser.T__11]:
                    self.state = 179
                    self.match(PrigogineParser.T__11)
                    self.state = 180
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.T__1, PrigogineParser.T__20]:
                    self.state = 181 
                    self.timeindex()

                else:
                    raise NoViableAltException(self)

                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self.match(PrigogineParser.T__8)
            self.state = 188 
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PopulationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.PopulationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def variablelist(self):
            return self.getTypedRuleContext(PrigogineParser.VariablelistContext,0)


        def equationlist(self):
            return self.getTypedRuleContext(PrigogineParser.EquationlistContext,0)


        def parameterlist(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ParameterlistContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ParameterlistContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_population

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterPopulation(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitPopulation(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitPopulation(self)
            else:
                return visitor.visitChildren(self)




    def population(self):

        localctx = PrigogineParser.PopulationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_population)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(PrigogineParser.T__13)
            self.state = 191
            self.match(PrigogineParser.ID)
            self.state = 192
            self.match(PrigogineParser.T__1)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__14:
                self.state = 193 
                self.parameterlist()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199 
            self.variablelist()
            self.state = 200 
            self.equationlist()
            self.state = 201
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterlistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.ParameterlistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ParameterContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ParameterContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_parameterlist

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterParameterlist(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitParameterlist(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitParameterlist(self)
            else:
                return visitor.visitChildren(self)




    def parameterlist(self):

        localctx = PrigogineParser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameterlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(PrigogineParser.T__14)
            self.state = 204
            self.match(PrigogineParser.T__1)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 205 
                self.parameter()
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 211
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariablelistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.VariablelistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.VariableContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.VariableContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_variablelist

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterVariablelist(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitVariablelist(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitVariablelist(self)
            else:
                return visitor.visitChildren(self)




    def variablelist(self):

        localctx = PrigogineParser.VariablelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variablelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(PrigogineParser.T__15)
            self.state = 214
            self.match(PrigogineParser.T__1)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 215 
                self.variable()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListcompContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.ListcompContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ExpressionContext,i)


        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def getRuleIndex(self):
            return PrigogineParser.RULE_listcomp

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterListcomp(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitListcomp(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitListcomp(self)
            else:
                return visitor.visitChildren(self)




    def listcomp(self):

        localctx = PrigogineParser.ListcompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listcomp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(PrigogineParser.T__1)
            self.state = 224 
            self.expression(0)
            self.state = 225
            self.match(PrigogineParser.T__16)
            self.state = 226
            self.match(PrigogineParser.ID)
            self.state = 227
            self.match(PrigogineParser.T__17)
            self.state = 228 
            self.expression(0)
            self.state = 229
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListdefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.ListdefContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i=None):
            if i is None:
                return self.getTokens(PrigogineParser.ID)
            else:
                return self.getToken(PrigogineParser.ID, i)

        def number(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.NumberContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.NumberContext,i)


        def string(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.StringContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.StringContext,i)


        def listdef(self):
            return self.getTypedRuleContext(PrigogineParser.ListdefContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_listdef

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterListdef(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitListdef(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitListdef(self)
            else:
                return visitor.visitChildren(self)




    def listdef(self):

        localctx = PrigogineParser.ListdefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_listdef)
        self._la = 0 # Token type
        try:
            self.state = 258
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(PrigogineParser.T__1)
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                    self.state = 235
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 232
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 233 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 234 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 245
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==PrigogineParser.T__9:
                        self.state = 237
                        self.match(PrigogineParser.T__9)
                        self.state = 241
                        token = self._input.LA(1)
                        if token in [PrigogineParser.ID]:
                            self.state = 238
                            self.match(PrigogineParser.ID)

                        elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                            self.state = 239 
                            self.number()

                        elif token in [PrigogineParser.STRING]:
                            self.state = 240 
                            self.string()

                        else:
                            raise NoViableAltException(self)

                        self.state = 247
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 252
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 253
                self.match(PrigogineParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(PrigogineParser.T__1)
                self.state = 255 
                self.listdef()
                self.state = 256
                self.match(PrigogineParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TupledefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.TupledefContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i=None):
            if i is None:
                return self.getTokens(PrigogineParser.ID)
            else:
                return self.getToken(PrigogineParser.ID, i)

        def number(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.NumberContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.NumberContext,i)


        def string(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.StringContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.StringContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_tupledef

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterTupledef(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitTupledef(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitTupledef(self)
            else:
                return visitor.visitChildren(self)




    def tupledef(self):

        localctx = PrigogineParser.TupledefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_tupledef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(PrigogineParser.T__18)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 264
                token = self._input.LA(1)
                if token in [PrigogineParser.ID]:
                    self.state = 261
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                    self.state = 262 
                    self.number()

                elif token in [PrigogineParser.STRING]:
                    self.state = 263 
                    self.string()

                else:
                    raise NoViableAltException(self)

                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 266
                    self.match(PrigogineParser.T__9)
                    self.state = 270
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 267
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 268 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 269 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 276
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 282
            self.match(PrigogineParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.VariableContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def getRuleIndex(self):
            return PrigogineParser.RULE_variable

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterVariable(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitVariable(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = PrigogineParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(PrigogineParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IndexedvariableContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.IndexedvariableContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def timeindex(self):
            return self.getTypedRuleContext(PrigogineParser.TimeindexContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_indexedvariable

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterIndexedvariable(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitIndexedvariable(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitIndexedvariable(self)
            else:
                return visitor.visitChildren(self)




    def indexedvariable(self):

        localctx = PrigogineParser.IndexedvariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_indexedvariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(PrigogineParser.ID)
            self.state = 287 
            self.timeindex()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.ParameterContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def getRuleIndex(self):
            return PrigogineParser.RULE_parameter

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterParameter(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitParameter(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = PrigogineParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(PrigogineParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TimeindexContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.TimeindexContext, self).__init__(parent, invokingState)
            self.parser = parser

        def timevar(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.TimevarContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.TimevarContext,i)


        def SUB(self, i=None):
            if i is None:
                return self.getTokens(PrigogineParser.SUB)
            else:
                return self.getToken(PrigogineParser.SUB, i)

        def INT(self, i=None):
            if i is None:
                return self.getTokens(PrigogineParser.INT)
            else:
                return self.getToken(PrigogineParser.INT, i)

        def getRuleIndex(self):
            return PrigogineParser.RULE_timeindex

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterTimeindex(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitTimeindex(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitTimeindex(self)
            else:
                return visitor.visitChildren(self)




    def timeindex(self):

        localctx = PrigogineParser.TimeindexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_timeindex)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 303
                    token = self._input.LA(1)
                    if token in [PrigogineParser.T__1]:
                        self.state = 291
                        self.match(PrigogineParser.T__1)
                        self.state = 292 
                        self.timevar()
                        self.state = 297
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==PrigogineParser.SUB:
                            self.state = 293
                            self.match(PrigogineParser.SUB)
                            self.state = 294
                            self.match(PrigogineParser.INT)
                            self.state = 299
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 300
                        self.match(PrigogineParser.T__2)

                    elif token in [PrigogineParser.T__20]:
                        self.state = 302
                        self.match(PrigogineParser.T__20)

                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 305 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TimevarContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.TimevarContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PrigogineParser.INT, 0)

        def getRuleIndex(self):
            return PrigogineParser.RULE_timevar

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterTimevar(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitTimevar(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitTimevar(self)
            else:
                return visitor.visitChildren(self)




    def timevar(self):

        localctx = PrigogineParser.TimevarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_timevar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            _la = self._input.LA(1)
            if not(_la==PrigogineParser.T__21 or _la==PrigogineParser.INT):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DictindexContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.DictindexContext, self).__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(PrigogineParser.StringContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_dictindex

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterDictindex(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitDictindex(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitDictindex(self)
            else:
                return visitor.visitChildren(self)




    def dictindex(self):

        localctx = PrigogineParser.DictindexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_dictindex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(PrigogineParser.T__1)
            self.state = 310 
            self.string()
            self.state = 311
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ExpressionContext,i)


        def assignment(self):
            return self.getTypedRuleContext(PrigogineParser.AssignmentContext,0)


        def pyforloop(self):
            return self.getTypedRuleContext(PrigogineParser.PyforloopContext,0)


        def string(self):
            return self.getTypedRuleContext(PrigogineParser.StringContext,0)


        def listdef(self):
            return self.getTypedRuleContext(PrigogineParser.ListdefContext,0)


        def tupledef(self):
            return self.getTypedRuleContext(PrigogineParser.TupledefContext,0)


        def number(self):
            return self.getTypedRuleContext(PrigogineParser.NumberContext,0)


        def func(self):
            return self.getTypedRuleContext(PrigogineParser.FuncContext,0)


        def listcomp(self):
            return self.getTypedRuleContext(PrigogineParser.ListcompContext,0)


        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def indexedvariable(self):
            return self.getTypedRuleContext(PrigogineParser.IndexedvariableContext,0)


        def timevar(self):
            return self.getTypedRuleContext(PrigogineParser.TimevarContext,0)


        def lparen(self):
            return self.getTypedRuleContext(PrigogineParser.LparenContext,0)


        def rparen(self):
            return self.getTypedRuleContext(PrigogineParser.RparenContext,0)


        def POWER(self):
            return self.getToken(PrigogineParser.POWER, 0)

        def MUL(self):
            return self.getToken(PrigogineParser.MUL, 0)

        def DIV(self):
            return self.getToken(PrigogineParser.DIV, 0)

        def ADD(self):
            return self.getToken(PrigogineParser.ADD, 0)

        def SUB(self):
            return self.getToken(PrigogineParser.SUB, 0)

        def PIPE(self):
            return self.getToken(PrigogineParser.PIPE, 0)

        def getRuleIndex(self):
            return PrigogineParser.RULE_expression

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PrigogineParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 314
                self.match(PrigogineParser.T__22)
                self.state = 315 
                self.expression(13)
                pass

            elif la_ == 2:
                self.state = 316 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 317 
                self.pyforloop()
                pass

            elif la_ == 4:
                self.state = 318
                self.match(PrigogineParser.T__22)
                self.state = 319 
                self.string()
                pass

            elif la_ == 5:
                self.state = 320
                self.match(PrigogineParser.T__22)
                self.state = 321 
                self.string()
                self.state = 322
                self.match(PrigogineParser.T__9)
                pass

            elif la_ == 6:
                self.state = 324 
                self.listdef()
                pass

            elif la_ == 7:
                self.state = 325 
                self.tupledef()
                pass

            elif la_ == 8:
                self.state = 326 
                self.string()
                pass

            elif la_ == 9:
                self.state = 327 
                self.number()
                pass

            elif la_ == 10:
                self.state = 328 
                self.func()
                pass

            elif la_ == 11:
                self.state = 329 
                self.listcomp()
                pass

            elif la_ == 12:
                self.state = 330
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 13:
                self.state = 331
                self.match(PrigogineParser.T__23)
                pass

            elif la_ == 14:
                self.state = 332 
                self.indexedvariable()
                pass

            elif la_ == 15:
                self.state = 333 
                self.timevar()
                pass

            elif la_ == 16:
                self.state = 334 
                self.lparen()
                self.state = 335 
                self.expression(0)
                self.state = 336 
                self.rparen()
                pass

            elif la_ == 17:
                self.state = 338
                self.match(PrigogineParser.T__24)
                self.state = 339
                self.match(PrigogineParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 359
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 357
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 342
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 343
                        self.match(PrigogineParser.T__11)
                        self.state = 344 
                        self.expression(22)
                        pass

                    elif la_ == 2:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 345
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 346
                        self.match(PrigogineParser.POWER)
                        self.state = 347 
                        self.expression(21)
                        pass

                    elif la_ == 3:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 348
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 349
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.MUL or _la==PrigogineParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 350 
                        self.expression(20)
                        pass

                    elif la_ == 4:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 351
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 352
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 353 
                        self.expression(19)
                        pass

                    elif la_ == 5:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 354
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 355
                        localctx.op = self.match(PrigogineParser.PIPE)
                        self.state = 356 
                        self.expression(18)
                        pass

             
                self.state = 361
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class CodeblockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.CodeblockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def codeline(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.CodelineContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.CodelineContext,i)


        def pyforloop(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.PyforloopContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.PyforloopContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_codeblock

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterCodeblock(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitCodeblock(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitCodeblock(self)
            else:
                return visitor.visitChildren(self)




    def codeblock(self):

        localctx = PrigogineParser.CodeblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_codeblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(PrigogineParser.T__1)
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__16) | (1 << PrigogineParser.T__18) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.T__22) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 365
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 363 
                    self.codeline()
                    pass

                elif la_ == 2:
                    self.state = 364 
                    self.pyforloop()
                    pass


                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 370
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CodelineContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.CodelineContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PrigogineParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_codeline

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterCodeline(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitCodeline(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitCodeline(self)
            else:
                return visitor.visitChildren(self)




    def codeline(self):

        localctx = PrigogineParser.CodelineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_codeline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372 
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PyforloopContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.PyforloopContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i=None):
            if i is None:
                return self.getTokens(PrigogineParser.ID)
            else:
                return self.getToken(PrigogineParser.ID, i)

        def timevar(self):
            return self.getTypedRuleContext(PrigogineParser.TimevarContext,0)


        def func(self):
            return self.getTypedRuleContext(PrigogineParser.FuncContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_pyforloop

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterPyforloop(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitPyforloop(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitPyforloop(self)
            else:
                return visitor.visitChildren(self)




    def pyforloop(self):

        localctx = PrigogineParser.PyforloopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_pyforloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(PrigogineParser.T__16)
            self.state = 377
            token = self._input.LA(1)
            if token in [PrigogineParser.ID]:
                self.state = 375
                self.match(PrigogineParser.ID)

            elif token in [PrigogineParser.T__21, PrigogineParser.INT]:
                self.state = 376 
                self.timevar()

            else:
                raise NoViableAltException(self)

            self.state = 379
            self.match(PrigogineParser.T__17)
            self.state = 382
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 380
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 2:
                self.state = 381 
                self.func()
                pass


            self.state = 384
            self.match(PrigogineParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.StringContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(PrigogineParser.STRING, 0)

        def getRuleIndex(self):
            return PrigogineParser.RULE_string

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterString(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitString(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = PrigogineParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(PrigogineParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.ConditionalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ExpressionContext,i)


        def lparen(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.LparenContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.LparenContext,i)


        def rparen(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.RparenContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.RparenContext,i)


        def conditional(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ConditionalContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_conditional

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterConditional(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitConditional(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = PrigogineParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 388 
                    self.lparen() 
                self.state = 393
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

            self.state = 394 
            self.expression(0)
            self.state = 395
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__25) | (1 << PrigogineParser.T__26) | (1 << PrigogineParser.T__27) | (1 << PrigogineParser.T__28) | (1 << PrigogineParser.T__29) | (1 << PrigogineParser.T__30))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            self.consume()
            self.state = 396 
            self.expression(0)
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__19:
                self.state = 397 
                self.rparen()
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 407
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 403
                    _la = self._input.LA(1)
                    if not(_la==PrigogineParser.T__31 or _la==PrigogineParser.PIPE):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 404 
                    self.conditional() 
                self.state = 409
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LparenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.LparenContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PrigogineParser.RULE_lparen

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterLparen(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitLparen(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitLparen(self)
            else:
                return visitor.visitChildren(self)




    def lparen(self):

        localctx = PrigogineParser.LparenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_lparen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(PrigogineParser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RparenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.RparenContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PrigogineParser.RULE_rparen

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterRparen(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitRparen(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitRparen(self)
            else:
                return visitor.visitChildren(self)




    def rparen(self):

        localctx = PrigogineParser.RparenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_rparen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(PrigogineParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.FuncContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def lparen(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.LparenContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.LparenContext,i)


        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ExpressionContext,i)


        def rparen(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.RparenContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.RparenContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_func

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterFunc(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitFunc(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = PrigogineParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(PrigogineParser.ID)
            self.state = 415
            self.match(PrigogineParser.T__18)
            self.state = 419
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 416 
                    self.lparen() 
                self.state = 421
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__16) | (1 << PrigogineParser.T__18) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.T__22) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 422 
                self.expression(0)
                self.state = 427
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 423
                    self.match(PrigogineParser.T__9)
                    self.state = 424 
                    self.expression(0)
                    self.state = 429
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 434
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 438
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 435 
                    self.rparen() 
                self.state = 440
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

            self.state = 441
            self.match(PrigogineParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.NumberContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PrigogineParser.INT, 0)

        def FLOAT(self):
            return self.getToken(PrigogineParser.FLOAT, 0)

        def getRuleIndex(self):
            return PrigogineParser.RULE_number

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterNumber(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitNumber(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = PrigogineParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            _la = self._input.LA(1)
            if not(_la==PrigogineParser.INT or _la==PrigogineParser.FLOAT):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[20] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 17)
         



