import pandas as pd

class Definition:

    def __init__(self, term):
        self.term = term.lower() # data csv has lower words

    def get_meaning(self):
        df = pd.read_csv('Resources/data.csv')
        return tuple(df.loc[df['word']==self.term].definition) # some words has more meaning
 
if __name__ == "__main__":
    define = Definition('dread')
    print(define.get_meaning())
