__all__ = ("ModelicaPEGLexer",)

from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import Comment, Keyword, Name, Operator, Punctuation, String, Text


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
            (r'"([^"]|"(?="))*"', String),
            (r"'([^']|'(?='))*'", String),
            (r"r'([^'\\]|\\.)*'", String.Regex),
            (r'r"([^"\\]|\\.)*"', String.Regex),
            (r"[:=|]", Operator),
            (r"(`)([a-z]+)(`)", bygroups(None, Keyword, None)),
            (r"[A-Z]([\-0-9A-Z]*[0-9A-Z])?", Name),
            (r"[a-z]([\-0-9a-z]*[0-9a-z])?", Name),
            (r"\[", Punctuation, "["),
            (r"\{", Punctuation, "{"),
            (r"\(", Punctuation, "("),
            (r"\s+", Text),
        ],
        "comment": [
            (r"/\*([^*]|\*[^/])*\*/", Comment.Multiline),
            (r"//.*", Comment.Single),
        ]
    }
