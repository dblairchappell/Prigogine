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
        buf.write(u"-\u00ff\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\3\2\6\2\64\n\2\r\2\16\2\65\3\2\7\29\n")
        buf.write(u"\2\f\2\16\2<\13\2\3\3\3\3\3\3\3\3\7\3B\n\3\f\3\16\3E")
        buf.write(u"\13\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4M\n\4\f\4\16\4P\13\4")
        buf.write(u"\3\5\3\5\7\5T\n\5\f\5\16\5W\13\5\3\5\3\5\3\6\3\6\3\6")
        buf.write(u"\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write(u"\3\t\3\t\7\tm\n\t\f\t\16\tp\13\t\3\t\3\t\5\tt\n\t\3\n")
        buf.write(u"\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\7\f\177\n\f\f\f")
        buf.write(u"\16\f\u0082\13\f\3\f\7\f\u0085\n\f\f\f\16\f\u0088\13")
        buf.write(u"\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7")
        buf.write(u"\r\u0096\n\r\f\r\16\r\u0099\13\r\3\r\3\r\5\r\u009d\n")
        buf.write(u"\r\3\16\3\16\3\16\5\16\u00a2\n\16\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\5\17\u00b5\n\17\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7")
        buf.write(u"\17\u00c6\n\17\f\17\16\17\u00c9\13\17\3\20\3\20\5\20")
        buf.write(u"\u00cd\n\20\3\20\3\20\3\20\3\21\3\21\7\21\u00d4\n\21")
        buf.write(u"\f\21\16\21\u00d7\13\21\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write(u"\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3")
        buf.write(u"\27\3\27\3\27\7\27\u00ec\n\27\f\27\16\27\u00ef\13\27")
        buf.write(u"\7\27\u00f1\n\27\f\27\16\27\u00f4\13\27\3\27\3\27\3\30")
        buf.write(u"\3\30\3\30\5\30\u00fb\n\30\3\31\3\31\3\31\2\3\34\32\2")
        buf.write(u"\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\2\6")
        buf.write(u"\3\2\'(\3\2%&\3\2\25\32\3\2!\"\u0107\2\63\3\2\2\2\4=")
        buf.write(u"\3\2\2\2\6H\3\2\2\2\bQ\3\2\2\2\nZ\3\2\2\2\fb\3\2\2\2")
        buf.write(u"\16d\3\2\2\2\20s\3\2\2\2\22u\3\2\2\2\24w\3\2\2\2\26{")
        buf.write(u"\3\2\2\2\30\u009c\3\2\2\2\32\u009e\3\2\2\2\34\u00b4\3")
        buf.write(u"\2\2\2\36\u00cc\3\2\2\2 \u00d1\3\2\2\2\"\u00da\3\2\2")
        buf.write(u"\2$\u00dc\3\2\2\2&\u00de\3\2\2\2(\u00e2\3\2\2\2*\u00e4")
        buf.write(u"\3\2\2\2,\u00e6\3\2\2\2.\u00fa\3\2\2\2\60\u00fc\3\2\2")
        buf.write(u"\2\62\64\5\4\3\2\63\62\3\2\2\2\64\65\3\2\2\2\65\63\3")
        buf.write(u"\2\2\2\65\66\3\2\2\2\66:\3\2\2\2\679\5\6\4\28\67\3\2")
        buf.write(u"\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\3\3\2\2\2<:\3\2\2")
        buf.write(u"\2=>\7\3\2\2>?\7#\2\2?C\5\b\5\2@B\5\26\f\2A@\3\2\2\2")
        buf.write(u"BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2DF\3\2\2\2EC\3\2\2\2FG")
        buf.write(u"\7\4\2\2G\5\3\2\2\2HI\7\5\2\2IJ\7#\2\2JN\7!\2\2KM\5 ")
        buf.write(u"\21\2LK\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\7\3\2")
        buf.write(u"\2\2PN\3\2\2\2QU\7\6\2\2RT\5\f\7\2SR\3\2\2\2TW\3\2\2")
        buf.write(u"\2US\3\2\2\2UV\3\2\2\2VX\3\2\2\2WU\3\2\2\2XY\7\4\2\2")
        buf.write(u"Y\t\3\2\2\2Z[\7\7\2\2[\\\5\34\17\2\\]\7\b\2\2]^\7#\2")
        buf.write(u"\2^_\7\t\2\2_`\5\34\17\2`a\7\n\2\2a\13\3\2\2\2bc\7#\2")
        buf.write(u"\2c\r\3\2\2\2de\7\6\2\2ef\5\24\13\2fg\5\20\t\2g\17\3")
        buf.write(u"\2\2\2hi\7\7\2\2in\7\13\2\2jk\t\2\2\2km\7!\2\2lj\3\2")
        buf.write(u"\2\2mp\3\2\2\2nl\3\2\2\2no\3\2\2\2oq\3\2\2\2pn\3\2\2")
        buf.write(u"\2qt\7\n\2\2rt\7\f\2\2sh\3\2\2\2sr\3\2\2\2t\21\3\2\2")
        buf.write(u"\2uv\7\13\2\2v\23\3\2\2\2wx\7\7\2\2xy\5$\23\2yz\7\n\2")
        buf.write(u"\2z\25\3\2\2\2{|\7\r\2\2|\u0080\7#\2\2}\177\5\30\r\2")
        buf.write(u"~}\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080\u0081")
        buf.write(u"\3\2\2\2\u0081\u0086\3\2\2\2\u0082\u0080\3\2\2\2\u0083")
        buf.write(u"\u0085\5\32\16\2\u0084\u0083\3\2\2\2\u0085\u0088\3\2")
        buf.write(u"\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0089")
        buf.write(u"\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u008a\7\4\2\2\u008a")
        buf.write(u"\27\3\2\2\2\u008b\u008c\7\16\2\2\u008c\u008d\7#\2\2\u008d")
        buf.write(u"\u008e\7\17\2\2\u008e\u009d\5&\24\2\u008f\u0090\7\16")
        buf.write(u"\2\2\u0090\u0091\7#\2\2\u0091\u0092\7\17\2\2\u0092\u0093")
        buf.write(u"\5&\24\2\u0093\u0097\7\20\2\2\u0094\u0096\5\32\16\2\u0095")
        buf.write(u"\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2")
        buf.write(u"\2\u0097\u0098\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u0097")
        buf.write(u"\3\2\2\2\u009a\u009b\7\4\2\2\u009b\u009d\3\2\2\2\u009c")
        buf.write(u"\u008b\3\2\2\2\u009c\u008f\3\2\2\2\u009d\31\3\2\2\2\u009e")
        buf.write(u"\u00a1\7\21\2\2\u009f\u00a2\5\"\22\2\u00a0\u00a2\5 \21")
        buf.write(u"\2\u00a1\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\33\3")
        buf.write(u"\2\2\2\u00a3\u00a4\b\17\1\2\u00a4\u00a5\7\23\2\2\u00a5")
        buf.write(u"\u00b5\5\34\17\13\u00a6\u00b5\5\36\20\2\u00a7\u00a8\7")
        buf.write(u"\23\2\2\u00a8\u00b5\5$\23\2\u00a9\u00b5\5$\23\2\u00aa")
        buf.write(u"\u00b5\5\60\31\2\u00ab\u00b5\5\16\b\2\u00ac\u00b5\5,")
        buf.write(u"\27\2\u00ad\u00b5\5\n\6\2\u00ae\u00b5\7#\2\2\u00af\u00b5")
        buf.write(u"\5\22\n\2\u00b0\u00b1\5(\25\2\u00b1\u00b2\5\34\17\2\u00b2")
        buf.write(u"\u00b3\5*\26\2\u00b3\u00b5\3\2\2\2\u00b4\u00a3\3\2\2")
        buf.write(u"\2\u00b4\u00a6\3\2\2\2\u00b4\u00a7\3\2\2\2\u00b4\u00a9")
        buf.write(u"\3\2\2\2\u00b4\u00aa\3\2\2\2\u00b4\u00ab\3\2\2\2\u00b4")
        buf.write(u"\u00ac\3\2\2\2\u00b4\u00ad\3\2\2\2\u00b4\u00ae\3\2\2")
        buf.write(u"\2\u00b4\u00af\3\2\2\2\u00b4\u00b0\3\2\2\2\u00b5\u00c7")
        buf.write(u"\3\2\2\2\u00b6\u00b7\f\21\2\2\u00b7\u00b8\7\22\2\2\u00b8")
        buf.write(u"\u00c6\5\34\17\22\u00b9\u00ba\f\20\2\2\u00ba\u00bb\7")
        buf.write(u"*\2\2\u00bb\u00c6\5\34\17\21\u00bc\u00bd\f\17\2\2\u00bd")
        buf.write(u"\u00be\t\3\2\2\u00be\u00c6\5\34\17\20\u00bf\u00c0\f\16")
        buf.write(u"\2\2\u00c0\u00c1\t\2\2\2\u00c1\u00c6\5\34\17\17\u00c2")
        buf.write(u"\u00c3\f\r\2\2\u00c3\u00c4\7)\2\2\u00c4\u00c6\5\34\17")
        buf.write(u"\16\u00c5\u00b6\3\2\2\2\u00c5\u00b9\3\2\2\2\u00c5\u00bc")
        buf.write(u"\3\2\2\2\u00c5\u00bf\3\2\2\2\u00c5\u00c2\3\2\2\2\u00c6")
        buf.write(u"\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2")
        buf.write(u"\2\u00c8\35\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cd\7")
        buf.write(u"#\2\2\u00cb\u00cd\5\16\b\2\u00cc\u00ca\3\2\2\2\u00cc")
        buf.write(u"\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\7\24\2")
        buf.write(u"\2\u00cf\u00d0\5\34\17\2\u00d0\37\3\2\2\2\u00d1\u00d5")
        buf.write(u"\7\20\2\2\u00d2\u00d4\5\"\22\2\u00d3\u00d2\3\2\2\2\u00d4")
        buf.write(u"\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2")
        buf.write(u"\2\u00d6\u00d8\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9")
        buf.write(u"\7\4\2\2\u00d9!\3\2\2\2\u00da\u00db\5\34\17\2\u00db#")
        buf.write(u"\3\2\2\2\u00dc\u00dd\7+\2\2\u00dd%\3\2\2\2\u00de\u00df")
        buf.write(u"\5\34\17\2\u00df\u00e0\t\4\2\2\u00e0\u00e1\5\34\17\2")
        buf.write(u"\u00e1\'\3\2\2\2\u00e2\u00e3\7\33\2\2\u00e3)\3\2\2\2")
        buf.write(u"\u00e4\u00e5\7\34\2\2\u00e5+\3\2\2\2\u00e6\u00e7\7#\2")
        buf.write(u"\2\u00e7\u00f2\7\33\2\2\u00e8\u00ed\5\34\17\2\u00e9\u00ea")
        buf.write(u"\7\35\2\2\u00ea\u00ec\5\34\17\2\u00eb\u00e9\3\2\2\2\u00ec")
        buf.write(u"\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2")
        buf.write(u"\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00e8")
        buf.write(u"\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2")
        buf.write(u"\u00f3\3\2\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00f2\3\2\2")
        buf.write(u"\2\u00f5\u00f6\7\34\2\2\u00f6-\3\2\2\2\u00f7\u00fb\5")
        buf.write(u"\60\31\2\u00f8\u00fb\7#\2\2\u00f9\u00fb\5,\27\2\u00fa")
        buf.write(u"\u00f7\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2\2")
        buf.write(u"\2\u00fb/\3\2\2\2\u00fc\u00fd\t\5\2\2\u00fd\61\3\2\2")
        buf.write(u"\2\26\65:CNUns\u0080\u0086\u0097\u009c\u00a1\u00b4\u00c5")
        buf.write(u"\u00c7\u00cc\u00d5\u00ed\u00f2\u00fa")
        return buf.getvalue()
		

class PrigogineParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'population'", u"'end'", u"'create'", 
                     u"'attributes'", u"'['", u"'for'", u"'in'", u"']'", 
                     u"'t'", u"'[:]'", u"'state'", u"'transition to'", u"'if'", 
                     u"'begin'", u"'action'", u"'.'", u"'print'", u"'='", 
                     u"'<'", u"'>'", u"'>='", u"'<='", u"'=='", u"'!='", 
                     u"'('", u"')'", u"','", u"<INVALID>", u"<INVALID>", 
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
                      u"LineComment", u"NEWLINE", u"ML_COMMENT", u"INT", 
                      u"FLOAT", u"ID", u"WS", u"MUL", u"DIV", u"ADD", u"SUB", 
                      u"PIPE", u"POWER", u"STRING", u"ESC", u"SPACE" ]

    RULE_filestart = 0
    RULE_population = 1
    RULE_createpopulation = 2
    RULE_attributelist = 3
    RULE_listcomp = 4
    RULE_attribute = 5
    RULE_attrsget = 6
    RULE_timeindex = 7
    RULE_timevar = 8
    RULE_dictindex = 9
    RULE_statedef = 10
    RULE_transition = 11
    RULE_action = 12
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

    ruleNames =  [ u"filestart", u"population", u"createpopulation", u"attributelist", 
                   u"listcomp", u"attribute", u"attrsget", u"timeindex", 
                   u"timevar", u"dictindex", u"statedef", u"transition", 
                   u"action", u"expression", u"assignment", u"codeblock", 
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
    T__26=27
    LineComment=28
    NEWLINE=29
    ML_COMMENT=30
    INT=31
    FLOAT=32
    ID=33
    WS=34
    MUL=35
    DIV=36
    ADD=37
    SUB=38
    PIPE=39
    POWER=40
    STRING=41
    ESC=42
    SPACE=43

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

            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__2:
                self.state = 53 
                self.createpopulation()
                self.state = 58
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
            self.state = 59
            self.match(PrigogineParser.T__0)
            self.state = 60
            self.match(PrigogineParser.ID)
            self.state = 61 
            self.attributelist()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__10:
                self.state = 62 
                self.statedef()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
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
            self.state = 70
            self.match(PrigogineParser.T__2)
            self.state = 71
            self.match(PrigogineParser.ID)
            self.state = 72
            self.match(PrigogineParser.INT)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__13:
                self.state = 73 
                self.codeblock()
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
        self.enterRule(localctx, 6, self.RULE_attributelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(PrigogineParser.T__3)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.ID:
                self.state = 80 
                self.attribute()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
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
        self.enterRule(localctx, 8, self.RULE_listcomp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(PrigogineParser.T__4)
            self.state = 89 
            self.expression(0)
            self.state = 90
            self.match(PrigogineParser.T__5)
            self.state = 91
            self.match(PrigogineParser.ID)
            self.state = 92
            self.match(PrigogineParser.T__6)
            self.state = 93 
            self.expression(0)
            self.state = 94
            self.match(PrigogineParser.T__7)
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
        self.enterRule(localctx, 10, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
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
        self.enterRule(localctx, 12, self.RULE_attrsget)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(PrigogineParser.T__3)
            self.state = 99 
            self.dictindex()
            self.state = 100 
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
        self.enterRule(localctx, 14, self.RULE_timeindex)
        self._la = 0 # Token type
        try:
            self.state = 113
            token = self._input.LA(1)
            if token in [PrigogineParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(PrigogineParser.T__4)
                self.state = 103
                self.match(PrigogineParser.T__8)
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.ADD or _la==PrigogineParser.SUB:
                    self.state = 104
                    _la = self._input.LA(1)
                    if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 105
                    self.match(PrigogineParser.INT)
                    self.state = 110
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 111
                self.match(PrigogineParser.T__7)

            elif token in [PrigogineParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
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
        self.enterRule(localctx, 16, self.RULE_timevar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
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
        self.enterRule(localctx, 18, self.RULE_dictindex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(PrigogineParser.T__4)
            self.state = 118 
            self.string()
            self.state = 119
            self.match(PrigogineParser.T__7)
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
        self.enterRule(localctx, 20, self.RULE_statedef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(PrigogineParser.T__10)
            self.state = 122
            self.match(PrigogineParser.ID)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__11:
                self.state = 123 
                self.transition()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrigogineParser.T__14:
                self.state = 129 
                self.action()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
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
        self.enterRule(localctx, 22, self.RULE_transition)
        self._la = 0 # Token type
        try:
            self.state = 154
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(PrigogineParser.T__11)
                self.state = 138
                self.match(PrigogineParser.ID)
                self.state = 139
                self.match(PrigogineParser.T__12)
                self.state = 140 
                self.conditional()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(PrigogineParser.T__11)
                self.state = 142
                self.match(PrigogineParser.ID)
                self.state = 143
                self.match(PrigogineParser.T__12)
                self.state = 144 
                self.conditional()
                self.state = 145
                self.match(PrigogineParser.T__13)
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__14:
                    self.state = 146 
                    self.action()
                    self.state = 151
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 152
                self.match(PrigogineParser.T__1)
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
        self.enterRule(localctx, 24, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(PrigogineParser.T__14)
            self.state = 159
            token = self._input.LA(1)
            if token in [PrigogineParser.T__3, PrigogineParser.T__4, PrigogineParser.T__8, PrigogineParser.T__16, PrigogineParser.T__24, PrigogineParser.INT, PrigogineParser.FLOAT, PrigogineParser.ID, PrigogineParser.STRING]:
                self.state = 157 
                self.codeline()

            elif token in [PrigogineParser.T__13]:
                self.state = 158 
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 162
                self.match(PrigogineParser.T__16)
                self.state = 163 
                self.expression(9)
                pass

            elif la_ == 2:
                self.state = 164 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 165
                self.match(PrigogineParser.T__16)
                self.state = 166 
                self.string()
                pass

            elif la_ == 4:
                self.state = 167 
                self.string()
                pass

            elif la_ == 5:
                self.state = 168 
                self.number()
                pass

            elif la_ == 6:
                self.state = 169 
                self.attrsget()
                pass

            elif la_ == 7:
                self.state = 170 
                self.func()
                pass

            elif la_ == 8:
                self.state = 171 
                self.listcomp()
                pass

            elif la_ == 9:
                self.state = 172
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 10:
                self.state = 173 
                self.timevar()
                pass

            elif la_ == 11:
                self.state = 174 
                self.lparen()
                self.state = 175 
                self.expression(0)
                self.state = 176 
                self.rparen()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 195
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 180
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 181
                        self.match(PrigogineParser.T__15)
                        self.state = 182 
                        self.expression(16)
                        pass

                    elif la_ == 2:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 183
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 184
                        self.match(PrigogineParser.POWER)
                        self.state = 185 
                        self.expression(15)
                        pass

                    elif la_ == 3:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 186
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 187
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.MUL or _la==PrigogineParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 188 
                        self.expression(14)
                        pass

                    elif la_ == 4:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 190
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PrigogineParser.ADD or _la==PrigogineParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 191 
                        self.expression(13)
                        pass

                    elif la_ == 5:
                        localctx = PrigogineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 192
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 193
                        localctx.op = self.match(PrigogineParser.PIPE)
                        self.state = 194 
                        self.expression(12)
                        pass

             
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            token = self._input.LA(1)
            if token in [PrigogineParser.ID]:
                self.state = 200
                self.match(PrigogineParser.ID)

            elif token in [PrigogineParser.T__3]:
                self.state = 201 
                self.attrsget()

            else:
                raise NoViableAltException(self)

            self.state = 204
            self.match(PrigogineParser.T__17)
            self.state = 205 
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
            self.state = 207
            self.match(PrigogineParser.T__13)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__3) | (1 << PrigogineParser.T__4) | (1 << PrigogineParser.T__8) | (1 << PrigogineParser.T__16) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 208 
                self.codeline()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 214
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
        self.enterRule(localctx, 32, self.RULE_codeline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216 
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
            self.state = 218
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
            self.state = 220 
            self.expression(0)
            self.state = 221
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__18) | (1 << PrigogineParser.T__19) | (1 << PrigogineParser.T__20) | (1 << PrigogineParser.T__21) | (1 << PrigogineParser.T__22) | (1 << PrigogineParser.T__23))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            self.consume()
            self.state = 222 
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
            self.state = 224
            self.match(PrigogineParser.T__24)
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
            self.state = 226
            self.match(PrigogineParser.T__25)
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
            self.state = 228
            self.match(PrigogineParser.ID)
            self.state = 229
            self.match(PrigogineParser.T__24)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PrigogineParser.T__3) | (1 << PrigogineParser.T__4) | (1 << PrigogineParser.T__8) | (1 << PrigogineParser.T__16) | (1 << PrigogineParser.T__24) | (1 << PrigogineParser.INT) | (1 << PrigogineParser.FLOAT) | (1 << PrigogineParser.ID) | (1 << PrigogineParser.STRING))) != 0):
                self.state = 230 
                self.expression(0)
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PrigogineParser.T__26:
                    self.state = 231
                    self.match(PrigogineParser.T__26)
                    self.state = 232 
                    self.expression(0)
                    self.state = 237
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 243
            self.match(PrigogineParser.T__25)
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
            self.state = 248
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245 
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.match(PrigogineParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 247 
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
            self.state = 250
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
         



