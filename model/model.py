from navec import Navec
from slovnet import NER
from model.Per_and_locations_spans import Per_and_Loc
from model.Persons.persons import Persons_extractor
from model.Locations.loc_extractor import LOC_extractor
from model.Paragraphs.Paragraphs import Paragraphs_Ext
from model.Dates.dates import Dates

class Model:
    def __init__(self):
        self.Per_and_Loc = Per_and_Loc()
        self.per_ext = Persons_extractor()
        self.loc_ext = LOC_extractor()
        self.par_ext = Paragraphs_Ext()
        self.dates_ext = Dates()
    def fit(self, document):
        entities = self.Per_and_Loc.fit(document)
        persons_spans = entities['PER']
        locations_spans = entities['LOC']
        persons = self.per_ext.fit(document, persons_spans)
        locations = self.loc_ext.fit(document, locations_spans)
        par_spans = self.par_ext.fit(document)
        dates = self.dates_ext.fit(document)

        d = DOC()
        d.text = document
        d.per = persons
        d.locations = locations

        ind = 0
        for par_span in par_spans:
            loc_in_par = []
            while (ind < len(locations) and locations[ind].span.stop <= par_span.stop):
                loc_in_par.append(locations[ind])
                ind += 1
                d.paragraphs.append(Paragraph(par_span, None, loc_in_par))
        return d


class DOC:
    __attributes__ = ['text', 'per', 'paragraphs', 'locations']
    text = None
    per = []
    paragraphs = []
    def __init__(self):
        pass

class Paragraph:
    __attributes__ = ['span', 'daterange', 'Locations']
    span = daterange = None
    Locations = []
    def __init__(self, span, daterange, Locations):
        self.span = span
        self.daterange = daterange
        self.Locations = Locations