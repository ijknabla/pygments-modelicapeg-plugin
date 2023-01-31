__all__ = ("ModelicaPEGLexer",)

from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import Comment, Keyword, Name, Operator, Punctuation, String, Text

STRING_LITERAL = r"'([^']|'(?='))*'" "|" r'"([^"]|"(?="))*"'
REGEX_LITERAL = r"r'([^'\\]|\\.)*'" "|" r'r"([^"\\]|\\.)*"'
IDENTIFIER = r"[A-Z][\-0-9A-Z_]*" "|" r"[a-z][\-0-9_a-z]*"


class ModelicaPEGLexer(RegexLexer):
    name = "ModelicaPeg"
    aliases = (
        "modelica-peg",
        "modelicapeg",
    )
    filenames = "*.modelicapeg"

    tokens = {
        "root": [
            include("common"),
        ],
        "[": [
            (r"\]", Punctuation, "#pop"),
            include("common"),
        ],
        "{": [
            (r"\}", Punctuation, "#pop"),
            include("common"),
        ],
        "(": [
            (r"\)", Punctuation, "#pop"),
            include("common"),
        ],
        "common": [
            include("comment"),
            include("primary"),
            (r"[|]", Operator),
            (r"\[", Punctuation, "["),
            (r"\{", Punctuation, "{"),
            (r"\(", Punctuation, "("),
            (r"\s+", Text),
        ],
        "comment": [
            (r"/\*([^*]|\*[^/])*\*/", Comment.Multiline),
            (r"//.*", Comment.Single),
        ],
        "primary": [
            (r"(`)([a-z]+)(`)", bygroups(None, Keyword, None)),
            (STRING_LITERAL, String),
            (REGEX_LITERAL, String.Regex),
            (rf"({IDENTIFIER})(\s*)([:=])", bygroups(Name.Variable, Text, Operator)),
            (IDENTIFIER, Name),
        ],
    }
