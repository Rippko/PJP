from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e) -> None:
        stack = list(recognizer.getRuleInvocationStack())
        message = f'\033[1;31mRule stack: ' + ' '.join(stack) + '\n\033[0m'
        message += f'\033[1;31mline {line}:{column} {msg}\033[0m'
        print(message)