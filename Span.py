def select_spans(spans, type_):
    spans_new = []
    for span in spans:
        if (span.type in type_):
            spans_new.append(span)
    return spans_new
