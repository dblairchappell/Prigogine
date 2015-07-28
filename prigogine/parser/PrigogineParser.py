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
        buf.write(u"\62\u01c1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\3\2\6\2@\n\2\r\2\16\2A\3\2")
        buf.write(u"\7\2E\n\2\f\2\16\2H\13\2\3\3\3\3\3\3\3\3\7\3N\n\3\f\3")
        buf.write(u"\16\3Q\13\3\3\3\3\3\3\3\6\3V\n\3\r\3\16\3W\3\3\3\3\3")
        buf.write(u"\4\3\4\3\4\3\4\3\4\3\5\7\5b\n\5\f\5\16\5e\13\5\3\6\3")
        buf.write(u"\6\3\6\3\6\7\6k\n\6\f\6\16\6n\13\6\3\6\3\6\3\7\3\7\3")
        buf.write(u"\7\3\7\3\7\3\7\3\7\7\7y\n\7\f\7\16\7|\13\7\3\7\3\7\3")
        buf.write(u"\7\7\7\u0081\n\7\f\7\16\7\u0084\13\7\3\7\3\7\3\7\3\7")
        buf.write(u"\3\7\3\7\7\7\u008c\n\7\f\7\16\7\u008f\13\7\5\7\u0091")
        buf.write(u"\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u009b\n\b\f")
        buf.write(u"\b\16\b\u009e\13\b\3\b\3\b\3\b\7\b\u00a3\n\b\f\b\16\b")
        buf.write(u"\u00a6\13\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00af\n\b")
        buf.write(u"\f\b\16\b\u00b2\13\b\5\b\u00b4\n\b\3\t\3\t\3\t\3\t\7")
        buf.write(u"\t\u00ba\n\t\f\t\16\t\u00bd\13\t\3\t\3\t\3\t\3\n\3\n")
        buf.write(u"\3\n\3\n\7\n\u00c6\n\n\f\n\16\n\u00c9\13\n\3\n\3\n\3")
        buf.write(u"\n\3\n\3\13\3\13\3\13\7\13\u00d2\n\13\f\13\16\13\u00d5")
        buf.write(u"\13\13\3\13\3\13\3\f\3\f\3\f\7\f\u00dc\n\f\f\f\16\f\u00df")
        buf.write(u"\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write(u"\16\3\16\3\16\5\16\u00ef\n\16\3\16\3\16\3\16\3\16\5\16")
        buf.write(u"\u00f5\n\16\7\16\u00f7\n\16\f\16\16\16\u00fa\13\16\7")
        buf.write(u"\16\u00fc\n\16\f\16\16\16\u00ff\13\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\5\16\u0106\n\16\3\17\3\17\3\17\3\17\5\17\u010c")
        buf.write(u"\n\17\3\17\3\17\3\17\3\17\5\17\u0112\n\17\7\17\u0114")
        buf.write(u"\n\17\f\17\16\17\u0117\13\17\7\17\u0119\n\17\f\17\16")
        buf.write(u"\17\u011c\13\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3")
        buf.write(u"\22\3\22\3\23\3\23\3\23\3\23\7\23\u012b\n\23\f\23\16")
        buf.write(u"\23\u012e\13\23\3\23\3\23\3\23\6\23\u0133\n\23\r\23\16")
        buf.write(u"\23\u0134\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\5\26\u0158\n\26\3\26\3\26\3\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write(u"\7\26\u0169\n\26\f\26\16\26\u016c\13\26\3\27\3\27\3\27")
        buf.write(u"\7\27\u0171\n\27\f\27\16\27\u0174\13\27\3\27\3\27\3\30")
        buf.write(u"\3\30\3\31\3\31\3\31\5\31\u017d\n\31\3\31\3\31\3\31\5")
        buf.write(u"\31\u0182\n\31\3\31\3\31\3\32\3\32\3\33\7\33\u0189\n")
        buf.write(u"\33\f\33\16\33\u018c\13\33\3\33\3\33\3\33\3\33\7\33\u0192")
        buf.write(u"\n\33\f\33\16\33\u0195\13\33\3\33\3\33\7\33\u0199\n\33")
        buf.write(u"\f\33\16\33\u019c\13\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write(u"\3\36\7\36\u01a5\n\36\f\36\16\36\u01a8\13\36\3\36\3\36")
        buf.write(u"\3\36\7\36\u01ad\n\36\f\36\16\36\u01b0\13\36\7\36\u01b2")
        buf.write(u"\n\36\f\36\16\36\u01b5\13\36\3\36\7\36\u01b8\n\36\f\36")
        buf.write(u"\16\36\u01bb\13\36\3\36\3\36\3\37\3\37\3\37\3c\3* \2")
        buf.write(u"\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write(u"\64\668:<\2\t\3\2\7\b\4\2\30\30&&\3\2*+\3\2,-\3\2\34")
        buf.write(u"!\4\2\"\"..\3\2&\'\u01e6\2?\3\2\2\2\4I\3\2\2\2\6[\3\2")
        buf.write(u"\2\2\bc\3\2\2\2\nf\3\2\2\2\f\u0090\3\2\2\2\16\u00b3\3")
        buf.write(u"\2\2\2\20\u00b5\3\2\2\2\22\u00c1\3\2\2\2\24\u00ce\3\2")
        buf.write(u"\2\2\26\u00d8\3\2\2\2\30\u00e2\3\2\2\2\32\u0105\3\2\2")
        buf.write(u"\2\34\u0107\3\2\2\2\36\u011f\3\2\2\2 \u0121\3\2\2\2\"")
        buf.write(u"\u0124\3\2\2\2$\u0132\3\2\2\2&\u0136\3\2\2\2(\u0138\3")
        buf.write(u"\2\2\2*\u0157\3\2\2\2,\u016d\3\2\2\2.\u0177\3\2\2\2\60")
        buf.write(u"\u0179\3\2\2\2\62\u0185\3\2\2\2\64\u018a\3\2\2\2\66\u019d")
        buf.write(u"\3\2\2\28\u019f\3\2\2\2:\u01a1\3\2\2\2<\u01be\3\2\2\2")
        buf.write(u">@\5\4\3\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2BF")
        buf.write(u"\3\2\2\2CE\5\6\4\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3")
        buf.write(u"\2\2\2G\3\3\2\2\2HF\3\2\2\2IJ\7\3\2\2JK\7(\2\2KO\7\4")
        buf.write(u"\2\2LN\5\24\13\2ML\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2")
        buf.write(u"\2\2PR\3\2\2\2QO\3\2\2\2RS\5\26\f\2SU\5\n\6\2TV\5\22")
        buf.write(u"\n\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2XY\3\2\2")
        buf.write(u"\2YZ\7\5\2\2Z\5\3\2\2\2[\\\7\6\2\2\\]\7\4\2\2]^\5\b\5")
        buf.write(u"\2^_\7\5\2\2_\7\3\2\2\2`b\n\2\2\2a`\3\2\2\2be\3\2\2\2")
        buf.write(u"cd\3\2\2\2ca\3\2\2\2d\t\3\2\2\2ec\3\2\2\2fg\7\t\2\2g")
        buf.write(u"l\7\4\2\2hk\5\f\7\2ik\5\16\b\2jh\3\2\2\2ji\3\2\2\2kn")
        buf.write(u"\3\2\2\2lj\3\2\2\2lm\3\2\2\2mo\3\2\2\2nl\3\2\2\2op\7")
        buf.write(u"\5\2\2p\13\3\2\2\2qr\7(\2\2rs\7\n\2\2st\7\13\2\2tz\5")
        buf.write(u"*\26\2uv\7\f\2\2vw\7\r\2\2wy\5\64\33\2xu\3\2\2\2y|\3")
        buf.write(u"\2\2\2zx\3\2\2\2z{\3\2\2\2{\u0091\3\2\2\2|z\3\2\2\2}")
        buf.write(u"\u0082\7(\2\2~\177\7\16\2\2\177\u0081\7(\2\2\u0080~\3")
        buf.write(u"\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082")
        buf.write(u"\u0083\3\2\2\2\u0083\u0085\3\2\2\2\u0084\u0082\3\2\2")
        buf.write(u"\2\u0085\u0086\7\n\2\2\u0086\u0087\7\13\2\2\u0087\u008d")
        buf.write(u"\5*\26\2\u0088\u0089\7\f\2\2\u0089\u008a\7\r\2\2\u008a")
        buf.write(u"\u008c\5\64\33\2\u008b\u0088\3\2\2\2\u008c\u008f\3\2")
        buf.write(u"\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0091")
        buf.write(u"\3\2\2\2\u008f\u008d\3\2\2\2\u0090q\3\2\2\2\u0090}\3")
        buf.write(u"\2\2\2\u0091\r\3\2\2\2\u0092\u0093\7(\2\2\u0093\u0094")
        buf.write(u"\7\n\2\2\u0094\u0095\7\17\2\2\u0095\u0096\7\13\2\2\u0096")
        buf.write(u"\u009c\5*\26\2\u0097\u0098\7\f\2\2\u0098\u0099\7\r\2")
        buf.write(u"\2\u0099\u009b\5\64\33\2\u009a\u0097\3\2\2\2\u009b\u009e")
        buf.write(u"\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write(u"\u00b4\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a4\7(\2\2")
        buf.write(u"\u00a0\u00a1\7\16\2\2\u00a1\u00a3\7(\2\2\u00a2\u00a0")
        buf.write(u"\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4")
        buf.write(u"\u00a5\3\2\2\2\u00a5\u00a7\3\2\2\2\u00a6\u00a4\3\2\2")
        buf.write(u"\2\u00a7\u00a8\7\n\2\2\u00a8\u00a9\7\17\2\2\u00a9\u00aa")
        buf.write(u"\7\13\2\2\u00aa\u00b0\5*\26\2\u00ab\u00ac\7\f\2\2\u00ac")
        buf.write(u"\u00ad\7\r\2\2\u00ad\u00af\5\64\33\2\u00ae\u00ab\3\2")
        buf.write(u"\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1")
        buf.write(u"\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3")
        buf.write(u"\u0092\3\2\2\2\u00b3\u009f\3\2\2\2\u00b4\17\3\2\2\2\u00b5")
        buf.write(u"\u00bb\7(\2\2\u00b6\u00b7\7\16\2\2\u00b7\u00ba\7(\2\2")
        buf.write(u"\u00b8\u00ba\5$\23\2\u00b9\u00b6\3\2\2\2\u00b9\u00b8")
        buf.write(u"\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb")
        buf.write(u"\u00bc\3\2\2\2\u00bc\u00be\3\2\2\2\u00bd\u00bb\3\2\2")
        buf.write(u"\2\u00be\u00bf\7\13\2\2\u00bf\u00c0\5*\26\2\u00c0\21")
        buf.write(u"\3\2\2\2\u00c1\u00c2\7\20\2\2\u00c2\u00c3\7(\2\2\u00c3")
        buf.write(u"\u00c7\7\4\2\2\u00c4\u00c6\5\24\13\2\u00c5\u00c4\3\2")
        buf.write(u"\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8")
        buf.write(u"\3\2\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca")
        buf.write(u"\u00cb\5\26\f\2\u00cb\u00cc\5\n\6\2\u00cc\u00cd\7\5\2")
        buf.write(u"\2\u00cd\23\3\2\2\2\u00ce\u00cf\7\21\2\2\u00cf\u00d3")
        buf.write(u"\7\4\2\2\u00d0\u00d2\5\"\22\2\u00d1\u00d0\3\2\2\2\u00d2")
        buf.write(u"\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2")
        buf.write(u"\2\u00d4\u00d6\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d7")
        buf.write(u"\7\5\2\2\u00d7\25\3\2\2\2\u00d8\u00d9\7\22\2\2\u00d9")
        buf.write(u"\u00dd\7\4\2\2\u00da\u00dc\5\36\20\2\u00db\u00da\3\2")
        buf.write(u"\2\2\u00dc\u00df\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de")
        buf.write(u"\3\2\2\2\u00de\u00e0\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0")
        buf.write(u"\u00e1\7\5\2\2\u00e1\27\3\2\2\2\u00e2\u00e3\7\4\2\2\u00e3")
        buf.write(u"\u00e4\5*\26\2\u00e4\u00e5\7\23\2\2\u00e5\u00e6\7(\2")
        buf.write(u"\2\u00e6\u00e7\7\24\2\2\u00e7\u00e8\5*\26\2\u00e8\u00e9")
        buf.write(u"\7\5\2\2\u00e9\31\3\2\2\2\u00ea\u00fd\7\4\2\2\u00eb\u00ef")
        buf.write(u"\7(\2\2\u00ec\u00ef\5<\37\2\u00ed\u00ef\5\62\32\2\u00ee")
        buf.write(u"\u00eb\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3\2\2")
        buf.write(u"\2\u00ef\u00f8\3\2\2\2\u00f0\u00f4\7\f\2\2\u00f1\u00f5")
        buf.write(u"\7(\2\2\u00f2\u00f5\5<\37\2\u00f3\u00f5\5\62\32\2\u00f4")
        buf.write(u"\u00f1\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f3\3\2\2")
        buf.write(u"\2\u00f5\u00f7\3\2\2\2\u00f6\u00f0\3\2\2\2\u00f7\u00fa")
        buf.write(u"\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9")
        buf.write(u"\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00ee\3\2\2")
        buf.write(u"\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe")
        buf.write(u"\3\2\2\2\u00fe\u0100\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100")
        buf.write(u"\u0106\7\5\2\2\u0101\u0102\7\4\2\2\u0102\u0103\5\32\16")
        buf.write(u"\2\u0103\u0104\7\5\2\2\u0104\u0106\3\2\2\2\u0105\u00ea")
        buf.write(u"\3\2\2\2\u0105\u0101\3\2\2\2\u0106\33\3\2\2\2\u0107\u011a")
        buf.write(u"\7\25\2\2\u0108\u010c\7(\2\2\u0109\u010c\5<\37\2\u010a")
        buf.write(u"\u010c\5\62\32\2\u010b\u0108\3\2\2\2\u010b\u0109\3\2")
        buf.write(u"\2\2\u010b\u010a\3\2\2\2\u010c\u0115\3\2\2\2\u010d\u0111")
        buf.write(u"\7\f\2\2\u010e\u0112\7(\2\2\u010f\u0112\5<\37\2\u0110")
        buf.write(u"\u0112\5\62\32\2\u0111\u010e\3\2\2\2\u0111\u010f\3\2")
        buf.write(u"\2\2\u0111\u0110\3\2\2\2\u0112\u0114\3\2\2\2\u0113\u010d")
        buf.write(u"\3\2\2\2\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115")
        buf.write(u"\u0116\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115\3\2\2")
        buf.write(u"\2\u0118\u010b\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118")
        buf.write(u"\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d\3\2\2\2\u011c")
        buf.write(u"\u011a\3\2\2\2\u011d\u011e\7\26\2\2\u011e\35\3\2\2\2")
        buf.write(u"\u011f\u0120\7(\2\2\u0120\37\3\2\2\2\u0121\u0122\7(\2")
        buf.write(u"\2\u0122\u0123\5$\23\2\u0123!\3\2\2\2\u0124\u0125\7(")
        buf.write(u"\2\2\u0125#\3\2\2\2\u0126\u0127\7\4\2\2\u0127\u012c\5")
        buf.write(u"&\24\2\u0128\u0129\7-\2\2\u0129\u012b\7&\2\2\u012a\u0128")
        buf.write(u"\3\2\2\2\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2\2\u012c")
        buf.write(u"\u012d\3\2\2\2\u012d\u012f\3\2\2\2\u012e\u012c\3\2\2")
        buf.write(u"\2\u012f\u0130\7\5\2\2\u0130\u0133\3\2\2\2\u0131\u0133")
        buf.write(u"\7\27\2\2\u0132\u0126\3\2\2\2\u0132\u0131\3\2\2\2\u0133")
        buf.write(u"\u0134\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2")
        buf.write(u"\2\u0135%\3\2\2\2\u0136\u0137\t\3\2\2\u0137\'\3\2\2\2")
        buf.write(u"\u0138\u0139\7\4\2\2\u0139\u013a\5\62\32\2\u013a\u013b")
        buf.write(u"\7\5\2\2\u013b)\3\2\2\2\u013c\u013d\b\26\1\2\u013d\u013e")
        buf.write(u"\7\31\2\2\u013e\u0158\5*\26\17\u013f\u0158\5\20\t\2\u0140")
        buf.write(u"\u0158\5\60\31\2\u0141\u0142\7\31\2\2\u0142\u0158\5\62")
        buf.write(u"\32\2\u0143\u0144\7\31\2\2\u0144\u0145\5\62\32\2\u0145")
        buf.write(u"\u0146\7\f\2\2\u0146\u0158\3\2\2\2\u0147\u0158\5\32\16")
        buf.write(u"\2\u0148\u0158\5\34\17\2\u0149\u0158\5\62\32\2\u014a")
        buf.write(u"\u0158\5<\37\2\u014b\u0158\5:\36\2\u014c\u0158\5\30\r")
        buf.write(u"\2\u014d\u0158\7(\2\2\u014e\u0158\7\32\2\2\u014f\u0158")
        buf.write(u"\5 \21\2\u0150\u0158\5&\24\2\u0151\u0152\5\66\34\2\u0152")
        buf.write(u"\u0153\5*\26\2\u0153\u0154\58\35\2\u0154\u0158\3\2\2")
        buf.write(u"\2\u0155\u0156\7\33\2\2\u0156\u0158\7(\2\2\u0157\u013c")
        buf.write(u"\3\2\2\2\u0157\u013f\3\2\2\2\u0157\u0140\3\2\2\2\u0157")
        buf.write(u"\u0141\3\2\2\2\u0157\u0143\3\2\2\2\u0157\u0147\3\2\2")
        buf.write(u"\2\u0157\u0148\3\2\2\2\u0157\u0149\3\2\2\2\u0157\u014a")
        buf.write(u"\3\2\2\2\u0157\u014b\3\2\2\2\u0157\u014c\3\2\2\2\u0157")
        buf.write(u"\u014d\3\2\2\2\u0157\u014e\3\2\2\2\u0157\u014f\3\2\2")
        buf.write(u"\2\u0157\u0150\3\2\2\2\u0157\u0151\3\2\2\2\u0157\u0155")
        buf.write(u"\3\2\2\2\u0158\u016a\3\2\2\2\u0159\u015a\f\27\2\2\u015a")
        buf.write(u"\u015b\7\16\2\2\u015b\u0169\5*\26\30\u015c\u015d\f\26")
        buf.write(u"\2\2\u015d\u015e\7/\2\2\u015e\u0169\5*\26\27\u015f\u0160")
        buf.write(u"\f\25\2\2\u0160\u0161\t\4\2\2\u0161\u0169\5*\26\26\u0162")
        buf.write(u"\u0163\f\24\2\2\u0163\u0164\t\5\2\2\u0164\u0169\5*\26")
        buf.write(u"\25\u0165\u0166\f\23\2\2\u0166\u0167\7.\2\2\u0167\u0169")
        buf.write(u"\5*\26\24\u0168\u0159\3\2\2\2\u0168\u015c\3\2\2\2\u0168")
        buf.write(u"\u015f\3\2\2\2\u0168\u0162\3\2\2\2\u0168\u0165\3\2\2")
        buf.write(u"\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b")
        buf.write(u"\3\2\2\2\u016b+\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u0172")
        buf.write(u"\7\4\2\2\u016e\u0171\5.\30\2\u016f\u0171\5\60\31\2\u0170")
        buf.write(u"\u016e\3\2\2\2\u0170\u016f\3\2\2\2\u0171\u0174\3\2\2")
        buf.write(u"\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0175")
        buf.write(u"\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0176\7\5\2\2\u0176")
        buf.write(u"-\3\2\2\2\u0177\u0178\5*\26\2\u0178/\3\2\2\2\u0179\u017c")
        buf.write(u"\7\23\2\2\u017a\u017d\7(\2\2\u017b\u017d\5&\24\2\u017c")
        buf.write(u"\u017a\3\2\2\2\u017c\u017b\3\2\2\2\u017d\u017e\3\2\2")
        buf.write(u"\2\u017e\u0181\7\24\2\2\u017f\u0182\7(\2\2\u0180\u0182")
        buf.write(u"\5:\36\2\u0181\u017f\3\2\2\2\u0181\u0180\3\2\2\2\u0182")
        buf.write(u"\u0183\3\2\2\2\u0183\u0184\7\32\2\2\u0184\61\3\2\2\2")
        buf.write(u"\u0185\u0186\7\60\2\2\u0186\63\3\2\2\2\u0187\u0189\5")
        buf.write(u"\66\34\2\u0188\u0187\3\2\2\2\u0189\u018c\3\2\2\2\u018a")
        buf.write(u"\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018d\3\2\2")
        buf.write(u"\2\u018c\u018a\3\2\2\2\u018d\u018e\5*\26\2\u018e\u018f")
        buf.write(u"\t\6\2\2\u018f\u0193\5*\26\2\u0190\u0192\58\35\2\u0191")
        buf.write(u"\u0190\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2")
        buf.write(u"\2\u0193\u0194\3\2\2\2\u0194\u019a\3\2\2\2\u0195\u0193")
        buf.write(u"\3\2\2\2\u0196\u0197\t\7\2\2\u0197\u0199\5\64\33\2\u0198")
        buf.write(u"\u0196\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2")
        buf.write(u"\2\u019a\u019b\3\2\2\2\u019b\65\3\2\2\2\u019c\u019a\3")
        buf.write(u"\2\2\2\u019d\u019e\7\25\2\2\u019e\67\3\2\2\2\u019f\u01a0")
        buf.write(u"\7\26\2\2\u01a09\3\2\2\2\u01a1\u01a2\7(\2\2\u01a2\u01a6")
        buf.write(u"\7\25\2\2\u01a3\u01a5\5\66\34\2\u01a4\u01a3\3\2\2\2\u01a5")
        buf.write(u"\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2")
        buf.write(u"\2\u01a7\u01b3\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01ae")
        buf.write(u"\5*\26\2\u01aa\u01ab\7\f\2\2\u01ab\u01ad\5*\26\2\u01ac")
        buf.write(u"\u01aa\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2")
        buf.write(u"\2\u01ae\u01af\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0\u01ae")
        buf.write(u"\3\2\2\2\u01b1\u01a9\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3")
        buf.write(u"\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b9\3\2\2")
        buf.write(u"\2\u01b5\u01b3\3\2\2\2\u01b6\u01b8\58\35\2\u01b7\u01b6")
        buf.write(u"\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write(u"\u01ba\3\2\2\2\u01ba\u01bc\3\2\2\2\u01bb\u01b9\3\2\2")
        buf.write(u"\2\u01bc\u01bd\7\26\2\2\u01bd;\3\2\2\2\u01be\u01bf\t")
        buf.write(u"\b\2\2\u01bf=\3\2\2\2\60AFOWcjlz\u0082\u008d\u0090\u009c")
        buf.write(u"\u00a4\u00b0\u00b3\u00b9\u00bb\u00c7\u00d3\u00dd\u00ee")
        buf.write(u"\u00f4\u00f8\u00fd\u0105\u010b\u0111\u0115\u011a\u012c")
        buf.write(u"\u0132\u0134\u0157\u0168\u016a\u0170\u0172\u017c\u0181")
        buf.write(u"\u018a\u0193\u019a\u01a6\u01ae\u01b3\u01b9")
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
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
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


                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
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
            self.state = 142
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(PrigogineParser.ID)
                self.state = 112
                self.match(PrigogineParser.T__7)
                self.state = 113
                self.match(PrigogineParser.T__8)
                self.state = 114 
                self.expression(0)
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 115
                    self.match(PrigogineParser.T__9)
                    self.state = 116
                    self.match(PrigogineParser.T__10)
                    self.state = 117 
                    self.conditional()
                    self.state = 122
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(PrigogineParser.ID)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__11:
                    self.state = 124
                    self.match(PrigogineParser.T__11)
                    self.state = 125
                    self.match(PrigogineParser.ID)
                    self.state = 130
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 131
                self.match(PrigogineParser.T__7)
                self.state = 132
                self.match(PrigogineParser.T__8)
                self.state = 133 
                self.expression(0)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 134
                    self.match(PrigogineParser.T__9)
                    self.state = 135
                    self.match(PrigogineParser.T__10)
                    self.state = 136 
                    self.conditional()
                    self.state = 141
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
            self.state = 177
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(PrigogineParser.ID)
                self.state = 145
                self.match(PrigogineParser.T__7)
                self.state = 146
                self.match(PrigogineParser.T__12)
                self.state = 147
                self.match(PrigogineParser.T__8)
                self.state = 148 
                self.expression(0)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 149
                    self.match(PrigogineParser.T__9)
                    self.state = 150
                    self.match(PrigogineParser.T__10)
                    self.state = 151 
                    self.conditional()
                    self.state = 156
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.match(PrigogineParser.ID)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__11:
                    self.state = 158
                    self.match(PrigogineParser.T__11)
                    self.state = 159
                    self.match(PrigogineParser.ID)
                    self.state = 164
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 165
                self.match(PrigogineParser.T__7)
                self.state = 166
                self.match(PrigogineParser.T__12)
                self.state = 167
                self.match(PrigogineParser.T__8)
                self.state = 168 
                self.expression(0)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 169
                    self.match(PrigogineParser.T__9)
                    self.state = 170
                    self.match(PrigogineParser.T__10)
                    self.state = 171 
                    self.conditional()
                    self.state = 176
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
            self.state = 179
            self.match(PrigogineParser.ID)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__11) | (1 << PrigogineParser.T__20))) != 0):
                self.state = 183
                token = self._input.LA(1)
                if token in [PrigogineParser.T__11]:
                    self.state = 180
                    self.match(PrigogineParser.T__11)
                    self.state = 181
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.T__1, PrigogineParser.T__20]:
                    self.state = 182 
                    self.timeindex()

                else:
                    raise NoViableAltException(self)

                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            self.match(PrigogineParser.T__8)
            self.state = 189 
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
            self.state = 191
            self.match(PrigogineParser.T__13)
            self.state = 192
            self.match(PrigogineParser.ID)
            self.state = 193
            self.match(PrigogineParser.T__1)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__14:
                self.state = 194 
                self.parameterlist()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200 
            self.variablelist()
            self.state = 201 
            self.equationlist()
            self.state = 202
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
            self.state = 204
            self.match(PrigogineParser.T__14)
            self.state = 205
            self.match(PrigogineParser.T__1)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 206 
                self.parameter()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
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
            self.state = 214
            self.match(PrigogineParser.T__15)
            self.state = 215
            self.match(PrigogineParser.T__1)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 216 
                self.variable()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 222
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
            self.state = 224
            self.match(PrigogineParser.T__1)
            self.state = 225 
            self.expression(0)
            self.state = 226
            self.match(PrigogineParser.T__16)
            self.state = 227
            self.match(PrigogineParser.ID)
            self.state = 228
            self.match(PrigogineParser.T__17)
            self.state = 229 
            self.expression(0)
            self.state = 230
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
            self.state = 259
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(PrigogineParser.T__1)
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                    self.state = 236
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 233
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 234 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 235 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 246
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==PrigogineParser.T__9:
                        self.state = 238
                        self.match(PrigogineParser.T__9)
                        self.state = 242
                        token = self._input.LA(1)
                        if token in [PrigogineParser.ID]:
                            self.state = 239
                            self.match(PrigogineParser.ID)

                        elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                            self.state = 240 
                            self.number()

                        elif token in [PrigogineParser.STRING]:
                            self.state = 241 
                            self.string()

                        else:
                            raise NoViableAltException(self)

                        self.state = 248
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 253
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 254
                self.match(PrigogineParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(PrigogineParser.T__1)
                self.state = 256 
                self.listdef()
                self.state = 257
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
            self.state = 261
            self.match(PrigogineParser.T__18)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 265
                token = self._input.LA(1)
                if token in [PrigogineParser.ID]:
                    self.state = 262
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                    self.state = 263 
                    self.number()

                elif token in [PrigogineParser.STRING]:
                    self.state = 264 
                    self.string()

                else:
                    raise NoViableAltException(self)

                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 267
                    self.match(PrigogineParser.T__9)
                    self.state = 271
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 268
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 269 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 270 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 277
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 283
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
            self.state = 285
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
            self.state = 287
            self.match(PrigogineParser.ID)
            self.state = 288 
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
            self.state = 290
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
            self.state = 304 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 304
                    token = self._input.LA(1)
                    if token in [PrigogineParser.T__1]:
                        self.state = 292
                        self.match(PrigogineParser.T__1)
                        self.state = 293 
                        self.timevar()
                        self.state = 298
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==PrigogineParser.SUB:
                            self.state = 294
                            self.match(PrigogineParser.SUB)
                            self.state = 295
                            self.match(PrigogineParser.INT)
                            self.state = 300
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 301
                        self.match(PrigogineParser.T__2)

                    elif token in [PrigogineParser.T__20]:
                        self.state = 303
                        self.match(PrigogineParser.T__20)

                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 306 
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
            self.state = 308
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
            self.state = 310
            self.match(PrigogineParser.T__1)
            self.state = 311 
            self.string()
            self.state = 312
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
            self.state = 341
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 315
                self.match(PrigogineParser.T__22)
                self.state = 316 
                self.expression(13)
                pass

            elif la_ == 2:
                self.state = 317 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 318 
                self.pyforloop()
                pass

            elif la_ == 4:
                self.state = 319
                self.match(PrigogineParser.T__22)
                self.state = 320 
                self.string()
                pass

            elif la_ == 5:
                self.state = 321
                self.match(PrigogineParser.T__22)
                self.state = 322 
                self.string()
                self.state = 323
                self.match(PrigogineParser.T__9)
                pass

            elif la_ == 6:
                self.state = 325 
                self.listdef()
                pass

            elif la_ == 7:
                self.state = 326 
                self.tupledef()
                pass

            elif la_ == 8:
                self.state = 327 
                self.string()
                pass

            elif la_ == 9:
                self.state = 328 
                self.number()
                pass

            elif la_ == 10:
                self.state = 329 
                self.func()
                pass

            elif la_ == 11:
                self.state = 330 
                self.listcomp()
                pass

            elif la_ == 12:
                self.state = 331
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 13:
                self.state = 332
                self.match(PrigogineParser.T__23)
                pass

            elif la_ == 14:
                self.state = 333 
                self.indexedvariable()
                pass

            elif la_ == 15:
                self.state = 334 
                self.timevar()
                pass

            elif la_ == 16:
                self.state = 335 
                self.lparen()
                self.state = 336 
                self.expression(0)
                self.state = 337 
                self.rparen()
                pass

            elif la_ == 17:
                self.state = 339
                self.match(PrigogineParser.T__24)
                self.state = 340
                self.match(PrigogineParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 360
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 358
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 343
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 344
                        self.match(PrigogineParser.T__11)
                        self.state = 345 
                        self.expression(22)
                        pass

                    elif la_ == 2:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 346
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 347
                        self.match(PrigogineParser.POWER)
                        self.state = 348 
                        self.expression(21)
                        pass

                    elif la_ == 3:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 349
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 350
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.MUL or _la==PrigogineParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 351 
                        self.expression(20)
                        pass

                    elif la_ == 4:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 352
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 353
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 354 
                        self.expression(19)
                        pass

                    elif la_ == 5:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 355
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 356
                        localctx.op = self.match(PrigogineParser.PIPE)
                        self.state = 357 
                        self.expression(18)
                        pass

             
                self.state = 362
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
            self.state = 363
            self.match(PrigogineParser.T__1)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__16) | (1 << PrigogineParser.T__18) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.T__22) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 366
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 364 
                    self.codeline()
                    pass

                elif la_ == 2:
                    self.state = 365 
                    self.pyforloop()
                    pass


                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 371
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
            self.state = 373 
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
            self.state = 375
            self.match(PrigogineParser.T__16)
            self.state = 378
            token = self._input.LA(1)
            if token in [PrigogineParser.ID]:
                self.state = 376
                self.match(PrigogineParser.ID)

            elif token in [PrigogineParser.T__21, PrigogineParser.INT]:
                self.state = 377 
                self.timevar()

            else:
                raise NoViableAltException(self)

            self.state = 380
            self.match(PrigogineParser.T__17)
            self.state = 383
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 381
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 2:
                self.state = 382 
                self.func()
                pass


            self.state = 385
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
            self.state = 387
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
            self.state = 392
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 389 
                    self.lparen() 
                self.state = 394
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

            self.state = 395 
            self.expression(0)
            self.state = 396
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__25) | (1 << PrigogineParser.T__26) | (1 << PrigogineParser.T__27) | (1 << PrigogineParser.T__28) | (1 << PrigogineParser.T__29) | (1 << PrigogineParser.T__30))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            self.consume()
            self.state = 397 
            self.expression(0)
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__19:
                self.state = 398 
                self.rparen()
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 404
                    _la = self._input.LA(1)
                    if not(_la==PrigogineParser.T__31 or _la==PrigogineParser.PIPE):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 405 
                    self.conditional() 
                self.state = 410
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
            self.state = 411
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
            self.state = 413
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
            self.state = 415
            self.match(PrigogineParser.ID)
            self.state = 416
            self.match(PrigogineParser.T__18)
            self.state = 420
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 417 
                    self.lparen() 
                self.state = 422
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__16) | (1 << PrigogineParser.T__18) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.T__22) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 423 
                self.expression(0)
                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 424
                    self.match(PrigogineParser.T__9)
                    self.state = 425 
                    self.expression(0)
                    self.state = 430
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 435
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 439
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 436 
                    self.rparen() 
                self.state = 441
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

            self.state = 442
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
            self.state = 444
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
         



