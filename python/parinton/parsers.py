def parse_medium():
    """
    There's a common pattern that in every artwork descriptions; he lists what tools
    and medium of the artwork (i.e. "Digital. Photoshop.")

    My approach is to go to the last lines of the description using .split('\n')
    and match mediums and whatever tools he uses
    """

    # TODO use difflib.get_close_matches for this one
    MEDIUM = ['digital', 'traditional']
    PROGRAMS = ['photoshop', 'medibang', 'procreate']
    TRADITIONAL_TOOLS = ['gouaches', 'watercolors',
                         'colored pencils', 'markers', 'indian ink', 'pencils']

    TOOLS = [*MEDIUM, *PROGRAMS, *TRADITIONAL_TOOLS]

    # TODO if nothing is detected, return "Not specified"
    ...


def get_average_dates(dates: list[str]):
    """
    A time series method that gets an average of artworks posted based on a ranges of dates

    :param dates: Requires a list of date strings that will be parsed automatically 
    :return: A dict of the total and average
    """
    ...
