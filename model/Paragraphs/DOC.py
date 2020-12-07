from slovnet.span import Span

class DOC:
    def __init__(self, document):
        self.text = document

        arr = self.text.split('\n\n')
        self.paros = []    # paragraphs in ordinary sense

        ind = 0
        for p in arr:
           if (len(p) != 0):
               self.paros.append(Span(ind, ind + len(p), type='Paros'))
               ind += len(p)
           ind += 2

    def paros_id(self, span):
        l = 0
        r = len(self.paros)
        while(r - l > 1):
            m = (r + l) // 2
            if (self.paros[m].start > span.start):
                r = m
            else:
                l = m
        return l