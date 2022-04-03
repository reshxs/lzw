import pathlib
from typer import Typer
from typer import Argument
from typer import Option


app = Typer()


@app.command(
    short_help='Encode file with LZW algorithm. Works only with ascii text!',
)
def encode_lzw(
    source_path: pathlib.Path = Argument(...),
    output_path: pathlib.Path = Option(None, '--output_path', '-o'),
    bit_depth: int = Option(16, '--bit_depth', '-d', help='bit depth of LZW encoding')
):
    from core import encode as _encode
    _encode(
        source_path=source_path,
        output_path=output_path,
        bit_depth=bit_depth,
    )


@app.command(
    short_help='Decode file encoded with LZW algorithm. Works only with ascii text!',
)
def decode_lzw(
    source_path: pathlib.Path = Argument(...),
    output_path: pathlib.Path = Option(None, '--output_path', '-o'),
):
    from core import decode as _decode
    _decode(
        source_path=source_path,
        output_path=output_path,
    )


if __name__ == '__main__':
    app()
