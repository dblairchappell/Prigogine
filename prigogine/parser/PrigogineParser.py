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
        buf.write(u"\62\u0173\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3")
        buf.write(u"\2\3\2\3\2\3\2\6\2K\n\2\r\2\16\2L\3\2\7\2P\n\2\f\2\16")
        buf.write(u"\2S\13\2\3\3\3\3\3\3\3\3\3\3\3\3\7\3[\n\3\f\3\16\3^\13")
        buf.write(u"\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write(u"\6\3\7\3\7\3\7\3\7\7\7q\n\7\f\7\16\7t\13\7\3\b\3\b\7")
        buf.write(u"\bx\n\b\f\b\16\b{\13\b\3\b\3\b\3\t\3\t\6\t\u0081\n\t")
        buf.write(u"\r\t\16\t\u0082\3\n\3\n\3\n\7\n\u0088\n\n\f\n\16\n\u008b")
        buf.write(u"\13\n\3\13\3\13\7\13\u008f\n\13\f\13\16\13\u0092\13\13")
        buf.write(u"\3\f\3\f\3\f\7\f\u0097\n\f\f\f\16\f\u009a\13\f\3\f\3")
        buf.write(u"\f\3\r\3\r\3\r\7\r\u00a1\n\r\f\r\16\r\u00a4\13\r\3\r")
        buf.write(u"\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write(u"\3\17\3\17\5\17\u00b4\n\17\3\17\3\17\3\17\3\17\5\17\u00ba")
        buf.write(u"\n\17\7\17\u00bc\n\17\f\17\16\17\u00bf\13\17\7\17\u00c1")
        buf.write(u"\n\17\f\17\16\17\u00c4\13\17\3\17\3\17\3\20\3\20\3\20")
        buf.write(u"\3\20\5\20\u00cc\n\20\3\20\3\20\3\20\3\20\5\20\u00d2")
        buf.write(u"\n\20\7\20\u00d4\n\20\f\20\16\20\u00d7\13\20\7\20\u00d9")
        buf.write(u"\n\20\f\20\16\20\u00dc\13\20\3\20\3\20\3\21\3\21\3\22")
        buf.write(u"\3\22\3\23\3\23\3\23\3\23\7\23\u00e8\n\23\f\23\16\23")
        buf.write(u"\u00eb\13\23\3\23\3\23\5\23\u00ef\n\23\3\24\3\24\3\25")
        buf.write(u"\3\25\3\25\3\25\3\26\3\26\3\26\3\26\7\26\u00fb\n\26\f")
        buf.write(u"\26\16\26\u00fe\13\26\3\26\7\26\u0101\n\26\f\26\16\26")
        buf.write(u"\u0104\13\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\7\27")
        buf.write(u"\u010d\n\27\f\27\16\27\u0110\13\27\3\30\3\30\3\30\3\30")
        buf.write(u"\5\30\u0116\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write(u"\3\31\3\31\5\31\u012c\n\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\7\31")
        buf.write(u"\u013d\n\31\f\31\16\31\u0140\13\31\3\32\3\32\3\32\3\32")
        buf.write(u"\3\33\3\33\7\33\u0148\n\33\f\33\16\33\u014b\13\33\3\33")
        buf.write(u"\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3")
        buf.write(u"\37\3 \3 \3!\3!\3!\3!\3!\7!\u0160\n!\f!\16!\u0163\13")
        buf.write(u"!\7!\u0165\n!\f!\16!\u0168\13!\3!\3!\3\"\3\"\3\"\5\"")
        buf.write(u"\u016f\n\"\3#\3#\3#\2\3\60$\2\4\6\b\n\f\16\20\22\24\26")
        buf.write(u"\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BD\2\6\3\2,-\3")
        buf.write(u"\2*+\3\2\35\"\3\2&\'\u0186\2J\3\2\2\2\4T\3\2\2\2\6a\3")
        buf.write(u"\2\2\2\be\3\2\2\2\ni\3\2\2\2\fl\3\2\2\2\16u\3\2\2\2\20")
        buf.write(u"\u0080\3\2\2\2\22\u0084\3\2\2\2\24\u008c\3\2\2\2\26\u0093")
        buf.write(u"\3\2\2\2\30\u009d\3\2\2\2\32\u00a7\3\2\2\2\34\u00af\3")
        buf.write(u"\2\2\2\36\u00c7\3\2\2\2 \u00df\3\2\2\2\"\u00e1\3\2\2")
        buf.write(u"\2$\u00ee\3\2\2\2&\u00f0\3\2\2\2(\u00f2\3\2\2\2*\u00f6")
        buf.write(u"\3\2\2\2,\u0107\3\2\2\2.\u0111\3\2\2\2\60\u012b\3\2\2")
        buf.write(u"\2\62\u0141\3\2\2\2\64\u0145\3\2\2\2\66\u014e\3\2\2\2")
        buf.write(u"8\u0150\3\2\2\2:\u0152\3\2\2\2<\u0156\3\2\2\2>\u0158")
        buf.write(u"\3\2\2\2@\u015a\3\2\2\2B\u016e\3\2\2\2D\u0170\3\2\2\2")
        buf.write(u"FK\5\4\3\2GK\5\6\4\2HK\5\f\7\2IK\5\22\n\2JF\3\2\2\2J")
        buf.write(u"G\3\2\2\2JH\3\2\2\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3")
        buf.write(u"\2\2\2MQ\3\2\2\2NP\5\24\13\2ON\3\2\2\2PS\3\2\2\2QO\3")
        buf.write(u"\2\2\2QR\3\2\2\2R\3\3\2\2\2SQ\3\2\2\2TU\7\3\2\2UV\7(")
        buf.write(u"\2\2VW\7\4\2\2WX\5\26\f\2X\\\5\30\r\2Y[\5*\26\2ZY\3\2")
        buf.write(u"\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]_\3\2\2\2^\\\3\2")
        buf.write(u"\2\2_`\7\5\2\2`\5\3\2\2\2ab\7\6\2\2bc\7(\2\2cd\5\60\31")
        buf.write(u"\2d\7\3\2\2\2ef\7\7\2\2fg\7(\2\2gh\5\60\31\2h\t\3\2\2")
        buf.write(u"\2ij\7\b\2\2jk\5\60\31\2k\13\3\2\2\2lm\7\t\2\2mn\7(\2")
        buf.write(u"\2nr\7&\2\2oq\5\16\b\2po\3\2\2\2qt\3\2\2\2rp\3\2\2\2")
        buf.write(u"rs\3\2\2\2s\r\3\2\2\2tr\3\2\2\2uy\7\4\2\2vx\5\20\t\2")
        buf.write(u"wv\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z|\3\2\2\2{y")
        buf.write(u"\3\2\2\2|}\7\5\2\2}\17\3\2\2\2~\u0081\5\b\5\2\177\u0081")
        buf.write(u"\5\n\6\2\u0080~\3\2\2\2\u0080\177\3\2\2\2\u0081\u0082")
        buf.write(u"\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write(u"\21\3\2\2\2\u0084\u0085\7\n\2\2\u0085\u0089\7&\2\2\u0086")
        buf.write(u"\u0088\5\64\33\2\u0087\u0086\3\2\2\2\u0088\u008b\3\2")
        buf.write(u"\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\23")
        buf.write(u"\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u0090\7\13\2\2\u008d")
        buf.write(u"\u008f\5\64\33\2\u008e\u008d\3\2\2\2\u008f\u0092\3\2")
        buf.write(u"\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\25")
        buf.write(u"\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094\7\f\2\2\u0094")
        buf.write(u"\u0098\7\4\2\2\u0095\u0097\5\"\22\2\u0096\u0095\3\2\2")
        buf.write(u"\2\u0097\u009a\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099")
        buf.write(u"\3\2\2\2\u0099\u009b\3\2\2\2\u009a\u0098\3\2\2\2\u009b")
        buf.write(u"\u009c\7\5\2\2\u009c\27\3\2\2\2\u009d\u009e\7\r\2\2\u009e")
        buf.write(u"\u00a2\7\4\2\2\u009f\u00a1\5 \21\2\u00a0\u009f\3\2\2")
        buf.write(u"\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3")
        buf.write(u"\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5")
        buf.write(u"\u00a6\7\5\2\2\u00a6\31\3\2\2\2\u00a7\u00a8\7\4\2\2\u00a8")
        buf.write(u"\u00a9\5\60\31\2\u00a9\u00aa\7\16\2\2\u00aa\u00ab\7(")
        buf.write(u"\2\2\u00ab\u00ac\7\17\2\2\u00ac\u00ad\5\60\31\2\u00ad")
        buf.write(u"\u00ae\7\5\2\2\u00ae\33\3\2\2\2\u00af\u00c2\7\4\2\2\u00b0")
        buf.write(u"\u00b4\7(\2\2\u00b1\u00b4\5D#\2\u00b2\u00b4\58\35\2\u00b3")
        buf.write(u"\u00b0\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b2\3\2\2")
        buf.write(u"\2\u00b4\u00bd\3\2\2\2\u00b5\u00b9\7\20\2\2\u00b6\u00ba")
        buf.write(u"\7(\2\2\u00b7\u00ba\5D#\2\u00b8\u00ba\58\35\2\u00b9\u00b6")
        buf.write(u"\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba")
        buf.write(u"\u00bc\3\2\2\2\u00bb\u00b5\3\2\2\2\u00bc\u00bf\3\2\2")
        buf.write(u"\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c1")
        buf.write(u"\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00b3\3\2\2\2\u00c1")
        buf.write(u"\u00c4\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2")
        buf.write(u"\2\u00c3\u00c5\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c5\u00c6")
        buf.write(u"\7\5\2\2\u00c6\35\3\2\2\2\u00c7\u00da\7\21\2\2\u00c8")
        buf.write(u"\u00cc\7(\2\2\u00c9\u00cc\5D#\2\u00ca\u00cc\58\35\2\u00cb")
        buf.write(u"\u00c8\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca\3\2\2")
        buf.write(u"\2\u00cc\u00d5\3\2\2\2\u00cd\u00d1\7\20\2\2\u00ce\u00d2")
        buf.write(u"\7(\2\2\u00cf\u00d2\5D#\2\u00d0\u00d2\58\35\2\u00d1\u00ce")
        buf.write(u"\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2")
        buf.write(u"\u00d4\3\2\2\2\u00d3\u00cd\3\2\2\2\u00d4\u00d7\3\2\2")
        buf.write(u"\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d9")
        buf.write(u"\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00cb\3\2\2\2\u00d9")
        buf.write(u"\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2")
        buf.write(u"\2\u00db\u00dd\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00de")
        buf.write(u"\7\22\2\2\u00de\37\3\2\2\2\u00df\u00e0\7(\2\2\u00e0!")
        buf.write(u"\3\2\2\2\u00e1\u00e2\7(\2\2\u00e2#\3\2\2\2\u00e3\u00e4")
        buf.write(u"\7\4\2\2\u00e4\u00e9\7\23\2\2\u00e5\u00e6\t\2\2\2\u00e6")
        buf.write(u"\u00e8\7&\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00eb\3\2\2\2")
        buf.write(u"\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00ec")
        buf.write(u"\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00ef\7\5\2\2\u00ed")
        buf.write(u"\u00ef\7\24\2\2\u00ee\u00e3\3\2\2\2\u00ee\u00ed\3\2\2")
        buf.write(u"\2\u00ef%\3\2\2\2\u00f0\u00f1\7\23\2\2\u00f1\'\3\2\2")
        buf.write(u"\2\u00f2\u00f3\7\4\2\2\u00f3\u00f4\58\35\2\u00f4\u00f5")
        buf.write(u"\7\5\2\2\u00f5)\3\2\2\2\u00f6\u00f7\7\25\2\2\u00f7\u00f8")
        buf.write(u"\7(\2\2\u00f8\u00fc\7\4\2\2\u00f9\u00fb\5,\27\2\u00fa")
        buf.write(u"\u00f9\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2")
        buf.write(u"\2\u00fc\u00fd\3\2\2\2\u00fd\u0102\3\2\2\2\u00fe\u00fc")
        buf.write(u"\3\2\2\2\u00ff\u0101\5.\30\2\u0100\u00ff\3\2\2\2\u0101")
        buf.write(u"\u0104\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2")
        buf.write(u"\2\u0103\u0105\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u0106")
        buf.write(u"\7\5\2\2\u0106+\3\2\2\2\u0107\u0108\7\26\2\2\u0108\u0109")
        buf.write(u"\7(\2\2\u0109\u010a\7\27\2\2\u010a\u010e\5:\36\2\u010b")
        buf.write(u"\u010d\5\64\33\2\u010c\u010b\3\2\2\2\u010d\u0110\3\2")
        buf.write(u"\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f-\3")
        buf.write(u"\2\2\2\u0110\u010e\3\2\2\2\u0111\u0112\7\30\2\2\u0112")
        buf.write(u"\u0115\7(\2\2\u0113\u0116\5\66\34\2\u0114\u0116\5\64")
        buf.write(u"\33\2\u0115\u0113\3\2\2\2\u0115\u0114\3\2\2\2\u0116/")
        buf.write(u"\3\2\2\2\u0117\u0118\b\31\1\2\u0118\u0119\7\32\2\2\u0119")
        buf.write(u"\u012c\5\60\31\r\u011a\u012c\5\62\32\2\u011b\u011c\7")
        buf.write(u"\32\2\2\u011c\u012c\58\35\2\u011d\u012c\5\34\17\2\u011e")
        buf.write(u"\u012c\5\36\20\2\u011f\u012c\58\35\2\u0120\u012c\5D#")
        buf.write(u"\2\u0121\u012c\5@!\2\u0122\u012c\5\32\16\2\u0123\u012c")
        buf.write(u"\7(\2\2\u0124\u012c\5&\24\2\u0125\u0126\5<\37\2\u0126")
        buf.write(u"\u0127\5\60\31\2\u0127\u0128\5> \2\u0128\u012c\3\2\2")
        buf.write(u"\2\u0129\u012a\7\33\2\2\u012a\u012c\7(\2\2\u012b\u0117")
        buf.write(u"\3\2\2\2\u012b\u011a\3\2\2\2\u012b\u011b\3\2\2\2\u012b")
        buf.write(u"\u011d\3\2\2\2\u012b\u011e\3\2\2\2\u012b\u011f\3\2\2")
        buf.write(u"\2\u012b\u0120\3\2\2\2\u012b\u0121\3\2\2\2\u012b\u0122")
        buf.write(u"\3\2\2\2\u012b\u0123\3\2\2\2\u012b\u0124\3\2\2\2\u012b")
        buf.write(u"\u0125\3\2\2\2\u012b\u0129\3\2\2\2\u012c\u013e\3\2\2")
        buf.write(u"\2\u012d\u012e\f\23\2\2\u012e\u012f\7\31\2\2\u012f\u013d")
        buf.write(u"\5\60\31\24\u0130\u0131\f\22\2\2\u0131\u0132\7/\2\2\u0132")
        buf.write(u"\u013d\5\60\31\23\u0133\u0134\f\21\2\2\u0134\u0135\t")
        buf.write(u"\3\2\2\u0135\u013d\5\60\31\22\u0136\u0137\f\20\2\2\u0137")
        buf.write(u"\u0138\t\2\2\2\u0138\u013d\5\60\31\21\u0139\u013a\f\17")
        buf.write(u"\2\2\u013a\u013b\7.\2\2\u013b\u013d\5\60\31\20\u013c")
        buf.write(u"\u012d\3\2\2\2\u013c\u0130\3\2\2\2\u013c\u0133\3\2\2")
        buf.write(u"\2\u013c\u0136\3\2\2\2\u013c\u0139\3\2\2\2\u013d\u0140")
        buf.write(u"\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f")
        buf.write(u"\61\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0142\7(\2\2\u0142")
        buf.write(u"\u0143\7\34\2\2\u0143\u0144\5\60\31\2\u0144\63\3\2\2")
        buf.write(u"\2\u0145\u0149\7\4\2\2\u0146\u0148\5\66\34\2\u0147\u0146")
        buf.write(u"\3\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2\u0149")
        buf.write(u"\u014a\3\2\2\2\u014a\u014c\3\2\2\2\u014b\u0149\3\2\2")
        buf.write(u"\2\u014c\u014d\7\5\2\2\u014d\65\3\2\2\2\u014e\u014f\5")
        buf.write(u"\60\31\2\u014f\67\3\2\2\2\u0150\u0151\7\60\2\2\u0151")
        buf.write(u"9\3\2\2\2\u0152\u0153\5\60\31\2\u0153\u0154\t\4\2\2\u0154")
        buf.write(u"\u0155\5\60\31\2\u0155;\3\2\2\2\u0156\u0157\7\21\2\2")
        buf.write(u"\u0157=\3\2\2\2\u0158\u0159\7\22\2\2\u0159?\3\2\2\2\u015a")
        buf.write(u"\u015b\7(\2\2\u015b\u0166\7\21\2\2\u015c\u0161\5\60\31")
        buf.write(u"\2\u015d\u015e\7\20\2\2\u015e\u0160\5\60\31\2\u015f\u015d")
        buf.write(u"\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2\u0161")
        buf.write(u"\u0162\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2")
        buf.write(u"\2\u0164\u015c\3\2\2\2\u0165\u0168\3\2\2\2\u0166\u0164")
        buf.write(u"\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0169\3\2\2\2\u0168")
        buf.write(u"\u0166\3\2\2\2\u0169\u016a\7\22\2\2\u016aA\3\2\2\2\u016b")
        buf.write(u"\u016f\5D#\2\u016c\u016f\7(\2\2\u016d\u016f\5@!\2\u016e")
        buf.write(u"\u016b\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016d\3\2\2")
        buf.write(u"\2\u016fC\3\2\2\2\u0170\u0171\t\5\2\2\u0171E\3\2\2\2")
        buf.write(u"#JLQ\\ry\u0080\u0082\u0089\u0090\u0098\u00a2\u00b3\u00b9")
        buf.write(u"\u00bd\u00c2\u00cb\u00d1\u00d5\u00da\u00e9\u00ee\u00fc")
        buf.write(u"\u0102\u010e\u0115\u012b\u013c\u013e\u0149\u0161\u0166")
        buf.write(u"\u016e")
        return buf.getvalue()
		

class PrigogineParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'population'", u"'['", u"']'", u"'initglobal'", 
                     u"'initvars'", u"'initstates'", u"'create'", u"'runmodel'", 
                     u"'finalise'", u"'parameters'", u"'variables'", u"'for'", 
                     u"'in'", u"','", u"'('", u"')'", u"'t'", u"'[:]'", 
                     u"'state'", u"'transition'", u"'where'", u"'update'", 
                     u"'.'", u"'print'", u"'return'", u"'='", u"'<'", u"'>'", 
                     u"'>='", u"'<='", u"'=='", u"'!='", u"<INVALID>", u"<INVALID>", 
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
    RULE_population = 1
    RULE_initglobal = 2
    RULE_initvars = 3
    RULE_initstates = 4
    RULE_create = 5
    RULE_createblock = 6
    RULE_createline = 7
    RULE_runmodel = 8
    RULE_finalise = 9
    RULE_parameterlist = 10
    RULE_variablelist = 11
    RULE_listcomp = 12
    RULE_listdef = 13
    RULE_tupledef = 14
    RULE_variable = 15
    RULE_parameter = 16
    RULE_timeindex = 17
    RULE_timevar = 18
    RULE_dictindex = 19
    RULE_statedef = 20
    RULE_transition = 21
    RULE_update = 22
    RULE_expression = 23
    RULE_assignment = 24
    RULE_codeblock = 25
    RULE_codeline = 26
    RULE_string = 27
    RULE_conditional = 28
    RULE_lparen = 29
    RULE_rparen = 30
    RULE_func = 31
    RULE_argument = 32
    RULE_number = 33

    ruleNames =  [ u"filestart", u"population", u"initglobal", u"initvars", 
                   u"initstates", u"create", u"createblock", u"createline", 
                   u"runmodel", u"finalise", u"parameterlist", u"variablelist", 
                   u"listcomp", u"listdef", u"tupledef", u"variable", u"parameter", 
                   u"timeindex", u"timevar", u"dictindex", u"statedef", 
                   u"transition", u"update", u"expression", u"assignment", 
                   u"codeblock", u"codeline", u"string", u"conditional", 
                   u"lparen", u"rparen", u"func", u"argument", u"number" ]

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

        def population(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.PopulationContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.PopulationContext,i)


        def initglobal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.InitglobalContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.InitglobalContext,i)


        def create(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.CreateContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.CreateContext,i)


        def runmodel(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.RunmodelContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.RunmodelContext,i)


        def finalise(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.FinaliseContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.FinaliseContext,i)


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
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                token = self._input.LA(1)
                if token in [PrigogineParser.T__0]:
                    self.state = 68 
                    self.population()

                elif token in [PrigogineParser.T__3]:
                    self.state = 69 
                    self.initglobal()

                elif token in [PrigogineParser.T__6]:
                    self.state = 70 
                    self.create()

                elif token in [PrigogineParser.T__7]:
                    self.state = 71 
                    self.runmodel()

                else:
                    raise NoViableAltException(self)

                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__0) | (1 << PrigogineParser.T__3) | (1 << PrigogineParser.T__6) | (1 << PrigogineParser.T__7))) != 0)):
                    break

            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__8:
                self.state = 76 
                self.finalise()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def parameterlist(self):
            return self.getTypedRuleContext(PrigogineParser.ParameterlistContext,0)


        def variablelist(self):
            return self.getTypedRuleContext(PrigogineParser.VariablelistContext,0)


        def statedef(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.StatedefContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.StatedefContext,i)


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
        self.enterRule(localctx, 2, self.RULE_population)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(PrigogineParser.T__0)
            self.state = 83
            self.match(PrigogineParser.ID)
            self.state = 84
            self.match(PrigogineParser.T__1)
            self.state = 85 
            self.parameterlist()
            self.state = 86 
            self.variablelist()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__18:
                self.state = 87 
                self.statedef()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitglobalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.InitglobalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(PrigogineParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_initglobal

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterInitglobal(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitInitglobal(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitInitglobal(self)
            else:
                return visitor.visitChildren(self)




    def initglobal(self):

        localctx = PrigogineParser.InitglobalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_initglobal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(PrigogineParser.T__3)
            self.state = 96
            self.match(PrigogineParser.ID)
            self.state = 97 
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitvarsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.InitvarsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(PrigogineParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_initvars

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterInitvars(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitInitvars(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitInitvars(self)
            else:
                return visitor.visitChildren(self)




    def initvars(self):

        localctx = PrigogineParser.InitvarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_initvars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(PrigogineParser.T__4)
            self.state = 100
            self.match(PrigogineParser.ID)
            self.state = 101 
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitstatesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.InitstatesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PrigogineParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_initstates

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterInitstates(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitInitstates(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitInitstates(self)
            else:
                return visitor.visitChildren(self)




    def initstates(self):

        localctx = PrigogineParser.InitstatesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_initstates)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(PrigogineParser.T__5)
            self.state = 104 
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CreateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.CreateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def INT(self):
            return self.getToken(PrigogineParser.INT, 0)

        def createblock(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.CreateblockContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.CreateblockContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_create

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterCreate(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitCreate(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitCreate(self)
            else:
                return visitor.visitChildren(self)




    def create(self):

        localctx = PrigogineParser.CreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(PrigogineParser.T__6)
            self.state = 107
            self.match(PrigogineParser.ID)
            self.state = 108
            self.match(PrigogineParser.INT)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__1:
                self.state = 109 
                self.createblock()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CreateblockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.CreateblockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def createline(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.CreatelineContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.CreatelineContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_createblock

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterCreateblock(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitCreateblock(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitCreateblock(self)
            else:
                return visitor.visitChildren(self)




    def createblock(self):

        localctx = PrigogineParser.CreateblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_createblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(PrigogineParser.T__1)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__4 or _la==PrigogineParser.T__5:
                self.state = 116 
                self.createline()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CreatelineContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.CreatelineContext, self).__init__(parent, invokingState)
            self.parser = parser

        def initvars(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.InitvarsContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.InitvarsContext,i)


        def initstates(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.InitstatesContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.InitstatesContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_createline

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterCreateline(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitCreateline(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitCreateline(self)
            else:
                return visitor.visitChildren(self)




    def createline(self):

        localctx = PrigogineParser.CreatelineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_createline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 126
                    token = self._input.LA(1)
                    if token in [PrigogineParser.T__4]:
                        self.state = 124 
                        self.initvars()

                    elif token in [PrigogineParser.T__5]:
                        self.state = 125 
                        self.initstates()

                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 128 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RunmodelContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.RunmodelContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PrigogineParser.INT, 0)

        def codeblock(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.CodeblockContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.CodeblockContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_runmodel

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterRunmodel(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitRunmodel(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitRunmodel(self)
            else:
                return visitor.visitChildren(self)




    def runmodel(self):

        localctx = PrigogineParser.RunmodelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_runmodel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(PrigogineParser.T__7)
            self.state = 131
            self.match(PrigogineParser.INT)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__1:
                self.state = 132 
                self.codeblock()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FinaliseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.FinaliseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def codeblock(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.CodeblockContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.CodeblockContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_finalise

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterFinalise(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitFinalise(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitFinalise(self)
            else:
                return visitor.visitChildren(self)




    def finalise(self):

        localctx = PrigogineParser.FinaliseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_finalise)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(PrigogineParser.T__8)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__1:
                self.state = 139 
                self.codeblock()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 20, self.RULE_parameterlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(PrigogineParser.T__9)
            self.state = 146
            self.match(PrigogineParser.T__1)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 147 
                self.parameter()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
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
        self.enterRule(localctx, 22, self.RULE_variablelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(PrigogineParser.T__10)
            self.state = 156
            self.match(PrigogineParser.T__1)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 157 
                self.variable()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 163
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
        self.enterRule(localctx, 24, self.RULE_listcomp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(PrigogineParser.T__1)
            self.state = 166 
            self.expression(0)
            self.state = 167
            self.match(PrigogineParser.T__11)
            self.state = 168
            self.match(PrigogineParser.ID)
            self.state = 169
            self.match(PrigogineParser.T__12)
            self.state = 170 
            self.expression(0)
            self.state = 171
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
        self.enterRule(localctx, 26, self.RULE_listdef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(PrigogineParser.T__1)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 177
                token = self._input.LA(1)
                if token in [PrigogineParser.ID]:
                    self.state = 174
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                    self.state = 175 
                    self.number()

                elif token in [PrigogineParser.STRING]:
                    self.state = 176 
                    self.string()

                else:
                    raise NoViableAltException(self)

                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__13:
                    self.state = 179
                    self.match(PrigogineParser.T__13)
                    self.state = 183
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 180
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 181 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 182 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 189
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 195
            self.match(PrigogineParser.T__2)
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
        self.enterRule(localctx, 28, self.RULE_tupledef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(PrigogineParser.T__14)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 201
                token = self._input.LA(1)
                if token in [PrigogineParser.ID]:
                    self.state = 198
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                    self.state = 199 
                    self.number()

                elif token in [PrigogineParser.STRING]:
                    self.state = 200 
                    self.string()

                else:
                    raise NoViableAltException(self)

                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__13:
                    self.state = 203
                    self.match(PrigogineParser.T__13)
                    self.state = 207
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 204
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 205 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 206 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 213
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 219
            self.match(PrigogineParser.T__15)
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
        self.enterRule(localctx, 30, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(PrigogineParser.ID)
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
            self.state = 223
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
            self.state = 236
            token = self._input.LA(1)
            if token in [PrigogineParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(PrigogineParser.T__1)
                self.state = 226
                self.match(PrigogineParser.T__16)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.ADD or _la==PrigogineParser.SUB:
                    self.state = 227
                    _la = self._input.LA(1)
                    if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 228
                    self.match(PrigogineParser.INT)
                    self.state = 233
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 234
                self.match(PrigogineParser.T__2)

            elif token in [PrigogineParser.T__17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(PrigogineParser.T__17)

            else:
                raise NoViableAltException(self)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(PrigogineParser.T__16)
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
            self.state = 240
            self.match(PrigogineParser.T__1)
            self.state = 241 
            self.string()
            self.state = 242
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatedefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.StatedefContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def transition(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.TransitionContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.TransitionContext,i)


        def update(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.UpdateContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.UpdateContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_statedef

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterStatedef(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitStatedef(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitStatedef(self)
            else:
                return visitor.visitChildren(self)




    def statedef(self):

        localctx = PrigogineParser.StatedefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_statedef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(PrigogineParser.T__18)
            self.state = 245
            self.match(PrigogineParser.ID)
            self.state = 246
            self.match(PrigogineParser.T__1)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__19:
                self.state = 247 
                self.transition()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__21:
                self.state = 253 
                self.update()
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 259
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TransitionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.TransitionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def conditional(self):
            return self.getTypedRuleContext(PrigogineParser.ConditionalContext,0)


        def codeblock(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.CodeblockContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.CodeblockContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_transition

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterTransition(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitTransition(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitTransition(self)
            else:
                return visitor.visitChildren(self)




    def transition(self):

        localctx = PrigogineParser.TransitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_transition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(PrigogineParser.T__19)
            self.state = 262
            self.match(PrigogineParser.ID)
            self.state = 263
            self.match(PrigogineParser.T__20)
            self.state = 264 
            self.conditional()
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__1:
                self.state = 265 
                self.codeblock()
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UpdateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.UpdateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def codeline(self):
            return self.getTypedRuleContext(PrigogineParser.CodelineContext,0)


        def codeblock(self):
            return self.getTypedRuleContext(PrigogineParser.CodeblockContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_update

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterUpdate(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitUpdate(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = PrigogineParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(PrigogineParser.T__21)
            self.state = 272
            self.match(PrigogineParser.ID)
            self.state = 275
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 273 
                self.codeline()
                pass

            elif la_ == 2:
                self.state = 274 
                self.codeblock()
                pass


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
            self.state = 297
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 278
                self.match(PrigogineParser.T__23)
                self.state = 279 
                self.expression(11)
                pass

            elif la_ == 2:
                self.state = 280 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 281
                self.match(PrigogineParser.T__23)
                self.state = 282 
                self.string()
                pass

            elif la_ == 4:
                self.state = 283 
                self.listdef()
                pass

            elif la_ == 5:
                self.state = 284 
                self.tupledef()
                pass

            elif la_ == 6:
                self.state = 285 
                self.string()
                pass

            elif la_ == 7:
                self.state = 286 
                self.number()
                pass

            elif la_ == 8:
                self.state = 287 
                self.func()
                pass

            elif la_ == 9:
                self.state = 288 
                self.listcomp()
                pass

            elif la_ == 10:
                self.state = 289
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 11:
                self.state = 290 
                self.timevar()
                pass

            elif la_ == 12:
                self.state = 291 
                self.lparen()
                self.state = 292 
                self.expression(0)
                self.state = 293 
                self.rparen()
                pass

            elif la_ == 13:
                self.state = 295
                self.match(PrigogineParser.T__24)
                self.state = 296
                self.match(PrigogineParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 316
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 314
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 299
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 300
                        self.match(PrigogineParser.T__22)
                        self.state = 301 
                        self.expression(18)
                        pass

                    elif la_ == 2:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 302
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 303
                        self.match(PrigogineParser.POWER)
                        self.state = 304 
                        self.expression(17)
                        pass

                    elif la_ == 3:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 305
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 306
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.MUL or _la==PrigogineParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 307 
                        self.expression(16)
                        pass

                    elif la_ == 4:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 308
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 309
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 310 
                        self.expression(15)
                        pass

                    elif la_ == 5:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 311
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 312
                        localctx.op = self.match(PrigogineParser.PIPE)
                        self.state = 313 
                        self.expression(14)
                        pass

             
                self.state = 318
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.AssignmentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(PrigogineParser.ExpressionContext,0)


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
        self.enterRule(localctx, 48, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(PrigogineParser.ID)
            self.state = 320
            self.match(PrigogineParser.T__25)
            self.state = 321 
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 50, self.RULE_codeblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(PrigogineParser.T__1)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__14) | (1 << PrigogineParser.T__16) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 324 
                self.codeline()
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 330
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
        self.enterRule(localctx, 52, self.RULE_codeline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332 
            self.expression(0)
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
            self.state = 334
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
            self.state = 336 
            self.expression(0)
            self.state = 337
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__26) | (1 << PrigogineParser.T__27) | (1 << PrigogineParser.T__28) | (1 << PrigogineParser.T__29) | (1 << PrigogineParser.T__30) | (1 << PrigogineParser.T__31))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            self.consume()
            self.state = 338 
            self.expression(0)
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
            self.state = 340
            self.match(PrigogineParser.T__14)
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
            self.state = 342
            self.match(PrigogineParser.T__15)
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

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ExpressionContext,i)


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
            self.state = 344
            self.match(PrigogineParser.ID)
            self.state = 345
            self.match(PrigogineParser.T__14)
            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__14) | (1 << PrigogineParser.T__16) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 346 
                self.expression(0)
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__13:
                    self.state = 347
                    self.match(PrigogineParser.T__13)
                    self.state = 348 
                    self.expression(0)
                    self.state = 353
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 359
            self.match(PrigogineParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.ArgumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(PrigogineParser.NumberContext,0)


        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def func(self):
            return self.getTypedRuleContext(PrigogineParser.FuncContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_argument

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitArgument(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = PrigogineParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_argument)
        try:
            self.state = 364
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361 
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 363 
                self.func()
                pass


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
        self.enterRule(localctx, 66, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
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
                return self.precpred(self._ctx, 17)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 13)
         



