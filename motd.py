import csv
from pathlib import Path
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from tqdm import tqdm

Base = declarative_base()


class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True)
    formatted = Column(String)


engine = create_engine("sqlite:///quotes.sqlite", future=True)
Base.metadata.create_all(engine)


CSV = Path(__file__).parent / "quotes.csv"

with CSV.open() as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar='"')

    with Session(engine) as session:
        for idx, row in tqdm(enumerate(reader)):
            if idx:
                session.add(Quote(formatted=f'"{row[0]}" - {row[1]}'))
                if idx % 100 == 0:
                    session.commit()
        session.commit()
