from AntlrComponents.ProjectGrammarParser import ProjectGrammarParser as GrammarParser
from AntlrComponents.ProjectGrammarListener import ProjectGrammarListener as GrammarListener

class EvalListener(GrammarListener):
    def __init__(self):
        self.values = {}
    
    def exitInt(self, ctx: GrammarParser.IntContext):
        self.values[ctx] = int(ctx.INT().getText(), 10)
    
    def exitFloat(self, ctx: GrammarParser.FloatContext):
        self.values[ctx] = float(ctx.FLOAT().getText())
    
    def exitBool(self, ctx: GrammarParser.BoolContext):
        if ctx.BOOL().getText() == 'true':
            self.values[ctx] = True
        else:
            self.values[ctx] = False
    
    def exitString(self, ctx: GrammarParser.StringContext):
        self.values[ctx] = ctx.STRING().getText().strip('"')

    def exitAdd(self, ctx: GrammarParser.AddSubContext):
        left = self.values[ctx.expr(0)]
        right = self.values[ctx.expr(1)]
        if ctx.op.text == '+':
            self.values[ctx] = left + right
        else:
            self.values[ctx] = left - right

    def exitMul(self, ctx: GrammarParser.MulDivContext):
        left = self.values[ctx.expr(0)]
        right = self.values[ctx.expr(1)]
        if ctx.op.text == '*':
            self.values[ctx] = left * right
        else:
            self.values[ctx] = left // right
            
    def exitProg(self, ctx: GrammarParser.ProgramContext):
        for expr in ctx.expr():
            print(self.values[expr])
        
    