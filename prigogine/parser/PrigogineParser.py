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
        buf.write(u"*\u00e8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\3\2\6\2\62\n\2\r\2\16\2\63\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\7\3;\n\3\f\3\16\3>\13\3\3\3\3\3\3\4\3\4\3\4\7\4E\n\4")
        buf.write(u"\f\4\16\4H\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\7\b^\n\b\f")
        buf.write(u"\b\16\ba\13\b\3\b\3\b\5\be\n\b\3\t\3\t\3\n\3\n\3\n\3")
        buf.write(u"\n\3\13\3\13\3\13\3\13\7\13q\n\13\f\13\16\13t\13\13\3")
        buf.write(u"\13\7\13w\n\13\f\13\16\13z\13\13\3\13\3\13\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\7\f\u0083\n\f\f\f\16\f\u0086\13\f\3\r\3\r")
        buf.write(u"\3\r\5\r\u008b\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5")
        buf.write(u"\16\u009e\n\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u00af\n\16\f")
        buf.write(u"\16\16\16\u00b2\13\16\3\17\3\17\5\17\u00b6\n\17\3\17")
        buf.write(u"\3\17\3\17\3\20\3\20\7\20\u00bd\n\20\f\20\16\20\u00c0")
        buf.write(u"\13\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3")
        buf.write(u"\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26\7\26")
        buf.write(u"\u00d5\n\26\f\26\16\26\u00d8\13\26\7\26\u00da\n\26\f")
        buf.write(u"\26\16\26\u00dd\13\26\3\26\3\26\3\27\3\27\3\27\5\27\u00e4")
        buf.write(u"\n\27\3\30\3\30\3\30\2\3\32\31\2\4\6\b\n\f\16\20\22\24")
        buf.write(u"\26\30\32\34\36 \"$&(*,.\2\6\3\2$%\3\2\"#\3\2\22\27\3")
        buf.write(u"\2\36\37\u00ee\2\61\3\2\2\2\4\65\3\2\2\2\6A\3\2\2\2\b")
        buf.write(u"K\3\2\2\2\nS\3\2\2\2\fU\3\2\2\2\16d\3\2\2\2\20f\3\2\2")
        buf.write(u"\2\22h\3\2\2\2\24l\3\2\2\2\26}\3\2\2\2\30\u0087\3\2\2")
        buf.write(u"\2\32\u009d\3\2\2\2\34\u00b5\3\2\2\2\36\u00ba\3\2\2\2")
        buf.write(u" \u00c3\3\2\2\2\"\u00c5\3\2\2\2$\u00c7\3\2\2\2&\u00cb")
        buf.write(u"\3\2\2\2(\u00cd\3\2\2\2*\u00cf\3\2\2\2,\u00e3\3\2\2\2")
        buf.write(u".\u00e5\3\2\2\2\60\62\5\4\3\2\61\60\3\2\2\2\62\63\3\2")
        buf.write(u"\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\3\3\2\2\2\65\66\7")
        buf.write(u"\3\2\2\66\67\5\"\22\2\678\7\4\2\28<\5\6\4\29;\5\24\13")
        buf.write(u"\2:9\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=?\3\2\2\2")
        buf.write(u"><\3\2\2\2?@\7\5\2\2@\5\3\2\2\2AB\7\6\2\2BF\7\4\2\2C")
        buf.write(u"E\5\n\6\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2GI\3")
        buf.write(u"\2\2\2HF\3\2\2\2IJ\7\5\2\2J\7\3\2\2\2KL\7\4\2\2LM\5\32")
        buf.write(u"\16\2MN\7\7\2\2NO\7 \2\2OP\7\b\2\2PQ\5\32\16\2QR\7\5")
        buf.write(u"\2\2R\t\3\2\2\2ST\5\"\22\2T\13\3\2\2\2UV\7\6\2\2VW\5")
        buf.write(u"\22\n\2WX\5\16\b\2X\r\3\2\2\2YZ\7\4\2\2Z_\7\t\2\2[\\")
        buf.write(u"\t\2\2\2\\^\7\36\2\2][\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`")
        buf.write(u"\3\2\2\2`b\3\2\2\2a_\3\2\2\2be\7\5\2\2ce\7\n\2\2dY\3")
        buf.write(u"\2\2\2dc\3\2\2\2e\17\3\2\2\2fg\7\t\2\2g\21\3\2\2\2hi")
        buf.write(u"\7\4\2\2ij\5\"\22\2jk\7\5\2\2k\23\3\2\2\2lm\7\13\2\2")
        buf.write(u"mn\5\"\22\2nr\7\4\2\2oq\5\26\f\2po\3\2\2\2qt\3\2\2\2")
        buf.write(u"rp\3\2\2\2rs\3\2\2\2sx\3\2\2\2tr\3\2\2\2uw\5\30\r\2v")
        buf.write(u"u\3\2\2\2wz\3\2\2\2xv\3\2\2\2xy\3\2\2\2y{\3\2\2\2zx\3")
        buf.write(u"\2\2\2{|\7\5\2\2|\25\3\2\2\2}~\7\f\2\2~\177\5\"\22\2")
        buf.write(u"\177\u0080\7\r\2\2\u0080\u0084\5$\23\2\u0081\u0083\5")
        buf.write(u"\36\20\2\u0082\u0081\3\2\2\2\u0083\u0086\3\2\2\2\u0084")
        buf.write(u"\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085\27\3\2\2\2\u0086")
        buf.write(u"\u0084\3\2\2\2\u0087\u008a\7\16\2\2\u0088\u008b\5 \21")
        buf.write(u"\2\u0089\u008b\5\36\20\2\u008a\u0088\3\2\2\2\u008a\u0089")
        buf.write(u"\3\2\2\2\u008b\31\3\2\2\2\u008c\u008d\b\16\1\2\u008d")
        buf.write(u"\u008e\7\20\2\2\u008e\u009e\5\32\16\13\u008f\u009e\5")
        buf.write(u"\34\17\2\u0090\u0091\7\20\2\2\u0091\u009e\5\"\22\2\u0092")
        buf.write(u"\u009e\5\"\22\2\u0093\u009e\5.\30\2\u0094\u009e\5\f\7")
        buf.write(u"\2\u0095\u009e\5*\26\2\u0096\u009e\5\b\5\2\u0097\u009e")
        buf.write(u"\7 \2\2\u0098\u009e\5\20\t\2\u0099\u009a\5&\24\2\u009a")
        buf.write(u"\u009b\5\32\16\2\u009b\u009c\5(\25\2\u009c\u009e\3\2")
        buf.write(u"\2\2\u009d\u008c\3\2\2\2\u009d\u008f\3\2\2\2\u009d\u0090")
        buf.write(u"\3\2\2\2\u009d\u0092\3\2\2\2\u009d\u0093\3\2\2\2\u009d")
        buf.write(u"\u0094\3\2\2\2\u009d\u0095\3\2\2\2\u009d\u0096\3\2\2")
        buf.write(u"\2\u009d\u0097\3\2\2\2\u009d\u0098\3\2\2\2\u009d\u0099")
        buf.write(u"\3\2\2\2\u009e\u00b0\3\2\2\2\u009f\u00a0\f\21\2\2\u00a0")
        buf.write(u"\u00a1\7\17\2\2\u00a1\u00af\5\32\16\22\u00a2\u00a3\f")
        buf.write(u"\20\2\2\u00a3\u00a4\7\'\2\2\u00a4\u00af\5\32\16\21\u00a5")
        buf.write(u"\u00a6\f\17\2\2\u00a6\u00a7\t\3\2\2\u00a7\u00af\5\32")
        buf.write(u"\16\20\u00a8\u00a9\f\16\2\2\u00a9\u00aa\t\2\2\2\u00aa")
        buf.write(u"\u00af\5\32\16\17\u00ab\u00ac\f\r\2\2\u00ac\u00ad\7&")
        buf.write(u"\2\2\u00ad\u00af\5\32\16\16\u00ae\u009f\3\2\2\2\u00ae")
        buf.write(u"\u00a2\3\2\2\2\u00ae\u00a5\3\2\2\2\u00ae\u00a8\3\2\2")
        buf.write(u"\2\u00ae\u00ab\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae")
        buf.write(u"\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\33\3\2\2\2\u00b2\u00b0")
        buf.write(u"\3\2\2\2\u00b3\u00b6\7 \2\2\u00b4\u00b6\5\f\7\2\u00b5")
        buf.write(u"\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\u00b7\3\2\2")
        buf.write(u"\2\u00b7\u00b8\7\21\2\2\u00b8\u00b9\5\32\16\2\u00b9\35")
        buf.write(u"\3\2\2\2\u00ba\u00be\7\4\2\2\u00bb\u00bd\5 \21\2\u00bc")
        buf.write(u"\u00bb\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2")
        buf.write(u"\2\u00be\u00bf\3\2\2\2\u00bf\u00c1\3\2\2\2\u00c0\u00be")
        buf.write(u"\3\2\2\2\u00c1\u00c2\7\5\2\2\u00c2\37\3\2\2\2\u00c3\u00c4")
        buf.write(u"\5\32\16\2\u00c4!\3\2\2\2\u00c5\u00c6\7(\2\2\u00c6#\3")
        buf.write(u"\2\2\2\u00c7\u00c8\5\32\16\2\u00c8\u00c9\t\4\2\2\u00c9")
        buf.write(u"\u00ca\5\32\16\2\u00ca%\3\2\2\2\u00cb\u00cc\7\30\2\2")
        buf.write(u"\u00cc\'\3\2\2\2\u00cd\u00ce\7\31\2\2\u00ce)\3\2\2\2")
        buf.write(u"\u00cf\u00d0\7 \2\2\u00d0\u00db\7\30\2\2\u00d1\u00d6")
        buf.write(u"\5\32\16\2\u00d2\u00d3\7\32\2\2\u00d3\u00d5\5\32\16\2")
        buf.write(u"\u00d4\u00d2\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4")
        buf.write(u"\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8")
        buf.write(u"\u00d6\3\2\2\2\u00d9\u00d1\3\2\2\2\u00da\u00dd\3\2\2")
        buf.write(u"\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00de")
        buf.write(u"\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00df\7\31\2\2\u00df")
        buf.write(u"+\3\2\2\2\u00e0\u00e4\5.\30\2\u00e1\u00e4\7 \2\2\u00e2")
        buf.write(u"\u00e4\5*\26\2\u00e3\u00e0\3\2\2\2\u00e3\u00e1\3\2\2")
        buf.write(u"\2\u00e3\u00e2\3\2\2\2\u00e4-\3\2\2\2\u00e5\u00e6\t\5")
        buf.write(u"\2\2\u00e6/\3\2\2\2\23\63<F_drx\u0084\u008a\u009d\u00ae")
        buf.write(u"\u00b0\u00b5\u00be\u00d6\u00db\u00e3")
        return buf.getvalue()
		

class PrigogineParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'population'", u"'['", u"']'", u"'attributes'", 
                     u"'for'", u"'in'", u"'t'", u"'[:]'", u"'state'", u"'transition to'", 
                     u"'if'", u"'action'", u"'.'", u"'print'", u"'='", u"'<'", 
                     u"'>'", u"'>='", u"'<='", u"'=='", u"'!='", u"'('", 
                     u"')'", u"','", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'*'", u"'/'", u"'+'", u"'-'", u"'|'", u"'^'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
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
    RULE_attributelist = 2
    RULE_listcomp = 3
    RULE_attribute = 4
    RULE_attrsget = 5
    RULE_timeindex = 6
    RULE_timevar = 7
    RULE_dictindex = 8
    RULE_statedef = 9
    RULE_transition = 10
    RULE_action = 11
    RULE_expression = 12
    RULE_assignment = 13
    RULE_codeblock = 14
    RULE_codeline = 15
    RULE_string = 16
    RULE_conditional = 17
    RULE_lparen = 18
    RULE_rparen = 19
    RULE_func = 20
    RULE_argument = 21
    RULE_number = 22

    ruleNames =  [ u"filestart", u"population", u"attributelist", u"listcomp", 
                   u"attribute", u"attrsget", u"timeindex", u"timevar", 
                   u"dictindex", u"statedef", u"transition", u"action", 
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
    LineComment=25
    NEWLINE=26
    ML_COMMENT=27
    INT=28
    FLOAT=29
    ID=30
    WS=31
    MUL=32
    DIV=33
    ADD=34
    SUB=35
    PIPE=36
    POWER=37
    STRING=38
    ESC=39
    SPACE=40

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
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46 
                self.population()
                self.state = 49 
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
            self.state = 51
            self.match(PrigogineParser.T__0)
            self.state = 52 
            self.string()
            self.state = 53
            self.match(PrigogineParser.T__1)
            self.state = 54 
            self.attributelist()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__8:
                self.state = 55 
                self.statedef()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(PrigogineParser.T__2)
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
        self.enterRule(localctx, 4, self.RULE_attributelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(PrigogineParser.T__3)
            self.state = 64
            self.match(PrigogineParser.T__1)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.STRING:
                self.state = 65 
                self.attribute()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
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
        self.enterRule(localctx, 6, self.RULE_listcomp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(PrigogineParser.T__1)
            self.state = 74 
            self.expression(0)
            self.state = 75
            self.match(PrigogineParser.T__4)
            self.state = 76
            self.match(PrigogineParser.ID)
            self.state = 77
            self.match(PrigogineParser.T__5)
            self.state = 78 
            self.expression(0)
            self.state = 79
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
        self.enterRule(localctx, 8, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81 
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
        self.enterRule(localctx, 10, self.RULE_attrsget)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(PrigogineParser.T__3)
            self.state = 84 
            self.dictindex()
            self.state = 85 
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
        self.enterRule(localctx, 12, self.RULE_timeindex)
        self._la = 0 # Token type
        try:
            self.state = 98
            token = self._input.LA(1)
            if token in [PrigogineParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(PrigogineParser.T__1)
                self.state = 88
                self.match(PrigogineParser.T__6)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.ADD or _la==PrigogineParser.SUB:
                    self.state = 89
                    _la = self._input.LA(1)
                    if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 90
                    self.match(PrigogineParser.INT)
                    self.state = 95
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 96
                self.match(PrigogineParser.T__2)

            elif token in [PrigogineParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(PrigogineParser.T__7)

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
        self.enterRule(localctx, 14, self.RULE_timevar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(PrigogineParser.T__6)
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
        self.enterRule(localctx, 16, self.RULE_dictindex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(PrigogineParser.T__1)
            self.state = 103 
            self.string()
            self.state = 104
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
        self.enterRule(localctx, 18, self.RULE_statedef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(PrigogineParser.T__8)
            self.state = 107 
            self.string()
            self.state = 108
            self.match(PrigogineParser.T__1)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__9:
                self.state = 109 
                self.transition()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__11:
                self.state = 115 
                self.action()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
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
        self.enterRule(localctx, 20, self.RULE_transition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(PrigogineParser.T__9)
            self.state = 124 
            self.string()
            self.state = 125
            self.match(PrigogineParser.T__10)
            self.state = 126 
            self.conditional()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__1:
                self.state = 127 
                self.codeblock()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 22, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(PrigogineParser.T__11)
            self.state = 136
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 134 
                self.codeline()
                pass

            elif la_ == 2:
                self.state = 135 
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 139
                self.match(PrigogineParser.T__13)
                self.state = 140 
                self.expression(9)
                pass

            elif la_ == 2:
                self.state = 141 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 142
                self.match(PrigogineParser.T__13)
                self.state = 143 
                self.string()
                pass

            elif la_ == 4:
                self.state = 144 
                self.string()
                pass

            elif la_ == 5:
                self.state = 145 
                self.number()
                pass

            elif la_ == 6:
                self.state = 146 
                self.attrsget()
                pass

            elif la_ == 7:
                self.state = 147 
                self.func()
                pass

            elif la_ == 8:
                self.state = 148 
                self.listcomp()
                pass

            elif la_ == 9:
                self.state = 149
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 10:
                self.state = 150 
                self.timevar()
                pass

            elif la_ == 11:
                self.state = 151 
                self.lparen()
                self.state = 152 
                self.expression(0)
                self.state = 153 
                self.rparen()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 172
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 157
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 158
                        self.match(PrigogineParser.T__12)
                        self.state = 159 
                        self.expression(16)
                        pass

                    elif la_ == 2:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 160
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 161
                        self.match(PrigogineParser.POWER)
                        self.state = 162 
                        self.expression(15)
                        pass

                    elif la_ == 3:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 163
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 164
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.MUL or _la==PrigogineParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 165 
                        self.expression(14)
                        pass

                    elif la_ == 4:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 166
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 167
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 168 
                        self.expression(13)
                        pass

                    elif la_ == 5:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 169
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 170
                        localctx.op = self.match(PrigogineParser.PIPE)
                        self.state = 171 
                        self.expression(12)
                        pass

             
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            token = self._input.LA(1)
            if token in [PrigogineParser.ID]:
                self.state = 177
                self.match(PrigogineParser.ID)

            elif token in [PrigogineParser.T__3]:
                self.state = 178 
                self.attrsget()

            else:
                raise NoViableAltException(self)

            self.state = 181
            self.match(PrigogineParser.T__14)
            self.state = 182 
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
        self.enterRule(localctx, 28, self.RULE_codeblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(PrigogineParser.T__1)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__3) | (1 << PrigogineParser.T__6) | (1 << PrigogineParser.T__13) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 185 
                self.codeline()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
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
        self.enterRule(localctx, 30, self.RULE_codeline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193 
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
        self.enterRule(localctx, 32, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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
        self.enterRule(localctx, 34, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197 
            self.expression(0)
            self.state = 198
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__15) | (1 << PrigogineParser.T__16) | (1 << PrigogineParser.T__17) | (1 << PrigogineParser.T__18) | (1 << PrigogineParser.T__19) | (1 << PrigogineParser.T__20))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            self.consume()
            self.state = 199 
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
        self.enterRule(localctx, 36, self.RULE_lparen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(PrigogineParser.T__21)
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
        self.enterRule(localctx, 38, self.RULE_rparen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(PrigogineParser.T__22)
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
        self.enterRule(localctx, 40, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(PrigogineParser.ID)
            self.state = 206
            self.match(PrigogineParser.T__21)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__1) | (1 << PrigogineParser.T__3) | (1 << PrigogineParser.T__6) | (1 << PrigogineParser.T__13) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 207 
                self.expression(0)
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__23:
                    self.state = 208
                    self.match(PrigogineParser.T__23)
                    self.state = 209 
                    self.expression(0)
                    self.state = 214
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 220
            self.match(PrigogineParser.T__22)
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
        self.enterRule(localctx, 42, self.RULE_argument)
        try:
            self.state = 225
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222 
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 224 
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
        self.enterRule(localctx, 44, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
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
        self._predicates[12] = self.expression_sempred
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
         



