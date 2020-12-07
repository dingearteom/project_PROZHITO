from model.Paragraphs.diary import Diary_Par
from model.Paragraphs.memoir import Memoir_Par
from model.Paragraphs.classification import Type_of_Text

class Paragraphs_Ext:
    def __init__(self):
        self.type_of_text = Type_of_Text()
        self.diary_par = Diary_Par()
        self.memoir_par = Memoir_Par()
    def fit(self, document):
        type =  self.type_of_text.fit(document)
        if (type == 'Diary'):
            return self.diary_par.fit(document)
        else:
            return self.memoir_par.fit(document)