# Установка

Скачать последнюю версию.

* C помощью git:
```
git clone https://github.com/latex-g7-32/latex-g7-32
```
* Или [скачать zip](https://github.com/latex-g7-32/latex-g7-32/archive/master.zip).
* Или взять из [релизов](https://github.com/rominf/latex-g7-32/releases).
Однако, релизы формируются с течением времени и могут содержать существенно устаревшую версию.

Скопировать следующие файлы в локальный texmf: 
- `G2-105.sty` 
- `G7-32.cls`
- `G7-32.sty`
- `GostBase.clo`
- `gosttitleGost7-32.sty`
- `gosttitleGostRV15-110.sty`
- `local-minted.sty`
- `cyrtimespatched.sty`

Для линукс это будет `$HOME/texmf/`.
Для Виндовс `C:\Users\USERNAME\texmf\`.
Проверить это можно командой `kpsewhich -var-value=TEXMFHOME`.
Относительно texmf путь будет `texmf/tex/latex/latex-g7-32/`.

Создание папки `texmf` при использовании MiKTeX: [ссылка](https://miktex.org/faq/local-additions).

## Установка под Windows

Для работы в Windows необходимо установить следующие зависимости:

1. [dwimperl](http://dwimperl.com/windows.html)
2. [texlive](https://www.tug.org/texlive/windows.html)
3. [inkscape](https://inkscape.org/ru/download/)
4. [dia](http://dia-installer.de/)
5. [graphviz](http://www.graphviz.org/Download_windows.php)
6. [ghostscript](https://ghostscript.com/download/gsdnld.html)
7. [babun](http://babun.github.io/) — не обязательно.
8. [cmake](https://cmake.org/download/) — не обязательно при использовании 
   `babun`, обязательно при работе без него. В случае с `babun` нужно 
   использовать `pact install cmake`, а не самостоятельную установку из 
   установщика на сайте. В любом случае необходимо либо иметь babun+make, либо 
   babun+cmake, либо cmake.

   Внимание: CMake не собирает ничего сам, он генерирует скрипты для make (и 
   ряда других программ), только он умеет использовать разные диалекты: nmake 
   (из Visual Studio), mingw32-make, MSYS make, … Поэтому что‐то из этого нужно 
   также установить. На данный момент сборка проверялась для `babun+cmake`, 
   `babun+make` и просто нативного `cmake`. В последнем случае использовалась 
   утилита `make` из пакета WinAVR, идентифицирующаяся как GNU make.
9. [python](https://www.python.org/downloads/windows/) — при использовании babun 
   не нужно, он уже установлен там.

   После установки python установить его пакет pygments.

После установки всех зависимостей необходимо добавить их в $PATH. Установщики 
некоторых (texlive, cmake и dwimperl) делают это сами (но, возможно, требуется 
установка галочки), для остальных нужно редактировать реестр, либо изменять PATH 
временно. В PATH помещаются каталоги, в которых находятся следующие файлы: 
`inkscape.exe`, `dia.exe`, `dot.exe`, `python.exe`.

Ghostscript предоставляет файлы gswin32.exe и gswin32c.exe, однако для работы 
нужно иметь файл gs.exe или gs.bat где‐то в $PATH. В случае с bat файл должен 
выглядеть так:

```bat
@echo off
P:\ath\to\ghostscript\gswin32c.exe %*
```

> ВНИМАНИЕ: именно `gswin32c.exe`, не `gswin32.exe`.
Можно просто скопировать `gswin32c.exe` в `gs.exe` и добавить каталог с ними в `$PATH`.

В случае использования python из babun вам дополнительно нужен в `$PATH` 
`pygmentize.bat` следующего содержания:

```bat
@echo off
C:\Users\{user}\.babun\cygwin\bin\python2.7.exe C:\Users\{user}\.babun\cygwin\bin\pygmentize %*
```

> Замените `{user}` на своего пользователя.

Что нужно в случае использования 
python без babun я не знаю, но исполняемый файл pygmentize должен быть 
в `$PATH`.

После того, как `$PATH` станет содержать пути ко всем необходимым исполняемым 
файлам можно будет использовать выбранную систему сборки для создания PDF‐файла.

> Сборка шаблона [под Windows](USAGE.md#Использование-под-Windows).

## Установка шрифтов

В отчёте можно использовать свободный аналог Times New Roman - PT Astra ([установка](../fonts/README.md)).

Опции класса документа, устанавливающие шрифты:

1. При использовании XeLaTeX:

    1. `astra` (по умолчанию) — свободные шрифты Astra Sans, Astra Serif, Liberation Mono.
    2. `times` — Шрифты Times New Roman, Arial, Courier New. Необходимо, чтобы у вас был подписан лицензионный договор с правообладателем шрифтов — компанией Monotype Imaging Inc.
    3. `cm` — Шрифты CMU, которые обычно включены в TeX Live.

2. При использовании PdfLaTeX:

   1. `times` (по умолчанию) — шрифты из пакета cyrtimes: Nimbus Roman и Nimbus Sans.
   2. `pscyr` — шрифты из пакета pscyr: Antiqua PSCyr, Textbook PSCyr, ERKurier PSCyr.
   3. `cm` — шрифты CM, которые обычно включены в TeX Live.

Если какой-то шрифт не найден, то вместо него будет использоваться соответствующий шрифт CM.

Эти опции нужно задавать в `\documentclass`, например так: `\documentclass[utf8x, times, 14pt]{G7-32}`

## Зависимости

### Основные для стилевого файла

#### LaTeX пакеты
```
caption etoolbox footmisc was iftex lastpage mfirstuc nomencl titlesec underscore
```
##### openSUSE
```
texlive-latex texlive-iftex 
```

### pdfLaTeX-версия
#### LaTeX пакеты
```
cmap babel mathtext pscyr ucs
```

Для придания таймовского вида нужно установить соотв. шрифты (пакет `cyrtimes.sty`), в Debian/Ubuntu это пакет `scalable-cyrfonts-tex`. Если этого пакета нет, оно использует стандартную гарнитуру CM.

### XeLaTeX-версия
#### LaTeX пакеты
```
cm-unicode minted polyglossia xecyr
```

##### openSUSE
```
cm-unicode texlive-minted texlive-polyglossia texlive-xecyr
```

#### Программы
```
inkscape dia graphviz python pygments
```

### LyX
```
lyx
```

### Установочный скрипт
```
python3.5
```

Копирует (или перемещает) файлы со стилями в общую `texmf` папку, макеты `LyX` в папку с настройками `LyX`. Для получения помощи вызовите `install.py --help`.