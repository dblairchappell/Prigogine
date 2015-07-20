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
        buf.write(u",\u00f2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\3\2\6\2\64\n\2\r\2\16\2\65\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\7\3>\n\3\f\3\16\3A\13\3\3\3\3\3\3\4\3")
        buf.write(u"\4\3\4\7\4H\n\4\f\4\16\4K\13\4\3\4\3\4\3\5\3\5\3\5\7")
        buf.write(u"\5R\n\5\f\5\16\5U\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\7\ti\n\t\f")
        buf.write(u"\t\16\tl\13\t\3\t\3\t\5\tp\n\t\3\n\3\n\3\13\3\13\3\13")
        buf.write(u"\3\13\3\f\3\f\3\f\3\f\7\f|\n\f\f\f\16\f\177\13\f\3\f")
        buf.write(u"\7\f\u0082\n\f\f\f\16\f\u0085\13\f\3\f\3\f\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\7\r\u008e\n\r\f\r\16\r\u0091\13\r\3\16\3\16")
        buf.write(u"\3\16\3\16\5\16\u0097\n\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\5\17\u00ab\n\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17")
        buf.write(u"\u00bc\n\17\f\17\16\17\u00bf\13\17\3\20\3\20\3\20\3\20")
        buf.write(u"\3\21\3\21\7\21\u00c7\n\21\f\21\16\21\u00ca\13\21\3\21")
        buf.write(u"\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3")
        buf.write(u"\25\3\26\3\26\3\27\3\27\3\27\3\27\3\27\7\27\u00df\n\27")
        buf.write(u"\f\27\16\27\u00e2\13\27\7\27\u00e4\n\27\f\27\16\27\u00e7")
        buf.write(u"\13\27\3\27\3\27\3\30\3\30\3\30\5\30\u00ee\n\30\3\31")
        buf.write(u"\3\31\3\31\2\3\34\32\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write(u"\34\36 \"$&(*,.\60\2\6\3\2&\'\3\2$%\3\2\24\31\3\2 !\u00f7")
        buf.write(u"\2\63\3\2\2\2\4\67\3\2\2\2\6D\3\2\2\2\bN\3\2\2\2\nX\3")
        buf.write(u"\2\2\2\f`\3\2\2\2\16b\3\2\2\2\20o\3\2\2\2\22q\3\2\2\2")
        buf.write(u"\24s\3\2\2\2\26w\3\2\2\2\30\u0088\3\2\2\2\32\u0092\3")
        buf.write(u"\2\2\2\34\u00aa\3\2\2\2\36\u00c0\3\2\2\2 \u00c4\3\2\2")
        buf.write(u"\2\"\u00cd\3\2\2\2$\u00cf\3\2\2\2&\u00d1\3\2\2\2(\u00d5")
        buf.write(u"\3\2\2\2*\u00d7\3\2\2\2,\u00d9\3\2\2\2.\u00ed\3\2\2\2")
        buf.write(u"\60\u00ef\3\2\2\2\62\64\5\4\3\2\63\62\3\2\2\2\64\65\3")
        buf.write(u"\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\3\3\2\2\2\678\7")
        buf.write(u"\3\2\289\5$\23\29:\7\4\2\2:;\5\6\4\2;?\5\b\5\2<>\5\26")
        buf.write(u"\f\2=<\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@B\3\2\2")
        buf.write(u"\2A?\3\2\2\2BC\7\5\2\2C\5\3\2\2\2DE\7\6\2\2EI\7\4\2\2")
        buf.write(u"FH\5\16\b\2GF\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J")
        buf.write(u"L\3\2\2\2KI\3\2\2\2LM\7\5\2\2M\7\3\2\2\2NO\7\7\2\2OS")
        buf.write(u"\7\4\2\2PR\5\f\7\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3")
        buf.write(u"\2\2\2TV\3\2\2\2US\3\2\2\2VW\7\5\2\2W\t\3\2\2\2XY\7\4")
        buf.write(u"\2\2YZ\5\34\17\2Z[\7\b\2\2[\\\7\"\2\2\\]\7\t\2\2]^\5")
        buf.write(u"\34\17\2^_\7\5\2\2_\13\3\2\2\2`a\5$\23\2a\r\3\2\2\2b")
        buf.write(u"c\5$\23\2c\17\3\2\2\2de\7\4\2\2ej\7\n\2\2fg\t\2\2\2g")
        buf.write(u"i\7 \2\2hf\3\2\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2\2km\3")
        buf.write(u"\2\2\2lj\3\2\2\2mp\7\5\2\2np\7\13\2\2od\3\2\2\2on\3\2")
        buf.write(u"\2\2p\21\3\2\2\2qr\7\n\2\2r\23\3\2\2\2st\7\4\2\2tu\5")
        buf.write(u"$\23\2uv\7\5\2\2v\25\3\2\2\2wx\7\f\2\2xy\5$\23\2y}\7")
        buf.write(u"\4\2\2z|\5\30\r\2{z\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~")
        buf.write(u"\3\2\2\2~\u0083\3\2\2\2\177}\3\2\2\2\u0080\u0082\5\32")
        buf.write(u"\16\2\u0081\u0080\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081")
        buf.write(u"\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0086\3\2\2\2\u0085")
        buf.write(u"\u0083\3\2\2\2\u0086\u0087\7\5\2\2\u0087\27\3\2\2\2\u0088")
        buf.write(u"\u0089\7\r\2\2\u0089\u008a\5$\23\2\u008a\u008b\7\16\2")
        buf.write(u"\2\u008b\u008f\5&\24\2\u008c\u008e\5 \21\2\u008d\u008c")
        buf.write(u"\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f")
        buf.write(u"\u0090\3\2\2\2\u0090\31\3\2\2\2\u0091\u008f\3\2\2\2\u0092")
        buf.write(u"\u0093\7\17\2\2\u0093\u0096\5$\23\2\u0094\u0097\5\"\22")
        buf.write(u"\2\u0095\u0097\5 \21\2\u0096\u0094\3\2\2\2\u0096\u0095")
        buf.write(u"\3\2\2\2\u0097\33\3\2\2\2\u0098\u0099\b\17\1\2\u0099")
        buf.write(u"\u009a\7\21\2\2\u009a\u00ab\5\34\17\13\u009b\u00ab\5")
        buf.write(u"\36\20\2\u009c\u009d\7\21\2\2\u009d\u00ab\5$\23\2\u009e")
        buf.write(u"\u00ab\5$\23\2\u009f\u00ab\5\60\31\2\u00a0\u00ab\5,\27")
        buf.write(u"\2\u00a1\u00ab\5\n\6\2\u00a2\u00ab\7\"\2\2\u00a3\u00ab")
        buf.write(u"\5\22\n\2\u00a4\u00a5\5(\25\2\u00a5\u00a6\5\34\17\2\u00a6")
        buf.write(u"\u00a7\5*\26\2\u00a7\u00ab\3\2\2\2\u00a8\u00a9\7\22\2")
        buf.write(u"\2\u00a9\u00ab\7\"\2\2\u00aa\u0098\3\2\2\2\u00aa\u009b")
        buf.write(u"\3\2\2\2\u00aa\u009c\3\2\2\2\u00aa\u009e\3\2\2\2\u00aa")
        buf.write(u"\u009f\3\2\2\2\u00aa\u00a0\3\2\2\2\u00aa\u00a1\3\2\2")
        buf.write(u"\2\u00aa\u00a2\3\2\2\2\u00aa\u00a3\3\2\2\2\u00aa\u00a4")
        buf.write(u"\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00bd\3\2\2\2\u00ac")
        buf.write(u"\u00ad\f\21\2\2\u00ad\u00ae\7\20\2\2\u00ae\u00bc\5\34")
        buf.write(u"\17\22\u00af\u00b0\f\20\2\2\u00b0\u00b1\7)\2\2\u00b1")
        buf.write(u"\u00bc\5\34\17\21\u00b2\u00b3\f\17\2\2\u00b3\u00b4\t")
        buf.write(u"\3\2\2\u00b4\u00bc\5\34\17\20\u00b5\u00b6\f\16\2\2\u00b6")
        buf.write(u"\u00b7\t\2\2\2\u00b7\u00bc\5\34\17\17\u00b8\u00b9\f\r")
        buf.write(u"\2\2\u00b9\u00ba\7(\2\2\u00ba\u00bc\5\34\17\16\u00bb")
        buf.write(u"\u00ac\3\2\2\2\u00bb\u00af\3\2\2\2\u00bb\u00b2\3\2\2")
        buf.write(u"\2\u00bb\u00b5\3\2\2\2\u00bb\u00b8\3\2\2\2\u00bc\u00bf")
        buf.write(u"\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write(u"\35\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c1\7\"\2\2\u00c1")
        buf.write(u"\u00c2\7\23\2\2\u00c2\u00c3\5\34\17\2\u00c3\37\3\2\2")
        buf.write(u"\2\u00c4\u00c8\7\4\2\2\u00c5\u00c7\5\"\22\2\u00c6\u00c5")
        buf.write(u"\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8")
        buf.write(u"\u00c9\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00c8\3\2\2")
        buf.write(u"\2\u00cb\u00cc\7\5\2\2\u00cc!\3\2\2\2\u00cd\u00ce\5\34")
        buf.write(u"\17\2\u00ce#\3\2\2\2\u00cf\u00d0\7*\2\2\u00d0%\3\2\2")
        buf.write(u"\2\u00d1\u00d2\5\34\17\2\u00d2\u00d3\t\4\2\2\u00d3\u00d4")
        buf.write(u"\5\34\17\2\u00d4\'\3\2\2\2\u00d5\u00d6\7\32\2\2\u00d6")
        buf.write(u")\3\2\2\2\u00d7\u00d8\7\33\2\2\u00d8+\3\2\2\2\u00d9\u00da")
        buf.write(u"\7\"\2\2\u00da\u00e5\7\32\2\2\u00db\u00e0\5\34\17\2\u00dc")
        buf.write(u"\u00dd\7\34\2\2\u00dd\u00df\5\34\17\2\u00de\u00dc\3\2")
        buf.write(u"\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1")
        buf.write(u"\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3")
        buf.write(u"\u00db\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2")
        buf.write(u"\2\u00e5\u00e6\3\2\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00e5")
        buf.write(u"\3\2\2\2\u00e8\u00e9\7\33\2\2\u00e9-\3\2\2\2\u00ea\u00ee")
        buf.write(u"\5\60\31\2\u00eb\u00ee\7\"\2\2\u00ec\u00ee\5,\27\2\u00ed")
        buf.write(u"\u00ea\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ec\3\2\2")
        buf.write(u"\2\u00ee/\3\2\2\2\u00ef\u00f0\t\5\2\2\u00f0\61\3\2\2")
        buf.write(u"\2\23\65?ISjo}\u0083\u008f\u0096\u00aa\u00bb\u00bd\u00c8")
        buf.write(u"\u00e0\u00e5\u00ed")
        return buf.getvalue()
		

class PrigogineParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'population'", u"'['", u"']'", u"'parameters'", 
                     u"'variables'", u"'for'", u"'in'", u"'t'", u"'[:]'", 
                     u"'state'", u"'transition'", u"'where'", u"'update'", 
                     u"'.'", u"'print'", u"'return'", u"'='", u"'<'", u"'>'", 
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
    RULE_population = 1
    RULE_parameterlist = 2
    RULE_variablelist = 3
    RULE_listcomp = 4
    RULE_variable = 5
    RULE_parameter = 6
    RULE_timeindex = 7
    RULE_timevar = 8
    RULE_dictindex = 9
    RULE_statedef = 10
    RULE_transition = 11
    RULE_update = 12
    RULE_expression = 13
    RULE_assignment = 14
    RULE_codeblock = 15
    RULE_codeline = 16
    RULE_string = 17
    RULE_conditional = 18
    RULE_lparen = 19
    RULE_rparen = 20
    RULE_func = 21
    RULE_argument = 22
    RULE_number = 23

    ruleNames =  [ u"filestart", u"population", u"parameterlist", u"variablelist", 
                   u"listcomp", u"variable", u"parameter", u"timeindex", 
                   u"timevar", u"dictindex", u"statedef", u"transition", 
                   u"update", u"expression", u"assignment", u"codeblock", 
                   u"codeline", u"string", u"conditional", u"lparen", u"rparen", 
                   u"func", u"argument", u"number" ]

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

        def population(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PrigogineParser.PopulationContext)
            else:
                return self.getTypedRuleContext(PrigogineParser.PopulationContext,i)


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
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48 
                self.population()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrigogineParser.T__0):
                    break

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
            self.state = 53
            self.match(PrigogineParser.T__0)
            self.state = 54 
            self.string()
            self.state = 55
            self.match(PrigogineParser.T__1)
            self.state = 56 
            self.parameterlist()
            self.state = 57 
            self.variablelist()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__9:
                self.state = 58 
                self.statedef()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
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
        self.enterRule(localctx, 4, self.RULE_parameterlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(PrigogineParser.T__3)
            self.state = 67
            self.match(PrigogineParser.T__1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.STRING:
                self.state = 68 
                self.parameter()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
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
        self.enterRule(localctx, 6, self.RULE_variablelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(PrigogineParser.T__4)
            self.state = 77
            self.match(PrigogineParser.T__1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.STRING:
                self.state = 78 
                self.variable()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
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
        self.enterRule(localctx, 8, self.RULE_listcomp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(PrigogineParser.T__1)
            self.state = 87 
            self.expression(0)
            self.state = 88
            self.match(PrigogineParser.T__5)
            self.state = 89
            self.match(PrigogineParser.ID)
            self.state = 90
            self.match(PrigogineParser.T__6)
            self.state = 91 
            self.expression(0)
            self.state = 92
            self.match(PrigogineParser.T__2)
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

        def string(self):
            return self.getTypedRuleContext(PrigogineParser.StringContext,0)


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
        self.enterRule(localctx, 10, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94 
            self.string()
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

        def string(self):
            return self.getTypedRuleContext(PrigogineParser.StringContext,0)


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
        self.enterRule(localctx, 12, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96 
            self.string()
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
        self.enterRule(localctx, 14, self.RULE_timeindex)
        self._la = 0 # Token type
        try:
            self.state = 109
            token = self._input.LA(1)
            if token in [PrigogineParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(PrigogineParser.T__1)
                self.state = 99
                self.match(PrigogineParser.T__7)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.ADD or _la==PrigogineParser.SUB:
                    self.state = 100
                    _la = self._input.LA(1)
                    if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 101
                    self.match(PrigogineParser.INT)
                    self.state = 106
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 107
                self.match(PrigogineParser.T__2)

            elif token in [PrigogineParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.match(PrigogineParser.T__8)

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
        self.enterRule(localctx, 16, self.RULE_timevar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(PrigogineParser.T__7)
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
        self.enterRule(localctx, 18, self.RULE_dictindex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(PrigogineParser.T__1)
            self.state = 114 
            self.string()
            self.state = 115
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
        self.enterRule(localctx, 20, self.RULE_statedef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(PrigogineParser.T__9)
            self.state = 118 
            self.string()
            self.state = 119
            self.match(PrigogineParser.T__1)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__10:
                self.state = 120 
                self.transition()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__12:
                self.state = 126 
                self.update()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
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
        self.enterRule(localctx, 22, self.RULE_transition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(PrigogineParser.T__10)
            self.state = 135 
            self.string()
            self.state = 136
            self.match(PrigogineParser.T__11)
            self.state = 137 
            self.conditional()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__1:
                self.state = 138 
                self.codeblock()
                self.state = 143
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

        def string(self):
            return self.getTypedRuleContext(PrigogineParser.StringContext,0)


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
        self.enterRule(localctx, 24, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(PrigogineParser.T__12)
            self.state = 145 
            self.string()
            self.state = 148
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 146 
                self.codeline()
                pass

            elif la_ == 2:
                self.state = 147 
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 151
                self.match(PrigogineParser.T__14)
                self.state = 152 
                self.expression(9)
                pass

            elif la_ == 2:
                self.state = 153 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 154
                self.match(PrigogineParser.T__14)
                self.state = 155 
                self.string()
                pass

            elif la_ == 4:
                self.state = 156 
                self.string()
                pass

            elif la_ == 5:
                self.state = 157 
                self.number()
                pass

            elif la_ == 6:
                self.state = 158 
                self.func()
                pass

            elif la_ == 7:
                self.state = 159 
                self.listcomp()
                pass

            elif la_ == 8:
                self.state = 160
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 9:
                self.state = 161 
                self.timevar()
                pass

            elif la_ == 10:
                self.state = 162 
                self.lparen()
                self.state = 163 
                self.expression(0)
                self.state = 164 
                self.rparen()
                pass

            elif la_ == 11:
                self.state = 166
                self.match(PrigogineParser.T__15)
                self.state = 167
                self.match(PrigogineParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 185
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 170
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 171
                        self.match(PrigogineParser.T__13)
                        self.state = 172 
                        self.expression(16)
                        pass

                    elif la_ == 2:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 173
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 174
                        self.match(PrigogineParser.POWER)
                        self.state = 175 
                        self.expression(15)
                        pass

                    elif la_ == 3:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 176
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 177
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.MUL or _la==PrigogineParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 178 
                        self.expression(14)
                        pass

                    elif la_ == 4:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 179
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 180
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 181 
                        self.expression(13)
                        pass

                    elif la_ == 5:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 182
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 183
                        localctx.op = self.match(PrigogineParser.PIPE)
                        self.state = 184 
                        self.expression(12)
                        pass

             
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(PrigogineParser.ID)
            self.state = 191
            self.match(PrigogineParser.T__16)
            self.state = 192 
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
        self.enterRule(localctx, 30, self.RULE_codeblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(PrigogineParser.T__1)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__7) | (1 << PrigogineParser.T__14) | (1 << PrigogineParser.T__15) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 195 
                self.codeline()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
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
        self.enterRule(localctx, 32, self.RULE_codeline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203 
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
        self.enterRule(localctx, 34, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
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
        self.enterRule(localctx, 36, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207 
            self.expression(0)
            self.state = 208
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__17) | (1 << PrigogineParser.T__18) | (1 << PrigogineParser.T__19) | (1 << PrigogineParser.T__20) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.T__22))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            self.consume()
            self.state = 209 
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
        self.enterRule(localctx, 38, self.RULE_lparen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
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
        self.enterRule(localctx, 40, self.RULE_rparen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
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
        self.enterRule(localctx, 42, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(PrigogineParser.ID)
            self.state = 216
            self.match(PrigogineParser.T__23)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__7) | (1 << PrigogineParser.T__14) | (1 << PrigogineParser.T__15) | (1 << PrigogineParser.T__23) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 217 
                self.expression(0)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__25:
                    self.state = 218
                    self.match(PrigogineParser.T__25)
                    self.state = 219 
                    self.expression(0)
                    self.state = 224
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 230
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
        self.enterRule(localctx, 44, self.RULE_argument)
        try:
            self.state = 235
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232 
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 234 
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
        self.enterRule(localctx, 46, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
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
        self._predicates[13] = self.expression_sempred
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
         



