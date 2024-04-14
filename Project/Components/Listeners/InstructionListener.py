from AntlrComponents.ProjectGrammarParser import ProjectGrammarParser as GrammarParser
from AntlrComponents.ProjectGrammarListener import ProjectGrammarListener as GrammarListener

class InstructionListener(GrammarListener):
    def __init__(self, filename):
        self.filename = filename
        self.blocks = [{}]
        self.need_convert_to_float = False
        self.label_count = 0
        self.init_file()
    
    def write_to_file(self, text: str) -> None:
        with open(self.filename, 'a') as f:
            f.write(text + '\n')
                
    def init_file(self) -> None:
        with open(self.filename, 'w') as f:
            f.write('')
            
    def enterBlockStatement(self, ctx: GrammarParser.BlockStatementContext):
        self.blocks.append({})
        
    def exitBlockStatement(self, ctx: GrammarParser.BlockStatementContext):
        self.blocks.pop()
            
    def exitInt(self, ctx: GrammarParser.IntContext):
        self.write_to_file(f'push I {ctx.INT().getText()}')
        if self.need_convert_to_float:
            self.write_to_file('itof')
            self.need_convert_to_float = False
    
    def exitFloat(self, ctx: GrammarParser.FloatContext):
        self.write_to_file(f'push F {ctx.FLOAT().getText()}')
        
    def exitString(self, ctx: GrammarParser.StringContext):
        self.write_to_file(f'push S {ctx.STRING().getText()}')
        
    def exitBool(self, ctx: GrammarParser.BoolContext):
        self.write_to_file(f'push B {ctx.BOOL().getText()}')
        
    def exitIdentifier(self, ctx: GrammarParser.IdentifierContext):
        if type(ctx.parentCtx) is not GrammarParser.ReadExprContext:
            self.write_to_file(f'load {ctx.ID()}')
    
    def exitUnary(self, ctx: GrammarParser.UnaryContext):
        expr_type = self.get_expr_type(ctx.expr())
        if expr_type == 'int':
            self.write_to_file('uminus')
        else:
            self.write_to_file('not')
        
    def exitMod(self, ctx: GrammarParser.ModContext):
        self.write_to_file('mod')
    
    def exitConcat(self, ctx: GrammarParser.ConcatContext):
        self.write_to_file('concat')
        
    def exitReadExpr(self, ctx: GrammarParser.ReadExprContext):
        for i in range(len(ctx.expr())):
            expr = ctx.expr(i)
            expr_type = self.get_expr_type(expr)
            
            match expr_type:
                case 'int':
                    self.write_to_file('read I')
                case 'float':
                    self.write_to_file('read F')
                case 'string':
                    self.write_to_file('read S')
                case 'bool':
                    self.write_to_file('read B')
            self.write_to_file(f'save {expr.ID()}')    
        
    def exitWriteExpr(self, ctx: GrammarParser.WriteExprContext):
        self.write_to_file(f'print {len(ctx.expr())}')
        
    def getLeftAndRight(self, ctx):
        left = self.get_expr_type(ctx.expr(0))
        right = self.get_expr_type(ctx.expr(1))
        return left, right    

    def get_expr_type(self, ctx):
        match type(ctx):
            case GrammarParser.IntContext:
                return 'int'
            case GrammarParser.FloatContext:
                return 'float'
            case GrammarParser.StringContext:
                return 'string'
            case GrammarParser.BoolContext:
                return 'bool'
            case GrammarParser.IdentifierContext:
                var_name = ctx.ID().getText()
                for block in self.blocks:
                    return block[var_name][0]
            case GrammarParser.AddSubContext:
                left, right = self.getLeftAndRight(ctx)
                if (left == 'int' and right == 'int' )or (left == 'float' and right == 'float'):
                    return left
            case GrammarParser.MulDivContext:
                left, right = self.getLeftAndRight(ctx)

                match left, right:
                    case 'int', 'int':
                        return 'int'
                    case 'int', 'float':
                        return 'float'
                    case 'float', 'int':
                        return 'float'
                    case 'float', 'float':
                        return 'float'
            case GrammarParser.ParensContext:
                return self.get_expr_type(ctx.expr())
            case GrammarParser.RelationalContext:
                return 'bool'
            case GrammarParser.ModContext:
                return 'int'
            case GrammarParser.ComparisonContext:
                return 'bool'
            case GrammarParser.AndContext:
                return 'bool'
            case GrammarParser.OrContext:
                return 'bool'
            case GrammarParser.AssignmentContext:
                return self.get_expr_type(ctx.expr())
            case GrammarParser.UnaryContext:
                return self.get_expr_type(ctx.expr())
            case GrammarParser.ConcatContext:
                return 'string'
    
    def enterAddSub(self, ctx: GrammarParser.AddSubContext):
        left, right = self.getLeftAndRight(ctx)
        if left == 'int' and right == 'float' or left == 'float' and right == 'int':
            self.need_convert_to_float = True
            
    def exitAddSub(self, ctx: GrammarParser.AddSubContext):
        if ctx.op.text == '+':
            self.write_to_file('add')
        else:
            self.write_to_file('sub')
            
    def enterMulDiv(self, ctx: GrammarParser.MulDivContext):
        left, right = self.getLeftAndRight(ctx)
        if left == 'int' and right == 'float' or left == 'float' and right == 'int':
            self.need_convert_to_float = True
            
    def exitMulDiv(self, ctx: GrammarParser.MulDivContext):
        if ctx.op.text == '*':
            self.write_to_file('mul')
        else:
            self.write_to_file('div')
            
    def exitDeclar(self, ctx: GrammarParser.DeclarContext):
        for i in range(len(ctx.ID())):
            name = ctx.ID(i).getText()
            type = ctx.primitiveType().getText()
            
            match type:
                case 'int':
                    self.write_to_file(f'push I 0')
                    self.blocks[-1][name] = ('int', 0)
                case 'float':
                    self.write_to_file(f'push F 0.0')
                    self.blocks[-1][name] = ('float', 0.0)
                case 'string':
                    self.write_to_file(f'push S ""')
                    self.blocks[-1][name] = ('string', '')
                case 'bool':
                    self.write_to_file(f'push B false')
                    self.blocks[-1][name] = ('bool', False)
                    
            self.write_to_file(f'save {name}')
    
    def enterAssignment(self, ctx: GrammarParser.AssignmentContext):
        name = ctx.ID().getText()
        expr_type = self.get_expr_type(ctx.expr())
        
        for i in range(len(self.blocks)):
            if name in self.blocks[i].keys():
                if expr_type == 'int' and self.blocks[i][name][0] == 'float':
                    self.need_convert_to_float = True
                return
        
    def exitAssignment(self, ctx: GrammarParser.AssignmentContext):
        name = ctx.ID().getText()
        self.write_to_file(f'save {name}')

        self.write_to_file(f'load {name}')
        
        if ctx.parentCtx.getChild(0) == ctx:
            self.write_to_file('pop')
            
    def exitAnd(self, ctx: GrammarParser.AndContext):
        self.write_to_file('and')
    
    def exitOr(self, ctx: GrammarParser.OrContext):
        self.write_to_file('or')
        
    def enterComparison(self, ctx: GrammarParser.ComparisonContext):
        left, right = self.getLeftAndRight(ctx)
        
        if left == 'int' and right == 'float' or left == 'float' and right == 'int':
            self.need_convert_to_float = True
            
    def exitComparison(self, ctx: GrammarParser.ComparisonContext):
        if ctx.op.getText() == '==':
            self.write_to_file('eq')
        elif ctx.op.getText() == '!=':
            self.write_to_file('eq')
            self.write_to_file('not')
            
    def enterRelational(self, ctx: GrammarParser.RelationalContext):
        left, right = self.getLeftAndRight(ctx)
        
        if left == 'int' and right == 'float' or left == 'float' and right == 'int':
            self.need_convert_to_float = True
            
    def exitRelational(self, ctx: GrammarParser.RelationalContext):
        if ctx.op.getText() == '>':
            self.write_to_file('gt')
        elif ctx.op.getText() == '<':
            self.write_to_file('lt')
        elif ctx.op.getText() == '>=':
            self.write_to_file('gte')
        elif ctx.op.getText() == '<=':
            self.write_to_file('lte')
    
    def exitRpar(self, ctx: GrammarParser.RparContext):
        match type(ctx.parentCtx):
            case GrammarParser.IfStatementContext:
                self.write_to_file(f"fjmp {self.label_count}")
                self.label_count += 1
            case GrammarParser.WhileStatementContext:
                self.label_count += 1
                self.write_to_file(f"fjmp {self.label_count}")
    
    def exitIfStatement(self, ctx: GrammarParser.IfStatementContext):
        if ctx.elseStatement() is None:
            self.write_to_file(f"jmp {self.label_count}")
            self.write_to_file(f"label {self.label_count - 1}")
            self.write_to_file(f"label {self.label_count}")
            self.label_count += 1
    
    def enterElseStatement(self, ctx: GrammarParser.ElseStatementContext):
        self.write_to_file(f"jmp {self.label_count}")
        self.write_to_file(f"label {self.label_count - 1}")
        self.label_count += 1
    
    def exitElseStatement(self, ctx: GrammarParser.ElseStatementContext):
        self.write_to_file(f"label {self.label_count - 1}")
    
    def enterWhileStatement(self, ctx: GrammarParser.WhileStatementContext):
        self.write_to_file(f"label {self.label_count}")
    
    def exitWhileStatement(self, ctx: GrammarParser.WhileStatementContext):
        self.write_to_file(f"jmp {self.label_count - 1}")
        self.write_to_file(f"label {self.label_count}")
        self.label_count += 1
        
    def enterDoWhileStatement(self, ctx: GrammarParser.DoWhileStatementContext):
        self.write_to_file(f"label {self.label_count}")

    def exitDoWhileStatement(self, ctx: GrammarParser.DoWhileStatementContext):
        self.write_to_file(f"label {self.label_count}")
        self.label_count += 1
        self.write_to_file(f"fjmp {self.label_count - 1}")
    