from typing import TextIO, Sequence, NamedTuple, List
from io import StringIO, BytesIO
from werkzeug.datastructures import FileStorage
from unidecode import unidecode
from ..config import HEADERS
from warnings import warn
import csv


class Info(NamedTuple):
    position: int
    name: str


Headers = List[Info]
CsvLine = List[str]


def process_headers(headers: Sequence) -> Headers:
    l: List[Info] = []
    ignored: List[str] = []
    for position, old_name in enumerate(headers):
        try:
            l.append(
                Info(position, HEADERS[old_name])
            )
        except KeyError:
            ignored.append(old_name)

    if len(ignored) > 0:
        warn(f"Colunas descartadas: {ignored}")

    if len(l) < 2:
        raise Exception("Less than 2 columns on final file")

    return l


def process_line(line: Sequence, headers: Headers) -> List[str]:
    new_line: List[str] = []
    for x in headers:
        new_line.append(unidecode(line[x.position]))
    return new_line


def process(content: TextIO) -> List[CsvLine]:
    new_lines: List[CsvLine] = []
    data: List[Info] = []

    lines = csv.reader(content)
    for i, line in enumerate(lines):
        if i == 0:
            data = process_headers(line)
            new_lines.append([v.name for v in data])
        else:
            new_line = process_line(line, data)
            new_lines.append(new_line)

    if len(new_lines) < 2:
        raise Exception("Less than 2 lines on final file")
    return new_lines


def generate_file(lines: List[CsvLine]) -> BytesIO:
    new = StringIO(newline="")
    writer = csv.writer(new, quoting=1)
    writer.writerows(lines)
    content = new.getvalue()
    return BytesIO(content.encode("utf-8"))


def process_request(file: FileStorage) -> BytesIO:
    content = file.stream.read().decode()
    wrapper = StringIO(content)
    new_file = process(wrapper)
    return generate_file(new_file)
