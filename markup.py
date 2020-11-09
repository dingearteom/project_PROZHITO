from exceptions import Mix
from slovnet.markup import SpanMarkup
from slovnet.span import Span

def mix(first_markup, second_markup):
    if (first_markup.text != second_markup.text):
        raise Mix

    spans = []

    j = 0
    for i in range(len(first_markup.spans)):
        while (j < (len(second_markup.spans)) and second_markup.spans[j].start < first_markup.spans[i].start):
            spans.append(Span(second_markup.spans[j].start, second_markup.spans[j].stop,
                              second_markup.spans[j].type + '_SECOND'))
            j += 1
        if (j < len(second_markup.spans) and second_markup.spans[j] == first_markup.spans[i]):
            spans.append(Span(second_markup.spans[j].start, second_markup.spans[j].stop,
                              second_markup.spans[j].type + '_BOTH'))
            j += 1
        else:
            spans.append(Span(first_markup.spans[i].start, first_markup.spans[i].stop,
                              first_markup.spans[i].type + '_FIRST'))

    while (j < len(second_markup.spans)):
        spans.append(Span(second_markup.spans[j].start, second_markup.spans[j].stop,
                          second_markup.spans[j].type + '_SECOND'))
        j += 1

    return SpanMarkup(first_markup.text, spans)
