from AntlrComponents.ProjectGrammarParser import ProjectGrammarParser as GrammarParser
from AntlrComponents.ProjectGrammarListener import ProjectGrammarListener as GrammarListener

class EvalListener(GrammarListener):
    def __init__(self):
        self.blocks = [{}]
        self.has_error = False
        
    def exitDeclar(self, ctx: GrammarParser.DeclarContext):
        var_type = ctx.primitiveType().getText()
        var_names = [var_name.getText() for var_name in ctx.ID()]
        
        for i in range(len(self.blocks)):
            for var_name in var_names:
                if var_name in self.blocks[i]:
                    self.has_error = True
                    print(f'\033[1;31mVariable [{var_name}] already declared\033[0m')
                    return
        
        default_value = None
        
        match var_type:
            case 'int':
                default_value = 0
            case 'float':
                default_value = 0.0
            case 'string':
                default_value = ''
            case 'bool':
                default_value = False
            case _:
                self.has_error = True
                print(f'Unknown type [{var_type}]')
                
        for var_name in var_names:
            self.blocks[-1][var_name] = (var_type, default_value)
    
    def enterBlockStatement(self, ctx: GrammarParser.BlockStatementContext):
        self.blocks.append({})
        
    def exitBlockStatement(self, ctx: GrammarParser.BlockStatementContext):
        self.blocks.pop()
        
    def exitAssignment(self, ctx: GrammarParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = ctx.expr().getText()
        
        for i in range(len(self.blocks)):
            if var_name in self.blocks[i].keys():
                var_type, _ = self.blocks[i][var_name]
                expr_type = self.get_expr_type(ctx.expr())
                if expr_type == 'int' and var_type == 'float':
                    expr_type = 'float'
                
                if var_type != expr_type:
                    self.has_error = True
                    print(f'\033[1;31mCannot assign [{expr_type}] to [{var_type}]\033[0m')
                    return
                    
                self.blocks[i][var_name] = (var_type, value)
                return
            
        self.has_error = True
        print(f'\033[1;31mVariable [{var_name}] not declared\033[0m')

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
                    if var_name in block:
                        return block[var_name][0]
                self.has_error = True
                print(f'\033[1;31mVariable [{var_name}] not declared\033[0m')
                return None
            case GrammarParser.AddSubContext:
                left, right = self.getLeftAndRight(ctx)

                if left == 'int' and right == 'int' or left == 'float' and right == 'float':
                    return left
                self.has_error = True
                print(f'\033[1;31mCannot add/sub [{left}] and [{right}]\033[0m')
                return None
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
                self.has_error = True
                print(f'\033[1;31mCannot mul/div [{left}] and [{right}]\033[0m')
                return None
            case GrammarParser.ParensContext:
                return self.get_expr_type(ctx.expr())
            case GrammarParser.RelationalContext:
                left, right = self.getLeftAndRight(ctx)

                if left in ['int', 'float'] and right in ['int', 'float']:
                    return 'bool'
                self.has_error = True
                print(f'\033[1;31mCannot compare [{left}] and [{right}]\033[0m')
                return None
            case GrammarParser.ModContext:
                left, right = self.getLeftAndRight(ctx)

                if left == 'int' and right == 'int':
                    return 'int'
                self.has_error = True
                print(f'\033[1;31mCannot mod [{left}] and [{right}]\033[0m')
                return None
            case GrammarParser.ComparisonContext:
                left, right = self.getLeftAndRight(ctx)

                if left == 'bool' or right == 'bool':
                    self.has_error = True
                    print(f'\033[1;31mCannot compare [{left}] and [{right}]\033[0m')
                    return None
                return 'bool'
            case GrammarParser.LogicalContext:
                left, right = self.getLeftAndRight(ctx)

                if left == 'bool' and right == 'bool':
                    return 'bool'
                self.has_error = True
                print(f'\033[1;31mCannot compare [{left}] and [{right}]\033[0m')
                return None
            case GrammarParser.AssignmentContext:
                return self.get_expr_type(ctx.expr())
            case GrammarParser.UnaryContext:
                return self.get_expr_type(ctx.expr())
            case GrammarParser.ConcatContext:
                left, right = self.getLeftAndRight(ctx)

                if left == 'string' and right == 'string':
                    return 'string'
                self.has_error = True
                print(f'\033[1;31mCannot concat [{left}] and [{right}]\033[0m')
                return None                
            case _:
                self.has_error = True
                print(f'\033[1;31mUnknown expression type [{type(ctx)}]\033[0m')
                return None
            
    def exitDoWhileStatement(self, ctx: GrammarParser.DoWhileStatementContext):
        statement = ctx.expr().getText()
        if self.get_expr_type(ctx.expr()) != 'bool':
            self.has_error = True
            print(f'\033[1;31mDo-While statement expects bool, got [{statement}]\033[0m')
            
    def exitWriteExpr(self, ctx: GrammarParser.WriteExprContext):
        for expr in ctx.expr():
            self.get_expr_type(expr)
            
    def exitWhileStatement(self, ctx: GrammarParser.WhileStatementContext):
        statement = ctx.expr().getText()
        if self.get_expr_type(ctx.expr()) != 'bool':
            self.has_error = True
            print(f'\033[1;31mWhile statement expects bool, got [{statement}]\033[0m')
            
    def exitIfStatement(self, ctx: GrammarParser.IfStatementContext):
        statement = ctx.expr().getText()
        if self.get_expr_type(ctx.expr()) != 'bool':
            self.has_error = True
            print(f'\033[1;31mIf statement expects bool, got [{statement}]\033[0m')
            
    # def enterEveryRule(self, ctx):
    #     name = str(type(ctx).__name__).replace("Context", "").lower()
    #     nameFormat = f"\033[1;38m{name}\033[0m"
    #     print("{:<30}".format(nameFormat), ctx.getText())
            
            