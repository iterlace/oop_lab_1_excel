# Generated from Excel.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("@\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\30\n\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2#\n\2\f\2\16\2&\13\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4\60\n\4\f\4\16\4\63\13")
        buf.write("\4\5\4\65\n\4\3\5\3\5\3\6\3\6\7\6;\n\6\f\6\16\6>\13\6")
        buf.write("\3\6\2\3\2\7\2\4\6\b\n\2\b\3\2\4\5\3\2\21\22\3\2\6\7\3")
        buf.write("\2\b\t\3\2\n\f\4\2\20\21\23\23\2D\2\27\3\2\2\2\4\'\3\2")
        buf.write("\2\2\6\64\3\2\2\2\b\66\3\2\2\2\n8\3\2\2\2\f\r\b\2\1\2")
        buf.write("\r\16\7\3\2\2\16\30\5\2\2\n\17\20\t\2\2\2\20\30\5\2\2")
        buf.write("\t\21\30\5\4\3\2\22\30\t\3\2\2\23\24\7\r\2\2\24\25\5\2")
        buf.write("\2\2\25\26\7\16\2\2\26\30\3\2\2\2\27\f\3\2\2\2\27\17\3")
        buf.write("\2\2\2\27\21\3\2\2\2\27\22\3\2\2\2\27\23\3\2\2\2\30$\3")
        buf.write("\2\2\2\31\32\f\7\2\2\32\33\t\4\2\2\33#\5\2\2\b\34\35\f")
        buf.write("\6\2\2\35\36\t\5\2\2\36#\5\2\2\7\37 \f\5\2\2 !\t\6\2\2")
        buf.write("!#\5\2\2\6\"\31\3\2\2\2\"\34\3\2\2\2\"\37\3\2\2\2#&\3")
        buf.write("\2\2\2$\"\3\2\2\2$%\3\2\2\2%\3\3\2\2\2&$\3\2\2\2\'(\5")
        buf.write("\n\6\2()\7\r\2\2)*\5\6\4\2*+\7\16\2\2+\5\3\2\2\2,\61\5")
        buf.write("\b\5\2-.\7\17\2\2.\60\5\b\5\2/-\3\2\2\2\60\63\3\2\2\2")
        buf.write("\61/\3\2\2\2\61\62\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2")
        buf.write("\64,\3\2\2\2\64\65\3\2\2\2\65\7\3\2\2\2\66\67\5\2\2\2")
        buf.write("\67\t\3\2\2\28<\7\23\2\29;\t\7\2\2:9\3\2\2\2;>\3\2\2\2")
        buf.write("<:\3\2\2\2<=\3\2\2\2=\13\3\2\2\2><\3\2\2\2\b\27\"$\61")
        buf.write("\64<")
        return buf.getvalue()


