# lzw
Архиватор текстовых файлов, использующих алгоритм LZW.

❗️Работает только с текстовыми файлами❗

## Установка зааисимостей
```bash
pip install -r requirements.txt
```
## Использование
Для кодирования/декодирования текстовых файлов можно воспользоваться CLI. 
Однако, модуль core предоставляет команды encode и decode, что позволяет использовать архиватор в коде или писать свои собственные интерфейсы.

### CLI
```bash
❯ python3 cli.py --help
Usage: cli.py [OPTIONS] COMMAND [ARGS]...python3 cli.py --help                                                                                         Py archiver 19:02:51

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  decode-lzw  Decode file encoded with LZW algorithm. Works only with ascii
              text!
  encode-lzw  Encode file with LZW algorithm. Works only with ascii text!
```

### Кодирование файла
```bash
❯ python3 cli.py encode-lzw --help
Usage: cli.py encode-lzw [OPTIONS] SOURCE_PATH

Arguments:
  SOURCE_PATH  [required]

Options:
  -o, --output_path PATH
  -d, --bit_depth INTEGER  bit depth of LZW encoding  [default: 16]
  --help                   Show this message and exit.
```
w
### Декодирование файла
```bash
❯ python3 cli.py decode-lzw --help
Usage: cli.py decode-lzw [OPTIONS] SOURCE_PATHn3 cli.py decode-lzw --help                                                                              Py archiver 19:01:14

Arguments:
  SOURCE_PATH  [required]

Options:
  -o, --output_path PATH
  --help                  Show this message and exit.
```
