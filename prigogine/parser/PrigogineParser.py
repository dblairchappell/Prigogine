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
        buf.write(u"\63\u017a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\3\2\3\2\3\2\3\2\6\2M\n\2\r\2\16\2N\3\2\7\2R\n\2")
        buf.write(u"\f\2\16\2U\13\2\3\3\3\3\3\3\3\3\3\3\3\3\7\3]\n\3\f\3")
        buf.write(u"\16\3`\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write(u"\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\7\bw\n\b\f")
        buf.write(u"\b\16\bz\13\b\3\t\3\t\7\t~\n\t\f\t\16\t\u0081\13\t\3")
        buf.write(u"\t\3\t\3\n\3\n\3\n\6\n\u0088\n\n\r\n\16\n\u0089\3\13")
        buf.write(u"\3\13\3\13\7\13\u008f\n\13\f\13\16\13\u0092\13\13\3\f")
        buf.write(u"\3\f\7\f\u0096\n\f\f\f\16\f\u0099\13\f\3\r\3\r\3\r\7")
        buf.write(u"\r\u009e\n\r\f\r\16\r\u00a1\13\r\3\r\3\r\3\16\3\16\3")
        buf.write(u"\16\7\16\u00a8\n\16\f\16\16\16\u00ab\13\16\3\16\3\16")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write(u"\20\3\20\5\20\u00bb\n\20\3\20\3\20\3\20\3\20\5\20\u00c1")
        buf.write(u"\n\20\7\20\u00c3\n\20\f\20\16\20\u00c6\13\20\7\20\u00c8")
        buf.write(u"\n\20\f\20\16\20\u00cb\13\20\3\20\3\20\3\21\3\21\3\21")
        buf.write(u"\3\21\5\21\u00d3\n\21\3\21\3\21\3\21\3\21\5\21\u00d9")
        buf.write(u"\n\21\7\21\u00db\n\21\f\21\16\21\u00de\13\21\7\21\u00e0")
        buf.write(u"\n\21\f\21\16\21\u00e3\13\21\3\21\3\21\3\22\3\22\3\23")
        buf.write(u"\3\23\3\24\3\24\3\24\3\24\7\24\u00ef\n\24\f\24\16\24")
        buf.write(u"\u00f2\13\24\3\24\3\24\5\24\u00f6\n\24\3\25\3\25\3\26")
        buf.write(u"\3\26\3\26\3\26\3\27\3\27\3\27\3\27\7\27\u0102\n\27\f")
        buf.write(u"\27\16\27\u0105\13\27\3\27\7\27\u0108\n\27\f\27\16\27")
        buf.write(u"\u010b\13\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\7\30")
        buf.write(u"\u0114\n\30\f\30\16\30\u0117\13\30\3\31\3\31\3\31\3\31")
        buf.write(u"\5\31\u011d\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write(u"\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write(u"\3\32\3\32\5\32\u0133\n\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write(u"\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32")
        buf.write(u"\u0144\n\32\f\32\16\32\u0147\13\32\3\33\3\33\3\33\3\33")
        buf.write(u"\3\34\3\34\7\34\u014f\n\34\f\34\16\34\u0152\13\34\3\34")
        buf.write(u"\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(u"!\3!\3\"\3\"\3\"\3\"\3\"\7\"\u0167\n\"\f\"\16\"\u016a")
        buf.write(u"\13\"\7\"\u016c\n\"\f\"\16\"\u016f\13\"\3\"\3\"\3#\3")
        buf.write(u"#\3#\5#\u0176\n#\3$\3$\3$\2\3\62%\2\4\6\b\n\f\16\20\22")
        buf.write(u"\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF\2\6\3")
        buf.write(u"\2-.\3\2+,\3\2\36#\3\2\'(\u018d\2L\3\2\2\2\4V\3\2\2\2")
        buf.write(u"\6c\3\2\2\2\bg\3\2\2\2\nk\3\2\2\2\fo\3\2\2\2\16r\3\2")
        buf.write(u"\2\2\20{\3\2\2\2\22\u0087\3\2\2\2\24\u008b\3\2\2\2\26")
        buf.write(u"\u0093\3\2\2\2\30\u009a\3\2\2\2\32\u00a4\3\2\2\2\34\u00ae")
        buf.write(u"\3\2\2\2\36\u00b6\3\2\2\2 \u00ce\3\2\2\2\"\u00e6\3\2")
        buf.write(u"\2\2$\u00e8\3\2\2\2&\u00f5\3\2\2\2(\u00f7\3\2\2\2*\u00f9")
        buf.write(u"\3\2\2\2,\u00fd\3\2\2\2.\u010e\3\2\2\2\60\u0118\3\2\2")
        buf.write(u"\2\62\u0132\3\2\2\2\64\u0148\3\2\2\2\66\u014c\3\2\2\2")
        buf.write(u"8\u0155\3\2\2\2:\u0157\3\2\2\2<\u0159\3\2\2\2>\u015d")
        buf.write(u"\3\2\2\2@\u015f\3\2\2\2B\u0161\3\2\2\2D\u0175\3\2\2\2")
        buf.write(u"F\u0177\3\2\2\2HM\5\4\3\2IM\5\6\4\2JM\5\16\b\2KM\5\24")
        buf.write(u"\13\2LH\3\2\2\2LI\3\2\2\2LJ\3\2\2\2LK\3\2\2\2MN\3\2\2")
        buf.write(u"\2NL\3\2\2\2NO\3\2\2\2OS\3\2\2\2PR\5\26\f\2QP\3\2\2\2")
        buf.write(u"RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\3\3\2\2\2US\3\2\2\2V")
        buf.write(u"W\7\3\2\2WX\7)\2\2XY\7\4\2\2YZ\5\30\r\2Z^\5\32\16\2[")
        buf.write(u"]\5,\27\2\\[\3\2\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_")
        buf.write(u"a\3\2\2\2`^\3\2\2\2ab\7\5\2\2b\5\3\2\2\2cd\7\6\2\2de")
        buf.write(u"\7)\2\2ef\5\62\32\2f\7\3\2\2\2gh\7\7\2\2hi\7)\2\2ij\5")
        buf.write(u"\62\32\2j\t\3\2\2\2kl\7\b\2\2lm\7)\2\2mn\5\62\32\2n\13")
        buf.write(u"\3\2\2\2op\7\t\2\2pq\5\62\32\2q\r\3\2\2\2rs\7\n\2\2s")
        buf.write(u"t\7)\2\2tx\7\'\2\2uw\5\20\t\2vu\3\2\2\2wz\3\2\2\2xv\3")
        buf.write(u"\2\2\2xy\3\2\2\2y\17\3\2\2\2zx\3\2\2\2{\177\7\4\2\2|")
        buf.write(u"~\5\22\n\2}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177")
        buf.write(u"\u0080\3\2\2\2\u0080\u0082\3\2\2\2\u0081\177\3\2\2\2")
        buf.write(u"\u0082\u0083\7\5\2\2\u0083\21\3\2\2\2\u0084\u0088\5\b")
        buf.write(u"\5\2\u0085\u0088\5\f\7\2\u0086\u0088\5\n\6\2\u0087\u0084")
        buf.write(u"\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0086\3\2\2\2\u0088")
        buf.write(u"\u0089\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2")
        buf.write(u"\2\u008a\23\3\2\2\2\u008b\u008c\7\13\2\2\u008c\u0090")
        buf.write(u"\7\'\2\2\u008d\u008f\5\66\34\2\u008e\u008d\3\2\2\2\u008f")
        buf.write(u"\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2")
        buf.write(u"\2\u0091\25\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0097\7")
        buf.write(u"\f\2\2\u0094\u0096\5\66\34\2\u0095\u0094\3\2\2\2\u0096")
        buf.write(u"\u0099\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2")
        buf.write(u"\2\u0098\27\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009b\7")
        buf.write(u"\r\2\2\u009b\u009f\7\4\2\2\u009c\u009e\5$\23\2\u009d")
        buf.write(u"\u009c\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2")
        buf.write(u"\2\u009f\u00a0\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1\u009f")
        buf.write(u"\3\2\2\2\u00a2\u00a3\7\5\2\2\u00a3\31\3\2\2\2\u00a4\u00a5")
        buf.write(u"\7\16\2\2\u00a5\u00a9\7\4\2\2\u00a6\u00a8\5\"\22\2\u00a7")
        buf.write(u"\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2")
        buf.write(u"\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a9")
        buf.write(u"\3\2\2\2\u00ac\u00ad\7\5\2\2\u00ad\33\3\2\2\2\u00ae\u00af")
        buf.write(u"\7\4\2\2\u00af\u00b0\5\62\32\2\u00b0\u00b1\7\17\2\2\u00b1")
        buf.write(u"\u00b2\7)\2\2\u00b2\u00b3\7\20\2\2\u00b3\u00b4\5\62\32")
        buf.write(u"\2\u00b4\u00b5\7\5\2\2\u00b5\35\3\2\2\2\u00b6\u00c9\7")
        buf.write(u"\4\2\2\u00b7\u00bb\7)\2\2\u00b8\u00bb\5F$\2\u00b9\u00bb")
        buf.write(u"\5:\36\2\u00ba\u00b7\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba")
        buf.write(u"\u00b9\3\2\2\2\u00bb\u00c4\3\2\2\2\u00bc\u00c0\7\21\2")
        buf.write(u"\2\u00bd\u00c1\7)\2\2\u00be\u00c1\5F$\2\u00bf\u00c1\5")
        buf.write(u":\36\2\u00c0\u00bd\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0")
        buf.write(u"\u00bf\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00bc\3\2\2")
        buf.write(u"\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5")
        buf.write(u"\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7")
        buf.write(u"\u00ba\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2")
        buf.write(u"\2\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb\u00c9")
        buf.write(u"\3\2\2\2\u00cc\u00cd\7\5\2\2\u00cd\37\3\2\2\2\u00ce\u00e1")
        buf.write(u"\7\22\2\2\u00cf\u00d3\7)\2\2\u00d0\u00d3\5F$\2\u00d1")
        buf.write(u"\u00d3\5:\36\2\u00d2\u00cf\3\2\2\2\u00d2\u00d0\3\2\2")
        buf.write(u"\2\u00d2\u00d1\3\2\2\2\u00d3\u00dc\3\2\2\2\u00d4\u00d8")
        buf.write(u"\7\21\2\2\u00d5\u00d9\7)\2\2\u00d6\u00d9\5F$\2\u00d7")
        buf.write(u"\u00d9\5:\36\2\u00d8\u00d5\3\2\2\2\u00d8\u00d6\3\2\2")
        buf.write(u"\2\u00d8\u00d7\3\2\2\2\u00d9\u00db\3\2\2\2\u00da\u00d4")
        buf.write(u"\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc")
        buf.write(u"\u00dd\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2")
        buf.write(u"\2\u00df\u00d2\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df")
        buf.write(u"\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e4\3\2\2\2\u00e3")
        buf.write(u"\u00e1\3\2\2\2\u00e4\u00e5\7\23\2\2\u00e5!\3\2\2\2\u00e6")
        buf.write(u"\u00e7\7)\2\2\u00e7#\3\2\2\2\u00e8\u00e9\7)\2\2\u00e9")
        buf.write(u"%\3\2\2\2\u00ea\u00eb\7\4\2\2\u00eb\u00f0\7\24\2\2\u00ec")
        buf.write(u"\u00ed\t\2\2\2\u00ed\u00ef\7\'\2\2\u00ee\u00ec\3\2\2")
        buf.write(u"\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1")
        buf.write(u"\3\2\2\2\u00f1\u00f3\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3")
        buf.write(u"\u00f6\7\5\2\2\u00f4\u00f6\7\25\2\2\u00f5\u00ea\3\2\2")
        buf.write(u"\2\u00f5\u00f4\3\2\2\2\u00f6\'\3\2\2\2\u00f7\u00f8\7")
        buf.write(u"\24\2\2\u00f8)\3\2\2\2\u00f9\u00fa\7\4\2\2\u00fa\u00fb")
        buf.write(u"\5:\36\2\u00fb\u00fc\7\5\2\2\u00fc+\3\2\2\2\u00fd\u00fe")
        buf.write(u"\7\26\2\2\u00fe\u00ff\7)\2\2\u00ff\u0103\7\4\2\2\u0100")
        buf.write(u"\u0102\5.\30\2\u0101\u0100\3\2\2\2\u0102\u0105\3\2\2")
        buf.write(u"\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0109")
        buf.write(u"\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0108\5\60\31\2\u0107")
        buf.write(u"\u0106\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2")
        buf.write(u"\2\u0109\u010a\3\2\2\2\u010a\u010c\3\2\2\2\u010b\u0109")
        buf.write(u"\3\2\2\2\u010c\u010d\7\5\2\2\u010d-\3\2\2\2\u010e\u010f")
        buf.write(u"\7\27\2\2\u010f\u0110\7)\2\2\u0110\u0111\7\30\2\2\u0111")
        buf.write(u"\u0115\5<\37\2\u0112\u0114\5\66\34\2\u0113\u0112\3\2")
        buf.write(u"\2\2\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116")
        buf.write(u"\3\2\2\2\u0116/\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119")
        buf.write(u"\7\31\2\2\u0119\u011c\7)\2\2\u011a\u011d\58\35\2\u011b")
        buf.write(u"\u011d\5\66\34\2\u011c\u011a\3\2\2\2\u011c\u011b\3\2")
        buf.write(u"\2\2\u011d\61\3\2\2\2\u011e\u011f\b\32\1\2\u011f\u0120")
        buf.write(u"\7\33\2\2\u0120\u0133\5\62\32\r\u0121\u0133\5\64\33\2")
        buf.write(u"\u0122\u0123\7\33\2\2\u0123\u0133\5:\36\2\u0124\u0133")
        buf.write(u"\5\36\20\2\u0125\u0133\5 \21\2\u0126\u0133\5:\36\2\u0127")
        buf.write(u"\u0133\5F$\2\u0128\u0133\5B\"\2\u0129\u0133\5\34\17\2")
        buf.write(u"\u012a\u0133\7)\2\2\u012b\u0133\5(\25\2\u012c\u012d\5")
        buf.write(u"> \2\u012d\u012e\5\62\32\2\u012e\u012f\5@!\2\u012f\u0133")
        buf.write(u"\3\2\2\2\u0130\u0131\7\34\2\2\u0131\u0133\7)\2\2\u0132")
        buf.write(u"\u011e\3\2\2\2\u0132\u0121\3\2\2\2\u0132\u0122\3\2\2")
        buf.write(u"\2\u0132\u0124\3\2\2\2\u0132\u0125\3\2\2\2\u0132\u0126")
        buf.write(u"\3\2\2\2\u0132\u0127\3\2\2\2\u0132\u0128\3\2\2\2\u0132")
        buf.write(u"\u0129\3\2\2\2\u0132\u012a\3\2\2\2\u0132\u012b\3\2\2")
        buf.write(u"\2\u0132\u012c\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u0145")
        buf.write(u"\3\2\2\2\u0134\u0135\f\23\2\2\u0135\u0136\7\32\2\2\u0136")
        buf.write(u"\u0144\5\62\32\24\u0137\u0138\f\22\2\2\u0138\u0139\7")
        buf.write(u"\60\2\2\u0139\u0144\5\62\32\23\u013a\u013b\f\21\2\2\u013b")
        buf.write(u"\u013c\t\3\2\2\u013c\u0144\5\62\32\22\u013d\u013e\f\20")
        buf.write(u"\2\2\u013e\u013f\t\2\2\2\u013f\u0144\5\62\32\21\u0140")
        buf.write(u"\u0141\f\17\2\2\u0141\u0142\7/\2\2\u0142\u0144\5\62\32")
        buf.write(u"\20\u0143\u0134\3\2\2\2\u0143\u0137\3\2\2\2\u0143\u013a")
        buf.write(u"\3\2\2\2\u0143\u013d\3\2\2\2\u0143\u0140\3\2\2\2\u0144")
        buf.write(u"\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2")
        buf.write(u"\2\u0146\63\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u0149\7")
        buf.write(u")\2\2\u0149\u014a\7\35\2\2\u014a\u014b\5\62\32\2\u014b")
        buf.write(u"\65\3\2\2\2\u014c\u0150\7\4\2\2\u014d\u014f\58\35\2\u014e")
        buf.write(u"\u014d\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3\2\2")
        buf.write(u"\2\u0150\u0151\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u0150")
        buf.write(u"\3\2\2\2\u0153\u0154\7\5\2\2\u0154\67\3\2\2\2\u0155\u0156")
        buf.write(u"\5\62\32\2\u01569\3\2\2\2\u0157\u0158\7\61\2\2\u0158")
        buf.write(u";\3\2\2\2\u0159\u015a\5\62\32\2\u015a\u015b\t\4\2\2\u015b")
        buf.write(u"\u015c\5\62\32\2\u015c=\3\2\2\2\u015d\u015e\7\22\2\2")
        buf.write(u"\u015e?\3\2\2\2\u015f\u0160\7\23\2\2\u0160A\3\2\2\2\u0161")
        buf.write(u"\u0162\7)\2\2\u0162\u016d\7\22\2\2\u0163\u0168\5\62\32")
        buf.write(u"\2\u0164\u0165\7\21\2\2\u0165\u0167\5\62\32\2\u0166\u0164")
        buf.write(u"\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168")
        buf.write(u"\u0169\3\2\2\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2")
        buf.write(u"\2\u016b\u0163\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b")
        buf.write(u"\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0170\3\2\2\2\u016f")
        buf.write(u"\u016d\3\2\2\2\u0170\u0171\7\23\2\2\u0171C\3\2\2\2\u0172")
        buf.write(u"\u0176\5F$\2\u0173\u0176\7)\2\2\u0174\u0176\5B\"\2\u0175")
        buf.write(u"\u0172\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0174\3\2\2")
        buf.write(u"\2\u0176E\3\2\2\2\u0177\u0178\t\5\2\2\u0178G\3\2\2\2")
        buf.write(u"#LNS^x\177\u0087\u0089\u0090\u0097\u009f\u00a9\u00ba")
        buf.write(u"\u00c0\u00c4\u00c9\u00d2\u00d8\u00dc\u00e1\u00f0\u00f5")
        buf.write(u"\u0103\u0109\u0115\u011c\u0132\u0143\u0145\u0150\u0168")
        buf.write(u"\u016d\u0175")
        return buf.getvalue()
		

class PrigogineParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'population'", u"'['", u"']'", u"'initglobal'", 
                     u"'initvars'", u"'initparams'", u"'initstates'", u"'create'", 
                     u"'runmodel'", u"'finalise'", u"'parameters'", u"'variables'", 
                     u"'for'", u"'in'", u"','", u"'('", u"')'", u"'t'", 
                     u"'[:]'", u"'state'", u"'transition'", u"'where'", 
                     u"'update'", u"'.'", u"'print'", u"'return'", u"'='", 
                     u"'<'", u"'>'", u"'>='", u"'<='", u"'=='", u"'!='", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
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
                      u"<INVALID>", u"<INVALID>", u"LineComment", u"NEWLINE", 
                      u"ML_COMMENT", u"INT", u"FLOAT", u"ID", u"WS", u"MUL", 
                      u"DIV", u"ADD", u"SUB", u"PIPE", u"POWER", u"STRING", 
                      u"ESC", u"SPACE" ]

    RULE_filestart = 0
    RULE_population = 1
    RULE_initglobal = 2
    RULE_initvars = 3
    RULE_initparams = 4
    RULE_initstates = 5
    RULE_create = 6
    RULE_createblock = 7
    RULE_createline = 8
    RULE_runmodel = 9
    RULE_finalise = 10
    RULE_parameterlist = 11
    RULE_variablelist = 12
    RULE_listcomp = 13
    RULE_listdef = 14
    RULE_tupledef = 15
    RULE_variable = 16
    RULE_parameter = 17
    RULE_timeindex = 18
    RULE_timevar = 19
    RULE_dictindex = 20
    RULE_statedef = 21
    RULE_transition = 22
    RULE_update = 23
    RULE_expression = 24
    RULE_assignment = 25
    RULE_codeblock = 26
    RULE_codeline = 27
    RULE_string = 28
    RULE_conditional = 29
    RULE_lparen = 30
    RULE_rparen = 31
    RULE_func = 32
    RULE_argument = 33
    RULE_number = 34

    ruleNames =  [ u"filestart", u"population", u"initglobal", u"initvars", 
                   u"initparams", u"initstates", u"create", u"createblock", 
                   u"createline", u"runmodel", u"finalise", u"parameterlist", 
                   u"variablelist", u"listcomp", u"listdef", u"tupledef", 
                   u"variable", u"parameter", u"timeindex", u"timevar", 
                   u"dictindex", u"statedef", u"transition", u"update", 
                   u"expression", u"assignment", u"codeblock", u"codeline", 
                   u"string", u"conditional", u"lparen", u"rparen", u"func", 
                   u"argument", u"number" ]

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
            self.state = 74 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                token = self._input.LA(1)
                if token in [PrigogineParser.T__0]:
                    self.state = 70 
                    self.population()

                elif token in [PrigogineParser.T__3]:
                    self.state = 71 
                    self.initglobal()

                elif token in [PrigogineParser.T__7]:
                    self.state = 72 
                    self.create()

                elif token in [PrigogineParser.T__8]:
                    self.state = 73 
                    self.runmodel()

                else:
                    raise NoViableAltException(self)

                self.state = 76 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__0) | (1 << PrigogineParser.T__3) | (1 << PrigogineParser.T__7) | (1 << PrigogineParser.T__8))) != 0)):
                    break

            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__9:
                self.state = 78 
                self.finalise()
                self.state = 83
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
            self.state = 84
            self.match(PrigogineParser.T__0)
            self.state = 85
            self.match(PrigogineParser.ID)
            self.state = 86
            self.match(PrigogineParser.T__1)
            self.state = 87 
            self.parameterlist()
            self.state = 88 
            self.variablelist()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__19:
                self.state = 89 
                self.statedef()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
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
            self.state = 97
            self.match(PrigogineParser.T__3)
            self.state = 98
            self.match(PrigogineParser.ID)
            self.state = 99 
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
            self.state = 101
            self.match(PrigogineParser.T__4)
            self.state = 102
            self.match(PrigogineParser.ID)
            self.state = 103 
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitparamsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.InitparamsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(PrigogineParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_initparams

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterInitparams(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitInitparams(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitInitparams(self)
            else:
                return visitor.visitChildren(self)




    def initparams(self):

        localctx = PrigogineParser.InitparamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_initparams)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(PrigogineParser.T__5)
            self.state = 106
            self.match(PrigogineParser.ID)
            self.state = 107 
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
        self.enterRule(localctx, 10, self.RULE_initstates)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(PrigogineParser.T__6)
            self.state = 110 
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
        self.enterRule(localctx, 12, self.RULE_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(PrigogineParser.T__7)
            self.state = 113
            self.match(PrigogineParser.ID)
            self.state = 114
            self.match(PrigogineParser.INT)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__1:
                self.state = 115 
                self.createblock()
                self.state = 120
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
        self.enterRule(localctx, 14, self.RULE_createblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(PrigogineParser.T__1)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__4) | (1 << PrigogineParser.T__5) | (1 << PrigogineParser.T__6))) != 0):
                self.state = 122 
                self.createline()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
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


        def initparams(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.InitparamsContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.InitparamsContext,i)


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
        self.enterRule(localctx, 16, self.RULE_createline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 133
                    token = self._input.LA(1)
                    if token in [PrigogineParser.T__4]:
                        self.state = 130 
                        self.initvars()

                    elif token in [PrigogineParser.T__6]:
                        self.state = 131 
                        self.initstates()

                    elif token in [PrigogineParser.T__5]:
                        self.state = 132 
                        self.initparams()

                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 135 
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
        self.enterRule(localctx, 18, self.RULE_runmodel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(PrigogineParser.T__8)
            self.state = 138
            self.match(PrigogineParser.INT)
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
        self.enterRule(localctx, 20, self.RULE_finalise)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(PrigogineParser.T__9)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__1:
                self.state = 146 
                self.codeblock()
                self.state = 151
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
        self.enterRule(localctx, 22, self.RULE_parameterlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(PrigogineParser.T__10)
            self.state = 153
            self.match(PrigogineParser.T__1)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 154 
                self.parameter()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
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
        self.enterRule(localctx, 24, self.RULE_variablelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(PrigogineParser.T__11)
            self.state = 163
            self.match(PrigogineParser.T__1)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 164 
                self.variable()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
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
        self.enterRule(localctx, 26, self.RULE_listcomp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(PrigogineParser.T__1)
            self.state = 173 
            self.expression(0)
            self.state = 174
            self.match(PrigogineParser.T__12)
            self.state = 175
            self.match(PrigogineParser.ID)
            self.state = 176
            self.match(PrigogineParser.T__13)
            self.state = 177 
            self.expression(0)
            self.state = 178
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
        self.enterRule(localctx, 28, self.RULE_listdef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(PrigogineParser.T__1)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 184
                token = self._input.LA(1)
                if token in [PrigogineParser.ID]:
                    self.state = 181
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                    self.state = 182 
                    self.number()

                elif token in [PrigogineParser.STRING]:
                    self.state = 183 
                    self.string()

                else:
                    raise NoViableAltException(self)

                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__14:
                    self.state = 186
                    self.match(PrigogineParser.T__14)
                    self.state = 190
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 187
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 188 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 189 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 196
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
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
        self.enterRule(localctx, 30, self.RULE_tupledef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(PrigogineParser.T__15)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 208
                token = self._input.LA(1)
                if token in [PrigogineParser.ID]:
                    self.state = 205
                    self.match(PrigogineParser.ID)

                elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                    self.state = 206 
                    self.number()

                elif token in [PrigogineParser.STRING]:
                    self.state = 207 
                    self.string()

                else:
                    raise NoViableAltException(self)

                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__14:
                    self.state = 210
                    self.match(PrigogineParser.T__14)
                    self.state = 214
                    token = self._input.LA(1)
                    if token in [PrigogineParser.ID]:
                        self.state = 211
                        self.match(PrigogineParser.ID)

                    elif token in [PrigogineParser.INT, PrigogineParser.FLOAT]:
                        self.state = 212 
                        self.number()

                    elif token in [PrigogineParser.STRING]:
                        self.state = 213 
                        self.string()

                    else:
                        raise NoViableAltException(self)

                    self.state = 220
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 226
            self.match(PrigogineParser.T__16)
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
        self.enterRule(localctx, 32, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
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
        self.enterRule(localctx, 34, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
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
        self.enterRule(localctx, 36, self.RULE_timeindex)
        self._la = 0 # Token type
        try:
            self.state = 243
            token = self._input.LA(1)
            if token in [PrigogineParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(PrigogineParser.T__1)
                self.state = 233
                self.match(PrigogineParser.T__17)
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.ADD or _la==PrigogineParser.SUB:
                    self.state = 234
                    _la = self._input.LA(1)
                    if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 235
                    self.match(PrigogineParser.INT)
                    self.state = 240
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 241
                self.match(PrigogineParser.T__2)

            elif token in [PrigogineParser.T__18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(PrigogineParser.T__18)

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
        self.enterRule(localctx, 38, self.RULE_timevar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(PrigogineParser.T__17)
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
        self.enterRule(localctx, 40, self.RULE_dictindex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(PrigogineParser.T__1)
            self.state = 248 
            self.string()
            self.state = 249
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
        self.enterRule(localctx, 42, self.RULE_statedef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(PrigogineParser.T__19)
            self.state = 252
            self.match(PrigogineParser.ID)
            self.state = 253
            self.match(PrigogineParser.T__1)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__20:
                self.state = 254 
                self.transition()
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__22:
                self.state = 260 
                self.update()
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
        self.enterRule(localctx, 44, self.RULE_transition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(PrigogineParser.T__20)
            self.state = 269
            self.match(PrigogineParser.ID)
            self.state = 270
            self.match(PrigogineParser.T__21)
            self.state = 271 
            self.conditional()
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__1:
                self.state = 272 
                self.codeblock()
                self.state = 277
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
        self.enterRule(localctx, 46, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(PrigogineParser.T__22)
            self.state = 279
            self.match(PrigogineParser.ID)
            self.state = 282
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 280 
                self.codeline()
                pass

            elif la_ == 2:
                self.state = 281 
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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 285
                self.match(PrigogineParser.T__24)
                self.state = 286 
                self.expression(11)
                pass

            elif la_ == 2:
                self.state = 287 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 288
                self.match(PrigogineParser.T__24)
                self.state = 289 
                self.string()
                pass

            elif la_ == 4:
                self.state = 290 
                self.listdef()
                pass

            elif la_ == 5:
                self.state = 291 
                self.tupledef()
                pass

            elif la_ == 6:
                self.state = 292 
                self.string()
                pass

            elif la_ == 7:
                self.state = 293 
                self.number()
                pass

            elif la_ == 8:
                self.state = 294 
                self.func()
                pass

            elif la_ == 9:
                self.state = 295 
                self.listcomp()
                pass

            elif la_ == 10:
                self.state = 296
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 11:
                self.state = 297 
                self.timevar()
                pass

            elif la_ == 12:
                self.state = 298 
                self.lparen()
                self.state = 299 
                self.expression(0)
                self.state = 300 
                self.rparen()
                pass

            elif la_ == 13:
                self.state = 302
                self.match(PrigogineParser.T__25)
                self.state = 303
                self.match(PrigogineParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 321
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 306
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 307
                        self.match(PrigogineParser.T__23)
                        self.state = 308 
                        self.expression(18)
                        pass

                    elif la_ == 2:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 309
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 310
                        self.match(PrigogineParser.POWER)
                        self.state = 311 
                        self.expression(17)
                        pass

                    elif la_ == 3:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 312
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 313
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.MUL or _la==PrigogineParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 314 
                        self.expression(16)
                        pass

                    elif la_ == 4:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 315
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 316
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 317 
                        self.expression(15)
                        pass

                    elif la_ == 5:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 318
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 319
                        localctx.op = self.match(PrigogineParser.PIPE)
                        self.state = 320 
                        self.expression(14)
                        pass

             
                self.state = 325
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
        self.enterRule(localctx, 50, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(PrigogineParser.ID)
            self.state = 327
            self.match(PrigogineParser.T__26)
            self.state = 328 
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
        self.enterRule(localctx, 52, self.RULE_codeblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(PrigogineParser.T__1)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__15) | (1 << PrigogineParser.T__17) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.T__25) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 331 
                self.codeline()
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 337
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
        self.enterRule(localctx, 54, self.RULE_codeline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339 
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
        self.enterRule(localctx, 56, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
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
        self.enterRule(localctx, 58, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343 
            self.expression(0)
            self.state = 344
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__27) | (1 << PrigogineParser.T__28) | (1 << PrigogineParser.T__29) | (1 << PrigogineParser.T__30) | (1 << PrigogineParser.T__31) | (1 << PrigogineParser.T__32))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            self.consume()
            self.state = 345 
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
        self.enterRule(localctx, 60, self.RULE_lparen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(PrigogineParser.T__15)
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
            self.state = 349
            self.match(PrigogineParser.T__16)
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
        self.enterRule(localctx, 64, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(PrigogineParser.ID)
            self.state = 352
            self.match(PrigogineParser.T__15)
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__15) | (1 << PrigogineParser.T__17) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.T__25) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 353 
                self.expression(0)
                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__14:
                    self.state = 354
                    self.match(PrigogineParser.T__14)
                    self.state = 355 
                    self.expression(0)
                    self.state = 360
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 366
            self.match(PrigogineParser.T__16)
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
        self.enterRule(localctx, 66, self.RULE_argument)
        try:
            self.state = 371
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368 
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 370 
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
        self.enterRule(localctx, 68, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
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
                return self.precpred(self._ctx, 17)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 13)
         



