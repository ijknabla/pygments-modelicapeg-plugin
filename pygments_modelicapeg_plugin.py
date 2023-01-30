__all__ = (
    "ModelicaPEGLexer",
)

from pygments.lexer import RegexLexer
from pygments.token import Text


class ModelicaPEGLexer(RegexLexer):
    name = "ModelicaPeg"
    aliases = ("modelica-peg", "modelicapeg",)
    filenames = ("*.modelicapeg")

    tokens = {
        "root": [
            (r".", Text),
        ],
    }
