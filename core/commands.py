import pathlib
import pickle

from .lzw import encode as _encode
from .lzw import decode as _decode


def encode(
    bit_depth: int,
    source_path: pathlib.Path,
    output_path: pathlib.Path,
):
    """Архивировать файл.

    :param bit_depth: разрядность кодирования;
    :param source_path: путь до исходного файла;
    :param output_path: путь для сжатого файла. Если None, то файл сохранится в ту же дирректорию
    с тем же именем, что и исходный файл с расширением .lzw;
    :return: None;
    """
    maximum_table_size = pow(2, bit_depth)

    with open(source_path.as_posix()) as source_file:
        data = source_file.read()

    compressed_data = _encode(data, maximum_table_size)

    with open(output_path.as_posix(), "wb") as output_file:
        pickle.dump(compressed_data, output_file)


def decode(source_path: pathlib.Path, output_path: pathlib.Path):
    """Разархивировать файл.

    :param source_path: путь до сжатого файла;
    :param output_path: путь для выходного файла;
    :return: None;
    """
    with open(source_path.as_posix(), 'rb') as source_file:
        compressed_data = pickle.load(source_file)

    with open(output_path.as_posix(), "w") as output_file:
        for data in _decode(compressed_data):
            output_file.write(data)
