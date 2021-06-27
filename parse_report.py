"""
This module is specifically designed to break data from a Team Manager Top Times
Report into individual events with swimmers. This parser will create an output
object that can be interacted with by a ranking script to generate rankings for
a team based on another team's Top Times Report.
"""

import camelot  # PDF extraction library
import pandas as pd

from table_index import TableIndex
from swimmer import Swimmer
from event import Event

class ReportParser:
    def __init__(self, top_times_pdf):
        self.top_times_pdf = top_times_pdf

        # Internal data
        self.__dataframe = self.__top_times_df()
        self.events = {}
        self.__compact_df()

        print(self.events["Girls 8 & Under  25 Free"])

        self.is_ranked = False

    def __top_times_df(self):
        """
        This function will use the camelot module to breakdown the Top Times
        Report into a group of Pandas dataframe objects. This returns raw data
        and is not intended to be used publicly.
        """
        # Extract top times tables
        top_times_tables = camelot.read_pdf(self.top_times_pdf, flavor="stream") #, pages="all")

        # Concatenate page-split tables into a unified dataframe
        return pd.concat([page_table.df for page_table in top_times_tables])

    def __compact_df(self):
        """
        Generate a dictionary of events with their corresponding event objects.
        """
        current_event_name = None

        # Iterate over all events and swimmer times
        # NOTE: This is normally not efficient, but we are working with a manageable sample size
        for swimmer in self.__dataframe.itertuples():
            # Set the event from the table
            if swimmer[TableIndex.EVENT] != "" and not swimmer[TableIndex.EVENT].isdigit():
                current_event_name = swimmer[TableIndex.EVENT]
                self.events[current_event_name] = Event(current_event_name)

            elif swimmer[TableIndex.EVENT] == "":
                pass    # This is the heading, ignore

            else:
                # Make sure an event is set
                assert current_event_name is not None

                # Add the swimmer and time to event
                self.events[current_event_name].swimmers.append(
                    Swimmer(
                        current_event_name,
                        swimmer[TableIndex.TIME].split()[0],
                        swimmer[TableIndex.STANDARD],
                        swimmer[TableIndex.NAME],
                        swimmer[TableIndex.AGE],
                        swimmer[TableIndex.TIME_DATE]
                    )
                )


    def generate_rankings(self, opponent):
        """
        Takes in an ReportParser object and gives a ranking for every swimmer in
        each event based on the times of another team's swimmers in the same event.
        """

    def to_csv(self):
        """
        Build a printable report based on ranked results.
        """

if __name__ == "__main__":
    ttr = ReportParser("aratoptimes.pdf")
