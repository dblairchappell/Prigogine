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
        buf.write(u"\62\u01e4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\6\2")
        buf.write(u"F\n\2\r\2\16\2G\3\2\7\2K\n\2\f\2\16\2N\13\2\3\3\3\3\3")
        buf.write(u"\3\3\3\7\3T\n\3\f\3\16\3W\13\3\3\3\3\3\3\3\6\3\\\n\3")
        buf.write(u"\r\3\16\3]\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\7\5h\n\5\f")
        buf.write(u"\5\16\5k\13\5\3\6\3\6\3\6\3\6\7\6q\n\6\f\6\16\6t\13\6")
        buf.write(u"\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\177\n\7\f\7")
        buf.write(u"\16\7\u0082\13\7\3\7\3\7\3\7\7\7\u0087\n\7\f\7\16\7\u008a")
        buf.write(u"\13\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u0092\n\7\f\7\16\7")
        buf.write(u"\u0095\13\7\5\7\u0097\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\7\b\u00a1\n\b\f\b\16\b\u00a4\13\b\3\b\3\b\3\b\7")
        buf.write(u"\b\u00a9\n\b\f\b\16\b\u00ac\13\b\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\7\b\u00b5\n\b\f\b\16\b\u00b8\13\b\5\b\u00ba")
        buf.write(u"\n\b\3\t\3\t\3\t\3\t\7\t\u00c0\n\t\f\t\16\t\u00c3\13")
        buf.write(u"\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\7\n\u00cc\n\n\f\n\16\n")
        buf.write(u"\u00cf\13\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\7\13\u00d8")
        buf.write(u"\n\13\f\13\16\13\u00db\13\13\3\13\3\13\3\f\3\f\3\f\7")
        buf.write(u"\f\u00e2\n\f\f\f\16\f\u00e5\13\f\3\f\3\f\3\r\3\r\3\r")
        buf.write(u"\7\r\u00ec\n\r\f\r\16\r\u00ef\13\r\3\r\3\r\3\16\3\16")
        buf.write(u"\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3")
        buf.write(u"\20\3\20\3\20\5\20\u0102\n\20\3\20\3\20\3\20\3\20\5\20")
        buf.write(u"\u0108\n\20\7\20\u010a\n\20\f\20\16\20\u010d\13\20\7")
        buf.write(u"\20\u010f\n\20\f\20\16\20\u0112\13\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\5\20\u0119\n\20\3\21\3\21\3\21\3\21\5\21\u011f")
        buf.write(u"\n\21\3\21\3\21\3\21\3\21\5\21\u0125\n\21\7\21\u0127")
        buf.write(u"\n\21\f\21\16\21\u012a\13\21\7\21\u012c\n\21\f\21\16")
        buf.write(u"\21\u012f\13\21\3\21\3\21\3\22\3\22\3\22\3\22\7\22\u0137")
        buf.write(u"\n\22\f\22\16\22\u013a\13\22\7\22\u013c\n\22\f\22\16")
        buf.write(u"\22\u013f\13\22\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3")
        buf.write(u"\25\3\25\3\26\3\26\3\26\3\26\7\26\u014e\n\26\f\26\16")
        buf.write(u"\26\u0151\13\26\3\26\3\26\3\26\6\26\u0156\n\26\r\26\16")
        buf.write(u"\26\u0157\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write(u"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write(u"\3\31\3\31\3\31\5\31\u017b\n\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write(u"\7\31\u018c\n\31\f\31\16\31\u018f\13\31\3\32\3\32\3\32")
        buf.write(u"\7\32\u0194\n\32\f\32\16\32\u0197\13\32\3\32\3\32\3\33")
        buf.write(u"\3\33\3\34\3\34\3\34\5\34\u01a0\n\34\3\34\3\34\3\34\5")
        buf.write(u"\34\u01a5\n\34\3\34\3\34\3\35\3\35\3\36\7\36\u01ac\n")
        buf.write(u"\36\f\36\16\36\u01af\13\36\3\36\3\36\3\36\3\36\7\36\u01b5")
        buf.write(u"\n\36\f\36\16\36\u01b8\13\36\3\36\3\36\7\36\u01bc\n\36")
        buf.write(u"\f\36\16\36\u01bf\13\36\3\37\3\37\3 \3 \3!\3!\3!\7!\u01c8")
        buf.write(u"\n!\f!\16!\u01cb\13!\3!\3!\3!\7!\u01d0\n!\f!\16!\u01d3")
        buf.write(u"\13!\7!\u01d5\n!\f!\16!\u01d8\13!\3!\7!\u01db\n!\f!\16")
        buf.write(u"!\u01de\13!\3!\3!\3\"\3\"\3\"\3i\3\60#\2\4\6\b\n\f\16")
        buf.write(u"\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@B\2")
        buf.write(u"\t\3\2\7\b\4\2\30\30&&\3\2*+\3\2,-\3\2\34!\4\2\"\"..")
        buf.write(u"\3\2&\'\u0209\2E\3\2\2\2\4O\3\2\2\2\6a\3\2\2\2\bi\3\2")
        buf.write(u"\2\2\nl\3\2\2\2\f\u0096\3\2\2\2\16\u00b9\3\2\2\2\20\u00bb")
        buf.write(u"\3\2\2\2\22\u00c7\3\2\2\2\24\u00d4\3\2\2\2\26\u00de\3")
        buf.write(u"\2\2\2\30\u00e8\3\2\2\2\32\u00f2\3\2\2\2\34\u00f5\3\2")
        buf.write(u"\2\2\36\u0118\3\2\2\2 \u011a\3\2\2\2\"\u0132\3\2\2\2")
        buf.write(u"$\u0142\3\2\2\2&\u0144\3\2\2\2(\u0147\3\2\2\2*\u0155")
        buf.write(u"\3\2\2\2,\u0159\3\2\2\2.\u015b\3\2\2\2\60\u017a\3\2\2")
        buf.write(u"\2\62\u0190\3\2\2\2\64\u019a\3\2\2\2\66\u019c\3\2\2\2")
        buf.write(u"8\u01a8\3\2\2\2:\u01ad\3\2\2\2<\u01c0\3\2\2\2>\u01c2")
        buf.write(u"\3\2\2\2@\u01c4\3\2\2\2B\u01e1\3\2\2\2DF\5\4\3\2ED\3")
        buf.write(u"\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HL\3\2\2\2IK\5\6")
        buf.write(u"\4\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\3\3\2\2")
        buf.write(u"\2NL\3\2\2\2OP\7\3\2\2PQ\7(\2\2QU\7\4\2\2RT\5\30\r\2")
        buf.write(u"SR\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2\2WU")
        buf.write(u"\3\2\2\2XY\5\26\f\2Y[\5\n\6\2Z\\\5\22\n\2[Z\3\2\2\2\\")
        buf.write(u"]\3\2\2\2][\3\2\2\2]^\3\2\2\2^_\3\2\2\2_`\7\5\2\2`\5")
        buf.write(u"\3\2\2\2ab\7\6\2\2bc\7\4\2\2cd\5\b\5\2de\7\5\2\2e\7\3")
        buf.write(u"\2\2\2fh\n\2\2\2gf\3\2\2\2hk\3\2\2\2ij\3\2\2\2ig\3\2")
        buf.write(u"\2\2j\t\3\2\2\2ki\3\2\2\2lm\7\t\2\2mr\7\4\2\2nq\5\f\7")
        buf.write(u"\2oq\5\16\b\2pn\3\2\2\2po\3\2\2\2qt\3\2\2\2rp\3\2\2\2")
        buf.write(u"rs\3\2\2\2su\3\2\2\2tr\3\2\2\2uv\7\5\2\2v\13\3\2\2\2")
        buf.write(u"wx\7(\2\2xy\7\n\2\2yz\7\13\2\2z\u0080\5\60\31\2{|\7\f")
        buf.write(u"\2\2|}\7\r\2\2}\177\5:\36\2~{\3\2\2\2\177\u0082\3\2\2")
        buf.write(u"\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0097\3\2")
        buf.write(u"\2\2\u0082\u0080\3\2\2\2\u0083\u0088\7(\2\2\u0084\u0085")
        buf.write(u"\7\16\2\2\u0085\u0087\7(\2\2\u0086\u0084\3\2\2\2\u0087")
        buf.write(u"\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2")
        buf.write(u"\2\u0089\u008b\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u008c")
        buf.write(u"\7\n\2\2\u008c\u008d\7\13\2\2\u008d\u0093\5\60\31\2\u008e")
        buf.write(u"\u008f\7\f\2\2\u008f\u0090\7\r\2\2\u0090\u0092\5:\36")
        buf.write(u"\2\u0091\u008e\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091")
        buf.write(u"\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0097\3\2\2\2\u0095")
        buf.write(u"\u0093\3\2\2\2\u0096w\3\2\2\2\u0096\u0083\3\2\2\2\u0097")
        buf.write(u"\r\3\2\2\2\u0098\u0099\7(\2\2\u0099\u009a\7\n\2\2\u009a")
        buf.write(u"\u009b\7\17\2\2\u009b\u009c\7\13\2\2\u009c\u00a2\5\60")
        buf.write(u"\31\2\u009d\u009e\7\f\2\2\u009e\u009f\7\r\2\2\u009f\u00a1")
        buf.write(u"\5:\36\2\u00a0\u009d\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2")
        buf.write(u"\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00ba\3\2\2")
        buf.write(u"\2\u00a4\u00a2\3\2\2\2\u00a5\u00aa\7(\2\2\u00a6\u00a7")
        buf.write(u"\7\16\2\2\u00a7\u00a9\7(\2\2\u00a8\u00a6\3\2\2\2\u00a9")
        buf.write(u"\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2")
        buf.write(u"\2\u00ab\u00ad\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae")
        buf.write(u"\7\n\2\2\u00ae\u00af\7\17\2\2\u00af\u00b0\7\13\2\2\u00b0")
        buf.write(u"\u00b6\5\60\31\2\u00b1\u00b2\7\f\2\2\u00b2\u00b3\7\r")
        buf.write(u"\2\2\u00b3\u00b5\5:\36\2\u00b4\u00b1\3\2\2\2\u00b5\u00b8")
        buf.write(u"\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7")
        buf.write(u"\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u0098\3\2\2")
        buf.write(u"\2\u00b9\u00a5\3\2\2\2\u00ba\17\3\2\2\2\u00bb\u00c1\7")
        buf.write(u"(\2\2\u00bc\u00bd\7\16\2\2\u00bd\u00c0\7(\2\2\u00be\u00c0")
        buf.write(u"\5*\26\2\u00bf\u00bc\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0")
        buf.write(u"\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2")
        buf.write(u"\2\u00c2\u00c4\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5")
        buf.write(u"\7\13\2\2\u00c5\u00c6\5\60\31\2\u00c6\21\3\2\2\2\u00c7")
        buf.write(u"\u00c8\7\20\2\2\u00c8\u00c9\7(\2\2\u00c9\u00cd\7\4\2")
        buf.write(u"\2\u00ca\u00cc\5\24\13\2\u00cb\u00ca\3\2\2\2\u00cc\u00cf")
        buf.write(u"\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write(u"\u00d0\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\5\26\f")
        buf.write(u"\2\u00d1\u00d2\5\n\6\2\u00d2\u00d3\7\5\2\2\u00d3\23\3")
        buf.write(u"\2\2\2\u00d4\u00d5\7\21\2\2\u00d5\u00d9\7\4\2\2\u00d6")
        buf.write(u"\u00d8\5(\25\2\u00d7\u00d6\3\2\2\2\u00d8\u00db\3\2\2")
        buf.write(u"\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00dc")
        buf.write(u"\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00dd\7\5\2\2\u00dd")
        buf.write(u"\25\3\2\2\2\u00de\u00df\7\22\2\2\u00df\u00e3\7\4\2\2")
        buf.write(u"\u00e0\u00e2\5$\23\2\u00e1\u00e0\3\2\2\2\u00e2\u00e5")
        buf.write(u"\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4")
        buf.write(u"\u00e6\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00e7\7\5\2")
        buf.write(u"\2\u00e7\27\3\2\2\2\u00e8\u00e9\7\23\2\2\u00e9\u00ed")
        buf.write(u"\7\4\2\2\u00ea\u00ec\5\32\16\2\u00eb\u00ea\3\2\2\2\u00ec")
        buf.write(u"\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2")
        buf.write(u"\2\u00ee\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f1")
        buf.write(u"\7\5\2\2\u00f1\31\3\2\2\2\u00f2\u00f3\7(\2\2\u00f3\u00f4")
        buf.write(u"\5\"\22\2\u00f4\33\3\2\2\2\u00f5\u00f6\7\4\2\2\u00f6")
        buf.write(u"\u00f7\5\60\31\2\u00f7\u00f8\7\24\2\2\u00f8\u00f9\7(")
        buf.write(u"\2\2\u00f9\u00fa\7\25\2\2\u00fa\u00fb\5\60\31\2\u00fb")
        buf.write(u"\u00fc\7\5\2\2\u00fc\35\3\2\2\2\u00fd\u0110\7\4\2\2\u00fe")
        buf.write(u"\u0102\7(\2\2\u00ff\u0102\5B\"\2\u0100\u0102\58\35\2")
        buf.write(u"\u0101\u00fe\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0100")
        buf.write(u"\3\2\2\2\u0102\u010b\3\2\2\2\u0103\u0107\7\f\2\2\u0104")
        buf.write(u"\u0108\7(\2\2\u0105\u0108\5B\"\2\u0106\u0108\58\35\2")
        buf.write(u"\u0107\u0104\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0106")
        buf.write(u"\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u0103\3\2\2\2\u010a")
        buf.write(u"\u010d\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2")
        buf.write(u"\2\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u0101")
        buf.write(u"\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e\3\2\2\2\u0110")
        buf.write(u"\u0111\3\2\2\2\u0111\u0113\3\2\2\2\u0112\u0110\3\2\2")
        buf.write(u"\2\u0113\u0119\7\5\2\2\u0114\u0115\7\4\2\2\u0115\u0116")
        buf.write(u"\5\36\20\2\u0116\u0117\7\5\2\2\u0117\u0119\3\2\2\2\u0118")
        buf.write(u"\u00fd\3\2\2\2\u0118\u0114\3\2\2\2\u0119\37\3\2\2\2\u011a")
        buf.write(u"\u012d\7\26\2\2\u011b\u011f\7(\2\2\u011c\u011f\5B\"\2")
        buf.write(u"\u011d\u011f\58\35\2\u011e\u011b\3\2\2\2\u011e\u011c")
        buf.write(u"\3\2\2\2\u011e\u011d\3\2\2\2\u011f\u0128\3\2\2\2\u0120")
        buf.write(u"\u0124\7\f\2\2\u0121\u0125\7(\2\2\u0122\u0125\5B\"\2")
        buf.write(u"\u0123\u0125\58\35\2\u0124\u0121\3\2\2\2\u0124\u0122")
        buf.write(u"\3\2\2\2\u0124\u0123\3\2\2\2\u0125\u0127\3\2\2\2\u0126")
        buf.write(u"\u0120\3\2\2\2\u0127\u012a\3\2\2\2\u0128\u0126\3\2\2")
        buf.write(u"\2\u0128\u0129\3\2\2\2\u0129\u012c\3\2\2\2\u012a\u0128")
        buf.write(u"\3\2\2\2\u012b\u011e\3\2\2\2\u012c\u012f\3\2\2\2\u012d")
        buf.write(u"\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u0130\3\2\2")
        buf.write(u"\2\u012f\u012d\3\2\2\2\u0130\u0131\7\27\2\2\u0131!\3")
        buf.write(u"\2\2\2\u0132\u013d\7\26\2\2\u0133\u0138\5B\"\2\u0134")
        buf.write(u"\u0135\7\f\2\2\u0135\u0137\5B\"\2\u0136\u0134\3\2\2\2")
        buf.write(u"\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139")
        buf.write(u"\3\2\2\2\u0139\u013c\3\2\2\2\u013a\u0138\3\2\2\2\u013b")
        buf.write(u"\u0133\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2")
        buf.write(u"\2\u013d\u013e\3\2\2\2\u013e\u0140\3\2\2\2\u013f\u013d")
        buf.write(u"\3\2\2\2\u0140\u0141\7\27\2\2\u0141#\3\2\2\2\u0142\u0143")
        buf.write(u"\7(\2\2\u0143%\3\2\2\2\u0144\u0145\7(\2\2\u0145\u0146")
        buf.write(u"\5*\26\2\u0146\'\3\2\2\2\u0147\u0148\7(\2\2\u0148)\3")
        buf.write(u"\2\2\2\u0149\u014a\7\4\2\2\u014a\u014f\5,\27\2\u014b")
        buf.write(u"\u014c\7-\2\2\u014c\u014e\7&\2\2\u014d\u014b\3\2\2\2")
        buf.write(u"\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150")
        buf.write(u"\3\2\2\2\u0150\u0152\3\2\2\2\u0151\u014f\3\2\2\2\u0152")
        buf.write(u"\u0153\7\5\2\2\u0153\u0156\3\2\2\2\u0154\u0156\7\17\2")
        buf.write(u"\2\u0155\u0149\3\2\2\2\u0155\u0154\3\2\2\2\u0156\u0157")
        buf.write(u"\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158")
        buf.write(u"+\3\2\2\2\u0159\u015a\t\3\2\2\u015a-\3\2\2\2\u015b\u015c")
        buf.write(u"\7\4\2\2\u015c\u015d\58\35\2\u015d\u015e\7\5\2\2\u015e")
        buf.write(u"/\3\2\2\2\u015f\u0160\b\31\1\2\u0160\u0161\7\31\2\2\u0161")
        buf.write(u"\u017b\5\60\31\17\u0162\u017b\5\20\t\2\u0163\u017b\5")
        buf.write(u"\66\34\2\u0164\u0165\7\31\2\2\u0165\u017b\58\35\2\u0166")
        buf.write(u"\u0167\7\31\2\2\u0167\u0168\58\35\2\u0168\u0169\7\f\2")
        buf.write(u"\2\u0169\u017b\3\2\2\2\u016a\u017b\5\36\20\2\u016b\u017b")
        buf.write(u"\5 \21\2\u016c\u017b\58\35\2\u016d\u017b\5B\"\2\u016e")
        buf.write(u"\u017b\5@!\2\u016f\u017b\5\34\17\2\u0170\u017b\7(\2\2")
        buf.write(u"\u0171\u017b\7\32\2\2\u0172\u017b\5&\24\2\u0173\u017b")
        buf.write(u"\5,\27\2\u0174\u0175\5<\37\2\u0175\u0176\5\60\31\2\u0176")
        buf.write(u"\u0177\5> \2\u0177\u017b\3\2\2\2\u0178\u0179\7\33\2\2")
        buf.write(u"\u0179\u017b\7(\2\2\u017a\u015f\3\2\2\2\u017a\u0162\3")
        buf.write(u"\2\2\2\u017a\u0163\3\2\2\2\u017a\u0164\3\2\2\2\u017a")
        buf.write(u"\u0166\3\2\2\2\u017a\u016a\3\2\2\2\u017a\u016b\3\2\2")
        buf.write(u"\2\u017a\u016c\3\2\2\2\u017a\u016d\3\2\2\2\u017a\u016e")
        buf.write(u"\3\2\2\2\u017a\u016f\3\2\2\2\u017a\u0170\3\2\2\2\u017a")
        buf.write(u"\u0171\3\2\2\2\u017a\u0172\3\2\2\2\u017a\u0173\3\2\2")
        buf.write(u"\2\u017a\u0174\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u018d")
        buf.write(u"\3\2\2\2\u017c\u017d\f\27\2\2\u017d\u017e\7\16\2\2\u017e")
        buf.write(u"\u018c\5\60\31\30\u017f\u0180\f\26\2\2\u0180\u0181\7")
        buf.write(u"/\2\2\u0181\u018c\5\60\31\27\u0182\u0183\f\25\2\2\u0183")
        buf.write(u"\u0184\t\4\2\2\u0184\u018c\5\60\31\26\u0185\u0186\f\24")
        buf.write(u"\2\2\u0186\u0187\t\5\2\2\u0187\u018c\5\60\31\25\u0188")
        buf.write(u"\u0189\f\23\2\2\u0189\u018a\7.\2\2\u018a\u018c\5\60\31")
        buf.write(u"\24\u018b\u017c\3\2\2\2\u018b\u017f\3\2\2\2\u018b\u0182")
        buf.write(u"\3\2\2\2\u018b\u0185\3\2\2\2\u018b\u0188\3\2\2\2\u018c")
        buf.write(u"\u018f\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2")
        buf.write(u"\2\u018e\61\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0195\7")
        buf.write(u"\4\2\2\u0191\u0194\5\64\33\2\u0192\u0194\5\66\34\2\u0193")
        buf.write(u"\u0191\3\2\2\2\u0193\u0192\3\2\2\2\u0194\u0197\3\2\2")
        buf.write(u"\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0198")
        buf.write(u"\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u0199\7\5\2\2\u0199")
        buf.write(u"\63\3\2\2\2\u019a\u019b\5\60\31\2\u019b\65\3\2\2\2\u019c")
        buf.write(u"\u019f\7\24\2\2\u019d\u01a0\7(\2\2\u019e\u01a0\5,\27")
        buf.write(u"\2\u019f\u019d\3\2\2\2\u019f\u019e\3\2\2\2\u01a0\u01a1")
        buf.write(u"\3\2\2\2\u01a1\u01a4\7\25\2\2\u01a2\u01a5\7(\2\2\u01a3")
        buf.write(u"\u01a5\5@!\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2")
        buf.write(u"\u01a5\u01a6\3\2\2\2\u01a6\u01a7\7\32\2\2\u01a7\67\3")
        buf.write(u"\2\2\2\u01a8\u01a9\7\60\2\2\u01a99\3\2\2\2\u01aa\u01ac")
        buf.write(u"\5<\37\2\u01ab\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad")
        buf.write(u"\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01b0\3\2\2")
        buf.write(u"\2\u01af\u01ad\3\2\2\2\u01b0\u01b1\5\60\31\2\u01b1\u01b2")
        buf.write(u"\t\6\2\2\u01b2\u01b6\5\60\31\2\u01b3\u01b5\5> \2\u01b4")
        buf.write(u"\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2")
        buf.write(u"\2\u01b6\u01b7\3\2\2\2\u01b7\u01bd\3\2\2\2\u01b8\u01b6")
        buf.write(u"\3\2\2\2\u01b9\u01ba\t\7\2\2\u01ba\u01bc\5:\36\2\u01bb")
        buf.write(u"\u01b9\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd\u01bb\3\2\2")
        buf.write(u"\2\u01bd\u01be\3\2\2\2\u01be;\3\2\2\2\u01bf\u01bd\3\2")
        buf.write(u"\2\2\u01c0\u01c1\7\26\2\2\u01c1=\3\2\2\2\u01c2\u01c3")
        buf.write(u"\7\27\2\2\u01c3?\3\2\2\2\u01c4\u01c5\7(\2\2\u01c5\u01c9")
        buf.write(u"\7\26\2\2\u01c6\u01c8\5<\37\2\u01c7\u01c6\3\2\2\2\u01c8")
        buf.write(u"\u01cb\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2")
        buf.write(u"\2\u01ca\u01d6\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01d1")
        buf.write(u"\5\60\31\2\u01cd\u01ce\7\f\2\2\u01ce\u01d0\5\60\31\2")
        buf.write(u"\u01cf\u01cd\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf")
        buf.write(u"\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3")
        buf.write(u"\u01d1\3\2\2\2\u01d4\u01cc\3\2\2\2\u01d5\u01d8\3\2\2")
        buf.write(u"\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01dc")
        buf.write(u"\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01db\5> \2\u01da")
        buf.write(u"\u01d9\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da\3\2\2")
        buf.write(u"\2\u01dc\u01dd\3\2\2\2\u01dd\u01df\3\2\2\2\u01de\u01dc")
        buf.write(u"\3\2\2\2\u01df\u01e0\7\27\2\2\u01e0A\3\2\2\2\u01e1\u01e2")
        buf.write(u"\t\b\2\2\u01e2C\3\2\2\2\63GLU]ipr\u0080\u0088\u0093\u0096")
        buf.write(u"\u00a2\u00aa\u00b6\u00b9\u00bf\u00c1\u00cd\u00d9\u00e3")
        buf.write(u"\u00ed\u0101\u0107\u010b\u0110\u0118\u011e\u0124\u0128")
        buf.write(u"\u012d\u0138\u013d\u014f\u0155\u0157\u017a\u018b\u018d")
        buf.write(u"\u0193\u0195\u019f\u01a4\u01ad\u01b6\u01bd\u01c9\u01d1")
        buf.write(u"\u01d6\u01dc")
        return buf.getvalue()
		

class PrigogineParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'model'", u"'['", u"']'", u"'simulation'", 
                     u"'\n'", u"'\r'", u"'equations'", u"'[t+1]'", u"'='", 
                     u"','", u"'where'", u"'.'", u"'[:]'", u"'population'", 
                     u"'parameters'", u"'variables'", u"'messageboards'", 
                     u"'for'", u"'in'", u"'('", u"')'", u"'t'", u"'print'", 
                     u"':'", u"'return'", u"'<'", u"'>'", u"'>='", u"'<='", 
                     u"'=='", u"'!='", u"'&'", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'*'", u"'/'", u"'+'", u"'-'", u"'|'", 
                     u"'^'" ]

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
    RULE_msgboardlist = 11
    RULE_msgboarddef = 12
    RULE_listcomp = 13
    RULE_listdef = 14
    RULE_tupledef = 15
    RULE_numbertuple = 16
    RULE_variable = 17
    RULE_indexedvariable = 18
    RULE_parameter = 19
    RULE_timeindex = 20
    RULE_timevar = 21
    RULE_dictindex = 22
    RULE_expression = 23
    RULE_codeblock = 24
    RULE_codeline = 25
    RULE_pyforloop = 26
    RULE_string = 27
    RULE_conditional = 28
    RULE_lparen = 29
    RULE_rparen = 30
    RULE_func = 31
    RULE_number = 32

    ruleNames =  [ u"filestart", u"model", u"simulation", u"codeinsert", 
                   u"equationlist", u"elementwiseEquation", u"mapEquation", 
                   u"assignment", u"population", u"parameterlist", u"variablelist", 
                   u"msgboardlist", u"msgboarddef", u"listcomp", u"listdef", 
                   u"tupledef", u"numbertuple", u"variable", u"indexedvariable", 
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
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66 
                self.model()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrigogineParser.T__0):
                    break

            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__3:
                self.state = 71 
                self.simulation()
                self.state = 76
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


        def msgboardlist(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.MsgboardlistContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.MsgboardlistContext,i)


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
            self.state = 77
            self.match(PrigogineParser.T__0)
            self.state = 78
            self.match(PrigogineParser.ID)
            self.state = 79
            self.match(PrigogineParser.T__1)

            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__16:
                self.state = 80 
                self.msgboardlist()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86 
            self.variablelist()
            self.state = 87 
            self.equationlist()
            self.state = 89 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 88 
                self.population()
                self.state = 91 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrigogineParser.T__13):
                    break

            self.state = 93
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
            self.state = 95
            self.match(PrigogineParser.T__3)
            self.state = 96
            self.match(PrigogineParser.T__1)
            self.state = 97 
            self.codeinsert()
            self.state = 98
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
            self.state = 103
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 100
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==PrigogineParser.T__4 or _la==PrigogineParser.T__5:
                        self._errHandler.recoverInline(self)
                    self.consume() 
                self.state = 105
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
            self.state = 106
            self.match(PrigogineParser.T__6)
            self.state = 107
            self.match(PrigogineParser.T__1)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 110
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 108 
                    self.elementwiseEquation()
                    pass

                elif la_ == 2:
                    self.state = 109 
                    self.mapEquation()
                    pass


                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
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
            self.state = 148
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(PrigogineParser.ID)
                self.state = 118
                self.match(PrigogineParser.T__7)
                self.state = 119
                self.match(PrigogineParser.T__8)
                self.state = 120 
                self.expression(0)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 121
                    self.match(PrigogineParser.T__9)
                    self.state = 122
                    self.match(PrigogineParser.T__10)
                    self.state = 123 
                    self.conditional()
                    self.state = 128
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(PrigogineParser.ID)
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__11:
                    self.state = 130
                    self.match(PrigogineParser.T__11)
                    self.state = 131
                    self.match(PrigogineParser.ID)
                    self.state = 136
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 137
                self.match(PrigogineParser.T__7)
                self.state = 138
                self.match(PrigogineParser.T__8)
                self.state = 139 
                self.expression(0)
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 140
                    self.match(PrigogineParser.T__9)
                    self.state = 141
                    self.match(PrigogineParser.T__10)
                    self.state = 142 
                    self.conditional()
                    self.state = 147
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
            self.state = 183
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(PrigogineParser.ID)
                self.state = 151
                self.match(PrigogineParser.T__7)
                self.state = 152
                self.match(PrigogineParser.T__12)
                self.state = 153
                self.match(PrigogineParser.T__8)
                self.state = 154 
                self.expression(0)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 155
                    self.match(PrigogineParser.T__9)
                    self.state = 156
                    self.match(PrigogineParser.T__10)
                    self.state = 157 
                    self.conditional()
                    self.state = 162
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(PrigogineParser.ID)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__11:
                    self.state = 164
                    self.match(PrigogineParser.T__11)
                    self.state = 165
                    self.match(PrigogineParser.ID)
                    self.state = 170
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 171
                self.match(PrigogineParser.T__7)
                self.state = 172
                self.match(PrigogineParser.T__12)
                self.state = 173
                self.match(PrigogineParser.T__8)
                self.state = 174 
                self.expression(0)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 175
                    self.match(PrigogineParser.T__9)
                    self.state = 176
                    self.match(PrigogineParser.T__10)
                    self.state = 177 
                    self.conditional()
                    self.state = 182
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
            self.state = 185
            self.match(PrigogineParser.ID)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__11) | (1 << PrigogineParser.T__12))) != 0):
                self.state = 189
                token = self._input.LA(1)
                if token in [PrigogineParser.T__11]:
                    self.state = 186
                    self.match(PrigogineParser.T__11)
                    self.state = 187
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.T__1, PrigogineParser.T__12]:
                    self.state = 188 
                    self.timeindex()

                else:
                    raise NoViableAltException(self)

                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 194
            self.match(PrigogineParser.T__8)
            self.state = 195 
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
            self.state = 197
            self.match(PrigogineParser.T__13)
            self.state = 198
            self.match(PrigogineParser.ID)
            self.state = 199
            self.match(PrigogineParser.T__1)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__14:
                self.state = 200 
                self.parameterlist()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206 
            self.variablelist()
            self.state = 207 
            self.equationlist()
            self.state = 208
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
            self.state = 210
            self.match(PrigogineParser.T__14)
            self.state = 211
            self.match(PrigogineParser.T__1)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 212 
                self.parameter()
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 218
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
            self.state = 220
            self.match(PrigogineParser.T__15)
            self.state = 221
            self.match(PrigogineParser.T__1)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 222 
                self.variable()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 228
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MsgboardlistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.MsgboardlistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def msgboarddef(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.MsgboarddefContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.MsgboarddefContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_msgboardlist

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterMsgboardlist(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitMsgboardlist(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitMsgboardlist(self)
            else:
                return visitor.visitChildren(self)




    def msgboardlist(self):

        localctx = PrigogineParser.MsgboardlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_msgboardlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(PrigogineParser.T__16)
            self.state = 231
            self.match(PrigogineParser.T__1)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 232 
                self.msgboarddef()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 238
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MsgboarddefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.MsgboarddefContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def numbertuple(self):
            return self.getTypedRuleContext(PrigogineParser.NumbertupleContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_msgboarddef

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterMsgboarddef(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitMsgboarddef(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitMsgboarddef(self)
            else:
                return visitor.visitChildren(self)




    def msgboarddef(self):

        localctx = PrigogineParser.MsgboarddefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_msgboarddef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(PrigogineParser.ID)
            self.state = 241 
            self.numbertuple()
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
        self.enterRule(localctx, 26, self.RULE_listcomp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(PrigogineParser.T__1)
            self.state = 244 
            self.expression(0)
            self.state = 245
            self.match(PrigogineParser.T__17)
            self.state = 246
            self.match(PrigogineParser.ID)
            self.state = 247
            self.match(PrigogineParser.T__18)
            self.state = 248 
            self.expression(0)
            self.state = 249
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
        self.enterRule(localctx, 28, self.RULE_listdef)
        self._la = 0 # Token type
        try:
            self.state = 278
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(PrigogineParser.T__1)
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                    self.state = 255
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 252
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 253 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 254 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 265
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==PrigogineParser.T__9:
                        self.state = 257
                        self.match(PrigogineParser.T__9)
                        self.state = 261
                        token = self._input.LA(1)
                        if token in [PrigogineParser.ID]:
                            self.state = 258
                            self.match(PrigogineParser.ID)

                        elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                            self.state = 259 
                            self.number()

                        elif token in [PrigogineParser.STRING]:
                            self.state = 260 
                            self.string()

                        else:
                            raise NoViableAltException(self)

                        self.state = 267
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 272
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 273
                self.match(PrigogineParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.match(PrigogineParser.T__1)
                self.state = 275 
                self.listdef()
                self.state = 276
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
        self.enterRule(localctx, 30, self.RULE_tupledef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(PrigogineParser.T__19)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 284
                token = self._input.LA(1)
                if token in [PrigogineParser.ID]:
                    self.state = 281
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                    self.state = 282 
                    self.number()

                elif token in [PrigogineParser.STRING]:
                    self.state = 283 
                    self.string()

                else:
                    raise NoViableAltException(self)

                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 286
                    self.match(PrigogineParser.T__9)
                    self.state = 290
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 287
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 288 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 289 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 296
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 302
            self.match(PrigogineParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumbertupleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.NumbertupleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def number(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.NumberContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.NumberContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_numbertuple

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterNumbertuple(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitNumbertuple(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitNumbertuple(self)
            else:
                return visitor.visitChildren(self)




    def numbertuple(self):

        localctx = PrigogineParser.NumbertupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_numbertuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(PrigogineParser.T__19)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.INT or _la==PrigogineParser.FLOAT:
                self.state = 305 
                self.number()
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 306
                    self.match(PrigogineParser.T__9)
                    self.state = 307 
                    self.number()
                    self.state = 312
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 318
            self.match(PrigogineParser.T__20)
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
        self.enterRule(localctx, 34, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
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
        self.enterRule(localctx, 36, self.RULE_indexedvariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(PrigogineParser.ID)
            self.state = 323 
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
        self.enterRule(localctx, 38, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
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
        self.enterRule(localctx, 40, self.RULE_timeindex)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 339
                    token = self._input.LA(1)
                    if token in [PrigogineParser.T__1]:
                        self.state = 327
                        self.match(PrigogineParser.T__1)
                        self.state = 328 
                        self.timevar()
                        self.state = 333
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==PrigogineParser.SUB:
                            self.state = 329
                            self.match(PrigogineParser.SUB)
                            self.state = 330
                            self.match(PrigogineParser.INT)
                            self.state = 335
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 336
                        self.match(PrigogineParser.T__2)

                    elif token in [PrigogineParser.T__12]:
                        self.state = 338
                        self.match(PrigogineParser.T__12)

                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 341 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_timevar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
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
        self.enterRule(localctx, 44, self.RULE_dictindex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(PrigogineParser.T__1)
            self.state = 346 
            self.string()
            self.state = 347
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 350
                self.match(PrigogineParser.T__22)
                self.state = 351 
                self.expression(13)
                pass

            elif la_ == 2:
                self.state = 352 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 353 
                self.pyforloop()
                pass

            elif la_ == 4:
                self.state = 354
                self.match(PrigogineParser.T__22)
                self.state = 355 
                self.string()
                pass

            elif la_ == 5:
                self.state = 356
                self.match(PrigogineParser.T__22)
                self.state = 357 
                self.string()
                self.state = 358
                self.match(PrigogineParser.T__9)
                pass

            elif la_ == 6:
                self.state = 360 
                self.listdef()
                pass

            elif la_ == 7:
                self.state = 361 
                self.tupledef()
                pass

            elif la_ == 8:
                self.state = 362 
                self.string()
                pass

            elif la_ == 9:
                self.state = 363 
                self.number()
                pass

            elif la_ == 10:
                self.state = 364 
                self.func()
                pass

            elif la_ == 11:
                self.state = 365 
                self.listcomp()
                pass

            elif la_ == 12:
                self.state = 366
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 13:
                self.state = 367
                self.match(PrigogineParser.T__23)
                pass

            elif la_ == 14:
                self.state = 368 
                self.indexedvariable()
                pass

            elif la_ == 15:
                self.state = 369 
                self.timevar()
                pass

            elif la_ == 16:
                self.state = 370 
                self.lparen()
                self.state = 371 
                self.expression(0)
                self.state = 372 
                self.rparen()
                pass

            elif la_ == 17:
                self.state = 374
                self.match(PrigogineParser.T__24)
                self.state = 375
                self.match(PrigogineParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 395
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 393
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 378
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 379
                        self.match(PrigogineParser.T__11)
                        self.state = 380 
                        self.expression(22)
                        pass

                    elif la_ == 2:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 381
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 382
                        self.match(PrigogineParser.POWER)
                        self.state = 383 
                        self.expression(21)
                        pass

                    elif la_ == 3:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 384
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 385
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.MUL or _la==PrigogineParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 386 
                        self.expression(20)
                        pass

                    elif la_ == 4:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 387
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 388
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 389 
                        self.expression(19)
                        pass

                    elif la_ == 5:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 390
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 391
                        localctx.op = self.match(PrigogineParser.PIPE)
                        self.state = 392 
                        self.expression(18)
                        pass

             
                self.state = 397
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
        self.enterRule(localctx, 48, self.RULE_codeblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(PrigogineParser.T__1)
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__17) | (1 << PrigogineParser.T__19) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.T__22) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 401
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 399 
                    self.codeline()
                    pass

                elif la_ == 2:
                    self.state = 400 
                    self.pyforloop()
                    pass


                self.state = 405
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 406
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
        self.enterRule(localctx, 50, self.RULE_codeline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408 
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
        self.enterRule(localctx, 52, self.RULE_pyforloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(PrigogineParser.T__17)
            self.state = 413
            token = self._input.LA(1)
            if token in [PrigogineParser.ID]:
                self.state = 411
                self.match(PrigogineParser.ID)

            elif token in [PrigogineParser.T__21, PrigogineParser.INT]:
                self.state = 412 
                self.timevar()

            else:
                raise NoViableAltException(self)

            self.state = 415
            self.match(PrigogineParser.T__18)
            self.state = 418
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 416
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 2:
                self.state = 417 
                self.func()
                pass


            self.state = 420
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
        self.enterRule(localctx, 54, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
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
        self.enterRule(localctx, 56, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 424 
                    self.lparen() 
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 430 
            self.expression(0)
            self.state = 431
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__25) | (1 << PrigogineParser.T__26) | (1 << PrigogineParser.T__27) | (1 << PrigogineParser.T__28) | (1 << PrigogineParser.T__29) | (1 << PrigogineParser.T__30))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            self.consume()
            self.state = 432 
            self.expression(0)
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__20:
                self.state = 433 
                self.rparen()
                self.state = 438
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 443
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 439
                    _la = self._input.LA(1)
                    if not(_la==PrigogineParser.T__31 or _la==PrigogineParser.PIPE):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 440 
                    self.conditional() 
                self.state = 445
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        self.enterRule(localctx, 58, self.RULE_lparen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(PrigogineParser.T__19)
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
        self.enterRule(localctx, 60, self.RULE_rparen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(PrigogineParser.T__20)
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
        self.enterRule(localctx, 62, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(PrigogineParser.ID)
            self.state = 451
            self.match(PrigogineParser.T__19)
            self.state = 455
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 452 
                    self.lparen() 
                self.state = 457
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__17) | (1 << PrigogineParser.T__19) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.T__22) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 458 
                self.expression(0)
                self.state = 463
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 459
                    self.match(PrigogineParser.T__9)
                    self.state = 460 
                    self.expression(0)
                    self.state = 465
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 470
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 474
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 471 
                    self.rparen() 
                self.state = 476
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

            self.state = 477
            self.match(PrigogineParser.T__20)
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
        self.enterRule(localctx, 64, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
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
        self._predicates[23] = self.expression_sempred
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
         



