from datetime import date

JAN = 1
FEB = 2
MAR = 3
APR = 4
MAY = 5
JUN = 6
JUL = 7
AUG = 8
SEP = 9
OCT = 1
NOV = 11
DEC = 12

# each track has...
READY = 0
MEDIA = 1
CHAPTER = 2
TITLE = 3
TEXTINDEX = 4
DATE = 5

# each part has...
NO_MEDIA = "x"
PART_1 = "1"
PART_2 = "2"
PART_3 = "3"
PART_4 = "4"
PART_5 = "5"
PEOPLE = "People &mdash; The Intrepid Explorers"
PROCESS = "Process &mdash; The Ragged Pathway"
CULTURE = "Culture &mdash; The Promised Land"
CITIZENSHIP = "Citizenship &mdash; a few early notes"
APPENDICES = "Appendices & Afterword "

tracks = [
    [1, "tps_av/prelude.m4a", "", "Prelude", 0, None],
    [1, "tps_av/intro2.m4a", "", "Introduction to Audio Edition", 4, None],
    [1, "tps_av/foreword.m4a", "", "Foreword by Ron Jeffries", 6, None],
    [1, NO_MEDIA, PART_1, PEOPLE, 12, None],
    [1, "tps_av/chapter01.m4a", "1",
        "A New Way of Thinking", 13, date(2008, MAR, 22)],
    [1, "tps_av/chapter02.m4a", "2",
        "The Heart of Scrum", 14, date(2009, AUG, 3)],
    [1, "tps_av/chapter03.m4a", "3",
        "Self-Organization and Anarchy", 15, date(2007, SEP, 13)],
    [1, "tps_av/chapter04.m4a", "4",
        "Shock Therapy...or Compassion?", 17, date(2008, SEP, 15)],
    [1, "tps_av/chapter05.m4a", "5",
        "Software Artisans", 18, date(2005, DEC, 31)],
    [1, "tps_av/chapter06.m4a", "6",
        "Distributed Teams are not Teams", 20, date(2008, JUL, 13)],
    [1, "tps_av/chapter07.m4a", "7",
        "With Great Power", 21, date(2006, AUG, 2)],
    [1, "tps_av/chapter08.m4a", "8",
        "Unearthing Impediments by Doing Less", 23, date(2009, JUN, 23)],
    [1, "tps_av/chapter09.m4a", "9",
        "Test(osterone)-Infected Developers", 25, date(2009, JUN, 25)],
    [1, "tps_av/chapter10.m4a", "10",
        "Paying Off Technical Debt", 26, date(2012, FEB, 12)],
    [1, "tps_av/chapter11.m4a", "11",
        "The Agile Explorer", 27, date(2012, APR, 19)],
    [1, "tps_av/chapter12.m4a", "12",
        "Heartfelt Emotionalism is the New Hardcore", 29, date(2009, JUN, 14)],
    [1, "tps_av/chapter13.m4a", "13",
        "The People&#700;s Scrum", 30, date(2009, DEC, 6)],
    [1, NO_MEDIA, PART_2, PROCESS, 32, None],
    [1, "tps_av/chapter14.m4a", "14",
        "Scrum: Its Place in the World", 33, date(2008, SEP, 26)],
    [1, "tps_av/chapter15.m4a", "15",
        "In Praise of Process *", 36, date(2012, OCT, 6)],
    [1, "tps_av/chapter16.m4a", "16",
        "Deadlines Kill *", 37, date(2012, NOV, 10)],
    [1, "tps_av/chapter17.m4a", "17",
        "The Robustness Index *", 39, date(2012, AUG, 27)],
    [1, "tps_av/chapter18.m4a", "18",
        "The Bug Myth *", 41, date(2012, DEC, 12)],
    [1, "tps_av/chapter19.m4a", "19",
        "Beyond Estimation", 43, date(2011, JAN, 24)],
    [1, "tps_av/chapter20.m4a", "20",
        "Scrum Roles: An Abstraction", 44, date(2009, OCT, 8)],
    [1, "tps_av/chapter21.m4a", "21",
        "Scrum Doesn&#700;t Do Anything", 46, date(2009, OCT, 11)],
    [1, "tps_av/chapter22.m4a", "22", "Marriage, But", 47, date(2011, MAY, 3)],
    [1, "tps_av/chapter23.m4a", "23",
        "Don&#700;t Have Meetings", 47, date(2011, MAR, 25)],
    [1, "tps_av/chapter24.m4a", "24",
        "Timebox != Commitment", 50, date(2012, APR, 20)],
    [1, "tps_av/chapter25.m4a", "25",
        "The Retrospective is Now", 51, date(2011, JAN, 22)],
    [1, "tps_av/chapter26.m4a", "26",
        "The Soul of Scrum", 52, date(2012, FEB, 15)],
    [1, NO_MEDIA, PART_3, CULTURE, 55, None],
    [1, "tps_av/chapter27.m4a", "27",
        "Catastrophic Organizational Change", 56, date(2005, DEC, 5)],
    [1, "tps_av/chapter28.m4a", "28",
        "Agile Anarchy", 57, date(2009, JUN, 10)],
    [1, "tps_av/chapter29.m4a", "29",
        "Riding a Dinosaur", 59, date(2009, MAR, 11)],
    [1, "tps_av/chapter30.m4a", "30",
        "Corporate Oppression", 61, date(2009, MAR, 16)],
    [1, "tps_av/chapter31.m4a", "31",
        "Organizational Blobs", 63, date(2005, DEC, 15)],
    [1, "tps_av/chapter32.m4a", "32",
        "In a Roundabout Sort of Way", 65, date(2009, AUG, 18)],
    [1, "tps_av/chapter33.m4a", "33",
        "The Change Agent&#700;s Blade is Thin and Keen", 66, date(2005, DEC, 23)],
    [1, "tps_av/chapter34.m4a", "34",
        "Scrum Adoption: The Awakening", 68, date(2010, JUL, 3)],
    [1, "tps_av/chapter35.m4a", "35",
        "Team Culture, Project Culture", 70, date(2012, APR, 17)],
    [1, "tps_av/chapter36.m4a", "36",
        "Don&#700;t Build Teams", 72, date(2012, FEB, 26)],
    [1, "tps_av/chapter37.m4a", "37",
        "Scaling Scrum: The Alcoholic Perspective", 73, date(2008, APR, 9)],
    [1, "tps_av/chapter38.m4a", "38",
        "Seeking Consent", 75, date(2012, AUG, 18)],
    [1, "tps_av/chapter39.m4a", "39",
        "The Spirit of Change", 77, date(2012, OCT, 1)],
    [1, NO_MEDIA, PART_5, APPENDICES, 0, None],
    [1, "tps_av/appendix1.m4a", "", "I. Simple Scrum", 80, None],
    [1, "tps_av/appendix2.m4a", "",
     "II. Mindful Scrum (describe this meadow)", 82, None],
    [1, "tps_av/appendix3.m4a", "", "III. The Liberated Scrum Master", 83, None],
    [1, "tps_av/afterword.m4a", "", "Afterword by Lyssa Adkins", 85, None],
    [1, "tps_av/coda.m4a", "", "Coda", 0, None]
]

base_url = "https:#tobiasmayer.uk/works/the-peoples-scrum/"


def download_file(source):
    pass


def download_all_files():
    pass
