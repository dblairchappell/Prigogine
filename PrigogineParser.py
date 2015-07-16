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
        buf.write(u",\u010e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\3\2\6\2\66\n\2\r\2\16\2\67")
        buf.write(u"\3\2\7\2;\n\2\f\2\16\2>\13\2\3\3\3\3\3\3\3\3\6\3D\n\3")
        buf.write(u"\r\3\16\3E\3\3\3\3\3\4\3\4\3\4\3\4\3\4\7\4O\n\4\f\4\16")
        buf.write(u"\4R\13\4\3\4\3\4\3\5\3\5\3\5\7\5Y\n\5\f\5\16\5\\\13\5")
        buf.write(u"\3\6\3\6\3\6\7\6a\n\6\f\6\16\6d\13\6\3\6\3\6\3\7\3\7")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\n")
        buf.write(u"\3\n\3\n\3\n\7\nz\n\n\f\n\16\n}\13\n\3\n\3\n\5\n\u0081")
        buf.write(u"\n\n\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\7\r\u008d")
        buf.write(u"\n\r\f\r\16\r\u0090\13\r\3\r\7\r\u0093\n\r\f\r\16\r\u0096")
        buf.write(u"\13\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\7\16\u00a5\n\16\f\16\16\16\u00a8\13\16")
        buf.write(u"\3\16\3\16\5\16\u00ac\n\16\3\17\3\17\3\17\5\17\u00b1")
        buf.write(u"\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00c4\n\20")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\7\20\u00d5\n\20\f\20\16\20\u00d8")
        buf.write(u"\13\20\3\21\3\21\5\21\u00dc\n\21\3\21\3\21\3\21\3\22")
        buf.write(u"\3\22\7\22\u00e3\n\22\f\22\16\22\u00e6\13\22\3\22\3\22")
        buf.write(u"\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3")
        buf.write(u"\27\3\27\3\30\3\30\3\30\3\30\3\30\7\30\u00fb\n\30\f\30")
        buf.write(u"\16\30\u00fe\13\30\7\30\u0100\n\30\f\30\16\30\u0103\13")
        buf.write(u"\30\3\30\3\30\3\31\3\31\3\31\5\31\u010a\n\31\3\32\3\32")
        buf.write(u"\3\32\2\3\36\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(u" \"$&(*,.\60\62\2\6\3\2&\'\3\2$%\3\2\24\31\3\2 !\u0116")
        buf.write(u"\2\65\3\2\2\2\4?\3\2\2\2\6I\3\2\2\2\bU\3\2\2\2\n]\3\2")
        buf.write(u"\2\2\fg\3\2\2\2\16o\3\2\2\2\20q\3\2\2\2\22\u0080\3\2")
        buf.write(u"\2\2\24\u0082\3\2\2\2\26\u0084\3\2\2\2\30\u0088\3\2\2")
        buf.write(u"\2\32\u00ab\3\2\2\2\34\u00ad\3\2\2\2\36\u00c3\3\2\2\2")
        buf.write(u" \u00db\3\2\2\2\"\u00e0\3\2\2\2$\u00e9\3\2\2\2&\u00eb")
        buf.write(u"\3\2\2\2(\u00ed\3\2\2\2*\u00f1\3\2\2\2,\u00f3\3\2\2\2")
        buf.write(u".\u00f5\3\2\2\2\60\u0109\3\2\2\2\62\u010b\3\2\2\2\64")
        buf.write(u"\66\5\4\3\2\65\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2")
        buf.write(u"\678\3\2\2\28<\3\2\2\29;\5\b\5\2:9\3\2\2\2;>\3\2\2\2")
        buf.write(u"<:\3\2\2\2<=\3\2\2\2=\3\3\2\2\2><\3\2\2\2?@\7\3\2\2@")
        buf.write(u"A\5&\24\2AC\7\4\2\2BD\5\6\4\2CB\3\2\2\2DE\3\2\2\2EC\3")
        buf.write(u"\2\2\2EF\3\2\2\2FG\3\2\2\2GH\7\5\2\2H\5\3\2\2\2IJ\7\6")
        buf.write(u"\2\2JK\5&\24\2KL\7\4\2\2LP\5\n\6\2MO\5\30\r\2NM\3\2\2")
        buf.write(u"\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QS\3\2\2\2RP\3\2\2\2")
        buf.write(u"ST\7\5\2\2T\7\3\2\2\2UV\7\7\2\2VZ\5&\24\2WY\5\"\22\2")
        buf.write(u"XW\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\t\3\2\2\2")
        buf.write(u"\\Z\3\2\2\2]^\7\b\2\2^b\7\4\2\2_a\5\16\b\2`_\3\2\2\2")
        buf.write(u"ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2ce\3\2\2\2db\3\2\2\2ef")
        buf.write(u"\7\5\2\2f\13\3\2\2\2gh\7\4\2\2hi\5\36\20\2ij\7\t\2\2")
        buf.write(u"jk\7\"\2\2kl\7\n\2\2lm\5\36\20\2mn\7\5\2\2n\r\3\2\2\2")
        buf.write(u"op\5&\24\2p\17\3\2\2\2qr\7\b\2\2rs\5\26\f\2st\5\22\n")
        buf.write(u"\2t\21\3\2\2\2uv\7\4\2\2v{\7\13\2\2wx\t\2\2\2xz\7 \2")
        buf.write(u"\2yw\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|~\3\2\2\2")
        buf.write(u"}{\3\2\2\2~\u0081\7\5\2\2\177\u0081\7\f\2\2\u0080u\3")
        buf.write(u"\2\2\2\u0080\177\3\2\2\2\u0081\23\3\2\2\2\u0082\u0083")
        buf.write(u"\7\13\2\2\u0083\25\3\2\2\2\u0084\u0085\7\4\2\2\u0085")
        buf.write(u"\u0086\5&\24\2\u0086\u0087\7\5\2\2\u0087\27\3\2\2\2\u0088")
        buf.write(u"\u0089\7\r\2\2\u0089\u008a\5&\24\2\u008a\u008e\7\4\2")
        buf.write(u"\2\u008b\u008d\5\32\16\2\u008c\u008b\3\2\2\2\u008d\u0090")
        buf.write(u"\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write(u"\u0094\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0093\5\34\17")
        buf.write(u"\2\u0092\u0091\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092")
        buf.write(u"\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097\3\2\2\2\u0096")
        buf.write(u"\u0094\3\2\2\2\u0097\u0098\7\5\2\2\u0098\31\3\2\2\2\u0099")
        buf.write(u"\u009a\7\16\2\2\u009a\u009b\5&\24\2\u009b\u009c\7\17")
        buf.write(u"\2\2\u009c\u009d\5(\25\2\u009d\u00ac\3\2\2\2\u009e\u009f")
        buf.write(u"\7\16\2\2\u009f\u00a0\5&\24\2\u00a0\u00a1\7\17\2\2\u00a1")
        buf.write(u"\u00a2\5(\25\2\u00a2\u00a6\7\4\2\2\u00a3\u00a5\5\34\17")
        buf.write(u"\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4")
        buf.write(u"\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a9\3\2\2\2\u00a8")
        buf.write(u"\u00a6\3\2\2\2\u00a9\u00aa\7\5\2\2\u00aa\u00ac\3\2\2")
        buf.write(u"\2\u00ab\u0099\3\2\2\2\u00ab\u009e\3\2\2\2\u00ac\33\3")
        buf.write(u"\2\2\2\u00ad\u00b0\7\20\2\2\u00ae\u00b1\5$\23\2\u00af")
        buf.write(u"\u00b1\5\"\22\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3\2\2")
        buf.write(u"\2\u00b1\35\3\2\2\2\u00b2\u00b3\b\20\1\2\u00b3\u00b4")
        buf.write(u"\7\22\2\2\u00b4\u00c4\5\36\20\13\u00b5\u00c4\5 \21\2")
        buf.write(u"\u00b6\u00b7\7\22\2\2\u00b7\u00c4\5&\24\2\u00b8\u00c4")
        buf.write(u"\5&\24\2\u00b9\u00c4\5\62\32\2\u00ba\u00c4\5\20\t\2\u00bb")
        buf.write(u"\u00c4\5.\30\2\u00bc\u00c4\5\f\7\2\u00bd\u00c4\7\"\2")
        buf.write(u"\2\u00be\u00c4\5\24\13\2\u00bf\u00c0\5*\26\2\u00c0\u00c1")
        buf.write(u"\5\36\20\2\u00c1\u00c2\5,\27\2\u00c2\u00c4\3\2\2\2\u00c3")
        buf.write(u"\u00b2\3\2\2\2\u00c3\u00b5\3\2\2\2\u00c3\u00b6\3\2\2")
        buf.write(u"\2\u00c3\u00b8\3\2\2\2\u00c3\u00b9\3\2\2\2\u00c3\u00ba")
        buf.write(u"\3\2\2\2\u00c3\u00bb\3\2\2\2\u00c3\u00bc\3\2\2\2\u00c3")
        buf.write(u"\u00bd\3\2\2\2\u00c3\u00be\3\2\2\2\u00c3\u00bf\3\2\2")
        buf.write(u"\2\u00c4\u00d6\3\2\2\2\u00c5\u00c6\f\21\2\2\u00c6\u00c7")
        buf.write(u"\7\21\2\2\u00c7\u00d5\5\36\20\22\u00c8\u00c9\f\20\2\2")
        buf.write(u"\u00c9\u00ca\7)\2\2\u00ca\u00d5\5\36\20\21\u00cb\u00cc")
        buf.write(u"\f\17\2\2\u00cc\u00cd\t\3\2\2\u00cd\u00d5\5\36\20\20")
        buf.write(u"\u00ce\u00cf\f\16\2\2\u00cf\u00d0\t\2\2\2\u00d0\u00d5")
        buf.write(u"\5\36\20\17\u00d1\u00d2\f\r\2\2\u00d2\u00d3\7(\2\2\u00d3")
        buf.write(u"\u00d5\5\36\20\16\u00d4\u00c5\3\2\2\2\u00d4\u00c8\3\2")
        buf.write(u"\2\2\u00d4\u00cb\3\2\2\2\u00d4\u00ce\3\2\2\2\u00d4\u00d1")
        buf.write(u"\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6")
        buf.write(u"\u00d7\3\2\2\2\u00d7\37\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9")
        buf.write(u"\u00dc\7\"\2\2\u00da\u00dc\5\20\t\2\u00db\u00d9\3\2\2")
        buf.write(u"\2\u00db\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de")
        buf.write(u"\7\23\2\2\u00de\u00df\5\36\20\2\u00df!\3\2\2\2\u00e0")
        buf.write(u"\u00e4\7\4\2\2\u00e1\u00e3\5$\23\2\u00e2\u00e1\3\2\2")
        buf.write(u"\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5")
        buf.write(u"\3\2\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7")
        buf.write(u"\u00e8\7\5\2\2\u00e8#\3\2\2\2\u00e9\u00ea\5\36\20\2\u00ea")
        buf.write(u"%\3\2\2\2\u00eb\u00ec\7*\2\2\u00ec\'\3\2\2\2\u00ed\u00ee")
        buf.write(u"\5\36\20\2\u00ee\u00ef\t\4\2\2\u00ef\u00f0\5\36\20\2")
        buf.write(u"\u00f0)\3\2\2\2\u00f1\u00f2\7\32\2\2\u00f2+\3\2\2\2\u00f3")
        buf.write(u"\u00f4\7\33\2\2\u00f4-\3\2\2\2\u00f5\u00f6\7\"\2\2\u00f6")
        buf.write(u"\u0101\7\32\2\2\u00f7\u00fc\5\36\20\2\u00f8\u00f9\7\34")
        buf.write(u"\2\2\u00f9\u00fb\5\36\20\2\u00fa\u00f8\3\2\2\2\u00fb")
        buf.write(u"\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2")
        buf.write(u"\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u00f7")
        buf.write(u"\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101")
        buf.write(u"\u0102\3\2\2\2\u0102\u0104\3\2\2\2\u0103\u0101\3\2\2")
        buf.write(u"\2\u0104\u0105\7\33\2\2\u0105/\3\2\2\2\u0106\u010a\5")
        buf.write(u"\62\32\2\u0107\u010a\7\"\2\2\u0108\u010a\5.\30\2\u0109")
        buf.write(u"\u0106\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2")
        buf.write(u"\2\u010a\61\3\2\2\2\u010b\u010c\t\5\2\2\u010c\63\3\2")
        buf.write(u"\2\2\27\67<EPZb{\u0080\u008e\u0094\u00a6\u00ab\u00b0")
        buf.write(u"\u00c3\u00d4\u00d6\u00db\u00e4\u00fc\u0101\u0109")
        return buf.getvalue()
		

class PrigogineParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'model'", u"'['", u"']'", u"'population'", 
                     u"'experiment'", u"'attributes'", u"'for'", u"'in'", 
                     u"'t'", u"'[:]'", u"'state'", u"'transition to'", u"'if'", 
                     u"'action'", u"'.'", u"'print'", u"'='", u"'<'", u"'>'", 
                     u"'>='", u"'<='", u"'=='", u"'!='", u"'('", u"')'", 
                     u"','", u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'*'", u"'/'", 
                     u"'+'", u"'-'", u"'|'", u"'^'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"LineComment", 
                      u"NEWLINE", u"ML_COMMENT", u"INT", u"FLOAT", u"ID", 
                      u"WS", u"MUL", u"DIV", u"ADD", u"SUB", u"PIPE", u"POWER", 
                      u"STRING", u"ESC", u"SPACE" ]

    RULE_filestart = 0
    RULE_modeldef = 1
    RULE_population = 2
    RULE_experiment = 3
    RULE_attributelist = 4
    RULE_listcomp = 5
    RULE_attribute = 6
    RULE_attrsget = 7
    RULE_timeindex = 8
    RULE_timevar = 9
    RULE_dictindex = 10
    RULE_statedef = 11
    RULE_transition = 12
    RULE_action = 13
    RULE_expression = 14
    RULE_assignment = 15
    RULE_codeblock = 16
    RULE_codeline = 17
    RULE_string = 18
    RULE_conditional = 19
    RULE_lparen = 20
    RULE_rparen = 21
    RULE_func = 22
    RULE_argument = 23
    RULE_number = 24

    ruleNames =  [ u"filestart", u"modeldef", u"population", u"experiment", 
                   u"attributelist", u"listcomp", u"attribute", u"attrsget", 
                   u"timeindex", u"timevar", u"dictindex", u"statedef", 
                   u"transition", u"action", u"expression", u"assignment", 
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
    LineComment=27
    NEWLINE=28
    ML_COMMENT=29
    INT=30
    FLOAT=31
    ID=32
    WS=33
    MUL=34
    DIV=35
    ADD=36
    SUB=37
    PIPE=38
    POWER=39
    STRING=40
    ESC=41
    SPACE=42

    def __init__(self, input):
        super(PrigogineParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class FilestartContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.FilestartContext, self).__init__(parent, invokingState)
            self.parser = parser

        def modeldef(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ModeldefContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ModeldefContext,i)


        def experiment(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ExperimentContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ExperimentContext,i)


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
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50 
                self.modeldef()
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrigogineParser.T__0):
                    break

            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__4:
                self.state = 55 
                self.experiment()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModeldefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.ModeldefContext, self).__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(PrigogineParser.StringContext,0)


        def population(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.PopulationContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.PopulationContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_modeldef

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterModeldef(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitModeldef(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitModeldef(self)
            else:
                return visitor.visitChildren(self)




    def modeldef(self):

        localctx = PrigogineParser.ModeldefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_modeldef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(PrigogineParser.T__0)
            self.state = 62 
            self.string()
            self.state = 63
            self.match(PrigogineParser.T__1)
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64 
                self.population()
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrigogineParser.T__3):
                    break

            self.state = 69
            self.match(PrigogineParser.T__2)
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

        def string(self):
            return self.getTypedRuleContext(PrigogineParser.StringContext,0)


        def attributelist(self):
            return self.getTypedRuleContext(PrigogineParser.AttributelistContext,0)


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
        self.enterRule(localctx, 4, self.RULE_population)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(PrigogineParser.T__3)
            self.state = 72 
            self.string()
            self.state = 73
            self.match(PrigogineParser.T__1)
            self.state = 74 
            self.attributelist()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__10:
                self.state = 75 
                self.statedef()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExperimentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.ExperimentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(PrigogineParser.StringContext,0)


        def codeblock(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.CodeblockContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.CodeblockContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_experiment

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterExperiment(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitExperiment(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitExperiment(self)
            else:
                return visitor.visitChildren(self)




    def experiment(self):

        localctx = PrigogineParser.ExperimentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_experiment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(PrigogineParser.T__4)
            self.state = 84 
            self.string()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__1:
                self.state = 85 
                self.codeblock()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributelistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.AttributelistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.AttributeContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.AttributeContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_attributelist

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterAttributelist(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitAttributelist(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitAttributelist(self)
            else:
                return visitor.visitChildren(self)




    def attributelist(self):

        localctx = PrigogineParser.AttributelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attributelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(PrigogineParser.T__5)
            self.state = 92
            self.match(PrigogineParser.T__1)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.STRING:
                self.state = 93 
                self.attribute()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
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
        self.enterRule(localctx, 10, self.RULE_listcomp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(PrigogineParser.T__1)
            self.state = 102 
            self.expression(0)
            self.state = 103
            self.match(PrigogineParser.T__6)
            self.state = 104
            self.match(PrigogineParser.ID)
            self.state = 105
            self.match(PrigogineParser.T__7)
            self.state = 106 
            self.expression(0)
            self.state = 107
            self.match(PrigogineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.AttributeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(PrigogineParser.StringContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_attribute

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterAttribute(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitAttribute(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = PrigogineParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109 
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttrsgetContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.AttrsgetContext, self).__init__(parent, invokingState)
            self.parser = parser

        def dictindex(self):
            return self.getTypedRuleContext(PrigogineParser.DictindexContext,0)


        def timeindex(self):
            return self.getTypedRuleContext(PrigogineParser.TimeindexContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_attrsget

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterAttrsget(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitAttrsget(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitAttrsget(self)
            else:
                return visitor.visitChildren(self)




    def attrsget(self):

        localctx = PrigogineParser.AttrsgetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attrsget)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(PrigogineParser.T__5)
            self.state = 112 
            self.dictindex()
            self.state = 113 
            self.timeindex()
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
        self.enterRule(localctx, 16, self.RULE_timeindex)
        self._la = 0 # Token type
        try:
            self.state = 126
            token = self._input.LA(1)
            if token in [PrigogineParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(PrigogineParser.T__1)
                self.state = 116
                self.match(PrigogineParser.T__8)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.ADD or _la==PrigogineParser.SUB:
                    self.state = 117
                    _la = self._input.LA(1)
                    if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 118
                    self.match(PrigogineParser.INT)
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 124
                self.match(PrigogineParser.T__2)

            elif token in [PrigogineParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(PrigogineParser.T__9)

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
        self.enterRule(localctx, 18, self.RULE_timevar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(PrigogineParser.T__8)
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
        self.enterRule(localctx, 20, self.RULE_dictindex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(PrigogineParser.T__1)
            self.state = 131 
            self.string()
            self.state = 132
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

        def string(self):
            return self.getTypedRuleContext(PrigogineParser.StringContext,0)


        def transition(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.TransitionContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.TransitionContext,i)


        def action(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ActionContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ActionContext,i)


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
        self.enterRule(localctx, 22, self.RULE_statedef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(PrigogineParser.T__10)
            self.state = 135 
            self.string()
            self.state = 136
            self.match(PrigogineParser.T__1)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__11:
                self.state = 137 
                self.transition()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__13:
                self.state = 143 
                self.action()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
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

        def string(self):
            return self.getTypedRuleContext(PrigogineParser.StringContext,0)


        def conditional(self):
            return self.getTypedRuleContext(PrigogineParser.ConditionalContext,0)


        def action(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.ActionContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.ActionContext,i)


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
        self.enterRule(localctx, 24, self.RULE_transition)
        self._la = 0 # Token type
        try:
            self.state = 169
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(PrigogineParser.T__11)
                self.state = 152 
                self.string()
                self.state = 153
                self.match(PrigogineParser.T__12)
                self.state = 154 
                self.conditional()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(PrigogineParser.T__11)
                self.state = 157 
                self.string()
                self.state = 158
                self.match(PrigogineParser.T__12)
                self.state = 159 
                self.conditional()
                self.state = 160
                self.match(PrigogineParser.T__1)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__13:
                    self.state = 161 
                    self.action()
                    self.state = 166
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 167
                self.match(PrigogineParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.ActionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def codeline(self):
            return self.getTypedRuleContext(PrigogineParser.CodelineContext,0)


        def codeblock(self):
            return self.getTypedRuleContext(PrigogineParser.CodeblockContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_action

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterAction(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitAction(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = PrigogineParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(PrigogineParser.T__13)
            self.state = 174
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 172 
                self.codeline()
                pass

            elif la_ == 2:
                self.state = 173 
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


        def number(self):
            return self.getTypedRuleContext(PrigogineParser.NumberContext,0)


        def attrsget(self):
            return self.getTypedRuleContext(PrigogineParser.AttrsgetContext,0)


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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 177
                self.match(PrigogineParser.T__15)
                self.state = 178 
                self.expression(9)
                pass

            elif la_ == 2:
                self.state = 179 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 180
                self.match(PrigogineParser.T__15)
                self.state = 181 
                self.string()
                pass

            elif la_ == 4:
                self.state = 182 
                self.string()
                pass

            elif la_ == 5:
                self.state = 183 
                self.number()
                pass

            elif la_ == 6:
                self.state = 184 
                self.attrsget()
                pass

            elif la_ == 7:
                self.state = 185 
                self.func()
                pass

            elif la_ == 8:
                self.state = 186 
                self.listcomp()
                pass

            elif la_ == 9:
                self.state = 187
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 10:
                self.state = 188 
                self.timevar()
                pass

            elif la_ == 11:
                self.state = 189 
                self.lparen()
                self.state = 190 
                self.expression(0)
                self.state = 191 
                self.rparen()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 210
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 195
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 196
                        self.match(PrigogineParser.T__14)
                        self.state = 197 
                        self.expression(16)
                        pass

                    elif la_ == 2:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 198
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 199
                        self.match(PrigogineParser.POWER)
                        self.state = 200 
                        self.expression(15)
                        pass

                    elif la_ == 3:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 201
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 202
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.MUL or _la==PrigogineParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 203 
                        self.expression(14)
                        pass

                    elif la_ == 4:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 204
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 205
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 206 
                        self.expression(13)
                        pass

                    elif la_ == 5:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 207
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 208
                        localctx.op = self.match(PrigogineParser.PIPE)
                        self.state = 209 
                        self.expression(12)
                        pass

             
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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

        def expression(self):
            return self.getTypedRuleContext(PrigogineParser.ExpressionContext,0)


        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def attrsget(self):
            return self.getTypedRuleContext(PrigogineParser.AttrsgetContext,0)


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
        self.enterRule(localctx, 30, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            token = self._input.LA(1)
            if token in [PrigogineParser.ID]:
                self.state = 215
                self.match(PrigogineParser.ID)

            elif token in [PrigogineParser.T__5]:
                self.state = 216 
                self.attrsget()

            else:
                raise NoViableAltException(self)

            self.state = 219
            self.match(PrigogineParser.T__16)
            self.state = 220 
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
        self.enterRule(localctx, 32, self.RULE_codeblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(PrigogineParser.T__1)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__5) | (1 << PrigogineParser.T__8) | (1 << PrigogineParser.T__15) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 223 
                self.codeline()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 229
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
        self.enterRule(localctx, 34, self.RULE_codeline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231 
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
        self.enterRule(localctx, 36, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
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
        self.enterRule(localctx, 38, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235 
            self.expression(0)
            self.state = 236
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__17) | (1 << PrigogineParser.T__18) | (1 << PrigogineParser.T__19) | (1 << PrigogineParser.T__20) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.T__22))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            self.consume()
            self.state = 237 
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
        self.enterRule(localctx, 40, self.RULE_lparen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(PrigogineParser.T__23)
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
        self.enterRule(localctx, 42, self.RULE_rparen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(PrigogineParser.T__24)
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
        self.enterRule(localctx, 44, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(PrigogineParser.ID)
            self.state = 244
            self.match(PrigogineParser.T__23)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__5) | (1 << PrigogineParser.T__8) | (1 << PrigogineParser.T__15) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 245 
                self.expression(0)
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__25:
                    self.state = 246
                    self.match(PrigogineParser.T__25)
                    self.state = 247 
                    self.expression(0)
                    self.state = 252
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 258
            self.match(PrigogineParser.T__24)
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
        self.enterRule(localctx, 46, self.RULE_argument)
        try:
            self.state = 263
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260 
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 262 
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
        self.enterRule(localctx, 48, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
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
        self._predicates[14] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         



