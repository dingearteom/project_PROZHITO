# prozhito-tools-research

Добавьте папку "Новая разметка" в папку data, если вы собираетесь запускать репозиторий локально:
https://yadi.sk/d/zW7wsNuUhVxeyg

В data вы можете найти:
compare.html

*PER_FIRST соответствует истинной разметке
*PER_SECOND соответствует результату работы наташи
*PER_BOTH там где истинная разметка совпала с разметкой наташи

first.html 

Отдельно истинная разметка

second.html

Отдельно разметка Наташи.


Запустив main вы также можете увидить вывод некоторых статистик по работе наташи.
Более подробные комментарии будут добавлены позже.

Пока видно, что Наташа работает неплохо.
* Она редко отмечает слова, которые прям точно не являются фамилией. Где-то 1% максимум, возможно меньше. 
* Ее проблема пока что скорее в том, что нам нужно отмечать не все имена фамилии. 
  Например, в обзаце мы имя, если оно встречается, должны выделить ровно один раз. Также, мы не должны отмечать личности, которые просто вскользь упоминаются.
* Там еще некоторые проблемы с инициалами. Например, из А. Николаев мы отмечаем только Николаев. Но тут проблема и с истинной разметкой.

Вообщем, как я дальше это вижу:

* нужно немного почистить истинную разметку
* можно построить модель машинного обучения на основе ответов, которые выдает наташа
* с моделью буду еще думать. Возможно придется применить нейронную сеть или CRF так как это делается в наташе. Правда в этом мне еще нужно разбираться дальше. 

