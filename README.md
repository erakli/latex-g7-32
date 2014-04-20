latex-g7-32
===========

Стиль LaTeX для расчётно-пояснительной записки к курсовым и дипломным работам (ГОСТ 7.32-2001). Ориентирован на студентов IT специальностей.

Изначально был написан в расчёте на `pdfLaTeX`, с коммита `23b1612` добавлена поддержка `XeLaTeX`. Если требуется использование `pdfLaTeX` то в `Makefile` надо поменять в третье строке `xelatex` на `pdflatex`.

## Установка

### Зависимости

#### LaTeX пакеты
```
amssymb amsmath caption flafter footmisc hyperref icomma iftex graphicx longtable underscore 
```

#### pdfLaTeX-версия
```
cmap babel mathtext pscyr ucs
```

Для придания таймовского вида нужно установить соотв. шрифты (пакет `cyrtimes.sty`), в Debian/Ubuntu это пакет `scalable-cyrfonts-tex`. Если этого пакета нет, оно использует стандартную гарнитуру CM.

#### XeLaTeX-версия
```
polyglossia xecyr
```

#### Программы
```
inkscape dia pgf context 
```

## Использование
После изменения РПЗ запустите `make` в корне. Результатом будет `rpz.pdf`.

### Редактор
Можно исползьзовать любой редактор, например, `Kile`. На комманду `cd .. && make` вешается горячая клавиша и создаётся проект с корректным главным докукментом.

Авторы
------
В порядке участия:

Алексей Томин

[Михаил Конник](http://mydebianblog.blogspot.ru/2008/09/732-2001-latex.html)

|[Всеволод Крищенко](http://sevik.ru/latex/)|
-------------------

[Иван Коротков](https://vk.com/ikorotkov)

Студенты кафедры [ИУ7](http://iu7.bmstu.ru)

[Роман Инфлянскас](https://github.com/rominf/latex-g7-32)
