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
        buf.write(u"\62\u01df\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\6\2")
        buf.write(u"F\n\2\r\2\16\2G\3\2\7\2K\n\2\f\2\16\2N\13\2\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\6\3W\n\3\r\3\16\3X\3\3\3\3\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\5\7\5c\n\5\f\5\16\5f\13\5\3\6\3\6\3\6")
        buf.write(u"\3\6\7\6l\n\6\f\6\16\6o\13\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write(u"\3\7\3\7\3\7\7\7z\n\7\f\7\16\7}\13\7\3\7\3\7\3\7\7\7")
        buf.write(u"\u0082\n\7\f\7\16\7\u0085\13\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write(u"\7\7\7\u008d\n\7\f\7\16\7\u0090\13\7\5\7\u0092\n\7\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u009c\n\b\f\b\16\b")
        buf.write(u"\u009f\13\b\3\b\3\b\3\b\7\b\u00a4\n\b\f\b\16\b\u00a7")
        buf.write(u"\13\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00b0\n\b\f\b\16")
        buf.write(u"\b\u00b3\13\b\5\b\u00b5\n\b\3\t\3\t\3\t\3\t\7\t\u00bb")
        buf.write(u"\n\t\f\t\16\t\u00be\13\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write(u"\7\n\u00c7\n\n\f\n\16\n\u00ca\13\n\3\n\3\n\3\n\3\n\3")
        buf.write(u"\13\3\13\3\13\7\13\u00d3\n\13\f\13\16\13\u00d6\13\13")
        buf.write(u"\3\13\3\13\3\f\3\f\3\f\7\f\u00dd\n\f\f\f\16\f\u00e0\13")
        buf.write(u"\f\3\f\3\f\3\r\3\r\3\r\7\r\u00e7\n\r\f\r\16\r\u00ea\13")
        buf.write(u"\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\20\3\20\3\20\3\20\5\20\u00fd\n\20\3\20")
        buf.write(u"\3\20\3\20\3\20\5\20\u0103\n\20\7\20\u0105\n\20\f\20")
        buf.write(u"\16\20\u0108\13\20\7\20\u010a\n\20\f\20\16\20\u010d\13")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\5\20\u0114\n\20\3\21\3\21")
        buf.write(u"\3\21\3\21\5\21\u011a\n\21\3\21\3\21\3\21\3\21\5\21\u0120")
        buf.write(u"\n\21\7\21\u0122\n\21\f\21\16\21\u0125\13\21\7\21\u0127")
        buf.write(u"\n\21\f\21\16\21\u012a\13\21\3\21\3\21\3\22\3\22\3\22")
        buf.write(u"\3\22\7\22\u0132\n\22\f\22\16\22\u0135\13\22\7\22\u0137")
        buf.write(u"\n\22\f\22\16\22\u013a\13\22\3\22\3\22\3\23\3\23\3\24")
        buf.write(u"\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26\7\26\u0149\n")
        buf.write(u"\26\f\26\16\26\u014c\13\26\3\26\3\26\3\26\6\26\u0151")
        buf.write(u"\n\26\r\26\16\26\u0152\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write(u"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write(u"\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0176\n\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write(u"\3\31\3\31\3\31\7\31\u0187\n\31\f\31\16\31\u018a\13\31")
        buf.write(u"\3\32\3\32\3\32\7\32\u018f\n\32\f\32\16\32\u0192\13\32")
        buf.write(u"\3\32\3\32\3\33\3\33\3\34\3\34\3\34\5\34\u019b\n\34\3")
        buf.write(u"\34\3\34\3\34\5\34\u01a0\n\34\3\34\3\34\3\35\3\35\3\36")
        buf.write(u"\7\36\u01a7\n\36\f\36\16\36\u01aa\13\36\3\36\3\36\3\36")
        buf.write(u"\3\36\7\36\u01b0\n\36\f\36\16\36\u01b3\13\36\3\36\3\36")
        buf.write(u"\7\36\u01b7\n\36\f\36\16\36\u01ba\13\36\3\37\3\37\3 ")
        buf.write(u"\3 \3!\3!\3!\7!\u01c3\n!\f!\16!\u01c6\13!\3!\3!\3!\7")
        buf.write(u"!\u01cb\n!\f!\16!\u01ce\13!\7!\u01d0\n!\f!\16!\u01d3")
        buf.write(u"\13!\3!\7!\u01d6\n!\f!\16!\u01d9\13!\3!\3!\3\"\3\"\3")
        buf.write(u"\"\3d\3\60#\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write(u"$&(*,.\60\62\64\668:<>@B\2\t\3\2\7\b\4\2\30\30&&\3\2")
        buf.write(u"*+\3\2,-\3\2\34!\4\2\"\"..\3\2&\'\u0203\2E\3\2\2\2\4")
        buf.write(u"O\3\2\2\2\6\\\3\2\2\2\bd\3\2\2\2\ng\3\2\2\2\f\u0091\3")
        buf.write(u"\2\2\2\16\u00b4\3\2\2\2\20\u00b6\3\2\2\2\22\u00c2\3\2")
        buf.write(u"\2\2\24\u00cf\3\2\2\2\26\u00d9\3\2\2\2\30\u00e3\3\2\2")
        buf.write(u"\2\32\u00ed\3\2\2\2\34\u00f0\3\2\2\2\36\u0113\3\2\2\2")
        buf.write(u" \u0115\3\2\2\2\"\u012d\3\2\2\2$\u013d\3\2\2\2&\u013f")
        buf.write(u"\3\2\2\2(\u0142\3\2\2\2*\u0150\3\2\2\2,\u0154\3\2\2\2")
        buf.write(u".\u0156\3\2\2\2\60\u0175\3\2\2\2\62\u018b\3\2\2\2\64")
        buf.write(u"\u0195\3\2\2\2\66\u0197\3\2\2\28\u01a3\3\2\2\2:\u01a8")
        buf.write(u"\3\2\2\2<\u01bb\3\2\2\2>\u01bd\3\2\2\2@\u01bf\3\2\2\2")
        buf.write(u"B\u01dc\3\2\2\2DF\5\4\3\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2")
        buf.write(u"\2GH\3\2\2\2HL\3\2\2\2IK\5\6\4\2JI\3\2\2\2KN\3\2\2\2")
        buf.write(u"LJ\3\2\2\2LM\3\2\2\2M\3\3\2\2\2NL\3\2\2\2OP\7\3\2\2P")
        buf.write(u"Q\7(\2\2QR\7\4\2\2RS\5\30\r\2ST\5\26\f\2TV\5\n\6\2UW")
        buf.write(u"\5\22\n\2VU\3\2\2\2WX\3\2\2\2XV\3\2\2\2XY\3\2\2\2YZ\3")
        buf.write(u"\2\2\2Z[\7\5\2\2[\5\3\2\2\2\\]\7\6\2\2]^\7\4\2\2^_\5")
        buf.write(u"\b\5\2_`\7\5\2\2`\7\3\2\2\2ac\n\2\2\2ba\3\2\2\2cf\3\2")
        buf.write(u"\2\2de\3\2\2\2db\3\2\2\2e\t\3\2\2\2fd\3\2\2\2gh\7\t\2")
        buf.write(u"\2hm\7\4\2\2il\5\f\7\2jl\5\16\b\2ki\3\2\2\2kj\3\2\2\2")
        buf.write(u"lo\3\2\2\2mk\3\2\2\2mn\3\2\2\2np\3\2\2\2om\3\2\2\2pq")
        buf.write(u"\7\5\2\2q\13\3\2\2\2rs\7(\2\2st\7\n\2\2tu\7\13\2\2u{")
        buf.write(u"\5\60\31\2vw\7\f\2\2wx\7\r\2\2xz\5:\36\2yv\3\2\2\2z}")
        buf.write(u"\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\u0092\3\2\2\2}{\3\2\2\2")
        buf.write(u"~\u0083\7(\2\2\177\u0080\7\16\2\2\u0080\u0082\7(\2\2")
        buf.write(u"\u0081\177\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3")
        buf.write(u"\2\2\2\u0083\u0084\3\2\2\2\u0084\u0086\3\2\2\2\u0085")
        buf.write(u"\u0083\3\2\2\2\u0086\u0087\7\n\2\2\u0087\u0088\7\13\2")
        buf.write(u"\2\u0088\u008e\5\60\31\2\u0089\u008a\7\f\2\2\u008a\u008b")
        buf.write(u"\7\r\2\2\u008b\u008d\5:\36\2\u008c\u0089\3\2\2\2\u008d")
        buf.write(u"\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2")
        buf.write(u"\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0091r\3\2")
        buf.write(u"\2\2\u0091~\3\2\2\2\u0092\r\3\2\2\2\u0093\u0094\7(\2")
        buf.write(u"\2\u0094\u0095\7\n\2\2\u0095\u0096\7\17\2\2\u0096\u0097")
        buf.write(u"\7\13\2\2\u0097\u009d\5\60\31\2\u0098\u0099\7\f\2\2\u0099")
        buf.write(u"\u009a\7\r\2\2\u009a\u009c\5:\36\2\u009b\u0098\3\2\2")
        buf.write(u"\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e")
        buf.write(u"\3\2\2\2\u009e\u00b5\3\2\2\2\u009f\u009d\3\2\2\2\u00a0")
        buf.write(u"\u00a5\7(\2\2\u00a1\u00a2\7\16\2\2\u00a2\u00a4\7(\2\2")
        buf.write(u"\u00a3\u00a1\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3")
        buf.write(u"\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7")
        buf.write(u"\u00a5\3\2\2\2\u00a8\u00a9\7\n\2\2\u00a9\u00aa\7\17\2")
        buf.write(u"\2\u00aa\u00ab\7\13\2\2\u00ab\u00b1\5\60\31\2\u00ac\u00ad")
        buf.write(u"\7\f\2\2\u00ad\u00ae\7\r\2\2\u00ae\u00b0\5:\36\2\u00af")
        buf.write(u"\u00ac\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2")
        buf.write(u"\2\u00b1\u00b2\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1")
        buf.write(u"\3\2\2\2\u00b4\u0093\3\2\2\2\u00b4\u00a0\3\2\2\2\u00b5")
        buf.write(u"\17\3\2\2\2\u00b6\u00bc\7(\2\2\u00b7\u00b8\7\16\2\2\u00b8")
        buf.write(u"\u00bb\7(\2\2\u00b9\u00bb\5*\26\2\u00ba\u00b7\3\2\2\2")
        buf.write(u"\u00ba\u00b9\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00ba")
        buf.write(u"\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00bf\3\2\2\2\u00be")
        buf.write(u"\u00bc\3\2\2\2\u00bf\u00c0\7\13\2\2\u00c0\u00c1\5\60")
        buf.write(u"\31\2\u00c1\21\3\2\2\2\u00c2\u00c3\7\20\2\2\u00c3\u00c4")
        buf.write(u"\7(\2\2\u00c4\u00c8\7\4\2\2\u00c5\u00c7\5\24\13\2\u00c6")
        buf.write(u"\u00c5\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2")
        buf.write(u"\2\u00c8\u00c9\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00c8")
        buf.write(u"\3\2\2\2\u00cb\u00cc\5\26\f\2\u00cc\u00cd\5\n\6\2\u00cd")
        buf.write(u"\u00ce\7\5\2\2\u00ce\23\3\2\2\2\u00cf\u00d0\7\21\2\2")
        buf.write(u"\u00d0\u00d4\7\4\2\2\u00d1\u00d3\5(\25\2\u00d2\u00d1")
        buf.write(u"\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4")
        buf.write(u"\u00d5\3\2\2\2\u00d5\u00d7\3\2\2\2\u00d6\u00d4\3\2\2")
        buf.write(u"\2\u00d7\u00d8\7\5\2\2\u00d8\25\3\2\2\2\u00d9\u00da\7")
        buf.write(u"\22\2\2\u00da\u00de\7\4\2\2\u00db\u00dd\5$\23\2\u00dc")
        buf.write(u"\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2")
        buf.write(u"\2\u00de\u00df\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0\u00de")
        buf.write(u"\3\2\2\2\u00e1\u00e2\7\5\2\2\u00e2\27\3\2\2\2\u00e3\u00e4")
        buf.write(u"\7\23\2\2\u00e4\u00e8\7\4\2\2\u00e5\u00e7\5\32\16\2\u00e6")
        buf.write(u"\u00e5\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8\u00e6\3\2\2")
        buf.write(u"\2\u00e8\u00e9\3\2\2\2\u00e9\u00eb\3\2\2\2\u00ea\u00e8")
        buf.write(u"\3\2\2\2\u00eb\u00ec\7\5\2\2\u00ec\31\3\2\2\2\u00ed\u00ee")
        buf.write(u"\7(\2\2\u00ee\u00ef\5\"\22\2\u00ef\33\3\2\2\2\u00f0\u00f1")
        buf.write(u"\7\4\2\2\u00f1\u00f2\5\60\31\2\u00f2\u00f3\7\24\2\2\u00f3")
        buf.write(u"\u00f4\7(\2\2\u00f4\u00f5\7\25\2\2\u00f5\u00f6\5\60\31")
        buf.write(u"\2\u00f6\u00f7\7\5\2\2\u00f7\35\3\2\2\2\u00f8\u010b\7")
        buf.write(u"\4\2\2\u00f9\u00fd\7(\2\2\u00fa\u00fd\5B\"\2\u00fb\u00fd")
        buf.write(u"\58\35\2\u00fc\u00f9\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc")
        buf.write(u"\u00fb\3\2\2\2\u00fd\u0106\3\2\2\2\u00fe\u0102\7\f\2")
        buf.write(u"\2\u00ff\u0103\7(\2\2\u0100\u0103\5B\"\2\u0101\u0103")
        buf.write(u"\58\35\2\u0102\u00ff\3\2\2\2\u0102\u0100\3\2\2\2\u0102")
        buf.write(u"\u0101\3\2\2\2\u0103\u0105\3\2\2\2\u0104\u00fe\3\2\2")
        buf.write(u"\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107")
        buf.write(u"\3\2\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2\u0109")
        buf.write(u"\u00fc\3\2\2\2\u010a\u010d\3\2\2\2\u010b\u0109\3\2\2")
        buf.write(u"\2\u010b\u010c\3\2\2\2\u010c\u010e\3\2\2\2\u010d\u010b")
        buf.write(u"\3\2\2\2\u010e\u0114\7\5\2\2\u010f\u0110\7\4\2\2\u0110")
        buf.write(u"\u0111\5\36\20\2\u0111\u0112\7\5\2\2\u0112\u0114\3\2")
        buf.write(u"\2\2\u0113\u00f8\3\2\2\2\u0113\u010f\3\2\2\2\u0114\37")
        buf.write(u"\3\2\2\2\u0115\u0128\7\26\2\2\u0116\u011a\7(\2\2\u0117")
        buf.write(u"\u011a\5B\"\2\u0118\u011a\58\35\2\u0119\u0116\3\2\2\2")
        buf.write(u"\u0119\u0117\3\2\2\2\u0119\u0118\3\2\2\2\u011a\u0123")
        buf.write(u"\3\2\2\2\u011b\u011f\7\f\2\2\u011c\u0120\7(\2\2\u011d")
        buf.write(u"\u0120\5B\"\2\u011e\u0120\58\35\2\u011f\u011c\3\2\2\2")
        buf.write(u"\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u0120\u0122")
        buf.write(u"\3\2\2\2\u0121\u011b\3\2\2\2\u0122\u0125\3\2\2\2\u0123")
        buf.write(u"\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0127\3\2\2")
        buf.write(u"\2\u0125\u0123\3\2\2\2\u0126\u0119\3\2\2\2\u0127\u012a")
        buf.write(u"\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129")
        buf.write(u"\u012b\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u012c\7\27\2")
        buf.write(u"\2\u012c!\3\2\2\2\u012d\u0138\7\26\2\2\u012e\u0133\5")
        buf.write(u"B\"\2\u012f\u0130\7\f\2\2\u0130\u0132\5B\"\2\u0131\u012f")
        buf.write(u"\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0133")
        buf.write(u"\u0134\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2")
        buf.write(u"\2\u0136\u012e\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136")
        buf.write(u"\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013b\3\2\2\2\u013a")
        buf.write(u"\u0138\3\2\2\2\u013b\u013c\7\27\2\2\u013c#\3\2\2\2\u013d")
        buf.write(u"\u013e\7(\2\2\u013e%\3\2\2\2\u013f\u0140\7(\2\2\u0140")
        buf.write(u"\u0141\5*\26\2\u0141\'\3\2\2\2\u0142\u0143\7(\2\2\u0143")
        buf.write(u")\3\2\2\2\u0144\u0145\7\4\2\2\u0145\u014a\5,\27\2\u0146")
        buf.write(u"\u0147\7-\2\2\u0147\u0149\7&\2\2\u0148\u0146\3\2\2\2")
        buf.write(u"\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b")
        buf.write(u"\3\2\2\2\u014b\u014d\3\2\2\2\u014c\u014a\3\2\2\2\u014d")
        buf.write(u"\u014e\7\5\2\2\u014e\u0151\3\2\2\2\u014f\u0151\7\17\2")
        buf.write(u"\2\u0150\u0144\3\2\2\2\u0150\u014f\3\2\2\2\u0151\u0152")
        buf.write(u"\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153")
        buf.write(u"+\3\2\2\2\u0154\u0155\t\3\2\2\u0155-\3\2\2\2\u0156\u0157")
        buf.write(u"\7\4\2\2\u0157\u0158\58\35\2\u0158\u0159\7\5\2\2\u0159")
        buf.write(u"/\3\2\2\2\u015a\u015b\b\31\1\2\u015b\u015c\7\31\2\2\u015c")
        buf.write(u"\u0176\5\60\31\17\u015d\u0176\5\20\t\2\u015e\u0176\5")
        buf.write(u"\66\34\2\u015f\u0160\7\31\2\2\u0160\u0176\58\35\2\u0161")
        buf.write(u"\u0162\7\31\2\2\u0162\u0163\58\35\2\u0163\u0164\7\f\2")
        buf.write(u"\2\u0164\u0176\3\2\2\2\u0165\u0176\5\36\20\2\u0166\u0176")
        buf.write(u"\5 \21\2\u0167\u0176\58\35\2\u0168\u0176\5B\"\2\u0169")
        buf.write(u"\u0176\5@!\2\u016a\u0176\5\34\17\2\u016b\u0176\7(\2\2")
        buf.write(u"\u016c\u0176\7\32\2\2\u016d\u0176\5&\24\2\u016e\u0176")
        buf.write(u"\5,\27\2\u016f\u0170\5<\37\2\u0170\u0171\5\60\31\2\u0171")
        buf.write(u"\u0172\5> \2\u0172\u0176\3\2\2\2\u0173\u0174\7\33\2\2")
        buf.write(u"\u0174\u0176\7(\2\2\u0175\u015a\3\2\2\2\u0175\u015d\3")
        buf.write(u"\2\2\2\u0175\u015e\3\2\2\2\u0175\u015f\3\2\2\2\u0175")
        buf.write(u"\u0161\3\2\2\2\u0175\u0165\3\2\2\2\u0175\u0166\3\2\2")
        buf.write(u"\2\u0175\u0167\3\2\2\2\u0175\u0168\3\2\2\2\u0175\u0169")
        buf.write(u"\3\2\2\2\u0175\u016a\3\2\2\2\u0175\u016b\3\2\2\2\u0175")
        buf.write(u"\u016c\3\2\2\2\u0175\u016d\3\2\2\2\u0175\u016e\3\2\2")
        buf.write(u"\2\u0175\u016f\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u0188")
        buf.write(u"\3\2\2\2\u0177\u0178\f\27\2\2\u0178\u0179\7\16\2\2\u0179")
        buf.write(u"\u0187\5\60\31\30\u017a\u017b\f\26\2\2\u017b\u017c\7")
        buf.write(u"/\2\2\u017c\u0187\5\60\31\27\u017d\u017e\f\25\2\2\u017e")
        buf.write(u"\u017f\t\4\2\2\u017f\u0187\5\60\31\26\u0180\u0181\f\24")
        buf.write(u"\2\2\u0181\u0182\t\5\2\2\u0182\u0187\5\60\31\25\u0183")
        buf.write(u"\u0184\f\23\2\2\u0184\u0185\7.\2\2\u0185\u0187\5\60\31")
        buf.write(u"\24\u0186\u0177\3\2\2\2\u0186\u017a\3\2\2\2\u0186\u017d")
        buf.write(u"\3\2\2\2\u0186\u0180\3\2\2\2\u0186\u0183\3\2\2\2\u0187")
        buf.write(u"\u018a\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2")
        buf.write(u"\2\u0189\61\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u0190\7")
        buf.write(u"\4\2\2\u018c\u018f\5\64\33\2\u018d\u018f\5\66\34\2\u018e")
        buf.write(u"\u018c\3\2\2\2\u018e\u018d\3\2\2\2\u018f\u0192\3\2\2")
        buf.write(u"\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0193")
        buf.write(u"\3\2\2\2\u0192\u0190\3\2\2\2\u0193\u0194\7\5\2\2\u0194")
        buf.write(u"\63\3\2\2\2\u0195\u0196\5\60\31\2\u0196\65\3\2\2\2\u0197")
        buf.write(u"\u019a\7\24\2\2\u0198\u019b\7(\2\2\u0199\u019b\5,\27")
        buf.write(u"\2\u019a\u0198\3\2\2\2\u019a\u0199\3\2\2\2\u019b\u019c")
        buf.write(u"\3\2\2\2\u019c\u019f\7\25\2\2\u019d\u01a0\7(\2\2\u019e")
        buf.write(u"\u01a0\5@!\2\u019f\u019d\3\2\2\2\u019f\u019e\3\2\2\2")
        buf.write(u"\u01a0\u01a1\3\2\2\2\u01a1\u01a2\7\32\2\2\u01a2\67\3")
        buf.write(u"\2\2\2\u01a3\u01a4\7\60\2\2\u01a49\3\2\2\2\u01a5\u01a7")
        buf.write(u"\5<\37\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8")
        buf.write(u"\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ab\3\2\2")
        buf.write(u"\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac\5\60\31\2\u01ac\u01ad")
        buf.write(u"\t\6\2\2\u01ad\u01b1\5\60\31\2\u01ae\u01b0\5> \2\u01af")
        buf.write(u"\u01ae\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2")
        buf.write(u"\2\u01b1\u01b2\3\2\2\2\u01b2\u01b8\3\2\2\2\u01b3\u01b1")
        buf.write(u"\3\2\2\2\u01b4\u01b5\t\7\2\2\u01b5\u01b7\5:\36\2\u01b6")
        buf.write(u"\u01b4\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2")
        buf.write(u"\2\u01b8\u01b9\3\2\2\2\u01b9;\3\2\2\2\u01ba\u01b8\3\2")
        buf.write(u"\2\2\u01bb\u01bc\7\26\2\2\u01bc=\3\2\2\2\u01bd\u01be")
        buf.write(u"\7\27\2\2\u01be?\3\2\2\2\u01bf\u01c0\7(\2\2\u01c0\u01c4")
        buf.write(u"\7\26\2\2\u01c1\u01c3\5<\37\2\u01c2\u01c1\3\2\2\2\u01c3")
        buf.write(u"\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2")
        buf.write(u"\2\u01c5\u01d1\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01cc")
        buf.write(u"\5\60\31\2\u01c8\u01c9\7\f\2\2\u01c9\u01cb\5\60\31\2")
        buf.write(u"\u01ca\u01c8\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca")
        buf.write(u"\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce")
        buf.write(u"\u01cc\3\2\2\2\u01cf\u01c7\3\2\2\2\u01d0\u01d3\3\2\2")
        buf.write(u"\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d7")
        buf.write(u"\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u01d6\5> \2\u01d5")
        buf.write(u"\u01d4\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2")
        buf.write(u"\2\u01d7\u01d8\3\2\2\2\u01d8\u01da\3\2\2\2\u01d9\u01d7")
        buf.write(u"\3\2\2\2\u01da\u01db\7\27\2\2\u01dbA\3\2\2\2\u01dc\u01dd")
        buf.write(u"\t\b\2\2\u01ddC\3\2\2\2\62GLXdkm{\u0083\u008e\u0091\u009d")
        buf.write(u"\u00a5\u00b1\u00b4\u00ba\u00bc\u00c8\u00d4\u00de\u00e8")
        buf.write(u"\u00fc\u0102\u0106\u010b\u0113\u0119\u011f\u0123\u0128")
        buf.write(u"\u0133\u0138\u014a\u0150\u0152\u0175\u0186\u0188\u018e")
        buf.write(u"\u0190\u019a\u019f\u01a8\u01b1\u01b8\u01c4\u01cc\u01d1")
        buf.write(u"\u01d7")
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

        def msgboardlist(self):
            return self.getTypedRuleContext(PrigogineParser.MsgboardlistContext,0)


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
            self.state = 77
            self.match(PrigogineParser.T__0)
            self.state = 78
            self.match(PrigogineParser.ID)
            self.state = 79
            self.match(PrigogineParser.T__1)

            self.state = 80 
            self.msgboardlist()
            self.state = 81 
            self.variablelist()
            self.state = 82 
            self.equationlist()
            self.state = 84 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 83 
                self.population()
                self.state = 86 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrigogineParser.T__13):
                    break

            self.state = 88
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
            self.state = 90
            self.match(PrigogineParser.T__3)
            self.state = 91
            self.match(PrigogineParser.T__1)
            self.state = 92 
            self.codeinsert()
            self.state = 93
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
            self.state = 98
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 95
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==PrigogineParser.T__4 or _la==PrigogineParser.T__5:
                        self._errHandler.recoverInline(self)
                    self.consume() 
                self.state = 100
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
            self.state = 101
            self.match(PrigogineParser.T__6)
            self.state = 102
            self.match(PrigogineParser.T__1)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 105
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 103 
                    self.elementwiseEquation()
                    pass

                elif la_ == 2:
                    self.state = 104 
                    self.mapEquation()
                    pass


                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
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
            self.state = 143
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.match(PrigogineParser.ID)
                self.state = 113
                self.match(PrigogineParser.T__7)
                self.state = 114
                self.match(PrigogineParser.T__8)
                self.state = 115 
                self.expression(0)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 116
                    self.match(PrigogineParser.T__9)
                    self.state = 117
                    self.match(PrigogineParser.T__10)
                    self.state = 118 
                    self.conditional()
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(PrigogineParser.ID)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__11:
                    self.state = 125
                    self.match(PrigogineParser.T__11)
                    self.state = 126
                    self.match(PrigogineParser.ID)
                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 132
                self.match(PrigogineParser.T__7)
                self.state = 133
                self.match(PrigogineParser.T__8)
                self.state = 134 
                self.expression(0)
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 135
                    self.match(PrigogineParser.T__9)
                    self.state = 136
                    self.match(PrigogineParser.T__10)
                    self.state = 137 
                    self.conditional()
                    self.state = 142
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
            self.state = 178
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(PrigogineParser.ID)
                self.state = 146
                self.match(PrigogineParser.T__7)
                self.state = 147
                self.match(PrigogineParser.T__12)
                self.state = 148
                self.match(PrigogineParser.T__8)
                self.state = 149 
                self.expression(0)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 150
                    self.match(PrigogineParser.T__9)
                    self.state = 151
                    self.match(PrigogineParser.T__10)
                    self.state = 152 
                    self.conditional()
                    self.state = 157
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(PrigogineParser.ID)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__11:
                    self.state = 159
                    self.match(PrigogineParser.T__11)
                    self.state = 160
                    self.match(PrigogineParser.ID)
                    self.state = 165
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 166
                self.match(PrigogineParser.T__7)
                self.state = 167
                self.match(PrigogineParser.T__12)
                self.state = 168
                self.match(PrigogineParser.T__8)
                self.state = 169 
                self.expression(0)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 170
                    self.match(PrigogineParser.T__9)
                    self.state = 171
                    self.match(PrigogineParser.T__10)
                    self.state = 172 
                    self.conditional()
                    self.state = 177
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
            self.state = 180
            self.match(PrigogineParser.ID)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__11) | (1 << PrigogineParser.T__12))) != 0):
                self.state = 184
                token = self._input.LA(1)
                if token in [PrigogineParser.T__11]:
                    self.state = 181
                    self.match(PrigogineParser.T__11)
                    self.state = 182
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.T__1, PrigogineParser.T__12]:
                    self.state = 183 
                    self.timeindex()

                else:
                    raise NoViableAltException(self)

                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 189
            self.match(PrigogineParser.T__8)
            self.state = 190 
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
            self.state = 192
            self.match(PrigogineParser.T__13)
            self.state = 193
            self.match(PrigogineParser.ID)
            self.state = 194
            self.match(PrigogineParser.T__1)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__14:
                self.state = 195 
                self.parameterlist()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201 
            self.variablelist()
            self.state = 202 
            self.equationlist()
            self.state = 203
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
            self.state = 205
            self.match(PrigogineParser.T__14)
            self.state = 206
            self.match(PrigogineParser.T__1)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 207 
                self.parameter()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 213
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
            self.state = 215
            self.match(PrigogineParser.T__15)
            self.state = 216
            self.match(PrigogineParser.T__1)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 217 
                self.variable()
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
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
            self.state = 225
            self.match(PrigogineParser.T__16)
            self.state = 226
            self.match(PrigogineParser.T__1)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 227 
                self.msgboarddef()
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 233
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
            self.state = 235
            self.match(PrigogineParser.ID)
            self.state = 236 
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
            self.state = 238
            self.match(PrigogineParser.T__1)
            self.state = 239 
            self.expression(0)
            self.state = 240
            self.match(PrigogineParser.T__17)
            self.state = 241
            self.match(PrigogineParser.ID)
            self.state = 242
            self.match(PrigogineParser.T__18)
            self.state = 243 
            self.expression(0)
            self.state = 244
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
            self.state = 273
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(PrigogineParser.T__1)
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                    self.state = 250
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 247
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 248 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 249 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 260
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==PrigogineParser.T__9:
                        self.state = 252
                        self.match(PrigogineParser.T__9)
                        self.state = 256
                        token = self._input.LA(1)
                        if token in [PrigogineParser.ID]:
                            self.state = 253
                            self.match(PrigogineParser.ID)

                        elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                            self.state = 254 
                            self.number()

                        elif token in [PrigogineParser.STRING]:
                            self.state = 255 
                            self.string()

                        else:
                            raise NoViableAltException(self)

                        self.state = 262
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 267
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 268
                self.match(PrigogineParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.match(PrigogineParser.T__1)
                self.state = 270 
                self.listdef()
                self.state = 271
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
            self.state = 275
            self.match(PrigogineParser.T__19)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 279
                token = self._input.LA(1)
                if token in [PrigogineParser.ID]:
                    self.state = 276
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                    self.state = 277 
                    self.number()

                elif token in [PrigogineParser.STRING]:
                    self.state = 278 
                    self.string()

                else:
                    raise NoViableAltException(self)

                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 281
                    self.match(PrigogineParser.T__9)
                    self.state = 285
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 282
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 283 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 284 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 291
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 297
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
            self.state = 299
            self.match(PrigogineParser.T__19)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.INT or _la==PrigogineParser.FLOAT:
                self.state = 300 
                self.number()
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 301
                    self.match(PrigogineParser.T__9)
                    self.state = 302 
                    self.number()
                    self.state = 307
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 313
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
            self.state = 315
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
            self.state = 317
            self.match(PrigogineParser.ID)
            self.state = 318 
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
            self.state = 320
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
            self.state = 334 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 334
                    token = self._input.LA(1)
                    if token in [PrigogineParser.T__1]:
                        self.state = 322
                        self.match(PrigogineParser.T__1)
                        self.state = 323 
                        self.timevar()
                        self.state = 328
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==PrigogineParser.SUB:
                            self.state = 324
                            self.match(PrigogineParser.SUB)
                            self.state = 325
                            self.match(PrigogineParser.INT)
                            self.state = 330
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 331
                        self.match(PrigogineParser.T__2)

                    elif token in [PrigogineParser.T__12]:
                        self.state = 333
                        self.match(PrigogineParser.T__12)

                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 336 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
            self.state = 338
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
            self.state = 340
            self.match(PrigogineParser.T__1)
            self.state = 341 
            self.string()
            self.state = 342
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
            self.state = 371
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 345
                self.match(PrigogineParser.T__22)
                self.state = 346 
                self.expression(13)
                pass

            elif la_ == 2:
                self.state = 347 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 348 
                self.pyforloop()
                pass

            elif la_ == 4:
                self.state = 349
                self.match(PrigogineParser.T__22)
                self.state = 350 
                self.string()
                pass

            elif la_ == 5:
                self.state = 351
                self.match(PrigogineParser.T__22)
                self.state = 352 
                self.string()
                self.state = 353
                self.match(PrigogineParser.T__9)
                pass

            elif la_ == 6:
                self.state = 355 
                self.listdef()
                pass

            elif la_ == 7:
                self.state = 356 
                self.tupledef()
                pass

            elif la_ == 8:
                self.state = 357 
                self.string()
                pass

            elif la_ == 9:
                self.state = 358 
                self.number()
                pass

            elif la_ == 10:
                self.state = 359 
                self.func()
                pass

            elif la_ == 11:
                self.state = 360 
                self.listcomp()
                pass

            elif la_ == 12:
                self.state = 361
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 13:
                self.state = 362
                self.match(PrigogineParser.T__23)
                pass

            elif la_ == 14:
                self.state = 363 
                self.indexedvariable()
                pass

            elif la_ == 15:
                self.state = 364 
                self.timevar()
                pass

            elif la_ == 16:
                self.state = 365 
                self.lparen()
                self.state = 366 
                self.expression(0)
                self.state = 367 
                self.rparen()
                pass

            elif la_ == 17:
                self.state = 369
                self.match(PrigogineParser.T__24)
                self.state = 370
                self.match(PrigogineParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 388
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 373
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 374
                        self.match(PrigogineParser.T__11)
                        self.state = 375 
                        self.expression(22)
                        pass

                    elif la_ == 2:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 376
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 377
                        self.match(PrigogineParser.POWER)
                        self.state = 378 
                        self.expression(21)
                        pass

                    elif la_ == 3:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 379
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 380
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.MUL or _la==PrigogineParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 381 
                        self.expression(20)
                        pass

                    elif la_ == 4:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 382
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 383
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 384 
                        self.expression(19)
                        pass

                    elif la_ == 5:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 385
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 386
                        localctx.op = self.match(PrigogineParser.PIPE)
                        self.state = 387 
                        self.expression(18)
                        pass

             
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
            self.state = 393
            self.match(PrigogineParser.T__1)
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__17) | (1 << PrigogineParser.T__19) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.T__22) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 396
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 394 
                    self.codeline()
                    pass

                elif la_ == 2:
                    self.state = 395 
                    self.pyforloop()
                    pass


                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 401
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
            self.state = 403 
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
            self.state = 405
            self.match(PrigogineParser.T__17)
            self.state = 408
            token = self._input.LA(1)
            if token in [PrigogineParser.ID]:
                self.state = 406
                self.match(PrigogineParser.ID)

            elif token in [PrigogineParser.T__21, PrigogineParser.INT]:
                self.state = 407 
                self.timevar()

            else:
                raise NoViableAltException(self)

            self.state = 410
            self.match(PrigogineParser.T__18)
            self.state = 413
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 411
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 2:
                self.state = 412 
                self.func()
                pass


            self.state = 415
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
            self.state = 417
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
            self.state = 422
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 419 
                    self.lparen() 
                self.state = 424
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

            self.state = 425 
            self.expression(0)
            self.state = 426
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__25) | (1 << PrigogineParser.T__26) | (1 << PrigogineParser.T__27) | (1 << PrigogineParser.T__28) | (1 << PrigogineParser.T__29) | (1 << PrigogineParser.T__30))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            self.consume()
            self.state = 427 
            self.expression(0)
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__20:
                self.state = 428 
                self.rparen()
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 438
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 434
                    _la = self._input.LA(1)
                    if not(_la==PrigogineParser.T__31 or _la==PrigogineParser.PIPE):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 435 
                    self.conditional() 
                self.state = 440
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
            self.state = 441
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
            self.state = 443
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
            self.state = 445
            self.match(PrigogineParser.ID)
            self.state = 446
            self.match(PrigogineParser.T__19)
            self.state = 450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 447 
                    self.lparen() 
                self.state = 452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

            self.state = 463
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__17) | (1 << PrigogineParser.T__19) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.T__22) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 453 
                self.expression(0)
                self.state = 458
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 454
                    self.match(PrigogineParser.T__9)
                    self.state = 455 
                    self.expression(0)
                    self.state = 460
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 465
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 469
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 466 
                    self.rparen() 
                self.state = 471
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

            self.state = 472
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
            self.state = 474
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
         



