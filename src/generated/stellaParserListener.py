# Generated from /home/ususi/itmo/typesystem/project/stella-typechecker/grammar/stellaParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .stellaParser import stellaParser
else:
    from stellaParser import stellaParser

# This class defines a complete listener for a parse tree produced by stellaParser.
class stellaParserListener(ParseTreeListener):

    # Enter a parse tree produced by stellaParser#start_Program.
    def enterStart_Program(self, ctx:stellaParser.Start_ProgramContext):
        pass

    # Exit a parse tree produced by stellaParser#start_Program.
    def exitStart_Program(self, ctx:stellaParser.Start_ProgramContext):
        pass


    # Enter a parse tree produced by stellaParser#start_Expr.
    def enterStart_Expr(self, ctx:stellaParser.Start_ExprContext):
        pass

    # Exit a parse tree produced by stellaParser#start_Expr.
    def exitStart_Expr(self, ctx:stellaParser.Start_ExprContext):
        pass


    # Enter a parse tree produced by stellaParser#start_Type.
    def enterStart_Type(self, ctx:stellaParser.Start_TypeContext):
        pass

    # Exit a parse tree produced by stellaParser#start_Type.
    def exitStart_Type(self, ctx:stellaParser.Start_TypeContext):
        pass


    # Enter a parse tree produced by stellaParser#program.
    def enterProgram(self, ctx:stellaParser.ProgramContext):
        pass

    # Exit a parse tree produced by stellaParser#program.
    def exitProgram(self, ctx:stellaParser.ProgramContext):
        pass


    # Enter a parse tree produced by stellaParser#LanguageCore.
    def enterLanguageCore(self, ctx:stellaParser.LanguageCoreContext):
        pass

    # Exit a parse tree produced by stellaParser#LanguageCore.
    def exitLanguageCore(self, ctx:stellaParser.LanguageCoreContext):
        pass


    # Enter a parse tree produced by stellaParser#AnExtension.
    def enterAnExtension(self, ctx:stellaParser.AnExtensionContext):
        pass

    # Exit a parse tree produced by stellaParser#AnExtension.
    def exitAnExtension(self, ctx:stellaParser.AnExtensionContext):
        pass


    # Enter a parse tree produced by stellaParser#DeclFun.
    def enterDeclFun(self, ctx:stellaParser.DeclFunContext):
        pass

    # Exit a parse tree produced by stellaParser#DeclFun.
    def exitDeclFun(self, ctx:stellaParser.DeclFunContext):
        pass


    # Enter a parse tree produced by stellaParser#DeclFunGeneric.
    def enterDeclFunGeneric(self, ctx:stellaParser.DeclFunGenericContext):
        pass

    # Exit a parse tree produced by stellaParser#DeclFunGeneric.
    def exitDeclFunGeneric(self, ctx:stellaParser.DeclFunGenericContext):
        pass


    # Enter a parse tree produced by stellaParser#DeclTypeAlias.
    def enterDeclTypeAlias(self, ctx:stellaParser.DeclTypeAliasContext):
        pass

    # Exit a parse tree produced by stellaParser#DeclTypeAlias.
    def exitDeclTypeAlias(self, ctx:stellaParser.DeclTypeAliasContext):
        pass


    # Enter a parse tree produced by stellaParser#DeclExceptionType.
    def enterDeclExceptionType(self, ctx:stellaParser.DeclExceptionTypeContext):
        pass

    # Exit a parse tree produced by stellaParser#DeclExceptionType.
    def exitDeclExceptionType(self, ctx:stellaParser.DeclExceptionTypeContext):
        pass


    # Enter a parse tree produced by stellaParser#DeclExceptionVariant.
    def enterDeclExceptionVariant(self, ctx:stellaParser.DeclExceptionVariantContext):
        pass

    # Exit a parse tree produced by stellaParser#DeclExceptionVariant.
    def exitDeclExceptionVariant(self, ctx:stellaParser.DeclExceptionVariantContext):
        pass


    # Enter a parse tree produced by stellaParser#InlineAnnotation.
    def enterInlineAnnotation(self, ctx:stellaParser.InlineAnnotationContext):
        pass

    # Exit a parse tree produced by stellaParser#InlineAnnotation.
    def exitInlineAnnotation(self, ctx:stellaParser.InlineAnnotationContext):
        pass


    # Enter a parse tree produced by stellaParser#paramDecl.
    def enterParamDecl(self, ctx:stellaParser.ParamDeclContext):
        pass

    # Exit a parse tree produced by stellaParser#paramDecl.
    def exitParamDecl(self, ctx:stellaParser.ParamDeclContext):
        pass


    # Enter a parse tree produced by stellaParser#Fold.
    def enterFold(self, ctx:stellaParser.FoldContext):
        pass

    # Exit a parse tree produced by stellaParser#Fold.
    def exitFold(self, ctx:stellaParser.FoldContext):
        pass


    # Enter a parse tree produced by stellaParser#Add.
    def enterAdd(self, ctx:stellaParser.AddContext):
        pass

    # Exit a parse tree produced by stellaParser#Add.
    def exitAdd(self, ctx:stellaParser.AddContext):
        pass


    # Enter a parse tree produced by stellaParser#IsZero.
    def enterIsZero(self, ctx:stellaParser.IsZeroContext):
        pass

    # Exit a parse tree produced by stellaParser#IsZero.
    def exitIsZero(self, ctx:stellaParser.IsZeroContext):
        pass


    # Enter a parse tree produced by stellaParser#Var.
    def enterVar(self, ctx:stellaParser.VarContext):
        pass

    # Exit a parse tree produced by stellaParser#Var.
    def exitVar(self, ctx:stellaParser.VarContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeAbstraction.
    def enterTypeAbstraction(self, ctx:stellaParser.TypeAbstractionContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeAbstraction.
    def exitTypeAbstraction(self, ctx:stellaParser.TypeAbstractionContext):
        pass


    # Enter a parse tree produced by stellaParser#Divide.
    def enterDivide(self, ctx:stellaParser.DivideContext):
        pass

    # Exit a parse tree produced by stellaParser#Divide.
    def exitDivide(self, ctx:stellaParser.DivideContext):
        pass


    # Enter a parse tree produced by stellaParser#LessThan.
    def enterLessThan(self, ctx:stellaParser.LessThanContext):
        pass

    # Exit a parse tree produced by stellaParser#LessThan.
    def exitLessThan(self, ctx:stellaParser.LessThanContext):
        pass


    # Enter a parse tree produced by stellaParser#DotRecord.
    def enterDotRecord(self, ctx:stellaParser.DotRecordContext):
        pass

    # Exit a parse tree produced by stellaParser#DotRecord.
    def exitDotRecord(self, ctx:stellaParser.DotRecordContext):
        pass


    # Enter a parse tree produced by stellaParser#GreaterThan.
    def enterGreaterThan(self, ctx:stellaParser.GreaterThanContext):
        pass

    # Exit a parse tree produced by stellaParser#GreaterThan.
    def exitGreaterThan(self, ctx:stellaParser.GreaterThanContext):
        pass


    # Enter a parse tree produced by stellaParser#Equal.
    def enterEqual(self, ctx:stellaParser.EqualContext):
        pass

    # Exit a parse tree produced by stellaParser#Equal.
    def exitEqual(self, ctx:stellaParser.EqualContext):
        pass


    # Enter a parse tree produced by stellaParser#Throw.
    def enterThrow(self, ctx:stellaParser.ThrowContext):
        pass

    # Exit a parse tree produced by stellaParser#Throw.
    def exitThrow(self, ctx:stellaParser.ThrowContext):
        pass


    # Enter a parse tree produced by stellaParser#Multiply.
    def enterMultiply(self, ctx:stellaParser.MultiplyContext):
        pass

    # Exit a parse tree produced by stellaParser#Multiply.
    def exitMultiply(self, ctx:stellaParser.MultiplyContext):
        pass


    # Enter a parse tree produced by stellaParser#ConstMemory.
    def enterConstMemory(self, ctx:stellaParser.ConstMemoryContext):
        pass

    # Exit a parse tree produced by stellaParser#ConstMemory.
    def exitConstMemory(self, ctx:stellaParser.ConstMemoryContext):
        pass


    # Enter a parse tree produced by stellaParser#List.
    def enterList(self, ctx:stellaParser.ListContext):
        pass

    # Exit a parse tree produced by stellaParser#List.
    def exitList(self, ctx:stellaParser.ListContext):
        pass


    # Enter a parse tree produced by stellaParser#TryCatch.
    def enterTryCatch(self, ctx:stellaParser.TryCatchContext):
        pass

    # Exit a parse tree produced by stellaParser#TryCatch.
    def exitTryCatch(self, ctx:stellaParser.TryCatchContext):
        pass


    # Enter a parse tree produced by stellaParser#TryCastAs.
    def enterTryCastAs(self, ctx:stellaParser.TryCastAsContext):
        pass

    # Exit a parse tree produced by stellaParser#TryCastAs.
    def exitTryCastAs(self, ctx:stellaParser.TryCastAsContext):
        pass


    # Enter a parse tree produced by stellaParser#Head.
    def enterHead(self, ctx:stellaParser.HeadContext):
        pass

    # Exit a parse tree produced by stellaParser#Head.
    def exitHead(self, ctx:stellaParser.HeadContext):
        pass


    # Enter a parse tree produced by stellaParser#TerminatingSemicolon.
    def enterTerminatingSemicolon(self, ctx:stellaParser.TerminatingSemicolonContext):
        pass

    # Exit a parse tree produced by stellaParser#TerminatingSemicolon.
    def exitTerminatingSemicolon(self, ctx:stellaParser.TerminatingSemicolonContext):
        pass


    # Enter a parse tree produced by stellaParser#NotEqual.
    def enterNotEqual(self, ctx:stellaParser.NotEqualContext):
        pass

    # Exit a parse tree produced by stellaParser#NotEqual.
    def exitNotEqual(self, ctx:stellaParser.NotEqualContext):
        pass


    # Enter a parse tree produced by stellaParser#ConstUnit.
    def enterConstUnit(self, ctx:stellaParser.ConstUnitContext):
        pass

    # Exit a parse tree produced by stellaParser#ConstUnit.
    def exitConstUnit(self, ctx:stellaParser.ConstUnitContext):
        pass


    # Enter a parse tree produced by stellaParser#Sequence.
    def enterSequence(self, ctx:stellaParser.SequenceContext):
        pass

    # Exit a parse tree produced by stellaParser#Sequence.
    def exitSequence(self, ctx:stellaParser.SequenceContext):
        pass


    # Enter a parse tree produced by stellaParser#ConstFalse.
    def enterConstFalse(self, ctx:stellaParser.ConstFalseContext):
        pass

    # Exit a parse tree produced by stellaParser#ConstFalse.
    def exitConstFalse(self, ctx:stellaParser.ConstFalseContext):
        pass


    # Enter a parse tree produced by stellaParser#Abstraction.
    def enterAbstraction(self, ctx:stellaParser.AbstractionContext):
        pass

    # Exit a parse tree produced by stellaParser#Abstraction.
    def exitAbstraction(self, ctx:stellaParser.AbstractionContext):
        pass


    # Enter a parse tree produced by stellaParser#ConstInt.
    def enterConstInt(self, ctx:stellaParser.ConstIntContext):
        pass

    # Exit a parse tree produced by stellaParser#ConstInt.
    def exitConstInt(self, ctx:stellaParser.ConstIntContext):
        pass


    # Enter a parse tree produced by stellaParser#Variant.
    def enterVariant(self, ctx:stellaParser.VariantContext):
        pass

    # Exit a parse tree produced by stellaParser#Variant.
    def exitVariant(self, ctx:stellaParser.VariantContext):
        pass


    # Enter a parse tree produced by stellaParser#ConstTrue.
    def enterConstTrue(self, ctx:stellaParser.ConstTrueContext):
        pass

    # Exit a parse tree produced by stellaParser#ConstTrue.
    def exitConstTrue(self, ctx:stellaParser.ConstTrueContext):
        pass


    # Enter a parse tree produced by stellaParser#Subtract.
    def enterSubtract(self, ctx:stellaParser.SubtractContext):
        pass

    # Exit a parse tree produced by stellaParser#Subtract.
    def exitSubtract(self, ctx:stellaParser.SubtractContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeCast.
    def enterTypeCast(self, ctx:stellaParser.TypeCastContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeCast.
    def exitTypeCast(self, ctx:stellaParser.TypeCastContext):
        pass


    # Enter a parse tree produced by stellaParser#If.
    def enterIf(self, ctx:stellaParser.IfContext):
        pass

    # Exit a parse tree produced by stellaParser#If.
    def exitIf(self, ctx:stellaParser.IfContext):
        pass


    # Enter a parse tree produced by stellaParser#Application.
    def enterApplication(self, ctx:stellaParser.ApplicationContext):
        pass

    # Exit a parse tree produced by stellaParser#Application.
    def exitApplication(self, ctx:stellaParser.ApplicationContext):
        pass


    # Enter a parse tree produced by stellaParser#Deref.
    def enterDeref(self, ctx:stellaParser.DerefContext):
        pass

    # Exit a parse tree produced by stellaParser#Deref.
    def exitDeref(self, ctx:stellaParser.DerefContext):
        pass


    # Enter a parse tree produced by stellaParser#IsEmpty.
    def enterIsEmpty(self, ctx:stellaParser.IsEmptyContext):
        pass

    # Exit a parse tree produced by stellaParser#IsEmpty.
    def exitIsEmpty(self, ctx:stellaParser.IsEmptyContext):
        pass


    # Enter a parse tree produced by stellaParser#Panic.
    def enterPanic(self, ctx:stellaParser.PanicContext):
        pass

    # Exit a parse tree produced by stellaParser#Panic.
    def exitPanic(self, ctx:stellaParser.PanicContext):
        pass


    # Enter a parse tree produced by stellaParser#LessThanOrEqual.
    def enterLessThanOrEqual(self, ctx:stellaParser.LessThanOrEqualContext):
        pass

    # Exit a parse tree produced by stellaParser#LessThanOrEqual.
    def exitLessThanOrEqual(self, ctx:stellaParser.LessThanOrEqualContext):
        pass


    # Enter a parse tree produced by stellaParser#Succ.
    def enterSucc(self, ctx:stellaParser.SuccContext):
        pass

    # Exit a parse tree produced by stellaParser#Succ.
    def exitSucc(self, ctx:stellaParser.SuccContext):
        pass


    # Enter a parse tree produced by stellaParser#Inl.
    def enterInl(self, ctx:stellaParser.InlContext):
        pass

    # Exit a parse tree produced by stellaParser#Inl.
    def exitInl(self, ctx:stellaParser.InlContext):
        pass


    # Enter a parse tree produced by stellaParser#GreaterThanOrEqual.
    def enterGreaterThanOrEqual(self, ctx:stellaParser.GreaterThanOrEqualContext):
        pass

    # Exit a parse tree produced by stellaParser#GreaterThanOrEqual.
    def exitGreaterThanOrEqual(self, ctx:stellaParser.GreaterThanOrEqualContext):
        pass


    # Enter a parse tree produced by stellaParser#Inr.
    def enterInr(self, ctx:stellaParser.InrContext):
        pass

    # Exit a parse tree produced by stellaParser#Inr.
    def exitInr(self, ctx:stellaParser.InrContext):
        pass


    # Enter a parse tree produced by stellaParser#Match.
    def enterMatch(self, ctx:stellaParser.MatchContext):
        pass

    # Exit a parse tree produced by stellaParser#Match.
    def exitMatch(self, ctx:stellaParser.MatchContext):
        pass


    # Enter a parse tree produced by stellaParser#LogicNot.
    def enterLogicNot(self, ctx:stellaParser.LogicNotContext):
        pass

    # Exit a parse tree produced by stellaParser#LogicNot.
    def exitLogicNot(self, ctx:stellaParser.LogicNotContext):
        pass


    # Enter a parse tree produced by stellaParser#ParenthesisedExpr.
    def enterParenthesisedExpr(self, ctx:stellaParser.ParenthesisedExprContext):
        pass

    # Exit a parse tree produced by stellaParser#ParenthesisedExpr.
    def exitParenthesisedExpr(self, ctx:stellaParser.ParenthesisedExprContext):
        pass


    # Enter a parse tree produced by stellaParser#Tail.
    def enterTail(self, ctx:stellaParser.TailContext):
        pass

    # Exit a parse tree produced by stellaParser#Tail.
    def exitTail(self, ctx:stellaParser.TailContext):
        pass


    # Enter a parse tree produced by stellaParser#Record.
    def enterRecord(self, ctx:stellaParser.RecordContext):
        pass

    # Exit a parse tree produced by stellaParser#Record.
    def exitRecord(self, ctx:stellaParser.RecordContext):
        pass


    # Enter a parse tree produced by stellaParser#LogicAnd.
    def enterLogicAnd(self, ctx:stellaParser.LogicAndContext):
        pass

    # Exit a parse tree produced by stellaParser#LogicAnd.
    def exitLogicAnd(self, ctx:stellaParser.LogicAndContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeApplication.
    def enterTypeApplication(self, ctx:stellaParser.TypeApplicationContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeApplication.
    def exitTypeApplication(self, ctx:stellaParser.TypeApplicationContext):
        pass


    # Enter a parse tree produced by stellaParser#LetRec.
    def enterLetRec(self, ctx:stellaParser.LetRecContext):
        pass

    # Exit a parse tree produced by stellaParser#LetRec.
    def exitLetRec(self, ctx:stellaParser.LetRecContext):
        pass


    # Enter a parse tree produced by stellaParser#LogicOr.
    def enterLogicOr(self, ctx:stellaParser.LogicOrContext):
        pass

    # Exit a parse tree produced by stellaParser#LogicOr.
    def exitLogicOr(self, ctx:stellaParser.LogicOrContext):
        pass


    # Enter a parse tree produced by stellaParser#TryWith.
    def enterTryWith(self, ctx:stellaParser.TryWithContext):
        pass

    # Exit a parse tree produced by stellaParser#TryWith.
    def exitTryWith(self, ctx:stellaParser.TryWithContext):
        pass


    # Enter a parse tree produced by stellaParser#Pred.
    def enterPred(self, ctx:stellaParser.PredContext):
        pass

    # Exit a parse tree produced by stellaParser#Pred.
    def exitPred(self, ctx:stellaParser.PredContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeAsc.
    def enterTypeAsc(self, ctx:stellaParser.TypeAscContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeAsc.
    def exitTypeAsc(self, ctx:stellaParser.TypeAscContext):
        pass


    # Enter a parse tree produced by stellaParser#NatRec.
    def enterNatRec(self, ctx:stellaParser.NatRecContext):
        pass

    # Exit a parse tree produced by stellaParser#NatRec.
    def exitNatRec(self, ctx:stellaParser.NatRecContext):
        pass


    # Enter a parse tree produced by stellaParser#Unfold.
    def enterUnfold(self, ctx:stellaParser.UnfoldContext):
        pass

    # Exit a parse tree produced by stellaParser#Unfold.
    def exitUnfold(self, ctx:stellaParser.UnfoldContext):
        pass


    # Enter a parse tree produced by stellaParser#Ref.
    def enterRef(self, ctx:stellaParser.RefContext):
        pass

    # Exit a parse tree produced by stellaParser#Ref.
    def exitRef(self, ctx:stellaParser.RefContext):
        pass


    # Enter a parse tree produced by stellaParser#DotTuple.
    def enterDotTuple(self, ctx:stellaParser.DotTupleContext):
        pass

    # Exit a parse tree produced by stellaParser#DotTuple.
    def exitDotTuple(self, ctx:stellaParser.DotTupleContext):
        pass


    # Enter a parse tree produced by stellaParser#Fix.
    def enterFix(self, ctx:stellaParser.FixContext):
        pass

    # Exit a parse tree produced by stellaParser#Fix.
    def exitFix(self, ctx:stellaParser.FixContext):
        pass


    # Enter a parse tree produced by stellaParser#Let.
    def enterLet(self, ctx:stellaParser.LetContext):
        pass

    # Exit a parse tree produced by stellaParser#Let.
    def exitLet(self, ctx:stellaParser.LetContext):
        pass


    # Enter a parse tree produced by stellaParser#Assign.
    def enterAssign(self, ctx:stellaParser.AssignContext):
        pass

    # Exit a parse tree produced by stellaParser#Assign.
    def exitAssign(self, ctx:stellaParser.AssignContext):
        pass


    # Enter a parse tree produced by stellaParser#Tuple.
    def enterTuple(self, ctx:stellaParser.TupleContext):
        pass

    # Exit a parse tree produced by stellaParser#Tuple.
    def exitTuple(self, ctx:stellaParser.TupleContext):
        pass


    # Enter a parse tree produced by stellaParser#ConsList.
    def enterConsList(self, ctx:stellaParser.ConsListContext):
        pass

    # Exit a parse tree produced by stellaParser#ConsList.
    def exitConsList(self, ctx:stellaParser.ConsListContext):
        pass


    # Enter a parse tree produced by stellaParser#patternBinding.
    def enterPatternBinding(self, ctx:stellaParser.PatternBindingContext):
        pass

    # Exit a parse tree produced by stellaParser#patternBinding.
    def exitPatternBinding(self, ctx:stellaParser.PatternBindingContext):
        pass


    # Enter a parse tree produced by stellaParser#binding.
    def enterBinding(self, ctx:stellaParser.BindingContext):
        pass

    # Exit a parse tree produced by stellaParser#binding.
    def exitBinding(self, ctx:stellaParser.BindingContext):
        pass


    # Enter a parse tree produced by stellaParser#matchCase.
    def enterMatchCase(self, ctx:stellaParser.MatchCaseContext):
        pass

    # Exit a parse tree produced by stellaParser#matchCase.
    def exitMatchCase(self, ctx:stellaParser.MatchCaseContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternCons.
    def enterPatternCons(self, ctx:stellaParser.PatternConsContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternCons.
    def exitPatternCons(self, ctx:stellaParser.PatternConsContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternTuple.
    def enterPatternTuple(self, ctx:stellaParser.PatternTupleContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternTuple.
    def exitPatternTuple(self, ctx:stellaParser.PatternTupleContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternList.
    def enterPatternList(self, ctx:stellaParser.PatternListContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternList.
    def exitPatternList(self, ctx:stellaParser.PatternListContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternRecord.
    def enterPatternRecord(self, ctx:stellaParser.PatternRecordContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternRecord.
    def exitPatternRecord(self, ctx:stellaParser.PatternRecordContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternVariant.
    def enterPatternVariant(self, ctx:stellaParser.PatternVariantContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternVariant.
    def exitPatternVariant(self, ctx:stellaParser.PatternVariantContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternAsc.
    def enterPatternAsc(self, ctx:stellaParser.PatternAscContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternAsc.
    def exitPatternAsc(self, ctx:stellaParser.PatternAscContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternInt.
    def enterPatternInt(self, ctx:stellaParser.PatternIntContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternInt.
    def exitPatternInt(self, ctx:stellaParser.PatternIntContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternInr.
    def enterPatternInr(self, ctx:stellaParser.PatternInrContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternInr.
    def exitPatternInr(self, ctx:stellaParser.PatternInrContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternTrue.
    def enterPatternTrue(self, ctx:stellaParser.PatternTrueContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternTrue.
    def exitPatternTrue(self, ctx:stellaParser.PatternTrueContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternInl.
    def enterPatternInl(self, ctx:stellaParser.PatternInlContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternInl.
    def exitPatternInl(self, ctx:stellaParser.PatternInlContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternVar.
    def enterPatternVar(self, ctx:stellaParser.PatternVarContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternVar.
    def exitPatternVar(self, ctx:stellaParser.PatternVarContext):
        pass


    # Enter a parse tree produced by stellaParser#patternCons.
    def enterPatternCons(self, ctx:stellaParser.PatternConsContext):
        pass

    # Exit a parse tree produced by stellaParser#patternCons.
    def exitPatternCons(self, ctx:stellaParser.PatternConsContext):
        pass


    # Enter a parse tree produced by stellaParser#ParenthesisedPattern.
    def enterParenthesisedPattern(self, ctx:stellaParser.ParenthesisedPatternContext):
        pass

    # Exit a parse tree produced by stellaParser#ParenthesisedPattern.
    def exitParenthesisedPattern(self, ctx:stellaParser.ParenthesisedPatternContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternSucc.
    def enterPatternSucc(self, ctx:stellaParser.PatternSuccContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternSucc.
    def exitPatternSucc(self, ctx:stellaParser.PatternSuccContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternFalse.
    def enterPatternFalse(self, ctx:stellaParser.PatternFalseContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternFalse.
    def exitPatternFalse(self, ctx:stellaParser.PatternFalseContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternUnit.
    def enterPatternUnit(self, ctx:stellaParser.PatternUnitContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternUnit.
    def exitPatternUnit(self, ctx:stellaParser.PatternUnitContext):
        pass


    # Enter a parse tree produced by stellaParser#PatternCastAs.
    def enterPatternCastAs(self, ctx:stellaParser.PatternCastAsContext):
        pass

    # Exit a parse tree produced by stellaParser#PatternCastAs.
    def exitPatternCastAs(self, ctx:stellaParser.PatternCastAsContext):
        pass


    # Enter a parse tree produced by stellaParser#labelledPattern.
    def enterLabelledPattern(self, ctx:stellaParser.LabelledPatternContext):
        pass

    # Exit a parse tree produced by stellaParser#labelledPattern.
    def exitLabelledPattern(self, ctx:stellaParser.LabelledPatternContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeTuple.
    def enterTypeTuple(self, ctx:stellaParser.TypeTupleContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeTuple.
    def exitTypeTuple(self, ctx:stellaParser.TypeTupleContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeTop.
    def enterTypeTop(self, ctx:stellaParser.TypeTopContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeTop.
    def exitTypeTop(self, ctx:stellaParser.TypeTopContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeBool.
    def enterTypeBool(self, ctx:stellaParser.TypeBoolContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeBool.
    def exitTypeBool(self, ctx:stellaParser.TypeBoolContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeRef.
    def enterTypeRef(self, ctx:stellaParser.TypeRefContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeRef.
    def exitTypeRef(self, ctx:stellaParser.TypeRefContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeRec.
    def enterTypeRec(self, ctx:stellaParser.TypeRecContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeRec.
    def exitTypeRec(self, ctx:stellaParser.TypeRecContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeAuto.
    def enterTypeAuto(self, ctx:stellaParser.TypeAutoContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeAuto.
    def exitTypeAuto(self, ctx:stellaParser.TypeAutoContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeSum.
    def enterTypeSum(self, ctx:stellaParser.TypeSumContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeSum.
    def exitTypeSum(self, ctx:stellaParser.TypeSumContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeVar.
    def enterTypeVar(self, ctx:stellaParser.TypeVarContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeVar.
    def exitTypeVar(self, ctx:stellaParser.TypeVarContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeVariant.
    def enterTypeVariant(self, ctx:stellaParser.TypeVariantContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeVariant.
    def exitTypeVariant(self, ctx:stellaParser.TypeVariantContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeUnit.
    def enterTypeUnit(self, ctx:stellaParser.TypeUnitContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeUnit.
    def exitTypeUnit(self, ctx:stellaParser.TypeUnitContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeNat.
    def enterTypeNat(self, ctx:stellaParser.TypeNatContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeNat.
    def exitTypeNat(self, ctx:stellaParser.TypeNatContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeBottom.
    def enterTypeBottom(self, ctx:stellaParser.TypeBottomContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeBottom.
    def exitTypeBottom(self, ctx:stellaParser.TypeBottomContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeParens.
    def enterTypeParens(self, ctx:stellaParser.TypeParensContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeParens.
    def exitTypeParens(self, ctx:stellaParser.TypeParensContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeFun.
    def enterTypeFun(self, ctx:stellaParser.TypeFunContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeFun.
    def exitTypeFun(self, ctx:stellaParser.TypeFunContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeForAll.
    def enterTypeForAll(self, ctx:stellaParser.TypeForAllContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeForAll.
    def exitTypeForAll(self, ctx:stellaParser.TypeForAllContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeRecord.
    def enterTypeRecord(self, ctx:stellaParser.TypeRecordContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeRecord.
    def exitTypeRecord(self, ctx:stellaParser.TypeRecordContext):
        pass


    # Enter a parse tree produced by stellaParser#TypeList.
    def enterTypeList(self, ctx:stellaParser.TypeListContext):
        pass

    # Exit a parse tree produced by stellaParser#TypeList.
    def exitTypeList(self, ctx:stellaParser.TypeListContext):
        pass


    # Enter a parse tree produced by stellaParser#recordFieldType.
    def enterRecordFieldType(self, ctx:stellaParser.RecordFieldTypeContext):
        pass

    # Exit a parse tree produced by stellaParser#recordFieldType.
    def exitRecordFieldType(self, ctx:stellaParser.RecordFieldTypeContext):
        pass


    # Enter a parse tree produced by stellaParser#variantFieldType.
    def enterVariantFieldType(self, ctx:stellaParser.VariantFieldTypeContext):
        pass

    # Exit a parse tree produced by stellaParser#variantFieldType.
    def exitVariantFieldType(self, ctx:stellaParser.VariantFieldTypeContext):
        pass



del stellaParser