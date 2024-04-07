from AntlrComponents.ProjectGrammarParser import ProjectGrammarParser as GrammarParser
from AntlrComponents.ProjectGrammarListener import ProjectGrammarListener as GrammarListener

class EvalListener(GrammarListener):
    def __init__(self):
        self.values = {}
        
    def exitDeclar(self, ctx: GrammarParser.DeclarContext):
        var_type = ctx.primitiveType().getText()
        for var in ctx.ID():
            if var_type == 'int':
                self.values[var] = 0
            elif var_type == 'float':
                self.values[var] = 0.0
            elif var_type == 'bool':
                self.values[var] = False
            elif var_type == 'string':
                self.values[var] = ''

    def exitInt(self, ctx: GrammarParser.IntContext):
        self.values[ctx] = int(ctx.INT().getText())
    
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