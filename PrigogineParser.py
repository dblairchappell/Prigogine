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
        buf.write(u".\u0108\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\3\2\6\2\66\n\2\r\2\16\2\67")
        buf.write(u"\3\2\7\2;\n\2\f\2\16\2>\13\2\3\3\3\3\3\3\3\3\7\3D\n\3")
        buf.write(u"\f\3\16\3G\13\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4O\n\4\f\4")
        buf.write(u"\16\4R\13\4\3\5\3\5\3\5\3\5\5\5X\n\5\3\6\3\6\7\6\\\n")
        buf.write(u"\6\f\6\16\6_\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write(u"\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\7\nu\n\n")
        buf.write(u"\f\n\16\nx\13\n\3\n\3\n\5\n|\n\n\3\13\3\13\3\f\3\f\3")
        buf.write(u"\f\3\f\3\r\3\r\3\r\7\r\u0087\n\r\f\r\16\r\u008a\13\r")
        buf.write(u"\3\r\7\r\u008d\n\r\f\r\16\r\u0090\13\r\3\r\3\r\3\16\3")
        buf.write(u"\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u009e")
        buf.write(u"\n\16\f\16\16\16\u00a1\13\16\3\16\3\16\5\16\u00a5\n\16")
        buf.write(u"\3\17\3\17\3\17\3\17\5\17\u00ab\n\17\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\3\20\5\20\u00be\n\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\7\20\u00cf\n\20\f\20\16\20\u00d2\13\20\3\21\3\21\5\21")
        buf.write(u"\u00d6\n\21\3\21\3\21\3\21\3\22\3\22\7\22\u00dd\n\22")
        buf.write(u"\f\22\16\22\u00e0\13\22\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write(u"\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3")
        buf.write(u"\30\3\30\3\30\7\30\u00f5\n\30\f\30\16\30\u00f8\13\30")
        buf.write(u"\7\30\u00fa\n\30\f\30\16\30\u00fd\13\30\3\30\3\30\3\31")
        buf.write(u"\3\31\3\31\5\31\u0104\n\31\3\32\3\32\3\32\2\3\36\33\2")
        buf.write(u"\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write(u"\2\6\3\2()\3\2&\'\3\2\26\33\3\2\"#\u0110\2\65\3\2\2\2")
        buf.write(u"\4?\3\2\2\2\6J\3\2\2\2\bS\3\2\2\2\nY\3\2\2\2\fb\3\2\2")
        buf.write(u"\2\16j\3\2\2\2\20l\3\2\2\2\22{\3\2\2\2\24}\3\2\2\2\26")
        buf.write(u"\177\3\2\2\2\30\u0083\3\2\2\2\32\u00a4\3\2\2\2\34\u00a6")
        buf.write(u"\3\2\2\2\36\u00bd\3\2\2\2 \u00d5\3\2\2\2\"\u00da\3\2")
        buf.write(u"\2\2$\u00e3\3\2\2\2&\u00e5\3\2\2\2(\u00e7\3\2\2\2*\u00eb")
        buf.write(u"\3\2\2\2,\u00ed\3\2\2\2.\u00ef\3\2\2\2\60\u0103\3\2\2")
        buf.write(u"\2\62\u0105\3\2\2\2\64\66\5\4\3\2\65\64\3\2\2\2\66\67")
        buf.write(u"\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28<\3\2\2\29;\5\6\4")
        buf.write(u"\2:9\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\3\3\2\2\2")
        buf.write(u"><\3\2\2\2?@\7\3\2\2@A\7$\2\2AE\5\n\6\2BD\5\30\r\2CB")
        buf.write(u"\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2FH\3\2\2\2GE\3")
        buf.write(u"\2\2\2HI\7\4\2\2I\5\3\2\2\2JK\7\5\2\2KL\7$\2\2LP\7\"")
        buf.write(u"\2\2MO\5\"\22\2NM\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2")
        buf.write(u"\2Q\7\3\2\2\2RP\3\2\2\2ST\7\6\2\2TW\5\20\t\2UX\5$\23")
        buf.write(u"\2VX\5\"\22\2WU\3\2\2\2WV\3\2\2\2X\t\3\2\2\2Y]\7\7\2")
        buf.write(u"\2Z\\\5\16\b\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2")
        buf.write(u"\2^`\3\2\2\2_]\3\2\2\2`a\7\4\2\2a\13\3\2\2\2bc\7\b\2")
        buf.write(u"\2cd\5\36\20\2de\7\t\2\2ef\7$\2\2fg\7\n\2\2gh\5\36\20")
        buf.write(u"\2hi\7\13\2\2i\r\3\2\2\2jk\7$\2\2k\17\3\2\2\2lm\7\7\2")
        buf.write(u"\2mn\5\26\f\2no\5\22\n\2o\21\3\2\2\2pq\7\b\2\2qv\7\f")
        buf.write(u"\2\2rs\t\2\2\2su\7\"\2\2tr\3\2\2\2ux\3\2\2\2vt\3\2\2")
        buf.write(u"\2vw\3\2\2\2wy\3\2\2\2xv\3\2\2\2y|\7\13\2\2z|\7\r\2\2")
        buf.write(u"{p\3\2\2\2{z\3\2\2\2|\23\3\2\2\2}~\7\f\2\2~\25\3\2\2")
        buf.write(u"\2\177\u0080\7\b\2\2\u0080\u0081\5&\24\2\u0081\u0082")
        buf.write(u"\7\13\2\2\u0082\27\3\2\2\2\u0083\u0084\7\16\2\2\u0084")
        buf.write(u"\u0088\7$\2\2\u0085\u0087\5\32\16\2\u0086\u0085\3\2\2")
        buf.write(u"\2\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089")
        buf.write(u"\3\2\2\2\u0089\u008e\3\2\2\2\u008a\u0088\3\2\2\2\u008b")
        buf.write(u"\u008d\5\34\17\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2")
        buf.write(u"\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091")
        buf.write(u"\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0092\7\4\2\2\u0092")
        buf.write(u"\31\3\2\2\2\u0093\u0094\7\17\2\2\u0094\u0095\7$\2\2\u0095")
        buf.write(u"\u0096\7\20\2\2\u0096\u00a5\5(\25\2\u0097\u0098\7\17")
        buf.write(u"\2\2\u0098\u0099\7$\2\2\u0099\u009a\7\20\2\2\u009a\u009b")
        buf.write(u"\5(\25\2\u009b\u009f\7\21\2\2\u009c\u009e\5\34\17\2\u009d")
        buf.write(u"\u009c\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2")
        buf.write(u"\2\u009f\u00a0\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1\u009f")
        buf.write(u"\3\2\2\2\u00a2\u00a3\7\4\2\2\u00a3\u00a5\3\2\2\2\u00a4")
        buf.write(u"\u0093\3\2\2\2\u00a4\u0097\3\2\2\2\u00a5\33\3\2\2\2\u00a6")
        buf.write(u"\u00a7\7\22\2\2\u00a7\u00aa\7$\2\2\u00a8\u00ab\5$\23")
        buf.write(u"\2\u00a9\u00ab\5\"\22\2\u00aa\u00a8\3\2\2\2\u00aa\u00a9")
        buf.write(u"\3\2\2\2\u00ab\35\3\2\2\2\u00ac\u00ad\b\20\1\2\u00ad")
        buf.write(u"\u00ae\7\24\2\2\u00ae\u00be\5\36\20\13\u00af\u00be\5")
        buf.write(u" \21\2\u00b0\u00b1\7\24\2\2\u00b1\u00be\5&\24\2\u00b2")
        buf.write(u"\u00be\5&\24\2\u00b3\u00be\5\62\32\2\u00b4\u00be\5\20")
        buf.write(u"\t\2\u00b5\u00be\5.\30\2\u00b6\u00be\5\f\7\2\u00b7\u00be")
        buf.write(u"\7$\2\2\u00b8\u00be\5\24\13\2\u00b9\u00ba\5*\26\2\u00ba")
        buf.write(u"\u00bb\5\36\20\2\u00bb\u00bc\5,\27\2\u00bc\u00be\3\2")
        buf.write(u"\2\2\u00bd\u00ac\3\2\2\2\u00bd\u00af\3\2\2\2\u00bd\u00b0")
        buf.write(u"\3\2\2\2\u00bd\u00b2\3\2\2\2\u00bd\u00b3\3\2\2\2\u00bd")
        buf.write(u"\u00b4\3\2\2\2\u00bd\u00b5\3\2\2\2\u00bd\u00b6\3\2\2")
        buf.write(u"\2\u00bd\u00b7\3\2\2\2\u00bd\u00b8\3\2\2\2\u00bd\u00b9")
        buf.write(u"\3\2\2\2\u00be\u00d0\3\2\2\2\u00bf\u00c0\f\21\2\2\u00c0")
        buf.write(u"\u00c1\7\23\2\2\u00c1\u00cf\5\36\20\22\u00c2\u00c3\f")
        buf.write(u"\20\2\2\u00c3\u00c4\7+\2\2\u00c4\u00cf\5\36\20\21\u00c5")
        buf.write(u"\u00c6\f\17\2\2\u00c6\u00c7\t\3\2\2\u00c7\u00cf\5\36")
        buf.write(u"\20\20\u00c8\u00c9\f\16\2\2\u00c9\u00ca\t\2\2\2\u00ca")
        buf.write(u"\u00cf\5\36\20\17\u00cb\u00cc\f\r\2\2\u00cc\u00cd\7*")
        buf.write(u"\2\2\u00cd\u00cf\5\36\20\16\u00ce\u00bf\3\2\2\2\u00ce")
        buf.write(u"\u00c2\3\2\2\2\u00ce\u00c5\3\2\2\2\u00ce\u00c8\3\2\2")
        buf.write(u"\2\u00ce\u00cb\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce")
        buf.write(u"\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\37\3\2\2\2\u00d2\u00d0")
        buf.write(u"\3\2\2\2\u00d3\u00d6\7$\2\2\u00d4\u00d6\5\20\t\2\u00d5")
        buf.write(u"\u00d3\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6\u00d7\3\2\2")
        buf.write(u"\2\u00d7\u00d8\7\25\2\2\u00d8\u00d9\5\36\20\2\u00d9!")
        buf.write(u"\3\2\2\2\u00da\u00de\7\21\2\2\u00db\u00dd\5$\23\2\u00dc")
        buf.write(u"\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2")
        buf.write(u"\2\u00de\u00df\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0\u00de")
        buf.write(u"\3\2\2\2\u00e1\u00e2\7\4\2\2\u00e2#\3\2\2\2\u00e3\u00e4")
        buf.write(u"\5\36\20\2\u00e4%\3\2\2\2\u00e5\u00e6\7,\2\2\u00e6\'")
        buf.write(u"\3\2\2\2\u00e7\u00e8\5\36\20\2\u00e8\u00e9\t\4\2\2\u00e9")
        buf.write(u"\u00ea\5\36\20\2\u00ea)\3\2\2\2\u00eb\u00ec\7\34\2\2")
        buf.write(u"\u00ec+\3\2\2\2\u00ed\u00ee\7\35\2\2\u00ee-\3\2\2\2\u00ef")
        buf.write(u"\u00f0\7$\2\2\u00f0\u00fb\7\34\2\2\u00f1\u00f6\5\36\20")
        buf.write(u"\2\u00f2\u00f3\7\36\2\2\u00f3\u00f5\5\36\20\2\u00f4\u00f2")
        buf.write(u"\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6")
        buf.write(u"\u00f7\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3\2\2")
        buf.write(u"\2\u00f9\u00f1\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9")
        buf.write(u"\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fe\3\2\2\2\u00fd")
        buf.write(u"\u00fb\3\2\2\2\u00fe\u00ff\7\35\2\2\u00ff/\3\2\2\2\u0100")
        buf.write(u"\u0104\5\62\32\2\u0101\u0104\7$\2\2\u0102\u0104\5.\30")
        buf.write(u"\2\u0103\u0100\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0102")
        buf.write(u"\3\2\2\2\u0104\61\3\2\2\2\u0105\u0106\t\5\2\2\u0106\63")
        buf.write(u"\3\2\2\2\27\67<EPW]v{\u0088\u008e\u009f\u00a4\u00aa\u00bd")
        buf.write(u"\u00ce\u00d0\u00d5\u00de\u00f6\u00fb\u0103")
        return buf.getvalue()
		

class PrigogineParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'population'", u"'end'", u"'create'", 
                     u"'init'", u"'attributes'", u"'['", u"'for'", u"'in'", 
                     u"']'", u"'t'", u"'[:]'", u"'state'", u"'transition to'", 
                     u"'if'", u"'begin'", u"'update'", u"'.'", u"'print'", 
                     u"'='", u"'<'", u"'>'", u"'>='", u"'<='", u"'=='", 
                     u"'!='", u"'('", u"')'", u"','", u"<INVALID>", u"<INVALID>", 
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
                      u"<INVALID>", u"LineComment", u"NEWLINE", u"ML_COMMENT", 
                      u"INT", u"FLOAT", u"ID", u"WS", u"MUL", u"DIV", u"ADD", 
                      u"SUB", u"PIPE", u"POWER", u"STRING", u"ESC", u"SPACE" ]

    RULE_filestart = 0
    RULE_population = 1
    RULE_createpopulation = 2
    RULE_initvar = 3
    RULE_attributelist = 4
    RULE_listcomp = 5
    RULE_attribute = 6
    RULE_attrsget = 7
    RULE_timeindex = 8
    RULE_timevar = 9
    RULE_dictindex = 10
    RULE_statedef = 11
    RULE_transition = 12
    RULE_update = 13
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

    ruleNames =  [ u"filestart", u"population", u"createpopulation", u"initvar", 
                   u"attributelist", u"listcomp", u"attribute", u"attrsget", 
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
    LineComment=29
    NEWLINE=30
    ML_COMMENT=31
    INT=32
    FLOAT=33
    ID=34
    WS=35
    MUL=36
    DIV=37
    ADD=38
    SUB=39
    PIPE=40
    POWER=41
    STRING=42
    ESC=43
    SPACE=44

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


        def createpopulation(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.CreatepopulationContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.CreatepopulationContext,i)


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
                self.population()
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrigogineParser.T__0):
                    break

            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__2:
                self.state = 55 
                self.createpopulation()
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

    class PopulationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.PopulationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

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
        self.enterRule(localctx, 2, self.RULE_population)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(PrigogineParser.T__0)
            self.state = 62
            self.match(PrigogineParser.ID)
            self.state = 63 
            self.attributelist()
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__11:
                self.state = 64 
                self.statedef()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(PrigogineParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CreatepopulationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.CreatepopulationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

        def INT(self):
            return self.getToken(PrigogineParser.INT, 0)

        def codeblock(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.CodeblockContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.CodeblockContext,i)


        def getRuleIndex(self):
            return PrigogineParser.RULE_createpopulation

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterCreatepopulation(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitCreatepopulation(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitCreatepopulation(self)
            else:
                return visitor.visitChildren(self)




    def createpopulation(self):

        localctx = PrigogineParser.CreatepopulationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_createpopulation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(PrigogineParser.T__2)
            self.state = 73
            self.match(PrigogineParser.ID)
            self.state = 74
            self.match(PrigogineParser.INT)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__14:
                self.state = 75 
                self.codeblock()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitvarContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PrigogineParser.InitvarContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attrsget(self):
            return self.getTypedRuleContext(PrigogineParser.AttrsgetContext,0)


        def codeline(self):
            return self.getTypedRuleContext(PrigogineParser.CodelineContext,0)


        def codeblock(self):
            return self.getTypedRuleContext(PrigogineParser.CodeblockContext,0)


        def getRuleIndex(self):
            return PrigogineParser.RULE_initvar

        def enterRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.enterInitvar(self)

        def exitRule(self, listener):
            if isinstance( listener, PrigogineListener ):
                listener.exitInitvar(self)

        def accept(self, visitor):
            if isinstance( visitor, PrigogineVisitor ):
                return visitor.visitInitvar(self)
            else:
                return visitor.visitChildren(self)




    def initvar(self):

        localctx = PrigogineParser.InitvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_initvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(PrigogineParser.T__3)
            self.state = 82 
            self.attrsget()
            self.state = 85
            token = self._input.LA(1)
            if token in [PrigogineParser.T__4, PrigogineParser.T__5, PrigogineParser.T__9, PrigogineParser.T__17, PrigogineParser.T__25, PrigogineParser.INT, PrigogineParser.FLOAT, PrigogineParser.ID, PrigogineParser.STRING]:
                self.state = 83 
                self.codeline()

            elif token in [PrigogineParser.T__14]:
                self.state = 84 
                self.codeblock()

            else:
                raise NoViableAltException(self)

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
            self.state = 87
            self.match(PrigogineParser.T__4)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 88 
                self.attribute()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.match(PrigogineParser.T__1)
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
            self.state = 96
            self.match(PrigogineParser.T__5)
            self.state = 97 
            self.expression(0)
            self.state = 98
            self.match(PrigogineParser.T__6)
            self.state = 99
            self.match(PrigogineParser.ID)
            self.state = 100
            self.match(PrigogineParser.T__7)
            self.state = 101 
            self.expression(0)
            self.state = 102
            self.match(PrigogineParser.T__8)
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

        def ID(self):
            return self.getToken(PrigogineParser.ID, 0)

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
            self.state = 104
            self.match(PrigogineParser.ID)
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
            self.state = 106
            self.match(PrigogineParser.T__4)
            self.state = 107 
            self.dictindex()
            self.state = 108 
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
            self.state = 121
            token = self._input.LA(1)
            if token in [PrigogineParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(PrigogineParser.T__5)
                self.state = 111
                self.match(PrigogineParser.T__9)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.ADD or _la==PrigogineParser.SUB:
                    self.state = 112
                    _la = self._input.LA(1)
                    if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 113
                    self.match(PrigogineParser.INT)
                    self.state = 118
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 119
                self.match(PrigogineParser.T__8)

            elif token in [PrigogineParser.T__10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(PrigogineParser.T__10)

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
            self.state = 123
            self.match(PrigogineParser.T__9)
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
            self.state = 125
            self.match(PrigogineParser.T__5)
            self.state = 126 
            self.string()
            self.state = 127
            self.match(PrigogineParser.T__8)
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
        self.enterRule(localctx, 22, self.RULE_statedef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(PrigogineParser.T__11)
            self.state = 130
            self.match(PrigogineParser.ID)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__12:
                self.state = 131 
                self.transition()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__15:
                self.state = 137 
                self.update()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self.match(PrigogineParser.T__1)
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


        def update(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.UpdateContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.UpdateContext,i)


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
            self.state = 162
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(PrigogineParser.T__12)
                self.state = 146
                self.match(PrigogineParser.ID)
                self.state = 147
                self.match(PrigogineParser.T__13)
                self.state = 148 
                self.conditional()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(PrigogineParser.T__12)
                self.state = 150
                self.match(PrigogineParser.ID)
                self.state = 151
                self.match(PrigogineParser.T__13)
                self.state = 152 
                self.conditional()
                self.state = 153
                self.match(PrigogineParser.T__14)
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__15:
                    self.state = 154 
                    self.update()
                    self.state = 159
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 160
                self.match(PrigogineParser.T__1)
                pass


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
        self.enterRule(localctx, 26, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(PrigogineParser.T__15)
            self.state = 165
            self.match(PrigogineParser.ID)
            self.state = 168
            token = self._input.LA(1)
            if token in [PrigogineParser.T__4, PrigogineParser.T__5, PrigogineParser.T__9, PrigogineParser.T__17, PrigogineParser.T__25, PrigogineParser.INT, PrigogineParser.FLOAT, PrigogineParser.ID, PrigogineParser.STRING]:
                self.state = 166 
                self.codeline()

            elif token in [PrigogineParser.T__14]:
                self.state = 167 
                self.codeblock()

            else:
                raise NoViableAltException(self)

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
            self.state = 187
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 171
                self.match(PrigogineParser.T__17)
                self.state = 172 
                self.expression(9)
                pass

            elif la_ == 2:
                self.state = 173 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 174
                self.match(PrigogineParser.T__17)
                self.state = 175 
                self.string()
                pass

            elif la_ == 4:
                self.state = 176 
                self.string()
                pass

            elif la_ == 5:
                self.state = 177 
                self.number()
                pass

            elif la_ == 6:
                self.state = 178 
                self.attrsget()
                pass

            elif la_ == 7:
                self.state = 179 
                self.func()
                pass

            elif la_ == 8:
                self.state = 180 
                self.listcomp()
                pass

            elif la_ == 9:
                self.state = 181
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 10:
                self.state = 182 
                self.timevar()
                pass

            elif la_ == 11:
                self.state = 183 
                self.lparen()
                self.state = 184 
                self.expression(0)
                self.state = 185 
                self.rparen()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 204
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 190
                        self.match(PrigogineParser.T__16)
                        self.state = 191 
                        self.expression(16)
                        pass

                    elif la_ == 2:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 192
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 193
                        self.match(PrigogineParser.POWER)
                        self.state = 194 
                        self.expression(15)
                        pass

                    elif la_ == 3:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 195
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 196
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.MUL or _la==PrigogineParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 197 
                        self.expression(14)
                        pass

                    elif la_ == 4:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 198
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 199
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 200 
                        self.expression(13)
                        pass

                    elif la_ == 5:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 201
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 202
                        localctx.op = self.match(PrigogineParser.PIPE)
                        self.state = 203 
                        self.expression(12)
                        pass

             
                self.state = 208
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
            self.state = 211
            token = self._input.LA(1)
            if token in [PrigogineParser.ID]:
                self.state = 209
                self.match(PrigogineParser.ID)

            elif token in [PrigogineParser.T__4]:
                self.state = 210 
                self.attrsget()

            else:
                raise NoViableAltException(self)

            self.state = 213
            self.match(PrigogineParser.T__18)
            self.state = 214 
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
            self.state = 216
            self.match(PrigogineParser.T__14)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__4) | (1 << PrigogineParser.T__5) | (1 << PrigogineParser.T__9) | (1 << PrigogineParser.T__17) | (1 << PrigogineParser.T__25) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 217 
                self.codeline()
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
            self.match(PrigogineParser.T__1)
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
            self.state = 225 
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
            self.state = 227
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
            self.state = 229 
            self.expression(0)
            self.state = 230
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__19) | (1 << PrigogineParser.T__20) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.T__22) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.T__24))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            self.consume()
            self.state = 231 
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
            self.state = 233
            self.match(PrigogineParser.T__25)
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
            self.state = 235
            self.match(PrigogineParser.T__26)
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
            self.state = 237
            self.match(PrigogineParser.ID)
            self.state = 238
            self.match(PrigogineParser.T__25)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__4) | (1 << PrigogineParser.T__5) | (1 << PrigogineParser.T__9) | (1 << PrigogineParser.T__17) | (1 << PrigogineParser.T__25) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 239 
                self.expression(0)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__27:
                    self.state = 240
                    self.match(PrigogineParser.T__27)
                    self.state = 241 
                    self.expression(0)
                    self.state = 246
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 252
            self.match(PrigogineParser.T__26)
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
            self.state = 257
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254 
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 256 
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
            self.state = 259
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
         



