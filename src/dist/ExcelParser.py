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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\27\n\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\7\2\"\n\2\f\2\16\2%\13\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4/\n\4\f\4\16\4\62\13\4\5")
        buf.write("\4\64\n\4\3\5\3\5\3\5\2\3\2\6\2\4\6\b\2\7\3\2\4\5\3\2")
        buf.write("\20\21\3\2\6\7\3\2\b\t\3\2\n\f\2=\2\26\3\2\2\2\4&\3\2")
        buf.write("\2\2\6\63\3\2\2\2\b\65\3\2\2\2\n\13\b\2\1\2\13\f\7\3\2")
        buf.write("\2\f\27\5\2\2\13\r\16\t\2\2\2\16\27\5\2\2\n\17\27\5\4")
        buf.write("\3\2\20\27\7\26\2\2\21\27\t\3\2\2\22\23\7\r\2\2\23\24")
        buf.write("\5\2\2\2\24\25\7\16\2\2\25\27\3\2\2\2\26\n\3\2\2\2\26")
        buf.write("\r\3\2\2\2\26\17\3\2\2\2\26\20\3\2\2\2\26\21\3\2\2\2\26")
        buf.write("\22\3\2\2\2\27#\3\2\2\2\30\31\f\7\2\2\31\32\t\4\2\2\32")
        buf.write("\"\5\2\2\b\33\34\f\6\2\2\34\35\t\5\2\2\35\"\5\2\2\7\36")
        buf.write("\37\f\5\2\2\37 \t\6\2\2 \"\5\2\2\6!\30\3\2\2\2!\33\3\2")
        buf.write("\2\2!\36\3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\3\3\2")
        buf.write("\2\2%#\3\2\2\2&\'\7\27\2\2\'(\7\r\2\2()\5\6\4\2)*\7\16")
        buf.write("\2\2*\5\3\2\2\2+\60\5\b\5\2,-\7\17\2\2-/\5\b\5\2.,\3\2")
        buf.write("\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\64\3\2\2")
        buf.write("\2\62\60\3\2\2\2\63+\3\2\2\2\63\64\3\2\2\2\64\7\3\2\2")
        buf.write("\2\65\66\5\2\2\2\66\t\3\2\2\2\7\26!#\60\63")
        return buf.getvalue()


class ExcelParser ( Parser ):

    grammarFileName = "Excel.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!'", "'++'", "'--'", "'*'", "'/'", "'+'", 
                     "'-'", "'>'", "'<'", "'='", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "FLOAT", "CHAR", 
                      "UPPERCHAR", "LOWERCHAR", "WHITESPACE", "CELL_NAME", 
                      "OBJECT_NAME" ]

    RULE_expr = 0
    RULE_function = 1
    RULE_function_args = 2
    RULE_function_arg = 3

    ruleNames =  [ "expr", "function", "function_args", "function_arg" ]

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
    INT=14
    FLOAT=15
    CHAR=16
    UPPERCHAR=17
    LOWERCHAR=18
    WHITESPACE=19
    CELL_NAME=20
    OBJECT_NAME=21

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


    class CellRefExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExcelParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CELL_NAME(self):
            return self.getToken(ExcelParser.CELL_NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCellRefExpr" ):
                listener.enterCellRefExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCellRefExpr" ):
                listener.exitCellRefExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCellRefExpr" ):
                return visitor.visitCellRefExpr(self)
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
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExcelParser.T__0]:
                localctx = ExcelParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 9
                self.match(ExcelParser.T__0)
                self.state = 10
                self.expr(9)
                pass
            elif token in [ExcelParser.T__1, ExcelParser.T__2]:
                localctx = ExcelParser.IncDecExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==ExcelParser.T__1 or _la==ExcelParser.T__2):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 12
                self.expr(8)
                pass
            elif token in [ExcelParser.OBJECT_NAME]:
                localctx = ExcelParser.FunExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.function()
                pass
            elif token in [ExcelParser.CELL_NAME]:
                localctx = ExcelParser.CellRefExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                self.match(ExcelParser.CELL_NAME)
                pass
            elif token in [ExcelParser.INT, ExcelParser.FLOAT]:
                localctx = ExcelParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
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
                self.state = 16
                self.match(ExcelParser.T__10)
                self.state = 17
                self.expr(0)
                self.state = 18
                self.match(ExcelParser.T__11)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 31
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExcelParser.InfixExprContext(self, ExcelParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 23
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ExcelParser.T__3 or _la==ExcelParser.T__4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 24
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExcelParser.InfixExprContext(self, ExcelParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 25
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 26
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ExcelParser.T__5 or _la==ExcelParser.T__6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 27
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ExcelParser.InfixExprContext(self, ExcelParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 29
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExcelParser.T__7) | (1 << ExcelParser.T__8) | (1 << ExcelParser.T__9))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 30
                        localctx.right = self.expr(4)
                        pass

             
                self.state = 35
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
            self.name = None # Token
            self.args = None # Function_argsContext

        def OBJECT_NAME(self):
            return self.getToken(ExcelParser.OBJECT_NAME, 0)

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
            self.state = 36
            localctx.name = self.match(ExcelParser.OBJECT_NAME)
            self.state = 37
            self.match(ExcelParser.T__10)
            self.state = 38
            localctx.args = self.function_args()
            self.state = 39
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
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExcelParser.T__0) | (1 << ExcelParser.T__1) | (1 << ExcelParser.T__2) | (1 << ExcelParser.T__10) | (1 << ExcelParser.INT) | (1 << ExcelParser.FLOAT) | (1 << ExcelParser.CELL_NAME) | (1 << ExcelParser.OBJECT_NAME))) != 0):
                self.state = 41
                self.function_arg()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ExcelParser.T__12:
                    self.state = 42
                    self.match(ExcelParser.T__12)
                    self.state = 43
                    self.function_arg()
                    self.state = 48
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
            self.state = 51
            self.expr(0)
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
         




