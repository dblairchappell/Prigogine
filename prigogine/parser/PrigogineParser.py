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
        buf.write(u"\61\u01bb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\3\2\6\2@\n\2\r\2\16\2A\3\2")
        buf.write(u"\7\2E\n\2\f\2\16\2H\13\2\3\3\3\3\3\3\3\3\3\3\3\3\6\3")
        buf.write(u"P\n\3\r\3\16\3Q\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\7\5\\")
        buf.write(u"\n\5\f\5\16\5_\13\5\3\6\3\6\3\6\3\6\7\6e\n\6\f\6\16\6")
        buf.write(u"h\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7s\n\7\f")
        buf.write(u"\7\16\7v\13\7\3\7\3\7\3\7\7\7{\n\7\f\7\16\7~\13\7\3\7")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\7\7\u0086\n\7\f\7\16\7\u0089\13")
        buf.write(u"\7\5\7\u008b\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b")
        buf.write(u"\u0095\n\b\f\b\16\b\u0098\13\b\3\b\3\b\3\b\7\b\u009d")
        buf.write(u"\n\b\f\b\16\b\u00a0\13\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\7\b\u00a9\n\b\f\b\16\b\u00ac\13\b\5\b\u00ae\n\b\3\t")
        buf.write(u"\3\t\3\t\3\t\7\t\u00b4\n\t\f\t\16\t\u00b7\13\t\3\t\3")
        buf.write(u"\t\3\t\3\n\3\n\3\n\3\n\7\n\u00c0\n\n\f\n\16\n\u00c3\13")
        buf.write(u"\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\7\13\u00cc\n\13\f\13")
        buf.write(u"\16\13\u00cf\13\13\3\13\3\13\3\f\3\f\3\f\7\f\u00d6\n")
        buf.write(u"\f\f\f\16\f\u00d9\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16\u00e9\n\16\3\16\3")
        buf.write(u"\16\3\16\3\16\5\16\u00ef\n\16\7\16\u00f1\n\16\f\16\16")
        buf.write(u"\16\u00f4\13\16\7\16\u00f6\n\16\f\16\16\16\u00f9\13\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\5\16\u0100\n\16\3\17\3\17\3")
        buf.write(u"\17\3\17\5\17\u0106\n\17\3\17\3\17\3\17\3\17\5\17\u010c")
        buf.write(u"\n\17\7\17\u010e\n\17\f\17\16\17\u0111\13\17\7\17\u0113")
        buf.write(u"\n\17\f\17\16\17\u0116\13\17\3\17\3\17\3\20\3\20\3\21")
        buf.write(u"\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\23\7\23\u0125\n")
        buf.write(u"\23\f\23\16\23\u0128\13\23\3\23\3\23\3\23\6\23\u012d")
        buf.write(u"\n\23\r\23\16\23\u012e\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write(u"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0152\n\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\7\26\u0163\n\26\f\26\16\26\u0166\13\26")
        buf.write(u"\3\27\3\27\3\27\7\27\u016b\n\27\f\27\16\27\u016e\13\27")
        buf.write(u"\3\27\3\27\3\30\3\30\3\31\3\31\3\31\5\31\u0177\n\31\3")
        buf.write(u"\31\3\31\3\31\5\31\u017c\n\31\3\31\3\31\3\32\3\32\3\33")
        buf.write(u"\7\33\u0183\n\33\f\33\16\33\u0186\13\33\3\33\3\33\3\33")
        buf.write(u"\3\33\7\33\u018c\n\33\f\33\16\33\u018f\13\33\3\33\3\33")
        buf.write(u"\7\33\u0193\n\33\f\33\16\33\u0196\13\33\3\34\3\34\3\35")
        buf.write(u"\3\35\3\36\3\36\3\36\7\36\u019f\n\36\f\36\16\36\u01a2")
        buf.write(u"\13\36\3\36\3\36\3\36\7\36\u01a7\n\36\f\36\16\36\u01aa")
        buf.write(u"\13\36\7\36\u01ac\n\36\f\36\16\36\u01af\13\36\3\36\7")
        buf.write(u"\36\u01b2\n\36\f\36\16\36\u01b5\13\36\3\36\3\36\3\37")
        buf.write(u"\3\37\3\37\3]\3* \2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write(u"\36 \"$&(*,.\60\62\64\668:<\2\t\3\2\7\b\4\2\27\27%%\3")
        buf.write(u"\2)*\3\2+,\3\2\33 \4\2!!--\3\2%&\u01df\2?\3\2\2\2\4I")
        buf.write(u"\3\2\2\2\6U\3\2\2\2\b]\3\2\2\2\n`\3\2\2\2\f\u008a\3\2")
        buf.write(u"\2\2\16\u00ad\3\2\2\2\20\u00af\3\2\2\2\22\u00bb\3\2\2")
        buf.write(u"\2\24\u00c8\3\2\2\2\26\u00d2\3\2\2\2\30\u00dc\3\2\2\2")
        buf.write(u"\32\u00ff\3\2\2\2\34\u0101\3\2\2\2\36\u0119\3\2\2\2 ")
        buf.write(u"\u011b\3\2\2\2\"\u011e\3\2\2\2$\u012c\3\2\2\2&\u0130")
        buf.write(u"\3\2\2\2(\u0132\3\2\2\2*\u0151\3\2\2\2,\u0167\3\2\2\2")
        buf.write(u".\u0171\3\2\2\2\60\u0173\3\2\2\2\62\u017f\3\2\2\2\64")
        buf.write(u"\u0184\3\2\2\2\66\u0197\3\2\2\28\u0199\3\2\2\2:\u019b")
        buf.write(u"\3\2\2\2<\u01b8\3\2\2\2>@\5\4\3\2?>\3\2\2\2@A\3\2\2\2")
        buf.write(u"A?\3\2\2\2AB\3\2\2\2BF\3\2\2\2CE\5\6\4\2DC\3\2\2\2EH")
        buf.write(u"\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\3\3\2\2\2HF\3\2\2\2IJ\7")
        buf.write(u"\3\2\2JK\7\'\2\2KL\7\4\2\2LM\5\26\f\2MO\5\n\6\2NP\5\22")
        buf.write(u"\n\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2RS\3\2\2")
        buf.write(u"\2ST\7\5\2\2T\5\3\2\2\2UV\7\6\2\2VW\7\4\2\2WX\5\b\5\2")
        buf.write(u"XY\7\5\2\2Y\7\3\2\2\2Z\\\n\2\2\2[Z\3\2\2\2\\_\3\2\2\2")
        buf.write(u"]^\3\2\2\2][\3\2\2\2^\t\3\2\2\2_]\3\2\2\2`a\7\t\2\2a")
        buf.write(u"f\7\4\2\2be\5\f\7\2ce\5\16\b\2db\3\2\2\2dc\3\2\2\2eh")
        buf.write(u"\3\2\2\2fd\3\2\2\2fg\3\2\2\2gi\3\2\2\2hf\3\2\2\2ij\7")
        buf.write(u"\5\2\2j\13\3\2\2\2kl\7\'\2\2lm\7\n\2\2mn\7\13\2\2nt\5")
        buf.write(u"*\26\2op\7\f\2\2pq\7\r\2\2qs\5\64\33\2ro\3\2\2\2sv\3")
        buf.write(u"\2\2\2tr\3\2\2\2tu\3\2\2\2u\u008b\3\2\2\2vt\3\2\2\2w")
        buf.write(u"|\7\'\2\2xy\7\16\2\2y{\7\'\2\2zx\3\2\2\2{~\3\2\2\2|z")
        buf.write(u"\3\2\2\2|}\3\2\2\2}\177\3\2\2\2~|\3\2\2\2\177\u0080\7")
        buf.write(u"\n\2\2\u0080\u0081\7\13\2\2\u0081\u0087\5*\26\2\u0082")
        buf.write(u"\u0083\7\f\2\2\u0083\u0084\7\r\2\2\u0084\u0086\5\64\33")
        buf.write(u"\2\u0085\u0082\3\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085")
        buf.write(u"\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u008b\3\2\2\2\u0089")
        buf.write(u"\u0087\3\2\2\2\u008ak\3\2\2\2\u008aw\3\2\2\2\u008b\r")
        buf.write(u"\3\2\2\2\u008c\u008d\7\'\2\2\u008d\u008e\7\n\2\2\u008e")
        buf.write(u"\u008f\7\17\2\2\u008f\u0090\7\13\2\2\u0090\u0096\5*\26")
        buf.write(u"\2\u0091\u0092\7\f\2\2\u0092\u0093\7\r\2\2\u0093\u0095")
        buf.write(u"\5\64\33\2\u0094\u0091\3\2\2\2\u0095\u0098\3\2\2\2\u0096")
        buf.write(u"\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u00ae\3\2\2")
        buf.write(u"\2\u0098\u0096\3\2\2\2\u0099\u009e\7\'\2\2\u009a\u009b")
        buf.write(u"\7\16\2\2\u009b\u009d\7\'\2\2\u009c\u009a\3\2\2\2\u009d")
        buf.write(u"\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2")
        buf.write(u"\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a2")
        buf.write(u"\7\n\2\2\u00a2\u00a3\7\17\2\2\u00a3\u00a4\7\13\2\2\u00a4")
        buf.write(u"\u00aa\5*\26\2\u00a5\u00a6\7\f\2\2\u00a6\u00a7\7\r\2")
        buf.write(u"\2\u00a7\u00a9\5\64\33\2\u00a8\u00a5\3\2\2\2\u00a9\u00ac")
        buf.write(u"\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab")
        buf.write(u"\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u008c\3\2\2")
        buf.write(u"\2\u00ad\u0099\3\2\2\2\u00ae\17\3\2\2\2\u00af\u00b5\7")
        buf.write(u"\'\2\2\u00b0\u00b1\7\16\2\2\u00b1\u00b4\7\'\2\2\u00b2")
        buf.write(u"\u00b4\5$\23\2\u00b3\u00b0\3\2\2\2\u00b3\u00b2\3\2\2")
        buf.write(u"\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6")
        buf.write(u"\3\2\2\2\u00b6\u00b8\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8")
        buf.write(u"\u00b9\7\13\2\2\u00b9\u00ba\5*\26\2\u00ba\21\3\2\2\2")
        buf.write(u"\u00bb\u00bc\7\20\2\2\u00bc\u00bd\7\'\2\2\u00bd\u00c1")
        buf.write(u"\7\4\2\2\u00be\u00c0\5\24\13\2\u00bf\u00be\3\2\2\2\u00c0")
        buf.write(u"\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2")
        buf.write(u"\2\u00c2\u00c4\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5")
        buf.write(u"\5\26\f\2\u00c5\u00c6\5\n\6\2\u00c6\u00c7\7\5\2\2\u00c7")
        buf.write(u"\23\3\2\2\2\u00c8\u00c9\7\21\2\2\u00c9\u00cd\7\4\2\2")
        buf.write(u"\u00ca\u00cc\5\"\22\2\u00cb\u00ca\3\2\2\2\u00cc\u00cf")
        buf.write(u"\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write(u"\u00d0\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\7\5\2")
        buf.write(u"\2\u00d1\25\3\2\2\2\u00d2\u00d3\7\22\2\2\u00d3\u00d7")
        buf.write(u"\7\4\2\2\u00d4\u00d6\5\36\20\2\u00d5\u00d4\3\2\2\2\u00d6")
        buf.write(u"\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2")
        buf.write(u"\2\u00d8\u00da\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00db")
        buf.write(u"\7\5\2\2\u00db\27\3\2\2\2\u00dc\u00dd\7\4\2\2\u00dd\u00de")
        buf.write(u"\5*\26\2\u00de\u00df\7\23\2\2\u00df\u00e0\7\'\2\2\u00e0")
        buf.write(u"\u00e1\7\24\2\2\u00e1\u00e2\5*\26\2\u00e2\u00e3\7\5\2")
        buf.write(u"\2\u00e3\31\3\2\2\2\u00e4\u00f7\7\4\2\2\u00e5\u00e9\7")
        buf.write(u"\'\2\2\u00e6\u00e9\5<\37\2\u00e7\u00e9\5\62\32\2\u00e8")
        buf.write(u"\u00e5\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3\2\2")
        buf.write(u"\2\u00e9\u00f2\3\2\2\2\u00ea\u00ee\7\f\2\2\u00eb\u00ef")
        buf.write(u"\7\'\2\2\u00ec\u00ef\5<\37\2\u00ed\u00ef\5\62\32\2\u00ee")
        buf.write(u"\u00eb\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3\2\2")
        buf.write(u"\2\u00ef\u00f1\3\2\2\2\u00f0\u00ea\3\2\2\2\u00f1\u00f4")
        buf.write(u"\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write(u"\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00e8\3\2\2")
        buf.write(u"\2\u00f6\u00f9\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8")
        buf.write(u"\3\2\2\2\u00f8\u00fa\3\2\2\2\u00f9\u00f7\3\2\2\2\u00fa")
        buf.write(u"\u0100\7\5\2\2\u00fb\u00fc\7\4\2\2\u00fc\u00fd\5\32\16")
        buf.write(u"\2\u00fd\u00fe\7\5\2\2\u00fe\u0100\3\2\2\2\u00ff\u00e4")
        buf.write(u"\3\2\2\2\u00ff\u00fb\3\2\2\2\u0100\33\3\2\2\2\u0101\u0114")
        buf.write(u"\7\25\2\2\u0102\u0106\7\'\2\2\u0103\u0106\5<\37\2\u0104")
        buf.write(u"\u0106\5\62\32\2\u0105\u0102\3\2\2\2\u0105\u0103\3\2")
        buf.write(u"\2\2\u0105\u0104\3\2\2\2\u0106\u010f\3\2\2\2\u0107\u010b")
        buf.write(u"\7\f\2\2\u0108\u010c\7\'\2\2\u0109\u010c\5<\37\2\u010a")
        buf.write(u"\u010c\5\62\32\2\u010b\u0108\3\2\2\2\u010b\u0109\3\2")
        buf.write(u"\2\2\u010b\u010a\3\2\2\2\u010c\u010e\3\2\2\2\u010d\u0107")
        buf.write(u"\3\2\2\2\u010e\u0111\3\2\2\2\u010f\u010d\3\2\2\2\u010f")
        buf.write(u"\u0110\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f\3\2\2")
        buf.write(u"\2\u0112\u0105\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0112")
        buf.write(u"\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117\3\2\2\2\u0116")
        buf.write(u"\u0114\3\2\2\2\u0117\u0118\7\26\2\2\u0118\35\3\2\2\2")
        buf.write(u"\u0119\u011a\7\'\2\2\u011a\37\3\2\2\2\u011b\u011c\7\'")
        buf.write(u"\2\2\u011c\u011d\5$\23\2\u011d!\3\2\2\2\u011e\u011f\7")
        buf.write(u"\'\2\2\u011f#\3\2\2\2\u0120\u0121\7\4\2\2\u0121\u0126")
        buf.write(u"\5&\24\2\u0122\u0123\7,\2\2\u0123\u0125\7%\2\2\u0124")
        buf.write(u"\u0122\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2")
        buf.write(u"\2\u0126\u0127\3\2\2\2\u0127\u0129\3\2\2\2\u0128\u0126")
        buf.write(u"\3\2\2\2\u0129\u012a\7\5\2\2\u012a\u012d\3\2\2\2\u012b")
        buf.write(u"\u012d\7\17\2\2\u012c\u0120\3\2\2\2\u012c\u012b\3\2\2")
        buf.write(u"\2\u012d\u012e\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f")
        buf.write(u"\3\2\2\2\u012f%\3\2\2\2\u0130\u0131\t\3\2\2\u0131\'\3")
        buf.write(u"\2\2\2\u0132\u0133\7\4\2\2\u0133\u0134\5\62\32\2\u0134")
        buf.write(u"\u0135\7\5\2\2\u0135)\3\2\2\2\u0136\u0137\b\26\1\2\u0137")
        buf.write(u"\u0138\7\30\2\2\u0138\u0152\5*\26\17\u0139\u0152\5\20")
        buf.write(u"\t\2\u013a\u0152\5\60\31\2\u013b\u013c\7\30\2\2\u013c")
        buf.write(u"\u0152\5\62\32\2\u013d\u013e\7\30\2\2\u013e\u013f\5\62")
        buf.write(u"\32\2\u013f\u0140\7\f\2\2\u0140\u0152\3\2\2\2\u0141\u0152")
        buf.write(u"\5\32\16\2\u0142\u0152\5\34\17\2\u0143\u0152\5\62\32")
        buf.write(u"\2\u0144\u0152\5<\37\2\u0145\u0152\5:\36\2\u0146\u0152")
        buf.write(u"\5\30\r\2\u0147\u0152\7\'\2\2\u0148\u0152\7\31\2\2\u0149")
        buf.write(u"\u0152\5 \21\2\u014a\u0152\5&\24\2\u014b\u014c\5\66\34")
        buf.write(u"\2\u014c\u014d\5*\26\2\u014d\u014e\58\35\2\u014e\u0152")
        buf.write(u"\3\2\2\2\u014f\u0150\7\32\2\2\u0150\u0152\7\'\2\2\u0151")
        buf.write(u"\u0136\3\2\2\2\u0151\u0139\3\2\2\2\u0151\u013a\3\2\2")
        buf.write(u"\2\u0151\u013b\3\2\2\2\u0151\u013d\3\2\2\2\u0151\u0141")
        buf.write(u"\3\2\2\2\u0151\u0142\3\2\2\2\u0151\u0143\3\2\2\2\u0151")
        buf.write(u"\u0144\3\2\2\2\u0151\u0145\3\2\2\2\u0151\u0146\3\2\2")
        buf.write(u"\2\u0151\u0147\3\2\2\2\u0151\u0148\3\2\2\2\u0151\u0149")
        buf.write(u"\3\2\2\2\u0151\u014a\3\2\2\2\u0151\u014b\3\2\2\2\u0151")
        buf.write(u"\u014f\3\2\2\2\u0152\u0164\3\2\2\2\u0153\u0154\f\27\2")
        buf.write(u"\2\u0154\u0155\7\16\2\2\u0155\u0163\5*\26\30\u0156\u0157")
        buf.write(u"\f\26\2\2\u0157\u0158\7.\2\2\u0158\u0163\5*\26\27\u0159")
        buf.write(u"\u015a\f\25\2\2\u015a\u015b\t\4\2\2\u015b\u0163\5*\26")
        buf.write(u"\26\u015c\u015d\f\24\2\2\u015d\u015e\t\5\2\2\u015e\u0163")
        buf.write(u"\5*\26\25\u015f\u0160\f\23\2\2\u0160\u0161\7-\2\2\u0161")
        buf.write(u"\u0163\5*\26\24\u0162\u0153\3\2\2\2\u0162\u0156\3\2\2")
        buf.write(u"\2\u0162\u0159\3\2\2\2\u0162\u015c\3\2\2\2\u0162\u015f")
        buf.write(u"\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164")
        buf.write(u"\u0165\3\2\2\2\u0165+\3\2\2\2\u0166\u0164\3\2\2\2\u0167")
        buf.write(u"\u016c\7\4\2\2\u0168\u016b\5.\30\2\u0169\u016b\5\60\31")
        buf.write(u"\2\u016a\u0168\3\2\2\2\u016a\u0169\3\2\2\2\u016b\u016e")
        buf.write(u"\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write(u"\u016f\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0170\7\5\2")
        buf.write(u"\2\u0170-\3\2\2\2\u0171\u0172\5*\26\2\u0172/\3\2\2\2")
        buf.write(u"\u0173\u0176\7\23\2\2\u0174\u0177\7\'\2\2\u0175\u0177")
        buf.write(u"\5&\24\2\u0176\u0174\3\2\2\2\u0176\u0175\3\2\2\2\u0177")
        buf.write(u"\u0178\3\2\2\2\u0178\u017b\7\24\2\2\u0179\u017c\7\'\2")
        buf.write(u"\2\u017a\u017c\5:\36\2\u017b\u0179\3\2\2\2\u017b\u017a")
        buf.write(u"\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e\7\31\2\2\u017e")
        buf.write(u"\61\3\2\2\2\u017f\u0180\7/\2\2\u0180\63\3\2\2\2\u0181")
        buf.write(u"\u0183\5\66\34\2\u0182\u0181\3\2\2\2\u0183\u0186\3\2")
        buf.write(u"\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0187")
        buf.write(u"\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188\5*\26\2\u0188")
        buf.write(u"\u0189\t\6\2\2\u0189\u018d\5*\26\2\u018a\u018c\58\35")
        buf.write(u"\2\u018b\u018a\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018b")
        buf.write(u"\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u0194\3\2\2\2\u018f")
        buf.write(u"\u018d\3\2\2\2\u0190\u0191\t\7\2\2\u0191\u0193\5\64\33")
        buf.write(u"\2\u0192\u0190\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192")
        buf.write(u"\3\2\2\2\u0194\u0195\3\2\2\2\u0195\65\3\2\2\2\u0196\u0194")
        buf.write(u"\3\2\2\2\u0197\u0198\7\25\2\2\u0198\67\3\2\2\2\u0199")
        buf.write(u"\u019a\7\26\2\2\u019a9\3\2\2\2\u019b\u019c\7\'\2\2\u019c")
        buf.write(u"\u01a0\7\25\2\2\u019d\u019f\5\66\34\2\u019e\u019d\3\2")
        buf.write(u"\2\2\u019f\u01a2\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1")
        buf.write(u"\3\2\2\2\u01a1\u01ad\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3")
        buf.write(u"\u01a8\5*\26\2\u01a4\u01a5\7\f\2\2\u01a5\u01a7\5*\26")
        buf.write(u"\2\u01a6\u01a4\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6")
        buf.write(u"\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa")
        buf.write(u"\u01a8\3\2\2\2\u01ab\u01a3\3\2\2\2\u01ac\u01af\3\2\2")
        buf.write(u"\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01b3")
        buf.write(u"\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b2\58\35\2\u01b1")
        buf.write(u"\u01b0\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1\3\2\2")
        buf.write(u"\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01b3")
        buf.write(u"\3\2\2\2\u01b6\u01b7\7\26\2\2\u01b7;\3\2\2\2\u01b8\u01b9")
        buf.write(u"\t\b\2\2\u01b9=\3\2\2\2/AFQ]dft|\u0087\u008a\u0096\u009e")
        buf.write(u"\u00aa\u00ad\u00b3\u00b5\u00c1\u00cd\u00d7\u00e8\u00ee")
        buf.write(u"\u00f2\u00f7\u00ff\u0105\u010b\u010f\u0114\u0126\u012c")
        buf.write(u"\u012e\u0151\u0162\u0164\u016a\u016c\u0176\u017b\u0184")
        buf.write(u"\u018d\u0194\u01a0\u01a8\u01ad\u01b3")
        return buf.getvalue()
		

class PrigogineParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'model'", u"'['", u"']'", u"'simulation'", 
                     u"'\n'", u"'\r'", u"'equations'", u"'[t+1]'", u"'='", 
                     u"','", u"'where'", u"'.'", u"'[:]'", u"'population'", 
                     u"'parameters'", u"'variables'", u"'for'", u"'in'", 
                     u"'('", u"')'", u"'t'", u"'print'", u"':'", u"'return'", 
                     u"'<'", u"'>'", u"'>='", u"'<='", u"'=='", u"'!='", 
                     u"'&'", u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'*'", u"'/'", 
                     u"'+'", u"'-'", u"'|'", u"'^'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"LineComment", u"NEWLINE", u"ML_COMMENT", u"INT", 
                      u"FLOAT", u"ID", u"WS", u"MUL", u"DIV", u"ADD", u"SUB", 
                      u"PIPE", u"POWER", u"STRING", u"ESC", u"SPACE" ]

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
    LineComment=32
    NEWLINE=33
    ML_COMMENT=34
    INT=35
    FLOAT=36
    ID=37
    WS=38
    MUL=39
    DIV=40
    ADD=41
    SUB=42
    PIPE=43
    POWER=44
    STRING=45
    ESC=46
    SPACE=47

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

            self.state = 74 
            self.variablelist()
            self.state = 75 
            self.equationlist()
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76 
                self.population()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrigogineParser.T__13):
                    break

            self.state = 81
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
            self.state = 83
            self.match(PrigogineParser.T__3)
            self.state = 84
            self.match(PrigogineParser.T__1)
            self.state = 85 
            self.codeinsert()
            self.state = 86
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
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 88
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==PrigogineParser.T__4 or _la==PrigogineParser.T__5:
                        self._errHandler.recoverInline(self)
                    self.consume() 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
            self.state = 94
            self.match(PrigogineParser.T__6)
            self.state = 95
            self.match(PrigogineParser.T__1)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 98
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 96 
                    self.elementwiseEquation()
                    pass

                elif la_ == 2:
                    self.state = 97 
                    self.mapEquation()
                    pass


                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
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
            self.state = 136
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(PrigogineParser.ID)
                self.state = 106
                self.match(PrigogineParser.T__7)
                self.state = 107
                self.match(PrigogineParser.T__8)
                self.state = 108 
                self.expression(0)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 109
                    self.match(PrigogineParser.T__9)
                    self.state = 110
                    self.match(PrigogineParser.T__10)
                    self.state = 111 
                    self.conditional()
                    self.state = 116
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(PrigogineParser.ID)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__11:
                    self.state = 118
                    self.match(PrigogineParser.T__11)
                    self.state = 119
                    self.match(PrigogineParser.ID)
                    self.state = 124
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 125
                self.match(PrigogineParser.T__7)
                self.state = 126
                self.match(PrigogineParser.T__8)
                self.state = 127 
                self.expression(0)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 128
                    self.match(PrigogineParser.T__9)
                    self.state = 129
                    self.match(PrigogineParser.T__10)
                    self.state = 130 
                    self.conditional()
                    self.state = 135
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
            self.state = 171
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(PrigogineParser.ID)
                self.state = 139
                self.match(PrigogineParser.T__7)
                self.state = 140
                self.match(PrigogineParser.T__12)
                self.state = 141
                self.match(PrigogineParser.T__8)
                self.state = 142 
                self.expression(0)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 143
                    self.match(PrigogineParser.T__9)
                    self.state = 144
                    self.match(PrigogineParser.T__10)
                    self.state = 145 
                    self.conditional()
                    self.state = 150
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(PrigogineParser.ID)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__11:
                    self.state = 152
                    self.match(PrigogineParser.T__11)
                    self.state = 153
                    self.match(PrigogineParser.ID)
                    self.state = 158
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 159
                self.match(PrigogineParser.T__7)
                self.state = 160
                self.match(PrigogineParser.T__12)
                self.state = 161
                self.match(PrigogineParser.T__8)
                self.state = 162 
                self.expression(0)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 163
                    self.match(PrigogineParser.T__9)
                    self.state = 164
                    self.match(PrigogineParser.T__10)
                    self.state = 165 
                    self.conditional()
                    self.state = 170
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
            self.state = 173
            self.match(PrigogineParser.ID)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__11) | (1 << PrigogineParser.T__12))) != 0):
                self.state = 177
                token = self._input.LA(1)
                if token in [PrigogineParser.T__11]:
                    self.state = 174
                    self.match(PrigogineParser.T__11)
                    self.state = 175
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.T__1, PrigogineParser.T__12]:
                    self.state = 176 
                    self.timeindex()

                else:
                    raise NoViableAltException(self)

                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self.match(PrigogineParser.T__8)
            self.state = 183 
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
            self.state = 185
            self.match(PrigogineParser.T__13)
            self.state = 186
            self.match(PrigogineParser.ID)
            self.state = 187
            self.match(PrigogineParser.T__1)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__14:
                self.state = 188 
                self.parameterlist()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 194 
            self.variablelist()
            self.state = 195 
            self.equationlist()
            self.state = 196
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
            self.state = 198
            self.match(PrigogineParser.T__14)
            self.state = 199
            self.match(PrigogineParser.T__1)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 200 
                self.parameter()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
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
            self.state = 208
            self.match(PrigogineParser.T__15)
            self.state = 209
            self.match(PrigogineParser.T__1)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 210 
                self.variable()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 216
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
            self.state = 218
            self.match(PrigogineParser.T__1)
            self.state = 219 
            self.expression(0)
            self.state = 220
            self.match(PrigogineParser.T__16)
            self.state = 221
            self.match(PrigogineParser.ID)
            self.state = 222
            self.match(PrigogineParser.T__17)
            self.state = 223 
            self.expression(0)
            self.state = 224
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
            self.state = 253
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(PrigogineParser.T__1)
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                    self.state = 230
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 227
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 228 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 229 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 240
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==PrigogineParser.T__9:
                        self.state = 232
                        self.match(PrigogineParser.T__9)
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

                        self.state = 242
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 247
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 248
                self.match(PrigogineParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(PrigogineParser.T__1)
                self.state = 250 
                self.listdef()
                self.state = 251
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
            self.state = 255
            self.match(PrigogineParser.T__18)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 259
                token = self._input.LA(1)
                if token in [PrigogineParser.ID]:
                    self.state = 256
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                    self.state = 257 
                    self.number()

                elif token in [PrigogineParser.STRING]:
                    self.state = 258 
                    self.string()

                else:
                    raise NoViableAltException(self)

                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 261
                    self.match(PrigogineParser.T__9)
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

                    self.state = 271
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 277
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
            self.state = 279
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
            self.state = 281
            self.match(PrigogineParser.ID)
            self.state = 282 
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
            self.state = 284
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
            self.state = 298 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 298
                    token = self._input.LA(1)
                    if token in [PrigogineParser.T__1]:
                        self.state = 286
                        self.match(PrigogineParser.T__1)
                        self.state = 287 
                        self.timevar()
                        self.state = 292
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==PrigogineParser.SUB:
                            self.state = 288
                            self.match(PrigogineParser.SUB)
                            self.state = 289
                            self.match(PrigogineParser.INT)
                            self.state = 294
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 295
                        self.match(PrigogineParser.T__2)

                    elif token in [PrigogineParser.T__12]:
                        self.state = 297
                        self.match(PrigogineParser.T__12)

                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 300 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
            self.state = 302
            _la = self._input.LA(1)
            if not(_la==PrigogineParser.T__20 or _la==PrigogineParser.INT):
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
            self.state = 304
            self.match(PrigogineParser.T__1)
            self.state = 305 
            self.string()
            self.state = 306
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
            self.state = 335
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 309
                self.match(PrigogineParser.T__21)
                self.state = 310 
                self.expression(13)
                pass

            elif la_ == 2:
                self.state = 311 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 312 
                self.pyforloop()
                pass

            elif la_ == 4:
                self.state = 313
                self.match(PrigogineParser.T__21)
                self.state = 314 
                self.string()
                pass

            elif la_ == 5:
                self.state = 315
                self.match(PrigogineParser.T__21)
                self.state = 316 
                self.string()
                self.state = 317
                self.match(PrigogineParser.T__9)
                pass

            elif la_ == 6:
                self.state = 319 
                self.listdef()
                pass

            elif la_ == 7:
                self.state = 320 
                self.tupledef()
                pass

            elif la_ == 8:
                self.state = 321 
                self.string()
                pass

            elif la_ == 9:
                self.state = 322 
                self.number()
                pass

            elif la_ == 10:
                self.state = 323 
                self.func()
                pass

            elif la_ == 11:
                self.state = 324 
                self.listcomp()
                pass

            elif la_ == 12:
                self.state = 325
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 13:
                self.state = 326
                self.match(PrigogineParser.T__22)
                pass

            elif la_ == 14:
                self.state = 327 
                self.indexedvariable()
                pass

            elif la_ == 15:
                self.state = 328 
                self.timevar()
                pass

            elif la_ == 16:
                self.state = 329 
                self.lparen()
                self.state = 330 
                self.expression(0)
                self.state = 331 
                self.rparen()
                pass

            elif la_ == 17:
                self.state = 333
                self.match(PrigogineParser.T__23)
                self.state = 334
                self.match(PrigogineParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 354
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 352
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 337
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 338
                        self.match(PrigogineParser.T__11)
                        self.state = 339 
                        self.expression(22)
                        pass

                    elif la_ == 2:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 340
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 341
                        self.match(PrigogineParser.POWER)
                        self.state = 342 
                        self.expression(21)
                        pass

                    elif la_ == 3:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 343
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 344
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.MUL or _la==PrigogineParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 345 
                        self.expression(20)
                        pass

                    elif la_ == 4:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 346
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 347
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 348 
                        self.expression(19)
                        pass

                    elif la_ == 5:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 349
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 350
                        localctx.op = self.match(PrigogineParser.PIPE)
                        self.state = 351 
                        self.expression(18)
                        pass

             
                self.state = 356
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
            self.state = 357
            self.match(PrigogineParser.T__1)
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__16) | (1 << PrigogineParser.T__18) | (1 << PrigogineParser.T__20) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.T__22) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 360
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 358 
                    self.codeline()
                    pass

                elif la_ == 2:
                    self.state = 359 
                    self.pyforloop()
                    pass


                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 365
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
            self.state = 367 
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
            self.state = 369
            self.match(PrigogineParser.T__16)
            self.state = 372
            token = self._input.LA(1)
            if token in [PrigogineParser.ID]:
                self.state = 370
                self.match(PrigogineParser.ID)

            elif token in [PrigogineParser.T__20, PrigogineParser.INT]:
                self.state = 371 
                self.timevar()

            else:
                raise NoViableAltException(self)

            self.state = 374
            self.match(PrigogineParser.T__17)
            self.state = 377
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 375
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 2:
                self.state = 376 
                self.func()
                pass


            self.state = 379
            self.match(PrigogineParser.T__22)
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
            self.state = 381
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
            self.state = 386
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 383 
                    self.lparen() 
                self.state = 388
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

            self.state = 389 
            self.expression(0)
            self.state = 390
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__24) | (1 << PrigogineParser.T__25) | (1 << PrigogineParser.T__26) | (1 << PrigogineParser.T__27) | (1 << PrigogineParser.T__28) | (1 << PrigogineParser.T__29))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            self.consume()
            self.state = 391 
            self.expression(0)
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__19:
                self.state = 392 
                self.rparen()
                self.state = 397
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 402
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 398
                    _la = self._input.LA(1)
                    if not(_la==PrigogineParser.T__30 or _la==PrigogineParser.PIPE):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 399 
                    self.conditional() 
                self.state = 404
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
            self.state = 405
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
            self.state = 407
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
            self.state = 409
            self.match(PrigogineParser.ID)
            self.state = 410
            self.match(PrigogineParser.T__18)
            self.state = 414
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 411 
                    self.lparen() 
                self.state = 416
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__16) | (1 << PrigogineParser.T__18) | (1 << PrigogineParser.T__20) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.T__22) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 417 
                self.expression(0)
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 418
                    self.match(PrigogineParser.T__9)
                    self.state = 419 
                    self.expression(0)
                    self.state = 424
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 429
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 433
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 430 
                    self.rparen() 
                self.state = 435
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

            self.state = 436
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
            self.state = 438
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
         