class ExcelParser ( Parser ):

    grammarFileName = "Excel.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!'", "'++'", "'--'", "'*'", "'/'", "'+'", 
                     "'-'", "'>'", "'<'", "'='", "'('", "')'", "','", "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "FLOAT", 
                      "CHAR", "UPPERCHAR", "LOWERCHAR", "WHITESPACE" ]

    RULE_expr = 0
    RULE_function = 1
    RULE_function_args = 2
    RULE_function_arg = 3
    RULE_object_name = 4

    ruleNames =  [ "expr", "function", "function_args", "function_arg", 
                   "object_name" ]

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
    INT=15
    FLOAT=16
    CHAR=17
    UPPERCHAR=18
    LOWERCHAR=19
    WHITESPACE=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExcelParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExcelParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ExcelParser.INT, 0)
        def FLOAT(self):
            return self.getToken(ExcelParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExcelParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExcelParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class IncDecExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExcelParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExcelParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncDecExpr" ):
                listener.enterIncDecExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncDecExpr" ):
                listener.exitIncDecExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncDecExpr" ):
                return visitor.visitIncDecExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExcelParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExcelParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExcelParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExcelParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExcelParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)


    class FunExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExcelParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function(self):
            return self.getTypedRuleContext(ExcelParser.FunctionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunExpr" ):
                listener.enterFunExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunExpr" ):
                listener.exitFunExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunExpr" ):
                return visitor.visitFunExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExcelParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExcelParser.T__0]:
                localctx = ExcelParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 11
                self.match(ExcelParser.T__0)
                self.state = 12
                self.expr(8)
                pass
            elif token in [ExcelParser.T__1, ExcelParser.T__2]:
                localctx = ExcelParser.IncDecExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==ExcelParser.T__1 or _la==ExcelParser.T__2):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 14
                self.expr(7)
                pass
            elif token in [ExcelParser.CHAR]:
                localctx = ExcelParser.FunExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.function()
                pass
            elif token in [ExcelParser.INT, ExcelParser.FLOAT]:
                localctx = ExcelParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                _la = self._input.LA(1)
                if not(_la==ExcelParser.INT or _la==ExcelParser.FLOAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [ExcelParser.T__10]:
                localctx = ExcelParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(ExcelParser.T__10)
                self.state = 18
                self.expr(0)
                self.state = 19
                self.match(ExcelParser.T__11)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 32
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExcelParser.InfixExprContext(self, ExcelParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 23
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 24
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ExcelParser.T__3 or _la==ExcelParser.T__4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 25
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExcelParser.InfixExprContext(self, ExcelParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 26
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 27
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ExcelParser.T__5 or _la==ExcelParser.T__6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 28
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ExcelParser.InfixExprContext(self, ExcelParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 30
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExcelParser.T__7) | (1 << ExcelParser.T__8) | (1 << ExcelParser.T__9))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        localctx.right = self.expr(4)
                        pass

             
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Object_nameContext
            self.args = None # Function_argsContext

        def object_name(self):
            return self.getTypedRuleContext(ExcelParser.Object_nameContext,0)


        def function_args(self):
            return self.getTypedRuleContext(ExcelParser.Function_argsContext,0)


        def getRuleIndex(self):
            return ExcelParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ExcelParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            localctx.name = self.object_name()
            self.state = 38
            self.match(ExcelParser.T__10)
            self.state = 39
            localctx.args = self.function_args()
            self.state = 40
            self.match(ExcelParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExcelParser.Function_argContext)
            else:
                return self.getTypedRuleContext(ExcelParser.Function_argContext,i)


        def getRuleIndex(self):
            return ExcelParser.RULE_function_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_args" ):
                listener.enterFunction_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_args" ):
                listener.exitFunction_args(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_args" ):
                return visitor.visitFunction_args(self)
            else:
                return visitor.visitChildren(self)




    def function_args(self):

        localctx = ExcelParser.Function_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExcelParser.T__0) | (1 << ExcelParser.T__1) | (1 << ExcelParser.T__2) | (1 << ExcelParser.T__10) | (1 << ExcelParser.INT) | (1 << ExcelParser.FLOAT) | (1 << ExcelParser.CHAR))) != 0):
                self.state = 42
                self.function_arg()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ExcelParser.T__12:
                    self.state = 43
                    self.match(ExcelParser.T__12)
                    self.state = 44
                    self.function_arg()
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExcelParser.ExprContext,0)


        def getRuleIndex(self):
            return ExcelParser.RULE_function_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_arg" ):
                listener.enterFunction_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_arg" ):
                listener.exitFunction_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_arg" ):
                return visitor.visitFunction_arg(self)
            else:
                return visitor.visitChildren(self)




    def function_arg(self):

        localctx = ExcelParser.Function_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(ExcelParser.CHAR)
            else:
                return self.getToken(ExcelParser.CHAR, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(ExcelParser.INT)
            else:
                return self.getToken(ExcelParser.INT, i)

        def getRuleIndex(self):
            return ExcelParser.RULE_object_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_name" ):
                listener.enterObject_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_name" ):
                listener.exitObject_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_name" ):
                return visitor.visitObject_name(self)
            else:
                return visitor.visitChildren(self)




    def object_name(self):

        localctx = ExcelParser.Object_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_object_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ExcelParser.CHAR)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExcelParser.T__13) | (1 << ExcelParser.INT) | (1 << ExcelParser.CHAR))) != 0):
                self.state = 55
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExcelParser.T__13) | (1 << ExcelParser.INT) | (1 << ExcelParser.CHAR))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




