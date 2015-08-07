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
        buf.write(u"\63\u020b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3")
        buf.write(u"\2\6\2H\n\2\r\2\16\2I\3\2\7\2M\n\2\f\2\16\2P\13\2\3\3")
        buf.write(u"\3\3\3\3\3\3\7\3V\n\3\f\3\16\3Y\13\3\3\3\3\3\3\3\6\3")
        buf.write(u"^\n\3\r\3\16\3_\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\7\5j")
        buf.write(u"\n\5\f\5\16\5m\13\5\3\6\3\6\3\6\3\6\3\6\7\6t\n\6\f\6")
        buf.write(u"\16\6w\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u0082")
        buf.write(u"\n\7\f\7\16\7\u0085\13\7\3\7\3\7\3\7\7\7\u008a\n\7\f")
        buf.write(u"\7\16\7\u008d\13\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u0095")
        buf.write(u"\n\7\f\7\16\7\u0098\13\7\5\7\u009a\n\7\3\b\3\b\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\7\b\u00a4\n\b\f\b\16\b\u00a7\13\b")
        buf.write(u"\3\b\3\b\3\b\7\b\u00ac\n\b\f\b\16\b\u00af\13\b\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\7\b\u00b8\n\b\f\b\16\b\u00bb\13")
        buf.write(u"\b\5\b\u00bd\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t")
        buf.write(u"\u00c7\n\t\f\t\16\t\u00ca\13\t\3\t\3\t\3\t\7\t\u00cf")
        buf.write(u"\n\t\f\t\16\t\u00d2\13\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write(u"\7\t\u00db\n\t\f\t\16\t\u00de\13\t\5\t\u00e0\n\t\3\n")
        buf.write(u"\3\n\3\n\3\n\7\n\u00e6\n\n\f\n\16\n\u00e9\13\n\3\n\3")
        buf.write(u"\n\3\n\3\13\3\13\3\13\3\13\7\13\u00f2\n\13\f\13\16\13")
        buf.write(u"\u00f5\13\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\7\f\u00fe")
        buf.write(u"\n\f\f\f\16\f\u0101\13\f\3\f\3\f\3\r\3\r\3\r\7\r\u0108")
        buf.write(u"\n\r\f\r\16\r\u010b\13\r\3\r\3\r\3\16\3\16\3\16\7\16")
        buf.write(u"\u0112\n\16\f\16\16\16\u0115\13\16\3\16\3\16\3\17\3\17")
        buf.write(u"\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3")
        buf.write(u"\21\3\21\3\21\5\21\u0128\n\21\3\21\3\21\3\21\3\21\5\21")
        buf.write(u"\u012e\n\21\7\21\u0130\n\21\f\21\16\21\u0133\13\21\7")
        buf.write(u"\21\u0135\n\21\f\21\16\21\u0138\13\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\5\21\u013f\n\21\3\22\3\22\3\22\3\22\5\22\u0145")
        buf.write(u"\n\22\3\22\3\22\3\22\3\22\5\22\u014b\n\22\7\22\u014d")
        buf.write(u"\n\22\f\22\16\22\u0150\13\22\7\22\u0152\n\22\f\22\16")
        buf.write(u"\22\u0155\13\22\3\22\3\22\3\23\3\23\3\23\3\23\7\23\u015d")
        buf.write(u"\n\23\f\23\16\23\u0160\13\23\7\23\u0162\n\23\f\23\16")
        buf.write(u"\23\u0165\13\23\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3")
        buf.write(u"\26\3\26\3\27\3\27\3\27\3\27\7\27\u0174\n\27\f\27\16")
        buf.write(u"\27\u0177\13\27\3\27\3\27\3\27\3\27\6\27\u017d\n\27\r")
        buf.write(u"\27\16\27\u017e\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3")
        buf.write(u"\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write(u"\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write(u"\32\3\32\3\32\3\32\3\32\5\32\u01a2\n\32\3\32\3\32\3\32")
        buf.write(u"\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write(u"\32\3\32\7\32\u01b3\n\32\f\32\16\32\u01b6\13\32\3\33")
        buf.write(u"\3\33\3\33\7\33\u01bb\n\33\f\33\16\33\u01be\13\33\3\33")
        buf.write(u"\3\33\3\34\3\34\3\35\3\35\3\35\5\35\u01c7\n\35\3\35\3")
        buf.write(u"\35\3\35\5\35\u01cc\n\35\3\35\3\35\3\36\3\36\3\37\7\37")
        buf.write(u"\u01d3\n\37\f\37\16\37\u01d6\13\37\3\37\3\37\3\37\3\37")
        buf.write(u"\7\37\u01dc\n\37\f\37\16\37\u01df\13\37\3\37\3\37\7\37")
        buf.write(u"\u01e3\n\37\f\37\16\37\u01e6\13\37\3 \3 \3!\3!\3\"\3")
        buf.write(u"\"\3\"\7\"\u01ef\n\"\f\"\16\"\u01f2\13\"\3\"\3\"\3\"")
        buf.write(u"\7\"\u01f7\n\"\f\"\16\"\u01fa\13\"\7\"\u01fc\n\"\f\"")
        buf.write(u"\16\"\u01ff\13\"\3\"\7\"\u0202\n\"\f\"\16\"\u0205\13")
        buf.write(u"\"\3\"\3\"\3#\3#\3#\3k\3\62$\2\4\6\b\n\f\16\20\22\24")
        buf.write(u"\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BD\2\t\3\2\7")
        buf.write(u"\b\4\2\31\31\'\'\3\2+,\3\2-.\3\2\35\"\4\2##//\3\2\'(")
        buf.write(u"\u0235\2G\3\2\2\2\4Q\3\2\2\2\6c\3\2\2\2\bk\3\2\2\2\n")
        buf.write(u"n\3\2\2\2\f\u0099\3\2\2\2\16\u00bc\3\2\2\2\20\u00df\3")
        buf.write(u"\2\2\2\22\u00e1\3\2\2\2\24\u00ed\3\2\2\2\26\u00fa\3\2")
        buf.write(u"\2\2\30\u0104\3\2\2\2\32\u010e\3\2\2\2\34\u0118\3\2\2")
        buf.write(u"\2\36\u011b\3\2\2\2 \u013e\3\2\2\2\"\u0140\3\2\2\2$\u0158")
        buf.write(u"\3\2\2\2&\u0168\3\2\2\2(\u016a\3\2\2\2*\u016d\3\2\2\2")
        buf.write(u",\u017c\3\2\2\2.\u0180\3\2\2\2\60\u0182\3\2\2\2\62\u01a1")
        buf.write(u"\3\2\2\2\64\u01b7\3\2\2\2\66\u01c1\3\2\2\28\u01c3\3\2")
        buf.write(u"\2\2:\u01cf\3\2\2\2<\u01d4\3\2\2\2>\u01e7\3\2\2\2@\u01e9")
        buf.write(u"\3\2\2\2B\u01eb\3\2\2\2D\u0208\3\2\2\2FH\5\4\3\2GF\3")
        buf.write(u"\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JN\3\2\2\2KM\5\6")
        buf.write(u"\4\2LK\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\3\3\2\2")
        buf.write(u"\2PN\3\2\2\2QR\7\3\2\2RS\7)\2\2SW\7\4\2\2TV\5\32\16\2")
        buf.write(u"UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2YW")
        buf.write(u"\3\2\2\2Z[\5\30\r\2[]\5\n\6\2\\^\5\24\13\2]\\\3\2\2\2")
        buf.write(u"^_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\7\5\2\2b\5")
        buf.write(u"\3\2\2\2cd\7\6\2\2de\7\4\2\2ef\5\b\5\2fg\7\5\2\2g\7\3")
        buf.write(u"\2\2\2hj\n\2\2\2ih\3\2\2\2jm\3\2\2\2kl\3\2\2\2ki\3\2")
        buf.write(u"\2\2l\t\3\2\2\2mk\3\2\2\2no\7\t\2\2ou\7\4\2\2pt\5\f\7")
        buf.write(u"\2qt\5\16\b\2rt\5\20\t\2sp\3\2\2\2sq\3\2\2\2sr\3\2\2")
        buf.write(u"\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2vx\3\2\2\2wu\3\2\2\2")
        buf.write(u"xy\7\5\2\2y\13\3\2\2\2z{\7)\2\2{|\7\n\2\2|}\7\13\2\2")
        buf.write(u"}\u0083\5\62\32\2~\177\7\f\2\2\177\u0080\7\r\2\2\u0080")
        buf.write(u"\u0082\5<\37\2\u0081~\3\2\2\2\u0082\u0085\3\2\2\2\u0083")
        buf.write(u"\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u009a\3\2\2")
        buf.write(u"\2\u0085\u0083\3\2\2\2\u0086\u008b\7)\2\2\u0087\u0088")
        buf.write(u"\7\16\2\2\u0088\u008a\7)\2\2\u0089\u0087\3\2\2\2\u008a")
        buf.write(u"\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2")
        buf.write(u"\2\u008c\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f")
        buf.write(u"\7\n\2\2\u008f\u0090\7\13\2\2\u0090\u0096\5\62\32\2\u0091")
        buf.write(u"\u0092\7\f\2\2\u0092\u0093\7\r\2\2\u0093\u0095\5<\37")
        buf.write(u"\2\u0094\u0091\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094")
        buf.write(u"\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u009a\3\2\2\2\u0098")
        buf.write(u"\u0096\3\2\2\2\u0099z\3\2\2\2\u0099\u0086\3\2\2\2\u009a")
        buf.write(u"\r\3\2\2\2\u009b\u009c\7)\2\2\u009c\u009d\7\n\2\2\u009d")
        buf.write(u"\u009e\7\17\2\2\u009e\u009f\7\13\2\2\u009f\u00a5\5\62")
        buf.write(u"\32\2\u00a0\u00a1\7\f\2\2\u00a1\u00a2\7\r\2\2\u00a2\u00a4")
        buf.write(u"\5<\37\2\u00a3\u00a0\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5")
        buf.write(u"\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00bd\3\2\2")
        buf.write(u"\2\u00a7\u00a5\3\2\2\2\u00a8\u00ad\7)\2\2\u00a9\u00aa")
        buf.write(u"\7\16\2\2\u00aa\u00ac\7)\2\2\u00ab\u00a9\3\2\2\2\u00ac")
        buf.write(u"\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2")
        buf.write(u"\2\u00ae\u00b0\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b1")
        buf.write(u"\7\n\2\2\u00b1\u00b2\7\17\2\2\u00b2\u00b3\7\13\2\2\u00b3")
        buf.write(u"\u00b9\5\62\32\2\u00b4\u00b5\7\f\2\2\u00b5\u00b6\7\r")
        buf.write(u"\2\2\u00b6\u00b8\5<\37\2\u00b7\u00b4\3\2\2\2\u00b8\u00bb")
        buf.write(u"\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba")
        buf.write(u"\u00bd\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u009b\3\2\2")
        buf.write(u"\2\u00bc\u00a8\3\2\2\2\u00bd\17\3\2\2\2\u00be\u00bf\7")
        buf.write(u")\2\2\u00bf\u00c0\7\n\2\2\u00c0\u00c1\7\20\2\2\u00c1")
        buf.write(u"\u00c2\7\13\2\2\u00c2\u00c8\5\62\32\2\u00c3\u00c4\7\f")
        buf.write(u"\2\2\u00c4\u00c5\7\r\2\2\u00c5\u00c7\5<\37\2\u00c6\u00c3")
        buf.write(u"\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8")
        buf.write(u"\u00c9\3\2\2\2\u00c9\u00e0\3\2\2\2\u00ca\u00c8\3\2\2")
        buf.write(u"\2\u00cb\u00d0\7)\2\2\u00cc\u00cd\7\16\2\2\u00cd\u00cf")
        buf.write(u"\7)\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0")
        buf.write(u"\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3\3\2\2")
        buf.write(u"\2\u00d2\u00d0\3\2\2\2\u00d3\u00d4\7\n\2\2\u00d4\u00d5")
        buf.write(u"\7\20\2\2\u00d5\u00d6\7\13\2\2\u00d6\u00dc\5\62\32\2")
        buf.write(u"\u00d7\u00d8\7\f\2\2\u00d8\u00d9\7\r\2\2\u00d9\u00db")
        buf.write(u"\5<\37\2\u00da\u00d7\3\2\2\2\u00db\u00de\3\2\2\2\u00dc")
        buf.write(u"\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00e0\3\2\2")
        buf.write(u"\2\u00de\u00dc\3\2\2\2\u00df\u00be\3\2\2\2\u00df\u00cb")
        buf.write(u"\3\2\2\2\u00e0\21\3\2\2\2\u00e1\u00e7\7)\2\2\u00e2\u00e3")
        buf.write(u"\7\16\2\2\u00e3\u00e6\7)\2\2\u00e4\u00e6\5,\27\2\u00e5")
        buf.write(u"\u00e2\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6\u00e9\3\2\2")
        buf.write(u"\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00ea")
        buf.write(u"\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb\7\13\2\2\u00eb")
        buf.write(u"\u00ec\5\62\32\2\u00ec\23\3\2\2\2\u00ed\u00ee\7\21\2")
        buf.write(u"\2\u00ee\u00ef\7)\2\2\u00ef\u00f3\7\4\2\2\u00f0\u00f2")
        buf.write(u"\5\26\f\2\u00f1\u00f0\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3")
        buf.write(u"\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f6\3\2\2")
        buf.write(u"\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7\5\30\r\2\u00f7\u00f8")
        buf.write(u"\5\n\6\2\u00f8\u00f9\7\5\2\2\u00f9\25\3\2\2\2\u00fa\u00fb")
        buf.write(u"\7\22\2\2\u00fb\u00ff\7\4\2\2\u00fc\u00fe\5*\26\2\u00fd")
        buf.write(u"\u00fc\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2")
        buf.write(u"\2\u00ff\u0100\3\2\2\2\u0100\u0102\3\2\2\2\u0101\u00ff")
        buf.write(u"\3\2\2\2\u0102\u0103\7\5\2\2\u0103\27\3\2\2\2\u0104\u0105")
        buf.write(u"\7\23\2\2\u0105\u0109\7\4\2\2\u0106\u0108\5&\24\2\u0107")
        buf.write(u"\u0106\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2")
        buf.write(u"\2\u0109\u010a\3\2\2\2\u010a\u010c\3\2\2\2\u010b\u0109")
        buf.write(u"\3\2\2\2\u010c\u010d\7\5\2\2\u010d\31\3\2\2\2\u010e\u010f")
        buf.write(u"\7\24\2\2\u010f\u0113\7\4\2\2\u0110\u0112\5\34\17\2\u0111")
        buf.write(u"\u0110\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111\3\2\2")
        buf.write(u"\2\u0113\u0114\3\2\2\2\u0114\u0116\3\2\2\2\u0115\u0113")
        buf.write(u"\3\2\2\2\u0116\u0117\7\5\2\2\u0117\33\3\2\2\2\u0118\u0119")
        buf.write(u"\7)\2\2\u0119\u011a\5$\23\2\u011a\35\3\2\2\2\u011b\u011c")
        buf.write(u"\7\4\2\2\u011c\u011d\5\62\32\2\u011d\u011e\7\25\2\2\u011e")
        buf.write(u"\u011f\7)\2\2\u011f\u0120\7\26\2\2\u0120\u0121\5\62\32")
        buf.write(u"\2\u0121\u0122\7\5\2\2\u0122\37\3\2\2\2\u0123\u0136\7")
        buf.write(u"\4\2\2\u0124\u0128\7)\2\2\u0125\u0128\5D#\2\u0126\u0128")
        buf.write(u"\5:\36\2\u0127\u0124\3\2\2\2\u0127\u0125\3\2\2\2\u0127")
        buf.write(u"\u0126\3\2\2\2\u0128\u0131\3\2\2\2\u0129\u012d\7\f\2")
        buf.write(u"\2\u012a\u012e\7)\2\2\u012b\u012e\5D#\2\u012c\u012e\5")
        buf.write(u":\36\2\u012d\u012a\3\2\2\2\u012d\u012b\3\2\2\2\u012d")
        buf.write(u"\u012c\3\2\2\2\u012e\u0130\3\2\2\2\u012f\u0129\3\2\2")
        buf.write(u"\2\u0130\u0133\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132")
        buf.write(u"\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0134")
        buf.write(u"\u0127\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2")
        buf.write(u"\2\u0136\u0137\3\2\2\2\u0137\u0139\3\2\2\2\u0138\u0136")
        buf.write(u"\3\2\2\2\u0139\u013f\7\5\2\2\u013a\u013b\7\4\2\2\u013b")
        buf.write(u"\u013c\5 \21\2\u013c\u013d\7\5\2\2\u013d\u013f\3\2\2")
        buf.write(u"\2\u013e\u0123\3\2\2\2\u013e\u013a\3\2\2\2\u013f!\3\2")
        buf.write(u"\2\2\u0140\u0153\7\27\2\2\u0141\u0145\7)\2\2\u0142\u0145")
        buf.write(u"\5D#\2\u0143\u0145\5:\36\2\u0144\u0141\3\2\2\2\u0144")
        buf.write(u"\u0142\3\2\2\2\u0144\u0143\3\2\2\2\u0145\u014e\3\2\2")
        buf.write(u"\2\u0146\u014a\7\f\2\2\u0147\u014b\7)\2\2\u0148\u014b")
        buf.write(u"\5D#\2\u0149\u014b\5:\36\2\u014a\u0147\3\2\2\2\u014a")
        buf.write(u"\u0148\3\2\2\2\u014a\u0149\3\2\2\2\u014b\u014d\3\2\2")
        buf.write(u"\2\u014c\u0146\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c")
        buf.write(u"\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0152\3\2\2\2\u0150")
        buf.write(u"\u014e\3\2\2\2\u0151\u0144\3\2\2\2\u0152\u0155\3\2\2")
        buf.write(u"\2\u0153\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0156")
        buf.write(u"\3\2\2\2\u0155\u0153\3\2\2\2\u0156\u0157\7\30\2\2\u0157")
        buf.write(u"#\3\2\2\2\u0158\u0163\7\27\2\2\u0159\u015e\5D#\2\u015a")
        buf.write(u"\u015b\7\f\2\2\u015b\u015d\5D#\2\u015c\u015a\3\2\2\2")
        buf.write(u"\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f")
        buf.write(u"\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0161")
        buf.write(u"\u0159\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2")
        buf.write(u"\2\u0163\u0164\3\2\2\2\u0164\u0166\3\2\2\2\u0165\u0163")
        buf.write(u"\3\2\2\2\u0166\u0167\7\30\2\2\u0167%\3\2\2\2\u0168\u0169")
        buf.write(u"\7)\2\2\u0169\'\3\2\2\2\u016a\u016b\7)\2\2\u016b\u016c")
        buf.write(u"\5,\27\2\u016c)\3\2\2\2\u016d\u016e\7)\2\2\u016e+\3\2")
        buf.write(u"\2\2\u016f\u0170\7\4\2\2\u0170\u0175\5.\30\2\u0171\u0172")
        buf.write(u"\7.\2\2\u0172\u0174\7\'\2\2\u0173\u0171\3\2\2\2\u0174")
        buf.write(u"\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2")
        buf.write(u"\2\u0176\u0178\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0179")
        buf.write(u"\7\5\2\2\u0179\u017d\3\2\2\2\u017a\u017d\7\17\2\2\u017b")
        buf.write(u"\u017d\7\20\2\2\u017c\u016f\3\2\2\2\u017c\u017a\3\2\2")
        buf.write(u"\2\u017c\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017c")
        buf.write(u"\3\2\2\2\u017e\u017f\3\2\2\2\u017f-\3\2\2\2\u0180\u0181")
        buf.write(u"\t\3\2\2\u0181/\3\2\2\2\u0182\u0183\7\4\2\2\u0183\u0184")
        buf.write(u"\5:\36\2\u0184\u0185\7\5\2\2\u0185\61\3\2\2\2\u0186\u0187")
        buf.write(u"\b\32\1\2\u0187\u0188\7\32\2\2\u0188\u01a2\5\62\32\17")
        buf.write(u"\u0189\u01a2\5\22\n\2\u018a\u01a2\58\35\2\u018b\u018c")
        buf.write(u"\7\32\2\2\u018c\u01a2\5:\36\2\u018d\u018e\7\32\2\2\u018e")
        buf.write(u"\u018f\5:\36\2\u018f\u0190\7\f\2\2\u0190\u01a2\3\2\2")
        buf.write(u"\2\u0191\u01a2\5 \21\2\u0192\u01a2\5\"\22\2\u0193\u01a2")
        buf.write(u"\5:\36\2\u0194\u01a2\5D#\2\u0195\u01a2\5B\"\2\u0196\u01a2")
        buf.write(u"\5\36\20\2\u0197\u01a2\7)\2\2\u0198\u01a2\7\33\2\2\u0199")
        buf.write(u"\u01a2\5(\25\2\u019a\u01a2\5.\30\2\u019b\u019c\5> \2")
        buf.write(u"\u019c\u019d\5\62\32\2\u019d\u019e\5@!\2\u019e\u01a2")
        buf.write(u"\3\2\2\2\u019f\u01a0\7\34\2\2\u01a0\u01a2\7)\2\2\u01a1")
        buf.write(u"\u0186\3\2\2\2\u01a1\u0189\3\2\2\2\u01a1\u018a\3\2\2")
        buf.write(u"\2\u01a1\u018b\3\2\2\2\u01a1\u018d\3\2\2\2\u01a1\u0191")
        buf.write(u"\3\2\2\2\u01a1\u0192\3\2\2\2\u01a1\u0193\3\2\2\2\u01a1")
        buf.write(u"\u0194\3\2\2\2\u01a1\u0195\3\2\2\2\u01a1\u0196\3\2\2")
        buf.write(u"\2\u01a1\u0197\3\2\2\2\u01a1\u0198\3\2\2\2\u01a1\u0199")
        buf.write(u"\3\2\2\2\u01a1\u019a\3\2\2\2\u01a1\u019b\3\2\2\2\u01a1")
        buf.write(u"\u019f\3\2\2\2\u01a2\u01b4\3\2\2\2\u01a3\u01a4\f\27\2")
        buf.write(u"\2\u01a4\u01a5\7\16\2\2\u01a5\u01b3\5\62\32\30\u01a6")
        buf.write(u"\u01a7\f\26\2\2\u01a7\u01a8\7\60\2\2\u01a8\u01b3\5\62")
        buf.write(u"\32\27\u01a9\u01aa\f\25\2\2\u01aa\u01ab\t\4\2\2\u01ab")
        buf.write(u"\u01b3\5\62\32\26\u01ac\u01ad\f\24\2\2\u01ad\u01ae\t")
        buf.write(u"\5\2\2\u01ae\u01b3\5\62\32\25\u01af\u01b0\f\23\2\2\u01b0")
        buf.write(u"\u01b1\7/\2\2\u01b1\u01b3\5\62\32\24\u01b2\u01a3\3\2")
        buf.write(u"\2\2\u01b2\u01a6\3\2\2\2\u01b2\u01a9\3\2\2\2\u01b2\u01ac")
        buf.write(u"\3\2\2\2\u01b2\u01af\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4")
        buf.write(u"\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\63\3\2\2\2\u01b6")
        buf.write(u"\u01b4\3\2\2\2\u01b7\u01bc\7\4\2\2\u01b8\u01bb\5\66\34")
        buf.write(u"\2\u01b9\u01bb\58\35\2\u01ba\u01b8\3\2\2\2\u01ba\u01b9")
        buf.write(u"\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write(u"\u01bd\3\2\2\2\u01bd\u01bf\3\2\2\2\u01be\u01bc\3\2\2")
        buf.write(u"\2\u01bf\u01c0\7\5\2\2\u01c0\65\3\2\2\2\u01c1\u01c2\5")
        buf.write(u"\62\32\2\u01c2\67\3\2\2\2\u01c3\u01c6\7\25\2\2\u01c4")
        buf.write(u"\u01c7\7)\2\2\u01c5\u01c7\5.\30\2\u01c6\u01c4\3\2\2\2")
        buf.write(u"\u01c6\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01cb")
        buf.write(u"\7\26\2\2\u01c9\u01cc\7)\2\2\u01ca\u01cc\5B\"\2\u01cb")
        buf.write(u"\u01c9\3\2\2\2\u01cb\u01ca\3\2\2\2\u01cc\u01cd\3\2\2")
        buf.write(u"\2\u01cd\u01ce\7\33\2\2\u01ce9\3\2\2\2\u01cf\u01d0\7")
        buf.write(u"\61\2\2\u01d0;\3\2\2\2\u01d1\u01d3\5> \2\u01d2\u01d1")
        buf.write(u"\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4")
        buf.write(u"\u01d5\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6\u01d4\3\2\2")
        buf.write(u"\2\u01d7\u01d8\5\62\32\2\u01d8\u01d9\t\6\2\2\u01d9\u01dd")
        buf.write(u"\5\62\32\2\u01da\u01dc\5@!\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write(u"\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2")
        buf.write(u"\2\u01de\u01e4\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e1")
        buf.write(u"\t\7\2\2\u01e1\u01e3\5<\37\2\u01e2\u01e0\3\2\2\2\u01e3")
        buf.write(u"\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3\2\2")
        buf.write(u"\2\u01e5=\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01e8\7\27")
        buf.write(u"\2\2\u01e8?\3\2\2\2\u01e9\u01ea\7\30\2\2\u01eaA\3\2\2")
        buf.write(u"\2\u01eb\u01ec\7)\2\2\u01ec\u01f0\7\27\2\2\u01ed\u01ef")
        buf.write(u"\5> \2\u01ee\u01ed\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0")
        buf.write(u"\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01fd\3\2\2")
        buf.write(u"\2\u01f2\u01f0\3\2\2\2\u01f3\u01f8\5\62\32\2\u01f4\u01f5")
        buf.write(u"\7\f\2\2\u01f5\u01f7\5\62\32\2\u01f6\u01f4\3\2\2\2\u01f7")
        buf.write(u"\u01fa\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2\2")
        buf.write(u"\2\u01f9\u01fc\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fb\u01f3")
        buf.write(u"\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd")
        buf.write(u"\u01fe\3\2\2\2\u01fe\u0203\3\2\2\2\u01ff\u01fd\3\2\2")
        buf.write(u"\2\u0200\u0202\5@!\2\u0201\u0200\3\2\2\2\u0202\u0205")
        buf.write(u"\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0204\3\2\2\2\u0204")
        buf.write(u"\u0206\3\2\2\2\u0205\u0203\3\2\2\2\u0206\u0207\7\30\2")
        buf.write(u"\2\u0207C\3\2\2\2\u0208\u0209\t\b\2\2\u0209E\3\2\2\2")
        buf.write(u"\67INW_ksu\u0083\u008b\u0096\u0099\u00a5\u00ad\u00b9")
        buf.write(u"\u00bc\u00c8\u00d0\u00dc\u00df\u00e5\u00e7\u00f3\u00ff")
        buf.write(u"\u0109\u0113\u0127\u012d\u0131\u0136\u013e\u0144\u014a")
        buf.write(u"\u014e\u0153\u015e\u0163\u0175\u017c\u017e\u01a1\u01b2")
        buf.write(u"\u01b4\u01ba\u01bc\u01c6\u01cb\u01d4\u01dd\u01e4\u01f0")
        buf.write(u"\u01f8\u01fd\u0203")
        return buf.getvalue()
		

class PrigogineParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'model'", u"'['", u"']'", u"'simulation'", 
                     u"'\n'", u"'\r'", u"'equations'", u"'[t+1]'", u"'='", 
                     u"','", u"'where'", u"'.'", u"'[:]'", u"'[n]'", u"'population'", 
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
                      u"<INVALID>", u"<INVALID>", u"LineComment", u"NEWLINE", 
                      u"ML_COMMENT", u"INT", u"FLOAT", u"ID", u"WS", u"MUL", 
                      u"DIV", u"ADD", u"SUB", u"PIPE", u"POWER", u"STRING", 
                      u"ESC", u"SPACE" ]

    RULE_filestart = 0
    RULE_model = 1
    RULE_simulation = 2
    RULE_codeinsert = 3
    RULE_equationlist = 4
    RULE_elementwiseEquation = 5
    RULE_mapEquation = 6
    RULE_nIndexedEquation = 7
    RULE_assignment = 8
    RULE_population = 9
    RULE_parameterlist = 10
    RULE_variablelist = 11
    RULE_msgboardlist = 12
    RULE_msgboarddef = 13
    RULE_listcomp = 14
    RULE_listdef = 15
    RULE_tupledef = 16
    RULE_numbertuple = 17
    RULE_variable = 18
    RULE_indexedvariable = 19
    RULE_parameter = 20
    RULE_timeindex = 21
    RULE_timevar = 22
    RULE_dictindex = 23
    RULE_expression = 24
    RULE_codeblock = 25
    RULE_codeline = 26
    RULE_pyforloop = 27
    RULE_string = 28
    RULE_conditional = 29
    RULE_lparen = 30
    RULE_rparen = 31
    RULE_func = 32
    RULE_number = 33

    ruleNames =  [ u"filestart", u"model", u"simulation", u"codeinsert", 
                   u"equationlist", u"elementwiseEquation", u"mapEquation", 
                   u"nIndexedEquation", u"assignment", u"population", u"parameterlist", 
                   u"variablelist", u"msgboardlist", u"msgboarddef", u"listcomp", 
                   u"listdef", u"tupledef", u"numbertuple", u"variable", 
                   u"indexedvariable", u"parameter", u"timeindex", u"timevar", 
                   u"dictindex", u"expression", u"codeblock", u"codeline", 
                   u"pyforloop", u"string", u"conditional", u"lparen", u"rparen", 
                   u"func", u"number" ]

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
    T__32=33
    LineComment=34
    NEWLINE=35
    ML_COMMENT=36
    INT=37
    FLOAT=38
    ID=39
    WS=40
    MUL=41
    DIV=42
    ADD=43
    SUB=44
    PIPE=45
    POWER=46
    STRING=47
    ESC=48
    SPACE=49

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
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68 
                self.model()
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrigogineParser.T__0):
                    break

            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__3:
                self.state = 73 
                self.simulation()
                self.state = 78
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
            self.state = 79
            self.match(PrigogineParser.T__0)
            self.state = 80
            self.match(PrigogineParser.ID)
            self.state = 81
            self.match(PrigogineParser.T__1)

            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__17:
                self.state = 82 
                self.msgboardlist()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88 
            self.variablelist()
            self.state = 89 
            self.equationlist()
            self.state = 91 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 90 
                self.population()
                self.state = 93 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrigogineParser.T__14):
                    break

            self.state = 95
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
            self.state = 97
            self.match(PrigogineParser.T__3)
            self.state = 98
            self.match(PrigogineParser.T__1)
            self.state = 99 
            self.codeinsert()
            self.state = 100
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
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 102
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==PrigogineParser.T__4 or _la==PrigogineParser.T__5:
                        self._errHandler.recoverInline(self)
                    self.consume() 
                self.state = 107
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


        def nIndexedEquation(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.NIndexedEquationContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.NIndexedEquationContext,i)


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
            self.state = 108
            self.match(PrigogineParser.T__6)
            self.state = 109
            self.match(PrigogineParser.T__1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 113
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 110 
                    self.elementwiseEquation()
                    pass

                elif la_ == 2:
                    self.state = 111 
                    self.mapEquation()
                    pass

                elif la_ == 3:
                    self.state = 112 
                    self.nIndexedEquation()
                    pass


                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
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
            self.state = 151
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(PrigogineParser.ID)
                self.state = 121
                self.match(PrigogineParser.T__7)
                self.state = 122
                self.match(PrigogineParser.T__8)
                self.state = 123 
                self.expression(0)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 124
                    self.match(PrigogineParser.T__9)
                    self.state = 125
                    self.match(PrigogineParser.T__10)
                    self.state = 126 
                    self.conditional()
                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(PrigogineParser.ID)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__11:
                    self.state = 133
                    self.match(PrigogineParser.T__11)
                    self.state = 134
                    self.match(PrigogineParser.ID)
                    self.state = 139
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 140
                self.match(PrigogineParser.T__7)
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
            self.state = 186
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(PrigogineParser.ID)
                self.state = 154
                self.match(PrigogineParser.T__7)
                self.state = 155
                self.match(PrigogineParser.T__12)
                self.state = 156
                self.match(PrigogineParser.T__8)
                self.state = 157 
                self.expression(0)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 158
                    self.match(PrigogineParser.T__9)
                    self.state = 159
                    self.match(PrigogineParser.T__10)
                    self.state = 160 
                    self.conditional()
                    self.state = 165
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(PrigogineParser.ID)
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__11:
                    self.state = 167
                    self.match(PrigogineParser.T__11)
                    self.state = 168
                    self.match(PrigogineParser.ID)
                    self.state = 173
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 174
                self.match(PrigogineParser.T__7)
                self.state = 175
                self.match(PrigogineParser.T__12)
                self.state = 176
                self.match(PrigogineParser.T__8)
                self.state = 177 
                self.expression(0)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 178
                    self.match(PrigogineParser.T__9)
                    self.state = 179
                    self.match(PrigogineParser.T__10)
                    self.state = 180 
                    self.conditional()
                    self.state = 185
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

    class NIndexedEquationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.NIndexedEquationContext, self).__init__(parent, invokingState)
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
            return PrigogineParser.RULE_nIndexedEquation

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterNIndexedEquation(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitNIndexedEquation(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitNIndexedEquation(self)
            else:
                return visitor.visitChildren(self)




    def nIndexedEquation(self):

        localctx = PrigogineParser.NIndexedEquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_nIndexedEquation)
        self._la = 0 # Token type
        try:
            self.state = 221
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(PrigogineParser.ID)
                self.state = 189
                self.match(PrigogineParser.T__7)
                self.state = 190
                self.match(PrigogineParser.T__13)
                self.state = 191
                self.match(PrigogineParser.T__8)
                self.state = 192 
                self.expression(0)
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 193
                    self.match(PrigogineParser.T__9)
                    self.state = 194
                    self.match(PrigogineParser.T__10)
                    self.state = 195 
                    self.conditional()
                    self.state = 200
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(PrigogineParser.ID)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__11:
                    self.state = 202
                    self.match(PrigogineParser.T__11)
                    self.state = 203
                    self.match(PrigogineParser.ID)
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 209
                self.match(PrigogineParser.T__7)
                self.state = 210
                self.match(PrigogineParser.T__13)
                self.state = 211
                self.match(PrigogineParser.T__8)
                self.state = 212 
                self.expression(0)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 213
                    self.match(PrigogineParser.T__9)
                    self.state = 214
                    self.match(PrigogineParser.T__10)
                    self.state = 215 
                    self.conditional()
                    self.state = 220
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
        self.enterRule(localctx, 16, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(PrigogineParser.ID)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__11) | (1 << PrigogineParser.T__12) | (1 << PrigogineParser.T__13))) != 0):
                self.state = 227
                token = self._input.LA(1)
                if token in [PrigogineParser.T__11]:
                    self.state = 224
                    self.match(PrigogineParser.T__11)
                    self.state = 225
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.T__1, PrigogineParser.T__12, PrigogineParser.T__13]:
                    self.state = 226 
                    self.timeindex()

                else:
                    raise NoViableAltException(self)

                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 232
            self.match(PrigogineParser.T__8)
            self.state = 233 
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
        self.enterRule(localctx, 18, self.RULE_population)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(PrigogineParser.T__14)
            self.state = 236
            self.match(PrigogineParser.ID)
            self.state = 237
            self.match(PrigogineParser.T__1)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__15:
                self.state = 238 
                self.parameterlist()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 244 
            self.variablelist()
            self.state = 245 
            self.equationlist()
            self.state = 246
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
        self.enterRule(localctx, 20, self.RULE_parameterlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(PrigogineParser.T__15)
            self.state = 249
            self.match(PrigogineParser.T__1)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 250 
                self.parameter()
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 256
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
            self.state = 258
            self.match(PrigogineParser.T__16)
            self.state = 259
            self.match(PrigogineParser.T__1)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 260 
                self.variable()
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 266
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
        self.enterRule(localctx, 24, self.RULE_msgboardlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(PrigogineParser.T__17)
            self.state = 269
            self.match(PrigogineParser.T__1)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 270 
                self.msgboarddef()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 276
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
        self.enterRule(localctx, 26, self.RULE_msgboarddef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(PrigogineParser.ID)
            self.state = 279 
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
        self.enterRule(localctx, 28, self.RULE_listcomp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(PrigogineParser.T__1)
            self.state = 282 
            self.expression(0)
            self.state = 283
            self.match(PrigogineParser.T__18)
            self.state = 284
            self.match(PrigogineParser.ID)
            self.state = 285
            self.match(PrigogineParser.T__19)
            self.state = 286 
            self.expression(0)
            self.state = 287
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
        self.enterRule(localctx, 30, self.RULE_listdef)
        self._la = 0 # Token type
        try:
            self.state = 316
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.match(PrigogineParser.T__1)
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                    self.state = 293
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 290
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 291 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 292 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 303
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==PrigogineParser.T__9:
                        self.state = 295
                        self.match(PrigogineParser.T__9)
                        self.state = 299
                        token = self._input.LA(1)
                        if token in [PrigogineParser.ID]:
                            self.state = 296
                            self.match(PrigogineParser.ID)

                        elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                            self.state = 297 
                            self.number()

                        elif token in [PrigogineParser.STRING]:
                            self.state = 298 
                            self.string()

                        else:
                            raise NoViableAltException(self)

                        self.state = 305
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 310
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 311
                self.match(PrigogineParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.match(PrigogineParser.T__1)
                self.state = 313 
                self.listdef()
                self.state = 314
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
        self.enterRule(localctx, 32, self.RULE_tupledef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(PrigogineParser.T__20)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 322
                token = self._input.LA(1)
                if token in [PrigogineParser.ID]:
                    self.state = 319
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                    self.state = 320 
                    self.number()

                elif token in [PrigogineParser.STRING]:
                    self.state = 321 
                    self.string()

                else:
                    raise NoViableAltException(self)

                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 324
                    self.match(PrigogineParser.T__9)
                    self.state = 328
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 325
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 326 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 327 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 334
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 340
            self.match(PrigogineParser.T__21)
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
        self.enterRule(localctx, 34, self.RULE_numbertuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(PrigogineParser.T__20)
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.INT or _la==PrigogineParser.FLOAT:
                self.state = 343 
                self.number()
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 344
                    self.match(PrigogineParser.T__9)
                    self.state = 345 
                    self.number()
                    self.state = 350
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 355
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 356
            self.match(PrigogineParser.T__21)
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
        self.enterRule(localctx, 36, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
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
        self.enterRule(localctx, 38, self.RULE_indexedvariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(PrigogineParser.ID)
            self.state = 361 
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
        self.enterRule(localctx, 40, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
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
        self.enterRule(localctx, 42, self.RULE_timeindex)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 378
                    token = self._input.LA(1)
                    if token in [PrigogineParser.T__1]:
                        self.state = 365
                        self.match(PrigogineParser.T__1)
                        self.state = 366 
                        self.timevar()
                        self.state = 371
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==PrigogineParser.SUB:
                            self.state = 367
                            self.match(PrigogineParser.SUB)
                            self.state = 368
                            self.match(PrigogineParser.INT)
                            self.state = 373
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 374
                        self.match(PrigogineParser.T__2)

                    elif token in [PrigogineParser.T__12]:
                        self.state = 376
                        self.match(PrigogineParser.T__12)

                    elif token in [PrigogineParser.T__13]:
                        self.state = 377
                        self.match(PrigogineParser.T__13)

                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 380 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
        self.enterRule(localctx, 44, self.RULE_timevar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            _la = self._input.LA(1)
            if not(_la==PrigogineParser.T__22 or _la==PrigogineParser.INT):
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
        self.enterRule(localctx, 46, self.RULE_dictindex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(PrigogineParser.T__1)
            self.state = 385 
            self.string()
            self.state = 386
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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 389
                self.match(PrigogineParser.T__23)
                self.state = 390 
                self.expression(13)
                pass

            elif la_ == 2:
                self.state = 391 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 392 
                self.pyforloop()
                pass

            elif la_ == 4:
                self.state = 393
                self.match(PrigogineParser.T__23)
                self.state = 394 
                self.string()
                pass

            elif la_ == 5:
                self.state = 395
                self.match(PrigogineParser.T__23)
                self.state = 396 
                self.string()
                self.state = 397
                self.match(PrigogineParser.T__9)
                pass

            elif la_ == 6:
                self.state = 399 
                self.listdef()
                pass

            elif la_ == 7:
                self.state = 400 
                self.tupledef()
                pass

            elif la_ == 8:
                self.state = 401 
                self.string()
                pass

            elif la_ == 9:
                self.state = 402 
                self.number()
                pass

            elif la_ == 10:
                self.state = 403 
                self.func()
                pass

            elif la_ == 11:
                self.state = 404 
                self.listcomp()
                pass

            elif la_ == 12:
                self.state = 405
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 13:
                self.state = 406
                self.match(PrigogineParser.T__24)
                pass

            elif la_ == 14:
                self.state = 407 
                self.indexedvariable()
                pass

            elif la_ == 15:
                self.state = 408 
                self.timevar()
                pass

            elif la_ == 16:
                self.state = 409 
                self.lparen()
                self.state = 410 
                self.expression(0)
                self.state = 411 
                self.rparen()
                pass

            elif la_ == 17:
                self.state = 413
                self.match(PrigogineParser.T__25)
                self.state = 414
                self.match(PrigogineParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 434
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 432
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 417
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 418
                        self.match(PrigogineParser.T__11)
                        self.state = 419 
                        self.expression(22)
                        pass

                    elif la_ == 2:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 420
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 421
                        self.match(PrigogineParser.POWER)
                        self.state = 422 
                        self.expression(21)
                        pass

                    elif la_ == 3:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 423
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 424
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.MUL or _la==PrigogineParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 425 
                        self.expression(20)
                        pass

                    elif la_ == 4:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 426
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 427
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 428 
                        self.expression(19)
                        pass

                    elif la_ == 5:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 429
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 430
                        localctx.op = self.match(PrigogineParser.PIPE)
                        self.state = 431 
                        self.expression(18)
                        pass

             
                self.state = 436
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
        self.enterRule(localctx, 50, self.RULE_codeblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(PrigogineParser.T__1)
            self.state = 442
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__18) | (1 << PrigogineParser.T__20) | (1 << PrigogineParser.T__22) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.T__25) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 440
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 438 
                    self.codeline()
                    pass

                elif la_ == 2:
                    self.state = 439 
                    self.pyforloop()
                    pass


                self.state = 444
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 445
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
            self.state = 447 
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
        self.enterRule(localctx, 54, self.RULE_pyforloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(PrigogineParser.T__18)
            self.state = 452
            token = self._input.LA(1)
            if token in [PrigogineParser.ID]:
                self.state = 450
                self.match(PrigogineParser.ID)

            elif token in [PrigogineParser.T__22, PrigogineParser.INT]:
                self.state = 451 
                self.timevar()

            else:
                raise NoViableAltException(self)

            self.state = 454
            self.match(PrigogineParser.T__19)
            self.state = 457
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 455
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 2:
                self.state = 456 
                self.func()
                pass


            self.state = 459
            self.match(PrigogineParser.T__24)
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
        self.enterRule(localctx, 56, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
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
        self.enterRule(localctx, 58, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 463 
                    self.lparen() 
                self.state = 468
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

            self.state = 469 
            self.expression(0)
            self.state = 470
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__26) | (1 << PrigogineParser.T__27) | (1 << PrigogineParser.T__28) | (1 << PrigogineParser.T__29) | (1 << PrigogineParser.T__30) | (1 << PrigogineParser.T__31))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            self.consume()
            self.state = 471 
            self.expression(0)
            self.state = 475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__21:
                self.state = 472 
                self.rparen()
                self.state = 477
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 482
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 478
                    _la = self._input.LA(1)
                    if not(_la==PrigogineParser.T__32 or _la==PrigogineParser.PIPE):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 479 
                    self.conditional() 
                self.state = 484
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

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
        self.enterRule(localctx, 60, self.RULE_lparen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(PrigogineParser.T__20)
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
        self.enterRule(localctx, 62, self.RULE_rparen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(PrigogineParser.T__21)
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
        self.enterRule(localctx, 64, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(PrigogineParser.ID)
            self.state = 490
            self.match(PrigogineParser.T__20)
            self.state = 494
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 491 
                    self.lparen() 
                self.state = 496
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

            self.state = 507
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__18) | (1 << PrigogineParser.T__20) | (1 << PrigogineParser.T__22) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.T__25) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 497 
                self.expression(0)
                self.state = 502
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__9:
                    self.state = 498
                    self.match(PrigogineParser.T__9)
                    self.state = 499 
                    self.expression(0)
                    self.state = 504
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 509
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 513
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 510 
                    self.rparen() 
                self.state = 515
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

            self.state = 516
            self.match(PrigogineParser.T__21)
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
            self.state = 518
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
        self._predicates[24] = self.expression_sempred
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
         



