# Generated from /home/ususi/itmo/typesystem/project/stella-typechecker/grammar/stellaParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,89,756,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,1,1,1,1,1,
        1,2,1,2,1,2,1,3,1,3,5,3,48,8,3,10,3,12,3,51,9,3,1,3,5,3,54,8,3,10,
        3,12,3,57,9,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,5,68,8,5,10,
        5,12,5,71,9,5,1,5,1,5,1,6,5,6,76,8,6,10,6,12,6,79,9,6,1,6,1,6,1,
        6,1,6,1,6,1,6,5,6,87,8,6,10,6,12,6,90,9,6,3,6,92,8,6,1,6,1,6,1,6,
        3,6,97,8,6,1,6,1,6,1,6,1,6,5,6,103,8,6,10,6,12,6,106,9,6,3,6,108,
        8,6,1,6,1,6,5,6,112,8,6,10,6,12,6,115,9,6,1,6,1,6,1,6,1,6,1,6,5,
        6,122,8,6,10,6,12,6,125,9,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,134,
        8,6,10,6,12,6,137,9,6,1,6,1,6,1,6,1,6,1,6,5,6,144,8,6,10,6,12,6,
        147,9,6,3,6,149,8,6,1,6,1,6,1,6,3,6,154,8,6,1,6,1,6,1,6,1,6,5,6,
        160,8,6,10,6,12,6,163,9,6,3,6,165,8,6,1,6,1,6,5,6,169,8,6,10,6,12,
        6,172,9,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,3,6,191,8,6,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,339,8,9,10,9,12,9,342,9,9,
        3,9,344,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,356,8,9,
        10,9,12,9,359,9,9,3,9,361,8,9,1,9,1,9,1,9,1,9,1,9,5,9,368,8,9,10,
        9,12,9,371,9,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,379,8,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,5,9,388,8,9,10,9,12,9,391,9,9,3,9,393,8,9,1,9,1,9,
        1,9,1,9,1,9,1,9,5,9,401,8,9,10,9,12,9,404,9,9,3,9,406,8,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,420,8,9,10,9,12,9,
        423,9,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,432,8,9,10,9,12,9,435,9,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,445,8,9,10,9,12,9,448,9,9,
        1,9,1,9,1,9,1,9,1,9,1,9,3,9,456,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,511,
        8,9,10,9,12,9,514,9,9,3,9,516,8,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,524,
        8,9,10,9,12,9,527,9,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,5,9,540,8,9,10,9,12,9,543,9,9,1,10,1,10,1,10,1,10,1,11,1,11,1,
        11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,13,562,8,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,5,13,579,8,13,10,13,12,13,582,9,13,3,13,584,8,13,1,
        13,1,13,1,13,1,13,1,13,5,13,591,8,13,10,13,12,13,594,9,13,3,13,596,
        8,13,1,13,1,13,1,13,1,13,1,13,5,13,603,8,13,10,13,12,13,606,9,13,
        3,13,608,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,3,13,638,8,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,5,13,647,8,13,10,13,12,13,650,9,13,1,14,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,666,8,15,
        10,15,12,15,669,9,15,3,15,671,8,15,1,15,1,15,1,15,1,15,1,15,5,15,
        678,8,15,10,15,12,15,681,9,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,5,15,693,8,15,10,15,12,15,696,9,15,3,15,698,8,15,
        1,15,1,15,1,15,1,15,1,15,5,15,705,8,15,10,15,12,15,708,9,15,1,15,
        1,15,1,15,1,15,1,15,1,15,5,15,716,8,15,10,15,12,15,719,9,15,3,15,
        721,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,3,15,737,8,15,1,15,1,15,1,15,5,15,742,8,15,10,15,
        12,15,745,9,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,3,17,754,8,17,
        1,17,0,3,18,26,30,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,0,0,881,0,36,1,0,0,0,2,39,1,0,0,0,4,42,1,0,0,0,6,45,1,0,0,
        0,8,58,1,0,0,0,10,62,1,0,0,0,12,190,1,0,0,0,14,192,1,0,0,0,16,194,
        1,0,0,0,18,455,1,0,0,0,20,544,1,0,0,0,22,548,1,0,0,0,24,552,1,0,
        0,0,26,637,1,0,0,0,28,651,1,0,0,0,30,736,1,0,0,0,32,746,1,0,0,0,
        34,750,1,0,0,0,36,37,3,6,3,0,37,38,5,0,0,1,38,1,1,0,0,0,39,40,3,
        18,9,0,40,41,5,0,0,1,41,3,1,0,0,0,42,43,3,30,15,0,43,44,5,0,0,1,
        44,5,1,0,0,0,45,49,3,8,4,0,46,48,3,10,5,0,47,46,1,0,0,0,48,51,1,
        0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,55,1,0,0,0,51,49,1,0,0,0,52,
        54,3,12,6,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,
        0,0,56,7,1,0,0,0,57,55,1,0,0,0,58,59,5,51,0,0,59,60,5,39,0,0,60,
        61,5,2,0,0,61,9,1,0,0,0,62,63,5,41,0,0,63,64,5,65,0,0,64,69,5,85,
        0,0,65,66,5,1,0,0,66,68,5,85,0,0,67,65,1,0,0,0,68,71,1,0,0,0,69,
        67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,73,5,2,0,
        0,73,11,1,0,0,0,74,76,3,14,7,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,
        1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,5,44,0,0,
        81,82,5,84,0,0,82,91,5,3,0,0,83,88,3,16,8,0,84,85,5,1,0,0,85,87,
        3,16,8,0,86,84,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,
        89,92,1,0,0,0,90,88,1,0,0,0,91,83,1,0,0,0,91,92,1,0,0,0,92,93,1,
        0,0,0,93,96,5,4,0,0,94,95,5,9,0,0,95,97,3,30,15,0,96,94,1,0,0,0,
        96,97,1,0,0,0,97,107,1,0,0,0,98,99,5,60,0,0,99,104,3,30,15,0,100,
        101,5,1,0,0,101,103,3,30,15,0,102,100,1,0,0,0,103,106,1,0,0,0,104,
        102,1,0,0,0,104,105,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,107,
        98,1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,113,5,5,0,0,110,112,
        3,12,6,0,111,110,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,
        1,0,0,0,114,116,1,0,0,0,115,113,1,0,0,0,116,117,5,57,0,0,117,118,
        3,18,9,0,118,119,5,6,0,0,119,191,1,0,0,0,120,122,3,14,7,0,121,120,
        1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,126,
        1,0,0,0,125,123,1,0,0,0,126,127,5,80,0,0,127,128,5,44,0,0,128,129,
        5,84,0,0,129,130,5,14,0,0,130,135,5,84,0,0,131,132,5,1,0,0,132,134,
        5,84,0,0,133,131,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,
        1,0,0,0,136,138,1,0,0,0,137,135,1,0,0,0,138,139,5,15,0,0,139,148,
        5,3,0,0,140,145,3,16,8,0,141,142,5,1,0,0,142,144,3,16,8,0,143,141,
        1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,149,
        1,0,0,0,147,145,1,0,0,0,148,140,1,0,0,0,148,149,1,0,0,0,149,150,
        1,0,0,0,150,153,5,4,0,0,151,152,5,9,0,0,152,154,3,30,15,0,153,151,
        1,0,0,0,153,154,1,0,0,0,154,164,1,0,0,0,155,156,5,60,0,0,156,161,
        3,30,15,0,157,158,5,1,0,0,158,160,3,30,15,0,159,157,1,0,0,0,160,
        163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,165,1,0,0,0,163,
        161,1,0,0,0,164,155,1,0,0,0,164,165,1,0,0,0,165,166,1,0,0,0,166,
        170,5,5,0,0,167,169,3,12,6,0,168,167,1,0,0,0,169,172,1,0,0,0,170,
        168,1,0,0,0,170,171,1,0,0,0,171,173,1,0,0,0,172,170,1,0,0,0,173,
        174,5,57,0,0,174,175,3,18,9,0,175,176,5,6,0,0,176,191,1,0,0,0,177,
        178,5,62,0,0,178,179,5,84,0,0,179,180,5,7,0,0,180,191,3,30,15,0,
        181,182,5,67,0,0,182,183,5,62,0,0,183,184,5,7,0,0,184,191,3,30,15,
        0,185,186,5,67,0,0,186,187,5,68,0,0,187,188,5,84,0,0,188,189,5,8,
        0,0,189,191,3,30,15,0,190,77,1,0,0,0,190,123,1,0,0,0,190,177,1,0,
        0,0,190,181,1,0,0,0,190,185,1,0,0,0,191,13,1,0,0,0,192,193,5,49,
        0,0,193,15,1,0,0,0,194,195,5,84,0,0,195,196,5,8,0,0,196,197,3,30,
        15,0,197,17,1,0,0,0,198,199,6,9,-1,0,199,456,5,61,0,0,200,456,5,
        42,0,0,201,456,5,64,0,0,202,456,5,87,0,0,203,456,5,86,0,0,204,456,
        5,84,0,0,205,456,5,73,0,0,206,207,5,74,0,0,207,208,5,3,0,0,208,209,
        3,18,9,0,209,210,5,4,0,0,210,456,1,0,0,0,211,212,5,75,0,0,212,213,
        5,5,0,0,213,214,3,18,9,0,214,215,5,6,0,0,215,216,5,76,0,0,216,217,
        5,5,0,0,217,218,3,26,13,0,218,219,5,10,0,0,219,220,3,18,9,0,220,
        221,5,6,0,0,221,456,1,0,0,0,222,223,5,75,0,0,223,224,5,5,0,0,224,
        225,3,18,9,0,225,226,5,6,0,0,226,227,5,69,0,0,227,228,5,37,0,0,228,
        229,3,30,15,0,229,230,5,5,0,0,230,231,3,26,13,0,231,232,5,10,0,0,
        232,233,3,18,9,0,233,234,5,6,0,0,234,235,5,65,0,0,235,236,5,5,0,
        0,236,237,3,18,9,0,237,238,5,6,0,0,238,456,1,0,0,0,239,240,5,75,
        0,0,240,241,5,5,0,0,241,242,3,18,9,0,242,243,5,6,0,0,243,244,5,65,
        0,0,244,245,5,5,0,0,245,246,3,18,9,0,246,247,5,6,0,0,247,456,1,0,
        0,0,248,249,5,48,0,0,249,250,5,3,0,0,250,251,3,18,9,0,251,252,5,
        4,0,0,252,456,1,0,0,0,253,254,5,50,0,0,254,255,5,3,0,0,255,256,3,
        18,9,0,256,257,5,4,0,0,257,456,1,0,0,0,258,259,5,38,0,0,259,260,
        5,3,0,0,260,261,3,18,9,0,261,262,5,1,0,0,262,263,3,18,9,0,263,264,
        5,4,0,0,264,456,1,0,0,0,265,266,5,27,0,0,266,267,5,3,0,0,267,268,
        3,18,9,0,268,269,5,4,0,0,269,456,1,0,0,0,270,271,5,28,0,0,271,272,
        5,3,0,0,272,273,3,18,9,0,273,274,5,4,0,0,274,456,1,0,0,0,275,276,
        5,29,0,0,276,277,5,3,0,0,277,278,3,18,9,0,278,279,5,4,0,0,279,456,
        1,0,0,0,280,281,5,58,0,0,281,282,5,3,0,0,282,283,3,18,9,0,283,284,
        5,4,0,0,284,456,1,0,0,0,285,286,5,55,0,0,286,287,5,3,0,0,287,288,
        3,18,9,0,288,289,5,4,0,0,289,456,1,0,0,0,290,291,5,30,0,0,291,292,
        5,3,0,0,292,293,3,18,9,0,293,294,5,4,0,0,294,456,1,0,0,0,295,296,
        5,31,0,0,296,297,5,3,0,0,297,298,3,18,9,0,298,299,5,4,0,0,299,456,
        1,0,0,0,300,301,5,43,0,0,301,302,5,3,0,0,302,303,3,18,9,0,303,304,
        5,4,0,0,304,456,1,0,0,0,305,306,5,32,0,0,306,307,5,3,0,0,307,308,
        3,18,9,0,308,309,5,1,0,0,309,310,3,18,9,0,310,311,5,1,0,0,311,312,
        3,18,9,0,312,313,5,4,0,0,313,456,1,0,0,0,314,315,5,45,0,0,315,316,
        5,14,0,0,316,317,3,30,15,0,317,318,5,15,0,0,318,319,3,18,9,34,319,
        456,1,0,0,0,320,321,5,63,0,0,321,322,5,14,0,0,322,323,3,30,15,0,
        323,324,5,15,0,0,324,325,3,18,9,33,325,456,1,0,0,0,326,327,5,72,
        0,0,327,328,5,3,0,0,328,329,3,18,9,0,329,330,5,4,0,0,330,456,1,0,
        0,0,331,332,5,24,0,0,332,456,3,18,9,26,333,334,5,44,0,0,334,343,
        5,3,0,0,335,340,3,16,8,0,336,337,5,1,0,0,337,339,3,16,8,0,338,336,
        1,0,0,0,339,342,1,0,0,0,340,338,1,0,0,0,340,341,1,0,0,0,341,344,
        1,0,0,0,342,340,1,0,0,0,343,335,1,0,0,0,343,344,1,0,0,0,344,345,
        1,0,0,0,345,346,5,4,0,0,346,347,5,5,0,0,347,348,5,57,0,0,348,349,
        3,18,9,0,349,350,5,6,0,0,350,456,1,0,0,0,351,360,5,5,0,0,352,357,
        3,18,9,0,353,354,5,1,0,0,354,356,3,18,9,0,355,353,1,0,0,0,356,359,
        1,0,0,0,357,355,1,0,0,0,357,358,1,0,0,0,358,361,1,0,0,0,359,357,
        1,0,0,0,360,352,1,0,0,0,360,361,1,0,0,0,361,362,1,0,0,0,362,456,
        5,6,0,0,363,364,5,5,0,0,364,369,3,22,11,0,365,366,5,1,0,0,366,368,
        3,22,11,0,367,365,1,0,0,0,368,371,1,0,0,0,369,367,1,0,0,0,369,370,
        1,0,0,0,370,372,1,0,0,0,371,369,1,0,0,0,372,373,5,6,0,0,373,456,
        1,0,0,0,374,375,5,12,0,0,375,378,5,84,0,0,376,377,5,7,0,0,377,379,
        3,18,9,0,378,376,1,0,0,0,378,379,1,0,0,0,379,380,1,0,0,0,380,456,
        5,13,0,0,381,382,5,54,0,0,382,383,3,18,9,0,383,392,5,5,0,0,384,389,
        3,24,12,0,385,386,5,11,0,0,386,388,3,24,12,0,387,385,1,0,0,0,388,
        391,1,0,0,0,389,387,1,0,0,0,389,390,1,0,0,0,390,393,1,0,0,0,391,
        389,1,0,0,0,392,384,1,0,0,0,392,393,1,0,0,0,393,394,1,0,0,0,394,
        395,5,6,0,0,395,456,1,0,0,0,396,405,5,14,0,0,397,402,3,18,9,0,398,
        399,5,1,0,0,399,401,3,18,9,0,400,398,1,0,0,0,401,404,1,0,0,0,402,
        400,1,0,0,0,402,403,1,0,0,0,403,406,1,0,0,0,404,402,1,0,0,0,405,
        397,1,0,0,0,405,406,1,0,0,0,406,407,1,0,0,0,407,456,5,15,0,0,408,
        409,5,46,0,0,409,410,3,18,9,0,410,411,5,59,0,0,411,412,3,18,9,0,
        412,413,5,40,0,0,413,414,3,18,9,7,414,456,1,0,0,0,415,416,5,52,0,
        0,416,421,3,20,10,0,417,418,5,1,0,0,418,420,3,20,10,0,419,417,1,
        0,0,0,420,423,1,0,0,0,421,419,1,0,0,0,421,422,1,0,0,0,422,424,1,
        0,0,0,423,421,1,0,0,0,424,425,5,47,0,0,425,426,3,18,9,5,426,456,
        1,0,0,0,427,428,5,53,0,0,428,433,3,20,10,0,429,430,5,1,0,0,430,432,
        3,20,10,0,431,429,1,0,0,0,432,435,1,0,0,0,433,431,1,0,0,0,433,434,
        1,0,0,0,434,436,1,0,0,0,435,433,1,0,0,0,436,437,5,47,0,0,437,438,
        3,18,9,4,438,456,1,0,0,0,439,440,5,80,0,0,440,441,5,14,0,0,441,446,
        5,84,0,0,442,443,5,1,0,0,443,445,5,84,0,0,444,442,1,0,0,0,445,448,
        1,0,0,0,446,444,1,0,0,0,446,447,1,0,0,0,447,449,1,0,0,0,448,446,
        1,0,0,0,449,450,5,15,0,0,450,456,3,18,9,3,451,452,5,3,0,0,452,453,
        3,18,9,0,453,454,5,4,0,0,454,456,1,0,0,0,455,198,1,0,0,0,455,200,
        1,0,0,0,455,201,1,0,0,0,455,202,1,0,0,0,455,203,1,0,0,0,455,204,
        1,0,0,0,455,205,1,0,0,0,455,206,1,0,0,0,455,211,1,0,0,0,455,222,
        1,0,0,0,455,239,1,0,0,0,455,248,1,0,0,0,455,253,1,0,0,0,455,258,
        1,0,0,0,455,265,1,0,0,0,455,270,1,0,0,0,455,275,1,0,0,0,455,280,
        1,0,0,0,455,285,1,0,0,0,455,290,1,0,0,0,455,295,1,0,0,0,455,300,
        1,0,0,0,455,305,1,0,0,0,455,314,1,0,0,0,455,320,1,0,0,0,455,326,
        1,0,0,0,455,331,1,0,0,0,455,333,1,0,0,0,455,351,1,0,0,0,455,363,
        1,0,0,0,455,374,1,0,0,0,455,381,1,0,0,0,455,396,1,0,0,0,455,408,
        1,0,0,0,455,415,1,0,0,0,455,427,1,0,0,0,455,439,1,0,0,0,455,451,
        1,0,0,0,456,541,1,0,0,0,457,458,10,30,0,0,458,459,5,24,0,0,459,540,
        3,18,9,31,460,461,10,29,0,0,461,462,5,25,0,0,462,540,3,18,9,30,463,
        464,10,28,0,0,464,465,5,36,0,0,465,540,3,18,9,29,466,467,10,25,0,
        0,467,468,5,22,0,0,468,540,3,18,9,26,469,470,10,24,0,0,470,471,5,
        23,0,0,471,540,3,18,9,25,472,473,10,23,0,0,473,474,5,56,0,0,474,
        540,3,18,9,24,475,476,10,14,0,0,476,477,5,16,0,0,477,540,3,18,9,
        15,478,479,10,13,0,0,479,480,5,17,0,0,480,540,3,18,9,14,481,482,
        10,12,0,0,482,483,5,18,0,0,483,540,3,18,9,13,484,485,10,11,0,0,485,
        486,5,19,0,0,486,540,3,18,9,12,487,488,10,10,0,0,488,489,5,20,0,
        0,489,540,3,18,9,11,490,491,10,9,0,0,491,492,5,21,0,0,492,540,3,
        18,9,10,493,494,10,8,0,0,494,495,5,70,0,0,495,540,3,18,9,9,496,497,
        10,6,0,0,497,498,5,2,0,0,498,540,3,18,9,7,499,500,10,59,0,0,500,
        501,5,26,0,0,501,540,5,84,0,0,502,503,10,58,0,0,503,504,5,26,0,0,
        504,540,5,87,0,0,505,506,10,32,0,0,506,515,5,3,0,0,507,512,3,18,
        9,0,508,509,5,1,0,0,509,511,3,18,9,0,510,508,1,0,0,0,511,514,1,0,
        0,0,512,510,1,0,0,0,512,513,1,0,0,0,513,516,1,0,0,0,514,512,1,0,
        0,0,515,507,1,0,0,0,515,516,1,0,0,0,516,517,1,0,0,0,517,540,5,4,
        0,0,518,519,10,31,0,0,519,520,5,14,0,0,520,525,3,30,15,0,521,522,
        5,1,0,0,522,524,3,30,15,0,523,521,1,0,0,0,524,527,1,0,0,0,525,523,
        1,0,0,0,525,526,1,0,0,0,526,528,1,0,0,0,527,525,1,0,0,0,528,529,
        5,15,0,0,529,540,1,0,0,0,530,531,10,22,0,0,531,532,5,37,0,0,532,
        540,3,30,15,0,533,534,10,21,0,0,534,535,5,69,0,0,535,536,5,37,0,
        0,536,540,3,30,15,0,537,538,10,1,0,0,538,540,5,2,0,0,539,457,1,0,
        0,0,539,460,1,0,0,0,539,463,1,0,0,0,539,466,1,0,0,0,539,469,1,0,
        0,0,539,472,1,0,0,0,539,475,1,0,0,0,539,478,1,0,0,0,539,481,1,0,
        0,0,539,484,1,0,0,0,539,487,1,0,0,0,539,490,1,0,0,0,539,493,1,0,
        0,0,539,496,1,0,0,0,539,499,1,0,0,0,539,502,1,0,0,0,539,505,1,0,
        0,0,539,518,1,0,0,0,539,530,1,0,0,0,539,533,1,0,0,0,539,537,1,0,
        0,0,540,543,1,0,0,0,541,539,1,0,0,0,541,542,1,0,0,0,542,19,1,0,0,
        0,543,541,1,0,0,0,544,545,3,26,13,0,545,546,5,7,0,0,546,547,3,18,
        9,0,547,21,1,0,0,0,548,549,5,84,0,0,549,550,5,7,0,0,550,551,3,18,
        9,0,551,23,1,0,0,0,552,553,3,26,13,0,553,554,5,10,0,0,554,555,3,
        18,9,0,555,25,1,0,0,0,556,557,6,13,-1,0,557,558,5,12,0,0,558,561,
        5,84,0,0,559,560,5,7,0,0,560,562,3,26,13,0,561,559,1,0,0,0,561,562,
        1,0,0,0,562,563,1,0,0,0,563,638,5,13,0,0,564,565,5,48,0,0,565,566,
        5,3,0,0,566,567,3,26,13,0,567,568,5,4,0,0,568,638,1,0,0,0,569,570,
        5,50,0,0,570,571,5,3,0,0,571,572,3,26,13,0,572,573,5,4,0,0,573,638,
        1,0,0,0,574,583,5,5,0,0,575,580,3,26,13,0,576,577,5,1,0,0,577,579,
        3,26,13,0,578,576,1,0,0,0,579,582,1,0,0,0,580,578,1,0,0,0,580,581,
        1,0,0,0,581,584,1,0,0,0,582,580,1,0,0,0,583,575,1,0,0,0,583,584,
        1,0,0,0,584,585,1,0,0,0,585,638,5,6,0,0,586,595,5,5,0,0,587,592,
        3,28,14,0,588,589,5,1,0,0,589,591,3,28,14,0,590,588,1,0,0,0,591,
        594,1,0,0,0,592,590,1,0,0,0,592,593,1,0,0,0,593,596,1,0,0,0,594,
        592,1,0,0,0,595,587,1,0,0,0,595,596,1,0,0,0,596,597,1,0,0,0,597,
        638,5,6,0,0,598,607,5,14,0,0,599,604,3,26,13,0,600,601,5,1,0,0,601,
        603,3,26,13,0,602,600,1,0,0,0,603,606,1,0,0,0,604,602,1,0,0,0,604,
        605,1,0,0,0,605,608,1,0,0,0,606,604,1,0,0,0,607,599,1,0,0,0,607,
        608,1,0,0,0,608,609,1,0,0,0,609,638,5,15,0,0,610,611,5,38,0,0,611,
        612,5,3,0,0,612,613,3,26,13,0,613,614,5,1,0,0,614,615,3,26,13,0,
        615,616,5,4,0,0,616,638,1,0,0,0,617,618,5,3,0,0,618,619,3,26,13,
        0,619,620,5,1,0,0,620,621,3,26,13,0,621,622,5,4,0,0,622,638,1,0,
        0,0,623,638,5,42,0,0,624,638,5,61,0,0,625,638,5,64,0,0,626,638,5,
        87,0,0,627,628,5,58,0,0,628,629,5,3,0,0,629,630,3,26,13,0,630,631,
        5,4,0,0,631,638,1,0,0,0,632,638,5,84,0,0,633,634,5,3,0,0,634,635,
        3,26,13,0,635,636,5,4,0,0,636,638,1,0,0,0,637,556,1,0,0,0,637,564,
        1,0,0,0,637,569,1,0,0,0,637,574,1,0,0,0,637,586,1,0,0,0,637,598,
        1,0,0,0,637,610,1,0,0,0,637,617,1,0,0,0,637,623,1,0,0,0,637,624,
        1,0,0,0,637,625,1,0,0,0,637,626,1,0,0,0,637,627,1,0,0,0,637,632,
        1,0,0,0,637,633,1,0,0,0,638,648,1,0,0,0,639,640,10,3,0,0,640,641,
        5,37,0,0,641,647,3,30,15,0,642,643,10,2,0,0,643,644,5,69,0,0,644,
        645,5,37,0,0,645,647,3,30,15,0,646,639,1,0,0,0,646,642,1,0,0,0,647,
        650,1,0,0,0,648,646,1,0,0,0,648,649,1,0,0,0,649,27,1,0,0,0,650,648,
        1,0,0,0,651,652,5,84,0,0,652,653,5,7,0,0,653,654,3,26,13,0,654,29,
        1,0,0,0,655,656,6,15,-1,0,656,737,5,33,0,0,657,737,5,34,0,0,658,
        659,5,71,0,0,659,737,3,30,15,15,660,661,5,44,0,0,661,670,5,3,0,0,
        662,667,3,30,15,0,663,664,5,1,0,0,664,666,3,30,15,0,665,663,1,0,
        0,0,666,669,1,0,0,0,667,665,1,0,0,0,667,668,1,0,0,0,668,671,1,0,
        0,0,669,667,1,0,0,0,670,662,1,0,0,0,670,671,1,0,0,0,671,672,1,0,
        0,0,672,673,5,4,0,0,673,674,5,9,0,0,674,737,3,30,15,13,675,679,5,
        81,0,0,676,678,5,84,0,0,677,676,1,0,0,0,678,681,1,0,0,0,679,677,
        1,0,0,0,679,680,1,0,0,0,680,682,1,0,0,0,681,679,1,0,0,0,682,683,
        5,26,0,0,683,737,3,30,15,12,684,685,5,66,0,0,685,686,5,84,0,0,686,
        687,5,26,0,0,687,737,3,30,15,11,688,697,5,5,0,0,689,694,3,30,15,
        0,690,691,5,1,0,0,691,693,3,30,15,0,692,690,1,0,0,0,693,696,1,0,
        0,0,694,692,1,0,0,0,694,695,1,0,0,0,695,698,1,0,0,0,696,694,1,0,
        0,0,697,689,1,0,0,0,697,698,1,0,0,0,698,699,1,0,0,0,699,737,5,6,
        0,0,700,701,5,5,0,0,701,706,3,32,16,0,702,703,5,1,0,0,703,705,3,
        32,16,0,704,702,1,0,0,0,705,708,1,0,0,0,706,704,1,0,0,0,706,707,
        1,0,0,0,707,709,1,0,0,0,708,706,1,0,0,0,709,710,5,6,0,0,710,737,
        1,0,0,0,711,720,5,12,0,0,712,717,3,34,17,0,713,714,5,1,0,0,714,716,
        3,34,17,0,715,713,1,0,0,0,716,719,1,0,0,0,717,715,1,0,0,0,717,718,
        1,0,0,0,718,721,1,0,0,0,719,717,1,0,0,0,720,712,1,0,0,0,720,721,
        1,0,0,0,721,722,1,0,0,0,722,737,5,13,0,0,723,724,5,14,0,0,724,725,
        3,30,15,0,725,726,5,15,0,0,726,737,1,0,0,0,727,737,5,35,0,0,728,
        737,5,77,0,0,729,737,5,78,0,0,730,737,5,79,0,0,731,737,5,84,0,0,
        732,733,5,3,0,0,733,734,3,30,15,0,734,735,5,4,0,0,735,737,1,0,0,
        0,736,655,1,0,0,0,736,657,1,0,0,0,736,658,1,0,0,0,736,660,1,0,0,
        0,736,675,1,0,0,0,736,684,1,0,0,0,736,688,1,0,0,0,736,700,1,0,0,
        0,736,711,1,0,0,0,736,723,1,0,0,0,736,727,1,0,0,0,736,728,1,0,0,
        0,736,729,1,0,0,0,736,730,1,0,0,0,736,731,1,0,0,0,736,732,1,0,0,
        0,737,743,1,0,0,0,738,739,10,14,0,0,739,740,5,22,0,0,740,742,3,30,
        15,15,741,738,1,0,0,0,742,745,1,0,0,0,743,741,1,0,0,0,743,744,1,
        0,0,0,744,31,1,0,0,0,745,743,1,0,0,0,746,747,5,84,0,0,747,748,5,
        8,0,0,748,749,3,30,15,0,749,33,1,0,0,0,750,753,5,84,0,0,751,752,
        5,8,0,0,752,754,3,30,15,0,753,751,1,0,0,0,753,754,1,0,0,0,754,35,
        1,0,0,0,59,49,55,69,77,88,91,96,104,107,113,123,135,145,148,153,
        161,164,170,190,340,343,357,360,369,378,389,392,402,405,421,433,
        446,455,512,515,525,539,541,561,580,583,592,595,604,607,637,646,
        648,667,670,679,694,697,706,717,720,736,743,753
    ]

class stellaParser ( Parser ):

    grammarFileName = "stellaParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "';'", "'('", "')'", "'{'", "'}'", 
                     "'='", "':'", "'->'", "'=>'", "'|'", "'<|'", "'|>'", 
                     "'['", "']'", "'<'", "'<='", "'>'", "'>='", "'=='", 
                     "'!='", "'+'", "'-'", "'*'", "'/'", "'.'", "'List::head'", 
                     "'List::isempty'", "'List::tail'", "'Nat::pred'", "'Nat::iszero'", 
                     "'Nat::rec'", "'Bool'", "'Nat'", "'Unit'", "'and'", 
                     "'as'", "'cons'", "'core'", "'else'", "'extend'", "'false'", 
                     "'fix'", "'fn'", "'fold'", "'if'", "'in'", "'inl'", 
                     "'inline'", "'inr'", "'language'", "'let'", "'letrec'", 
                     "'match'", "'not'", "'or'", "'return'", "'succ'", "'then'", 
                     "'throws'", "'true'", "'type'", "'unfold'", "'unit'", 
                     "'with'", "'\\u00B5'", "'exception'", "'variant'", 
                     "'cast'", "':='", "'&'", "'new'", "'panic!'", "'throw'", 
                     "'try'", "'catch'", "'Top'", "'Bot'", "'auto'", "'generic'", 
                     "'forall'" ]

    symbolicNames = [ "<INVALID>", "Surrogate_id_SYMB_0", "Surrogate_id_SYMB_1", 
                      "Surrogate_id_SYMB_2", "Surrogate_id_SYMB_3", "Surrogate_id_SYMB_4", 
                      "Surrogate_id_SYMB_5", "Surrogate_id_SYMB_6", "Surrogate_id_SYMB_7", 
                      "Surrogate_id_SYMB_8", "Surrogate_id_SYMB_9", "Surrogate_id_SYMB_10", 
                      "Surrogate_id_SYMB_11", "Surrogate_id_SYMB_12", "Surrogate_id_SYMB_13", 
                      "Surrogate_id_SYMB_14", "Surrogate_id_SYMB_15", "Surrogate_id_SYMB_16", 
                      "Surrogate_id_SYMB_17", "Surrogate_id_SYMB_18", "Surrogate_id_SYMB_19", 
                      "Surrogate_id_SYMB_20", "Surrogate_id_SYMB_21", "Surrogate_id_SYMB_22", 
                      "Surrogate_id_SYMB_23", "Surrogate_id_SYMB_24", "Surrogate_id_SYMB_25", 
                      "Surrogate_id_SYMB_26", "Surrogate_id_SYMB_27", "Surrogate_id_SYMB_28", 
                      "Surrogate_id_SYMB_29", "Surrogate_id_SYMB_30", "Surrogate_id_SYMB_31", 
                      "Surrogate_id_SYMB_32", "Surrogate_id_SYMB_33", "Surrogate_id_SYMB_34", 
                      "Surrogate_id_SYMB_35", "Surrogate_id_SYMB_36", "Surrogate_id_SYMB_37", 
                      "Surrogate_id_SYMB_38", "Surrogate_id_SYMB_39", "Surrogate_id_SYMB_40", 
                      "Surrogate_id_SYMB_41", "Surrogate_id_SYMB_42", "Surrogate_id_SYMB_43", 
                      "Surrogate_id_SYMB_44", "Surrogate_id_SYMB_45", "Surrogate_id_SYMB_46", 
                      "Surrogate_id_SYMB_47", "Surrogate_id_SYMB_48", "Surrogate_id_SYMB_49", 
                      "Surrogate_id_SYMB_50", "Surrogate_id_SYMB_51", "Surrogate_id_SYMB_52", 
                      "Surrogate_id_SYMB_53", "Surrogate_id_SYMB_54", "Surrogate_id_SYMB_55", 
                      "Surrogate_id_SYMB_56", "Surrogate_id_SYMB_57", "Surrogate_id_SYMB_58", 
                      "Surrogate_id_SYMB_59", "Surrogate_id_SYMB_60", "Surrogate_id_SYMB_61", 
                      "Surrogate_id_SYMB_62", "Surrogate_id_SYMB_63", "Surrogate_id_SYMB_64", 
                      "Surrogate_id_SYMB_65", "EXCEPTION", "VARIANT", "CAST", 
                      "ASSIGN", "REF_TYPE", "REFERENCE", "PANIC", "THROW", 
                      "TRY", "CATCH", "TOP_TYPE", "BOTTOM_TYPE", "AUTO_TYPE", 
                      "GENERIC", "FORALL", "COMMENT_antlr_builtin", "MULTICOMMENT_antlr_builtin", 
                      "StellaIdent", "ExtensionName", "MemoryAddress", "INTEGER", 
                      "WS", "ErrorToken" ]

    RULE_start_Program = 0
    RULE_start_Expr = 1
    RULE_start_Type = 2
    RULE_program = 3
    RULE_languageDecl = 4
    RULE_extension = 5
    RULE_decl = 6
    RULE_annotation = 7
    RULE_paramDecl = 8
    RULE_expr = 9
    RULE_patternBinding = 10
    RULE_binding = 11
    RULE_matchCase = 12
    RULE_pattern = 13
    RULE_labelledPattern = 14
    RULE_stellatype = 15
    RULE_recordFieldType = 16
    RULE_variantFieldType = 17

    ruleNames =  [ "start_Program", "start_Expr", "start_Type", "program", 
                   "languageDecl", "extension", "decl", "annotation", "paramDecl", 
                   "expr", "patternBinding", "binding", "matchCase", "pattern", 
                   "labelledPattern", "stellatype", "recordFieldType", "variantFieldType" ]

    EOF = Token.EOF
    Surrogate_id_SYMB_0=1
    Surrogate_id_SYMB_1=2
    Surrogate_id_SYMB_2=3
    Surrogate_id_SYMB_3=4
    Surrogate_id_SYMB_4=5
    Surrogate_id_SYMB_5=6
    Surrogate_id_SYMB_6=7
    Surrogate_id_SYMB_7=8
    Surrogate_id_SYMB_8=9
    Surrogate_id_SYMB_9=10
    Surrogate_id_SYMB_10=11
    Surrogate_id_SYMB_11=12
    Surrogate_id_SYMB_12=13
    Surrogate_id_SYMB_13=14
    Surrogate_id_SYMB_14=15
    Surrogate_id_SYMB_15=16
    Surrogate_id_SYMB_16=17
    Surrogate_id_SYMB_17=18
    Surrogate_id_SYMB_18=19
    Surrogate_id_SYMB_19=20
    Surrogate_id_SYMB_20=21
    Surrogate_id_SYMB_21=22
    Surrogate_id_SYMB_22=23
    Surrogate_id_SYMB_23=24
    Surrogate_id_SYMB_24=25
    Surrogate_id_SYMB_25=26
    Surrogate_id_SYMB_26=27
    Surrogate_id_SYMB_27=28
    Surrogate_id_SYMB_28=29
    Surrogate_id_SYMB_29=30
    Surrogate_id_SYMB_30=31
    Surrogate_id_SYMB_31=32
    Surrogate_id_SYMB_32=33
    Surrogate_id_SYMB_33=34
    Surrogate_id_SYMB_34=35
    Surrogate_id_SYMB_35=36
    Surrogate_id_SYMB_36=37
    Surrogate_id_SYMB_37=38
    Surrogate_id_SYMB_38=39
    Surrogate_id_SYMB_39=40
    Surrogate_id_SYMB_40=41
    Surrogate_id_SYMB_41=42
    Surrogate_id_SYMB_42=43
    Surrogate_id_SYMB_43=44
    Surrogate_id_SYMB_44=45
    Surrogate_id_SYMB_45=46
    Surrogate_id_SYMB_46=47
    Surrogate_id_SYMB_47=48
    Surrogate_id_SYMB_48=49
    Surrogate_id_SYMB_49=50
    Surrogate_id_SYMB_50=51
    Surrogate_id_SYMB_51=52
    Surrogate_id_SYMB_52=53
    Surrogate_id_SYMB_53=54
    Surrogate_id_SYMB_54=55
    Surrogate_id_SYMB_55=56
    Surrogate_id_SYMB_56=57
    Surrogate_id_SYMB_57=58
    Surrogate_id_SYMB_58=59
    Surrogate_id_SYMB_59=60
    Surrogate_id_SYMB_60=61
    Surrogate_id_SYMB_61=62
    Surrogate_id_SYMB_62=63
    Surrogate_id_SYMB_63=64
    Surrogate_id_SYMB_64=65
    Surrogate_id_SYMB_65=66
    EXCEPTION=67
    VARIANT=68
    CAST=69
    ASSIGN=70
    REF_TYPE=71
    REFERENCE=72
    PANIC=73
    THROW=74
    TRY=75
    CATCH=76
    TOP_TYPE=77
    BOTTOM_TYPE=78
    AUTO_TYPE=79
    GENERIC=80
    FORALL=81
    COMMENT_antlr_builtin=82
    MULTICOMMENT_antlr_builtin=83
    StellaIdent=84
    ExtensionName=85
    MemoryAddress=86
    INTEGER=87
    WS=88
    ErrorToken=89

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Start_ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.x = None # ProgramContext

        def EOF(self):
            return self.getToken(stellaParser.EOF, 0)

        def program(self):
            return self.getTypedRuleContext(stellaParser.ProgramContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_start_Program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_Program" ):
                listener.enterStart_Program(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_Program" ):
                listener.exitStart_Program(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_Program" ):
                return visitor.visitStart_Program(self)
            else:
                return visitor.visitChildren(self)




    def start_Program(self):

        localctx = stellaParser.Start_ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start_Program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            localctx.x = self.program()
            self.state = 37
            self.match(stellaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.x = None # ExprContext

        def EOF(self):
            return self.getToken(stellaParser.EOF, 0)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_start_Expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_Expr" ):
                listener.enterStart_Expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_Expr" ):
                listener.exitStart_Expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_Expr" ):
                return visitor.visitStart_Expr(self)
            else:
                return visitor.visitChildren(self)




    def start_Expr(self):

        localctx = stellaParser.Start_ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start_Expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            localctx.x = self.expr(0)
            self.state = 40
            self.match(stellaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.x = None # StellatypeContext

        def EOF(self):
            return self.getToken(stellaParser.EOF, 0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_start_Type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_Type" ):
                listener.enterStart_Type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_Type" ):
                listener.exitStart_Type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_Type" ):
                return visitor.visitStart_Type(self)
            else:
                return visitor.visitChildren(self)




    def start_Type(self):

        localctx = stellaParser.Start_TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_start_Type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            localctx.x = self.stellatype(0)
            self.state = 43
            self.match(stellaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._extension = None # ExtensionContext
            self.extensions = list() # of ExtensionContexts
            self._decl = None # DeclContext
            self.decls = list() # of DeclContexts

        def languageDecl(self):
            return self.getTypedRuleContext(stellaParser.LanguageDeclContext,0)


        def extension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExtensionContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExtensionContext,i)


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.DeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.DeclContext,i)


        def getRuleIndex(self):
            return stellaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = stellaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.languageDecl()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 46
                localctx._extension = self.extension()
                localctx.extensions.append(localctx._extension)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 44)) & ~0x3f) == 0 and ((1 << (_la - 44)) & 68728127521) != 0):
                self.state = 52
                localctx._decl = self.decl()
                localctx.decls.append(localctx._decl)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LanguageDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_languageDecl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LanguageCoreContext(LanguageDeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.LanguageDeclContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_50(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_50, 0)
        def Surrogate_id_SYMB_38(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_38, 0)
        def Surrogate_id_SYMB_1(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_1, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLanguageCore" ):
                listener.enterLanguageCore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLanguageCore" ):
                listener.exitLanguageCore(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLanguageCore" ):
                return visitor.visitLanguageCore(self)
            else:
                return visitor.visitChildren(self)



    def languageDecl(self):

        localctx = stellaParser.LanguageDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_languageDecl)
        try:
            localctx = stellaParser.LanguageCoreContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(stellaParser.Surrogate_id_SYMB_50)
            self.state = 59
            self.match(stellaParser.Surrogate_id_SYMB_38)
            self.state = 60
            self.match(stellaParser.Surrogate_id_SYMB_1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_extension

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AnExtensionContext(ExtensionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExtensionContext
            super().__init__(parser)
            self._ExtensionName = None # Token
            self.extensionNames = list() # of Tokens
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_40(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_40, 0)
        def Surrogate_id_SYMB_64(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_64, 0)
        def Surrogate_id_SYMB_1(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_1, 0)
        def ExtensionName(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.ExtensionName)
            else:
                return self.getToken(stellaParser.ExtensionName, i)
        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnExtension" ):
                listener.enterAnExtension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnExtension" ):
                listener.exitAnExtension(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnExtension" ):
                return visitor.visitAnExtension(self)
            else:
                return visitor.visitChildren(self)



    def extension(self):

        localctx = stellaParser.ExtensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_extension)
        self._la = 0 # Token type
        try:
            localctx = stellaParser.AnExtensionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(stellaParser.Surrogate_id_SYMB_40)
            self.state = 63
            self.match(stellaParser.Surrogate_id_SYMB_64)
            self.state = 64
            localctx._ExtensionName = self.match(stellaParser.ExtensionName)
            localctx.extensionNames.append(localctx._ExtensionName)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 65
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 66
                localctx._ExtensionName = self.match(stellaParser.ExtensionName)
                localctx.extensionNames.append(localctx._ExtensionName)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(stellaParser.Surrogate_id_SYMB_1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_decl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclTypeAliasContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.DeclContext
            super().__init__(parser)
            self.name = None # Token
            self.atype = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_61(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_61, 0)
        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclTypeAlias" ):
                listener.enterDeclTypeAlias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclTypeAlias" ):
                listener.exitDeclTypeAlias(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclTypeAlias" ):
                return visitor.visitDeclTypeAlias(self)
            else:
                return visitor.visitChildren(self)


    class DeclExceptionTypeContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.DeclContext
            super().__init__(parser)
            self.exceptionType = None # StellatypeContext
            self.copyFrom(ctx)

        def EXCEPTION(self):
            return self.getToken(stellaParser.EXCEPTION, 0)
        def Surrogate_id_SYMB_61(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_61, 0)
        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclExceptionType" ):
                listener.enterDeclExceptionType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclExceptionType" ):
                listener.exitDeclExceptionType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclExceptionType" ):
                return visitor.visitDeclExceptionType(self)
            else:
                return visitor.visitChildren(self)


    class DeclFunContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.DeclContext
            super().__init__(parser)
            self._annotation = None # AnnotationContext
            self.annotations = list() # of AnnotationContexts
            self.name = None # Token
            self._paramDecl = None # ParamDeclContext
            self.paramDecls = list() # of ParamDeclContexts
            self.returnType = None # StellatypeContext
            self._stellatype = None # StellatypeContext
            self.throwTypes = list() # of StellatypeContexts
            self._decl = None # DeclContext
            self.localDecls = list() # of DeclContexts
            self.returnExpr = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_43(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_43, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_56(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_56, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def Surrogate_id_SYMB_8(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_8, 0)
        def Surrogate_id_SYMB_59(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_59, 0)
        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.AnnotationContext)
            else:
                return self.getTypedRuleContext(stellaParser.AnnotationContext,i)

        def paramDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ParamDeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.ParamDeclContext,i)

        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.DeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.DeclContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclFun" ):
                listener.enterDeclFun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclFun" ):
                listener.exitDeclFun(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclFun" ):
                return visitor.visitDeclFun(self)
            else:
                return visitor.visitChildren(self)


    class DeclExceptionVariantContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.DeclContext
            super().__init__(parser)
            self.name = None # Token
            self.variantType = None # StellatypeContext
            self.copyFrom(ctx)

        def EXCEPTION(self):
            return self.getToken(stellaParser.EXCEPTION, 0)
        def VARIANT(self):
            return self.getToken(stellaParser.VARIANT, 0)
        def Surrogate_id_SYMB_7(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_7, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclExceptionVariant" ):
                listener.enterDeclExceptionVariant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclExceptionVariant" ):
                listener.exitDeclExceptionVariant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclExceptionVariant" ):
                return visitor.visitDeclExceptionVariant(self)
            else:
                return visitor.visitChildren(self)


    class DeclFunGenericContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.DeclContext
            super().__init__(parser)
            self._annotation = None # AnnotationContext
            self.annotations = list() # of AnnotationContexts
            self.name = None # Token
            self._StellaIdent = None # Token
            self.generics = list() # of Tokens
            self._paramDecl = None # ParamDeclContext
            self.paramDecls = list() # of ParamDeclContexts
            self.returnType = None # StellatypeContext
            self._stellatype = None # StellatypeContext
            self.throwTypes = list() # of StellatypeContexts
            self._decl = None # DeclContext
            self.localDecls = list() # of DeclContexts
            self.returnExpr = None # ExprContext
            self.copyFrom(ctx)

        def GENERIC(self):
            return self.getToken(stellaParser.GENERIC, 0)
        def Surrogate_id_SYMB_43(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_43, 0)
        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_56(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_56, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def StellaIdent(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.StellaIdent)
            else:
                return self.getToken(stellaParser.StellaIdent, i)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)
        def Surrogate_id_SYMB_8(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_8, 0)
        def Surrogate_id_SYMB_59(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_59, 0)
        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.AnnotationContext)
            else:
                return self.getTypedRuleContext(stellaParser.AnnotationContext,i)

        def paramDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ParamDeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.ParamDeclContext,i)

        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.DeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.DeclContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclFunGeneric" ):
                listener.enterDeclFunGeneric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclFunGeneric" ):
                listener.exitDeclFunGeneric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclFunGeneric" ):
                return visitor.visitDeclFunGeneric(self)
            else:
                return visitor.visitChildren(self)



    def decl(self):

        localctx = stellaParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = stellaParser.DeclFunContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==49:
                    self.state = 74
                    localctx._annotation = self.annotation()
                    localctx.annotations.append(localctx._annotation)
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 80
                self.match(stellaParser.Surrogate_id_SYMB_43)
                self.state = 81
                localctx.name = self.match(stellaParser.StellaIdent)
                self.state = 82
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==84:
                    self.state = 83
                    localctx._paramDecl = self.paramDecl()
                    localctx.paramDecls.append(localctx._paramDecl)
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 84
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 85
                        localctx._paramDecl = self.paramDecl()
                        localctx.paramDecls.append(localctx._paramDecl)
                        self.state = 90
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 93
                self.match(stellaParser.Surrogate_id_SYMB_3)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 94
                    self.match(stellaParser.Surrogate_id_SYMB_8)
                    self.state = 95
                    localctx.returnType = self.stellatype(0)


                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==60:
                    self.state = 98
                    self.match(stellaParser.Surrogate_id_SYMB_59)
                    self.state = 99
                    localctx._stellatype = self.stellatype(0)
                    localctx.throwTypes.append(localctx._stellatype)
                    self.state = 104
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 100
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 101
                        localctx._stellatype = self.stellatype(0)
                        localctx.throwTypes.append(localctx._stellatype)
                        self.state = 106
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 109
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 44)) & ~0x3f) == 0 and ((1 << (_la - 44)) & 68728127521) != 0):
                    self.state = 110
                    localctx._decl = self.decl()
                    localctx.localDecls.append(localctx._decl)
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 116
                self.match(stellaParser.Surrogate_id_SYMB_56)
                self.state = 117
                localctx.returnExpr = self.expr(0)
                self.state = 118
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 2:
                localctx = stellaParser.DeclFunGenericContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==49:
                    self.state = 120
                    localctx._annotation = self.annotation()
                    localctx.annotations.append(localctx._annotation)
                    self.state = 125
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 126
                self.match(stellaParser.GENERIC)
                self.state = 127
                self.match(stellaParser.Surrogate_id_SYMB_43)
                self.state = 128
                localctx.name = self.match(stellaParser.StellaIdent)
                self.state = 129
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 130
                localctx._StellaIdent = self.match(stellaParser.StellaIdent)
                localctx.generics.append(localctx._StellaIdent)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 131
                    self.match(stellaParser.Surrogate_id_SYMB_0)
                    self.state = 132
                    localctx._StellaIdent = self.match(stellaParser.StellaIdent)
                    localctx.generics.append(localctx._StellaIdent)
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 138
                self.match(stellaParser.Surrogate_id_SYMB_14)
                self.state = 139
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==84:
                    self.state = 140
                    localctx._paramDecl = self.paramDecl()
                    localctx.paramDecls.append(localctx._paramDecl)
                    self.state = 145
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 141
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 142
                        localctx._paramDecl = self.paramDecl()
                        localctx.paramDecls.append(localctx._paramDecl)
                        self.state = 147
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 150
                self.match(stellaParser.Surrogate_id_SYMB_3)
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 151
                    self.match(stellaParser.Surrogate_id_SYMB_8)
                    self.state = 152
                    localctx.returnType = self.stellatype(0)


                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==60:
                    self.state = 155
                    self.match(stellaParser.Surrogate_id_SYMB_59)
                    self.state = 156
                    localctx._stellatype = self.stellatype(0)
                    localctx.throwTypes.append(localctx._stellatype)
                    self.state = 161
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 157
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 158
                        localctx._stellatype = self.stellatype(0)
                        localctx.throwTypes.append(localctx._stellatype)
                        self.state = 163
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 166
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 44)) & ~0x3f) == 0 and ((1 << (_la - 44)) & 68728127521) != 0):
                    self.state = 167
                    localctx._decl = self.decl()
                    localctx.localDecls.append(localctx._decl)
                    self.state = 172
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 173
                self.match(stellaParser.Surrogate_id_SYMB_56)
                self.state = 174
                localctx.returnExpr = self.expr(0)
                self.state = 175
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 3:
                localctx = stellaParser.DeclTypeAliasContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.match(stellaParser.Surrogate_id_SYMB_61)
                self.state = 178
                localctx.name = self.match(stellaParser.StellaIdent)
                self.state = 179
                self.match(stellaParser.Surrogate_id_SYMB_6)
                self.state = 180
                localctx.atype = self.stellatype(0)
                pass

            elif la_ == 4:
                localctx = stellaParser.DeclExceptionTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.match(stellaParser.EXCEPTION)
                self.state = 182
                self.match(stellaParser.Surrogate_id_SYMB_61)
                self.state = 183
                self.match(stellaParser.Surrogate_id_SYMB_6)
                self.state = 184
                localctx.exceptionType = self.stellatype(0)
                pass

            elif la_ == 5:
                localctx = stellaParser.DeclExceptionVariantContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 185
                self.match(stellaParser.EXCEPTION)
                self.state = 186
                self.match(stellaParser.VARIANT)
                self.state = 187
                localctx.name = self.match(stellaParser.StellaIdent)
                self.state = 188
                self.match(stellaParser.Surrogate_id_SYMB_7)
                self.state = 189
                localctx.variantType = self.stellatype(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_annotation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InlineAnnotationContext(AnnotationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.AnnotationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_48(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_48, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineAnnotation" ):
                listener.enterInlineAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineAnnotation" ):
                listener.exitInlineAnnotation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineAnnotation" ):
                return visitor.visitInlineAnnotation(self)
            else:
                return visitor.visitChildren(self)



    def annotation(self):

        localctx = stellaParser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_annotation)
        try:
            localctx = stellaParser.InlineAnnotationContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(stellaParser.Surrogate_id_SYMB_48)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.paramType = None # StellatypeContext

        def Surrogate_id_SYMB_7(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_7, 0)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_paramDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamDecl" ):
                listener.enterParamDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamDecl" ):
                listener.exitParamDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDecl" ):
                return visitor.visitParamDecl(self)
            else:
                return visitor.visitChildren(self)




    def paramDecl(self):

        localctx = stellaParser.ParamDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            localctx.name = self.match(stellaParser.StellaIdent)
            self.state = 195
            self.match(stellaParser.Surrogate_id_SYMB_7)
            self.state = 196
            localctx.paramType = self.stellatype(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class FoldContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.type_ = None # StellatypeContext
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_44(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_44, 0)
        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFold" ):
                listener.enterFold(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFold" ):
                listener.exitFold(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFold" ):
                return visitor.visitFold(self)
            else:
                return visitor.visitChildren(self)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_21(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_21, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class IsZeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.n = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_30(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_30, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsZero" ):
                listener.enterIsZero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsZero" ):
                listener.exitIsZero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsZero" ):
                return visitor.visitIsZero(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class TypeAbstractionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._StellaIdent = None # Token
            self.generics = list() # of Tokens
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def GENERIC(self):
            return self.getToken(stellaParser.GENERIC, 0)
        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def StellaIdent(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.StellaIdent)
            else:
                return self.getToken(stellaParser.StellaIdent, i)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeAbstraction" ):
                listener.enterTypeAbstraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeAbstraction" ):
                listener.exitTypeAbstraction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeAbstraction" ):
                return visitor.visitTypeAbstraction(self)
            else:
                return visitor.visitChildren(self)


    class DivideContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_24(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_24, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivide" ):
                listener.enterDivide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivide" ):
                listener.exitDivide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivide" ):
                return visitor.visitDivide(self)
            else:
                return visitor.visitChildren(self)


    class LessThanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_15(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_15, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessThan" ):
                listener.enterLessThan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessThan" ):
                listener.exitLessThan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThan" ):
                return visitor.visitLessThan(self)
            else:
                return visitor.visitChildren(self)


    class DotRecordContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.label = None # Token
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_25(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_25, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDotRecord" ):
                listener.enterDotRecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDotRecord" ):
                listener.exitDotRecord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDotRecord" ):
                return visitor.visitDotRecord(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_17(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_17, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterThan" ):
                listener.enterGreaterThan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterThan" ):
                listener.exitGreaterThan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThan" ):
                return visitor.visitGreaterThan(self)
            else:
                return visitor.visitChildren(self)


    class EqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_19(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_19, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)


    class ThrowContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def THROW(self):
            return self.getToken(stellaParser.THROW, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrow" ):
                listener.enterThrow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrow" ):
                listener.exitThrow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThrow" ):
                return visitor.visitThrow(self)
            else:
                return visitor.visitChildren(self)


    class MultiplyContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_23(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_23, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiply" ):
                listener.enterMultiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiply" ):
                listener.exitMultiply(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiply" ):
                return visitor.visitMultiply(self)
            else:
                return visitor.visitChildren(self)


    class ConstMemoryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.mem = None # Token
            self.copyFrom(ctx)

        def MemoryAddress(self):
            return self.getToken(stellaParser.MemoryAddress, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstMemory" ):
                listener.enterConstMemory(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstMemory" ):
                listener.exitConstMemory(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstMemory" ):
                return visitor.visitConstMemory(self)
            else:
                return visitor.visitChildren(self)


    class ListContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self.exprs = list() # of ExprContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)


    class TryCatchContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.tryExpr = None # ExprContext
            self.pat = None # PatternContext
            self.fallbackExpr = None # ExprContext
            self.copyFrom(ctx)

        def TRY(self):
            return self.getToken(stellaParser.TRY, 0)
        def Surrogate_id_SYMB_4(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_4)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_4, i)
        def Surrogate_id_SYMB_5(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_5)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_5, i)
        def CATCH(self):
            return self.getToken(stellaParser.CATCH, 0)
        def Surrogate_id_SYMB_9(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_9, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryCatch" ):
                listener.enterTryCatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryCatch" ):
                listener.exitTryCatch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTryCatch" ):
                return visitor.visitTryCatch(self)
            else:
                return visitor.visitChildren(self)


    class TryCastAsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.tryExpr = None # ExprContext
            self.type_ = None # StellatypeContext
            self.pattern_ = None # PatternContext
            self.expr_ = None # ExprContext
            self.fallbackExpr = None # ExprContext
            self.copyFrom(ctx)

        def TRY(self):
            return self.getToken(stellaParser.TRY, 0)
        def Surrogate_id_SYMB_4(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_4)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_4, i)
        def Surrogate_id_SYMB_5(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_5)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_5, i)
        def CAST(self):
            return self.getToken(stellaParser.CAST, 0)
        def Surrogate_id_SYMB_36(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_36, 0)
        def Surrogate_id_SYMB_9(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_9, 0)
        def Surrogate_id_SYMB_64(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_64, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)

        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryCastAs" ):
                listener.enterTryCastAs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryCastAs" ):
                listener.exitTryCastAs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTryCastAs" ):
                return visitor.visitTryCastAs(self)
            else:
                return visitor.visitChildren(self)


    class HeadContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.list_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_26(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_26, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHead" ):
                listener.enterHead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHead" ):
                listener.exitHead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHead" ):
                return visitor.visitHead(self)
            else:
                return visitor.visitChildren(self)


    class TerminatingSemicolonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_1(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_1, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminatingSemicolon" ):
                listener.enterTerminatingSemicolon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminatingSemicolon" ):
                listener.exitTerminatingSemicolon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminatingSemicolon" ):
                return visitor.visitTerminatingSemicolon(self)
            else:
                return visitor.visitChildren(self)


    class NotEqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_20(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_20, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotEqual" ):
                listener.enterNotEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotEqual" ):
                listener.exitNotEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotEqual" ):
                return visitor.visitNotEqual(self)
            else:
                return visitor.visitChildren(self)


    class ConstUnitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_63(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_63, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstUnit" ):
                listener.enterConstUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstUnit" ):
                listener.exitConstUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstUnit" ):
                return visitor.visitConstUnit(self)
            else:
                return visitor.visitChildren(self)


    class SequenceContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr1 = None # ExprContext
            self.expr2 = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_1(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_1, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence" ):
                listener.enterSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence" ):
                listener.exitSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)


    class ConstFalseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_41(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_41, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstFalse" ):
                listener.enterConstFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstFalse" ):
                listener.exitConstFalse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstFalse" ):
                return visitor.visitConstFalse(self)
            else:
                return visitor.visitChildren(self)


    class AbstractionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._paramDecl = None # ParamDeclContext
            self.paramDecls = list() # of ParamDeclContexts
            self.returnExpr = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_43(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_43, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_56(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_56, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def paramDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ParamDeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.ParamDeclContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstraction" ):
                listener.enterAbstraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstraction" ):
                listener.exitAbstraction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraction" ):
                return visitor.visitAbstraction(self)
            else:
                return visitor.visitChildren(self)


    class ConstIntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.n = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(stellaParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstInt" ):
                listener.enterConstInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstInt" ):
                listener.exitConstInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstInt" ):
                return visitor.visitConstInt(self)
            else:
                return visitor.visitChildren(self)


    class VariantContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.label = None # Token
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_11(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_11, 0)
        def Surrogate_id_SYMB_12(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_12, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariant" ):
                listener.enterVariant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariant" ):
                listener.exitVariant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariant" ):
                return visitor.visitVariant(self)
            else:
                return visitor.visitChildren(self)


    class ConstTrueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_60(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_60, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstTrue" ):
                listener.enterConstTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstTrue" ):
                listener.exitConstTrue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstTrue" ):
                return visitor.visitConstTrue(self)
            else:
                return visitor.visitChildren(self)


    class SubtractContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_22(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_22, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtract" ):
                listener.enterSubtract(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtract" ):
                listener.exitSubtract(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtract" ):
                return visitor.visitSubtract(self)
            else:
                return visitor.visitChildren(self)


    class TypeCastContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def CAST(self):
            return self.getToken(stellaParser.CAST, 0)
        def Surrogate_id_SYMB_36(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_36, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeCast" ):
                listener.enterTypeCast(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeCast" ):
                listener.exitTypeCast(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeCast" ):
                return visitor.visitTypeCast(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.condition = None # ExprContext
            self.thenExpr = None # ExprContext
            self.elseExpr = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_45(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_45, 0)
        def Surrogate_id_SYMB_58(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_58, 0)
        def Surrogate_id_SYMB_39(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_39, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class ApplicationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.fun = None # ExprContext
            self._expr = None # ExprContext
            self.args = list() # of ExprContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApplication" ):
                listener.enterApplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApplication" ):
                listener.exitApplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApplication" ):
                return visitor.visitApplication(self)
            else:
                return visitor.visitChildren(self)


    class DerefContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_23(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_23, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeref" ):
                listener.enterDeref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeref" ):
                listener.exitDeref(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeref" ):
                return visitor.visitDeref(self)
            else:
                return visitor.visitChildren(self)


    class IsEmptyContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.list_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_27(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_27, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsEmpty" ):
                listener.enterIsEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsEmpty" ):
                listener.exitIsEmpty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsEmpty" ):
                return visitor.visitIsEmpty(self)
            else:
                return visitor.visitChildren(self)


    class PanicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PANIC(self):
            return self.getToken(stellaParser.PANIC, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPanic" ):
                listener.enterPanic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPanic" ):
                listener.exitPanic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPanic" ):
                return visitor.visitPanic(self)
            else:
                return visitor.visitChildren(self)


    class LessThanOrEqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_16(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_16, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessThanOrEqual" ):
                listener.enterLessThanOrEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessThanOrEqual" ):
                listener.exitLessThanOrEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThanOrEqual" ):
                return visitor.visitLessThanOrEqual(self)
            else:
                return visitor.visitChildren(self)


    class SuccContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.n = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_57(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_57, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSucc" ):
                listener.enterSucc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSucc" ):
                listener.exitSucc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSucc" ):
                return visitor.visitSucc(self)
            else:
                return visitor.visitChildren(self)


    class InlContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_47(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_47, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInl" ):
                listener.enterInl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInl" ):
                listener.exitInl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInl" ):
                return visitor.visitInl(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanOrEqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_18(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_18, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterThanOrEqual" ):
                listener.enterGreaterThanOrEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterThanOrEqual" ):
                listener.exitGreaterThanOrEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThanOrEqual" ):
                return visitor.visitGreaterThanOrEqual(self)
            else:
                return visitor.visitChildren(self)


    class InrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_49(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_49, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInr" ):
                listener.enterInr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInr" ):
                listener.exitInr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInr" ):
                return visitor.visitInr(self)
            else:
                return visitor.visitChildren(self)


    class MatchContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self._matchCase = None # MatchCaseContext
            self.cases = list() # of MatchCaseContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_53(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_53, 0)
        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def matchCase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.MatchCaseContext)
            else:
                return self.getTypedRuleContext(stellaParser.MatchCaseContext,i)

        def Surrogate_id_SYMB_10(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_10)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_10, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatch" ):
                listener.enterMatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatch" ):
                listener.exitMatch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatch" ):
                return visitor.visitMatch(self)
            else:
                return visitor.visitChildren(self)


    class LogicNotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_54(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_54, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicNot" ):
                listener.enterLogicNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicNot" ):
                listener.exitLogicNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicNot" ):
                return visitor.visitLogicNot(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisedExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesisedExpr" ):
                listener.enterParenthesisedExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesisedExpr" ):
                listener.exitParenthesisedExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesisedExpr" ):
                return visitor.visitParenthesisedExpr(self)
            else:
                return visitor.visitChildren(self)


    class TailContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.list_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_28(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_28, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTail" ):
                listener.enterTail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTail" ):
                listener.exitTail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTail" ):
                return visitor.visitTail(self)
            else:
                return visitor.visitChildren(self)


    class RecordContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._binding = None # BindingContext
            self.bindings = list() # of BindingContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def binding(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.BindingContext)
            else:
                return self.getTypedRuleContext(stellaParser.BindingContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecord" ):
                listener.enterRecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecord" ):
                listener.exitRecord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecord" ):
                return visitor.visitRecord(self)
            else:
                return visitor.visitChildren(self)


    class LogicAndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_35(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_35, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicAnd" ):
                listener.enterLogicAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicAnd" ):
                listener.exitLogicAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicAnd" ):
                return visitor.visitLogicAnd(self)
            else:
                return visitor.visitChildren(self)


    class TypeApplicationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.fun = None # ExprContext
            self._stellatype = None # StellatypeContext
            self.types = list() # of StellatypeContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeApplication" ):
                listener.enterTypeApplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeApplication" ):
                listener.exitTypeApplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeApplication" ):
                return visitor.visitTypeApplication(self)
            else:
                return visitor.visitChildren(self)


    class LetRecContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._patternBinding = None # PatternBindingContext
            self.patternBindings = list() # of PatternBindingContexts
            self.body = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_52(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_52, 0)
        def Surrogate_id_SYMB_46(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_46, 0)
        def patternBinding(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.PatternBindingContext)
            else:
                return self.getTypedRuleContext(stellaParser.PatternBindingContext,i)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetRec" ):
                listener.enterLetRec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetRec" ):
                listener.exitLetRec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetRec" ):
                return visitor.visitLetRec(self)
            else:
                return visitor.visitChildren(self)


    class LogicOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_55(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_55, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicOr" ):
                listener.enterLogicOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicOr" ):
                listener.exitLogicOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOr" ):
                return visitor.visitLogicOr(self)
            else:
                return visitor.visitChildren(self)


    class TryWithContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.tryExpr = None # ExprContext
            self.fallbackExpr = None # ExprContext
            self.copyFrom(ctx)

        def TRY(self):
            return self.getToken(stellaParser.TRY, 0)
        def Surrogate_id_SYMB_4(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_4)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_4, i)
        def Surrogate_id_SYMB_5(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_5)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_5, i)
        def Surrogate_id_SYMB_64(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_64, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryWith" ):
                listener.enterTryWith(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryWith" ):
                listener.exitTryWith(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTryWith" ):
                return visitor.visitTryWith(self)
            else:
                return visitor.visitChildren(self)


    class PredContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.n = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_29(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_29, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPred" ):
                listener.enterPred(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPred" ):
                listener.exitPred(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPred" ):
                return visitor.visitPred(self)
            else:
                return visitor.visitChildren(self)


    class TypeAscContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_36(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_36, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeAsc" ):
                listener.enterTypeAsc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeAsc" ):
                listener.exitTypeAsc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeAsc" ):
                return visitor.visitTypeAsc(self)
            else:
                return visitor.visitChildren(self)


    class NatRecContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.n = None # ExprContext
            self.initial = None # ExprContext
            self.step = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_31(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_31, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNatRec" ):
                listener.enterNatRec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNatRec" ):
                listener.exitNatRec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNatRec" ):
                return visitor.visitNatRec(self)
            else:
                return visitor.visitChildren(self)


    class UnfoldContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.type_ = None # StellatypeContext
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_62(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_62, 0)
        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnfold" ):
                listener.enterUnfold(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnfold" ):
                listener.exitUnfold(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnfold" ):
                return visitor.visitUnfold(self)
            else:
                return visitor.visitChildren(self)


    class RefContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def REFERENCE(self):
            return self.getToken(stellaParser.REFERENCE, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRef" ):
                listener.enterRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRef" ):
                listener.exitRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRef" ):
                return visitor.visitRef(self)
            else:
                return visitor.visitChildren(self)


    class DotTupleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.index = None # Token
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_25(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_25, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def INTEGER(self):
            return self.getToken(stellaParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDotTuple" ):
                listener.enterDotTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDotTuple" ):
                listener.exitDotTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDotTuple" ):
                return visitor.visitDotTuple(self)
            else:
                return visitor.visitChildren(self)


    class FixContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_42(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_42, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFix" ):
                listener.enterFix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFix" ):
                listener.exitFix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFix" ):
                return visitor.visitFix(self)
            else:
                return visitor.visitChildren(self)


    class LetContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._patternBinding = None # PatternBindingContext
            self.patternBindings = list() # of PatternBindingContexts
            self.body = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_51(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_51, 0)
        def Surrogate_id_SYMB_46(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_46, 0)
        def patternBinding(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.PatternBindingContext)
            else:
                return self.getTypedRuleContext(stellaParser.PatternBindingContext,i)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet" ):
                listener.enterLet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet" ):
                listener.exitLet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet" ):
                return visitor.visitLet(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def ASSIGN(self):
            return self.getToken(stellaParser.ASSIGN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class TupleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self.exprs = list() # of ExprContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)


    class ConsListContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.head = None # ExprContext
            self.tail = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_37(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_37, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_0(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_0, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConsList" ):
                listener.enterConsList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConsList" ):
                listener.exitConsList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConsList" ):
                return visitor.visitConsList(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = stellaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                localctx = stellaParser.ConstTrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 199
                self.match(stellaParser.Surrogate_id_SYMB_60)
                pass

            elif la_ == 2:
                localctx = stellaParser.ConstFalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 200
                self.match(stellaParser.Surrogate_id_SYMB_41)
                pass

            elif la_ == 3:
                localctx = stellaParser.ConstUnitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 201
                self.match(stellaParser.Surrogate_id_SYMB_63)
                pass

            elif la_ == 4:
                localctx = stellaParser.ConstIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 202
                localctx.n = self.match(stellaParser.INTEGER)
                pass

            elif la_ == 5:
                localctx = stellaParser.ConstMemoryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 203
                localctx.mem = self.match(stellaParser.MemoryAddress)
                pass

            elif la_ == 6:
                localctx = stellaParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 204
                localctx.name = self.match(stellaParser.StellaIdent)
                pass

            elif la_ == 7:
                localctx = stellaParser.PanicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 205
                self.match(stellaParser.PANIC)
                pass

            elif la_ == 8:
                localctx = stellaParser.ThrowContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 206
                self.match(stellaParser.THROW)
                self.state = 207
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 208
                localctx.expr_ = self.expr(0)
                self.state = 209
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 9:
                localctx = stellaParser.TryCatchContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 211
                self.match(stellaParser.TRY)
                self.state = 212
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 213
                localctx.tryExpr = self.expr(0)
                self.state = 214
                self.match(stellaParser.Surrogate_id_SYMB_5)
                self.state = 215
                self.match(stellaParser.CATCH)
                self.state = 216
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 217
                localctx.pat = self.pattern(0)
                self.state = 218
                self.match(stellaParser.Surrogate_id_SYMB_9)
                self.state = 219
                localctx.fallbackExpr = self.expr(0)
                self.state = 220
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 10:
                localctx = stellaParser.TryCastAsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 222
                self.match(stellaParser.TRY)
                self.state = 223
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 224
                localctx.tryExpr = self.expr(0)
                self.state = 225
                self.match(stellaParser.Surrogate_id_SYMB_5)
                self.state = 226
                self.match(stellaParser.CAST)
                self.state = 227
                self.match(stellaParser.Surrogate_id_SYMB_36)
                self.state = 228
                localctx.type_ = self.stellatype(0)
                self.state = 229
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 230
                localctx.pattern_ = self.pattern(0)
                self.state = 231
                self.match(stellaParser.Surrogate_id_SYMB_9)
                self.state = 232
                localctx.expr_ = self.expr(0)
                self.state = 233
                self.match(stellaParser.Surrogate_id_SYMB_5)
                self.state = 234
                self.match(stellaParser.Surrogate_id_SYMB_64)
                self.state = 235
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 236
                localctx.fallbackExpr = self.expr(0)
                self.state = 237
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 11:
                localctx = stellaParser.TryWithContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 239
                self.match(stellaParser.TRY)
                self.state = 240
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 241
                localctx.tryExpr = self.expr(0)
                self.state = 242
                self.match(stellaParser.Surrogate_id_SYMB_5)
                self.state = 243
                self.match(stellaParser.Surrogate_id_SYMB_64)
                self.state = 244
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 245
                localctx.fallbackExpr = self.expr(0)
                self.state = 246
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 12:
                localctx = stellaParser.InlContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 248
                self.match(stellaParser.Surrogate_id_SYMB_47)
                self.state = 249
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 250
                localctx.expr_ = self.expr(0)
                self.state = 251
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 13:
                localctx = stellaParser.InrContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 253
                self.match(stellaParser.Surrogate_id_SYMB_49)
                self.state = 254
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 255
                localctx.expr_ = self.expr(0)
                self.state = 256
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 14:
                localctx = stellaParser.ConsListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 258
                self.match(stellaParser.Surrogate_id_SYMB_37)
                self.state = 259
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 260
                localctx.head = self.expr(0)
                self.state = 261
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 262
                localctx.tail = self.expr(0)
                self.state = 263
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 15:
                localctx = stellaParser.HeadContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 265
                self.match(stellaParser.Surrogate_id_SYMB_26)
                self.state = 266
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 267
                localctx.list_ = self.expr(0)
                self.state = 268
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 16:
                localctx = stellaParser.IsEmptyContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 270
                self.match(stellaParser.Surrogate_id_SYMB_27)
                self.state = 271
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 272
                localctx.list_ = self.expr(0)
                self.state = 273
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 17:
                localctx = stellaParser.TailContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 275
                self.match(stellaParser.Surrogate_id_SYMB_28)
                self.state = 276
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 277
                localctx.list_ = self.expr(0)
                self.state = 278
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 18:
                localctx = stellaParser.SuccContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 280
                self.match(stellaParser.Surrogate_id_SYMB_57)
                self.state = 281
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 282
                localctx.n = self.expr(0)
                self.state = 283
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 19:
                localctx = stellaParser.LogicNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 285
                self.match(stellaParser.Surrogate_id_SYMB_54)
                self.state = 286
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 287
                localctx.expr_ = self.expr(0)
                self.state = 288
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 20:
                localctx = stellaParser.PredContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 290
                self.match(stellaParser.Surrogate_id_SYMB_29)
                self.state = 291
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 292
                localctx.n = self.expr(0)
                self.state = 293
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 21:
                localctx = stellaParser.IsZeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 295
                self.match(stellaParser.Surrogate_id_SYMB_30)
                self.state = 296
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 297
                localctx.n = self.expr(0)
                self.state = 298
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 22:
                localctx = stellaParser.FixContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 300
                self.match(stellaParser.Surrogate_id_SYMB_42)
                self.state = 301
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 302
                localctx.expr_ = self.expr(0)
                self.state = 303
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 23:
                localctx = stellaParser.NatRecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 305
                self.match(stellaParser.Surrogate_id_SYMB_31)
                self.state = 306
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 307
                localctx.n = self.expr(0)
                self.state = 308
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 309
                localctx.initial = self.expr(0)
                self.state = 310
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 311
                localctx.step = self.expr(0)
                self.state = 312
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 24:
                localctx = stellaParser.FoldContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 314
                self.match(stellaParser.Surrogate_id_SYMB_44)
                self.state = 315
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 316
                localctx.type_ = self.stellatype(0)
                self.state = 317
                self.match(stellaParser.Surrogate_id_SYMB_14)
                self.state = 318
                localctx.expr_ = self.expr(34)
                pass

            elif la_ == 25:
                localctx = stellaParser.UnfoldContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 320
                self.match(stellaParser.Surrogate_id_SYMB_62)
                self.state = 321
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 322
                localctx.type_ = self.stellatype(0)
                self.state = 323
                self.match(stellaParser.Surrogate_id_SYMB_14)
                self.state = 324
                localctx.expr_ = self.expr(33)
                pass

            elif la_ == 26:
                localctx = stellaParser.RefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 326
                self.match(stellaParser.REFERENCE)
                self.state = 327
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 328
                localctx.expr_ = self.expr(0)
                self.state = 329
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 27:
                localctx = stellaParser.DerefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 331
                self.match(stellaParser.Surrogate_id_SYMB_23)
                self.state = 332
                localctx.expr_ = self.expr(26)
                pass

            elif la_ == 28:
                localctx = stellaParser.AbstractionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 333
                self.match(stellaParser.Surrogate_id_SYMB_43)
                self.state = 334
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==84:
                    self.state = 335
                    localctx._paramDecl = self.paramDecl()
                    localctx.paramDecls.append(localctx._paramDecl)
                    self.state = 340
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 336
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 337
                        localctx._paramDecl = self.paramDecl()
                        localctx.paramDecls.append(localctx._paramDecl)
                        self.state = 342
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 345
                self.match(stellaParser.Surrogate_id_SYMB_3)
                self.state = 346
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 347
                self.match(stellaParser.Surrogate_id_SYMB_56)
                self.state = 348
                localctx.returnExpr = self.expr(0)
                self.state = 349
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 29:
                localctx = stellaParser.TupleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 351
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -6560200659402993624) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 13700865) != 0):
                    self.state = 352
                    localctx._expr = self.expr(0)
                    localctx.exprs.append(localctx._expr)
                    self.state = 357
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 353
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 354
                        localctx._expr = self.expr(0)
                        localctx.exprs.append(localctx._expr)
                        self.state = 359
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 362
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 30:
                localctx = stellaParser.RecordContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 363
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 364
                localctx._binding = self.binding()
                localctx.bindings.append(localctx._binding)
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 365
                    self.match(stellaParser.Surrogate_id_SYMB_0)
                    self.state = 366
                    localctx._binding = self.binding()
                    localctx.bindings.append(localctx._binding)
                    self.state = 371
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 372
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 31:
                localctx = stellaParser.VariantContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 374
                self.match(stellaParser.Surrogate_id_SYMB_11)
                self.state = 375
                localctx.label = self.match(stellaParser.StellaIdent)
                self.state = 378
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 376
                    self.match(stellaParser.Surrogate_id_SYMB_6)
                    self.state = 377
                    localctx.rhs = self.expr(0)


                self.state = 380
                self.match(stellaParser.Surrogate_id_SYMB_12)
                pass

            elif la_ == 32:
                localctx = stellaParser.MatchContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 381
                self.match(stellaParser.Surrogate_id_SYMB_53)
                self.state = 382
                localctx.expr_ = self.expr(0)
                self.state = 383
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 392
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2595485433173397544) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 9437185) != 0):
                    self.state = 384
                    localctx._matchCase = self.matchCase()
                    localctx.cases.append(localctx._matchCase)
                    self.state = 389
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==11:
                        self.state = 385
                        self.match(stellaParser.Surrogate_id_SYMB_10)
                        self.state = 386
                        localctx._matchCase = self.matchCase()
                        localctx.cases.append(localctx._matchCase)
                        self.state = 391
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 394
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 33:
                localctx = stellaParser.ListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 396
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 405
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -6560200659402993624) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 13700865) != 0):
                    self.state = 397
                    localctx._expr = self.expr(0)
                    localctx.exprs.append(localctx._expr)
                    self.state = 402
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 398
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 399
                        localctx._expr = self.expr(0)
                        localctx.exprs.append(localctx._expr)
                        self.state = 404
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 407
                self.match(stellaParser.Surrogate_id_SYMB_14)
                pass

            elif la_ == 34:
                localctx = stellaParser.IfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 408
                self.match(stellaParser.Surrogate_id_SYMB_45)
                self.state = 409
                localctx.condition = self.expr(0)
                self.state = 410
                self.match(stellaParser.Surrogate_id_SYMB_58)
                self.state = 411
                localctx.thenExpr = self.expr(0)
                self.state = 412
                self.match(stellaParser.Surrogate_id_SYMB_39)
                self.state = 413
                localctx.elseExpr = self.expr(7)
                pass

            elif la_ == 35:
                localctx = stellaParser.LetContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 415
                self.match(stellaParser.Surrogate_id_SYMB_51)
                self.state = 416
                localctx._patternBinding = self.patternBinding()
                localctx.patternBindings.append(localctx._patternBinding)
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 417
                    self.match(stellaParser.Surrogate_id_SYMB_0)
                    self.state = 418
                    localctx._patternBinding = self.patternBinding()
                    localctx.patternBindings.append(localctx._patternBinding)
                    self.state = 423
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 424
                self.match(stellaParser.Surrogate_id_SYMB_46)
                self.state = 425
                localctx.body = self.expr(5)
                pass

            elif la_ == 36:
                localctx = stellaParser.LetRecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 427
                self.match(stellaParser.Surrogate_id_SYMB_52)
                self.state = 428
                localctx._patternBinding = self.patternBinding()
                localctx.patternBindings.append(localctx._patternBinding)
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 429
                    self.match(stellaParser.Surrogate_id_SYMB_0)
                    self.state = 430
                    localctx._patternBinding = self.patternBinding()
                    localctx.patternBindings.append(localctx._patternBinding)
                    self.state = 435
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 436
                self.match(stellaParser.Surrogate_id_SYMB_46)
                self.state = 437
                localctx.body = self.expr(4)
                pass

            elif la_ == 37:
                localctx = stellaParser.TypeAbstractionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 439
                self.match(stellaParser.GENERIC)
                self.state = 440
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 441
                localctx._StellaIdent = self.match(stellaParser.StellaIdent)
                localctx.generics.append(localctx._StellaIdent)
                self.state = 446
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 442
                    self.match(stellaParser.Surrogate_id_SYMB_0)
                    self.state = 443
                    localctx._StellaIdent = self.match(stellaParser.StellaIdent)
                    localctx.generics.append(localctx._StellaIdent)
                    self.state = 448
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 449
                self.match(stellaParser.Surrogate_id_SYMB_14)
                self.state = 450
                localctx.expr_ = self.expr(3)
                pass

            elif la_ == 38:
                localctx = stellaParser.ParenthesisedExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 451
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 452
                localctx.expr_ = self.expr(0)
                self.state = 453
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 541
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 539
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = stellaParser.MultiplyContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 457
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 458
                        self.match(stellaParser.Surrogate_id_SYMB_23)
                        self.state = 459
                        localctx.right = self.expr(31)
                        pass

                    elif la_ == 2:
                        localctx = stellaParser.DivideContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 460
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 461
                        self.match(stellaParser.Surrogate_id_SYMB_24)
                        self.state = 462
                        localctx.right = self.expr(30)
                        pass

                    elif la_ == 3:
                        localctx = stellaParser.LogicAndContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 463
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 464
                        self.match(stellaParser.Surrogate_id_SYMB_35)
                        self.state = 465
                        localctx.right = self.expr(29)
                        pass

                    elif la_ == 4:
                        localctx = stellaParser.AddContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 466
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 467
                        self.match(stellaParser.Surrogate_id_SYMB_21)
                        self.state = 468
                        localctx.right = self.expr(26)
                        pass

                    elif la_ == 5:
                        localctx = stellaParser.SubtractContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 469
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 470
                        self.match(stellaParser.Surrogate_id_SYMB_22)
                        self.state = 471
                        localctx.right = self.expr(25)
                        pass

                    elif la_ == 6:
                        localctx = stellaParser.LogicOrContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 472
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 473
                        self.match(stellaParser.Surrogate_id_SYMB_55)
                        self.state = 474
                        localctx.right = self.expr(24)
                        pass

                    elif la_ == 7:
                        localctx = stellaParser.LessThanContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 475
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 476
                        self.match(stellaParser.Surrogate_id_SYMB_15)
                        self.state = 477
                        localctx.right = self.expr(15)
                        pass

                    elif la_ == 8:
                        localctx = stellaParser.LessThanOrEqualContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 478
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 479
                        self.match(stellaParser.Surrogate_id_SYMB_16)
                        self.state = 480
                        localctx.right = self.expr(14)
                        pass

                    elif la_ == 9:
                        localctx = stellaParser.GreaterThanContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 481
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 482
                        self.match(stellaParser.Surrogate_id_SYMB_17)
                        self.state = 483
                        localctx.right = self.expr(13)
                        pass

                    elif la_ == 10:
                        localctx = stellaParser.GreaterThanOrEqualContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 484
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 485
                        self.match(stellaParser.Surrogate_id_SYMB_18)
                        self.state = 486
                        localctx.right = self.expr(12)
                        pass

                    elif la_ == 11:
                        localctx = stellaParser.EqualContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 487
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 488
                        self.match(stellaParser.Surrogate_id_SYMB_19)
                        self.state = 489
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 12:
                        localctx = stellaParser.NotEqualContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 490
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 491
                        self.match(stellaParser.Surrogate_id_SYMB_20)
                        self.state = 492
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 13:
                        localctx = stellaParser.AssignContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 493
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 494
                        self.match(stellaParser.ASSIGN)
                        self.state = 495
                        localctx.rhs = self.expr(9)
                        pass

                    elif la_ == 14:
                        localctx = stellaParser.SequenceContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expr1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 496
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 497
                        self.match(stellaParser.Surrogate_id_SYMB_1)
                        self.state = 498
                        localctx.expr2 = self.expr(7)
                        pass

                    elif la_ == 15:
                        localctx = stellaParser.DotRecordContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expr_ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 499
                        if not self.precpred(self._ctx, 59):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 59)")
                        self.state = 500
                        self.match(stellaParser.Surrogate_id_SYMB_25)
                        self.state = 501
                        localctx.label = self.match(stellaParser.StellaIdent)
                        pass

                    elif la_ == 16:
                        localctx = stellaParser.DotTupleContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expr_ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 502
                        if not self.precpred(self._ctx, 58):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 58)")
                        self.state = 503
                        self.match(stellaParser.Surrogate_id_SYMB_25)
                        self.state = 504
                        localctx.index = self.match(stellaParser.INTEGER)
                        pass

                    elif la_ == 17:
                        localctx = stellaParser.ApplicationContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.fun = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 505
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 506
                        self.match(stellaParser.Surrogate_id_SYMB_2)
                        self.state = 515
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & -6560200659402993624) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 13700865) != 0):
                            self.state = 507
                            localctx._expr = self.expr(0)
                            localctx.args.append(localctx._expr)
                            self.state = 512
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==1:
                                self.state = 508
                                self.match(stellaParser.Surrogate_id_SYMB_0)
                                self.state = 509
                                localctx._expr = self.expr(0)
                                localctx.args.append(localctx._expr)
                                self.state = 514
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 517
                        self.match(stellaParser.Surrogate_id_SYMB_3)
                        pass

                    elif la_ == 18:
                        localctx = stellaParser.TypeApplicationContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.fun = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 518
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 519
                        self.match(stellaParser.Surrogate_id_SYMB_13)

                        self.state = 520
                        localctx._stellatype = self.stellatype(0)
                        localctx.types.append(localctx._stellatype)
                        self.state = 525
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==1:
                            self.state = 521
                            self.match(stellaParser.Surrogate_id_SYMB_0)
                            self.state = 522
                            localctx._stellatype = self.stellatype(0)
                            localctx.types.append(localctx._stellatype)
                            self.state = 527
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 528
                        self.match(stellaParser.Surrogate_id_SYMB_14)
                        pass

                    elif la_ == 19:
                        localctx = stellaParser.TypeAscContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expr_ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 530
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 531
                        self.match(stellaParser.Surrogate_id_SYMB_36)
                        self.state = 532
                        localctx.type_ = self.stellatype(0)
                        pass

                    elif la_ == 20:
                        localctx = stellaParser.TypeCastContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expr_ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 533
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 534
                        self.match(stellaParser.CAST)
                        self.state = 535
                        self.match(stellaParser.Surrogate_id_SYMB_36)
                        self.state = 536
                        localctx.type_ = self.stellatype(0)
                        pass

                    elif la_ == 21:
                        localctx = stellaParser.TerminatingSemicolonContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expr_ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 537
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 538
                        self.match(stellaParser.Surrogate_id_SYMB_1)
                        pass

             
                self.state = 543
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PatternBindingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pat = None # PatternContext
            self.rhs = None # ExprContext

        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)

        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_patternBinding

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternBinding" ):
                listener.enterPatternBinding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternBinding" ):
                listener.exitPatternBinding(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternBinding" ):
                return visitor.visitPatternBinding(self)
            else:
                return visitor.visitChildren(self)




    def patternBinding(self):

        localctx = stellaParser.PatternBindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_patternBinding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            localctx.pat = self.pattern(0)
            self.state = 545
            self.match(stellaParser.Surrogate_id_SYMB_6)
            self.state = 546
            localctx.rhs = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BindingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.rhs = None # ExprContext

        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_binding

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinding" ):
                listener.enterBinding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinding" ):
                listener.exitBinding(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinding" ):
                return visitor.visitBinding(self)
            else:
                return visitor.visitChildren(self)




    def binding(self):

        localctx = stellaParser.BindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            localctx.name = self.match(stellaParser.StellaIdent)
            self.state = 549
            self.match(stellaParser.Surrogate_id_SYMB_6)
            self.state = 550
            localctx.rhs = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pattern_ = None # PatternContext
            self.expr_ = None # ExprContext

        def Surrogate_id_SYMB_9(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_9, 0)

        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_matchCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatchCase" ):
                listener.enterMatchCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatchCase" ):
                listener.exitMatchCase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchCase" ):
                return visitor.visitMatchCase(self)
            else:
                return visitor.visitChildren(self)




    def matchCase(self):

        localctx = stellaParser.MatchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_matchCase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            localctx.pattern_ = self.pattern(0)
            self.state = 553
            self.match(stellaParser.Surrogate_id_SYMB_9)
            self.state = 554
            localctx.expr_ = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_pattern

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PatternConsContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.head = None # PatternContext
            self.tail = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_37(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_37, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_0(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_0, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.PatternContext)
            else:
                return self.getTypedRuleContext(stellaParser.PatternContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternCons" ):
                listener.enterPatternCons(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternCons" ):
                listener.exitPatternCons(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternCons" ):
                return visitor.visitPatternCons(self)
            else:
                return visitor.visitChildren(self)


    class PatternTupleContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self._pattern = None # PatternContext
            self.patterns = list() # of PatternContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.PatternContext)
            else:
                return self.getTypedRuleContext(stellaParser.PatternContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternTuple" ):
                listener.enterPatternTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternTuple" ):
                listener.exitPatternTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternTuple" ):
                return visitor.visitPatternTuple(self)
            else:
                return visitor.visitChildren(self)


    class PatternListContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self._pattern = None # PatternContext
            self.patterns = list() # of PatternContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.PatternContext)
            else:
                return self.getTypedRuleContext(stellaParser.PatternContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternList" ):
                listener.enterPatternList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternList" ):
                listener.exitPatternList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternList" ):
                return visitor.visitPatternList(self)
            else:
                return visitor.visitChildren(self)


    class PatternRecordContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self._labelledPattern = None # LabelledPatternContext
            self.patterns = list() # of LabelledPatternContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def labelledPattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.LabelledPatternContext)
            else:
                return self.getTypedRuleContext(stellaParser.LabelledPatternContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternRecord" ):
                listener.enterPatternRecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternRecord" ):
                listener.exitPatternRecord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternRecord" ):
                return visitor.visitPatternRecord(self)
            else:
                return visitor.visitChildren(self)


    class PatternVariantContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.label = None # Token
            self.pattern_ = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_11(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_11, 0)
        def Surrogate_id_SYMB_12(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_12, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternVariant" ):
                listener.enterPatternVariant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternVariant" ):
                listener.exitPatternVariant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternVariant" ):
                return visitor.visitPatternVariant(self)
            else:
                return visitor.visitChildren(self)


    class PatternAscContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.pattern_ = None # PatternContext
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_36(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_36, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternAsc" ):
                listener.enterPatternAsc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternAsc" ):
                listener.exitPatternAsc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternAsc" ):
                return visitor.visitPatternAsc(self)
            else:
                return visitor.visitChildren(self)


    class PatternIntContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.n = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(stellaParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternInt" ):
                listener.enterPatternInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternInt" ):
                listener.exitPatternInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternInt" ):
                return visitor.visitPatternInt(self)
            else:
                return visitor.visitChildren(self)


    class PatternInrContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.pattern_ = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_49(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_49, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternInr" ):
                listener.enterPatternInr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternInr" ):
                listener.exitPatternInr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternInr" ):
                return visitor.visitPatternInr(self)
            else:
                return visitor.visitChildren(self)


    class PatternTrueContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_60(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_60, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternTrue" ):
                listener.enterPatternTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternTrue" ):
                listener.exitPatternTrue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternTrue" ):
                return visitor.visitPatternTrue(self)
            else:
                return visitor.visitChildren(self)


    class PatternInlContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.pattern_ = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_47(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_47, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternInl" ):
                listener.enterPatternInl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternInl" ):
                listener.exitPatternInl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternInl" ):
                return visitor.visitPatternInl(self)
            else:
                return visitor.visitChildren(self)


    class PatternVarContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternVar" ):
                listener.enterPatternVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternVar" ):
                listener.exitPatternVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternVar" ):
                return visitor.visitPatternVar(self)
            else:
                return visitor.visitChildren(self)


    class PatternConsContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.p1 = None # PatternContext
            self.p2 = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_0(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_0, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.PatternContext)
            else:
                return self.getTypedRuleContext(stellaParser.PatternContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternCons" ):
                listener.enterPatternCons(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternCons" ):
                listener.exitPatternCons(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternCons" ):
                return visitor.visitPatternCons(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisedPatternContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.pattern_ = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesisedPattern" ):
                listener.enterParenthesisedPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesisedPattern" ):
                listener.exitParenthesisedPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesisedPattern" ):
                return visitor.visitParenthesisedPattern(self)
            else:
                return visitor.visitChildren(self)


    class PatternSuccContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.pattern_ = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_57(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_57, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternSucc" ):
                listener.enterPatternSucc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternSucc" ):
                listener.exitPatternSucc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternSucc" ):
                return visitor.visitPatternSucc(self)
            else:
                return visitor.visitChildren(self)


    class PatternFalseContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_41(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_41, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternFalse" ):
                listener.enterPatternFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternFalse" ):
                listener.exitPatternFalse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternFalse" ):
                return visitor.visitPatternFalse(self)
            else:
                return visitor.visitChildren(self)


    class PatternUnitContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_63(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_63, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternUnit" ):
                listener.enterPatternUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternUnit" ):
                listener.exitPatternUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternUnit" ):
                return visitor.visitPatternUnit(self)
            else:
                return visitor.visitChildren(self)


    class PatternCastAsContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.pattern_ = None # PatternContext
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def CAST(self):
            return self.getToken(stellaParser.CAST, 0)
        def Surrogate_id_SYMB_36(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_36, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternCastAs" ):
                listener.enterPatternCastAs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternCastAs" ):
                listener.exitPatternCastAs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternCastAs" ):
                return visitor.visitPatternCastAs(self)
            else:
                return visitor.visitChildren(self)



    def pattern(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = stellaParser.PatternContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_pattern, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                localctx = stellaParser.PatternVariantContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 557
                self.match(stellaParser.Surrogate_id_SYMB_11)
                self.state = 558
                localctx.label = self.match(stellaParser.StellaIdent)
                self.state = 561
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 559
                    self.match(stellaParser.Surrogate_id_SYMB_6)
                    self.state = 560
                    localctx.pattern_ = self.pattern(0)


                self.state = 563
                self.match(stellaParser.Surrogate_id_SYMB_12)
                pass

            elif la_ == 2:
                localctx = stellaParser.PatternInlContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 564
                self.match(stellaParser.Surrogate_id_SYMB_47)
                self.state = 565
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 566
                localctx.pattern_ = self.pattern(0)
                self.state = 567
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 3:
                localctx = stellaParser.PatternInrContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 569
                self.match(stellaParser.Surrogate_id_SYMB_49)
                self.state = 570
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 571
                localctx.pattern_ = self.pattern(0)
                self.state = 572
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 4:
                localctx = stellaParser.PatternTupleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 574
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 583
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2595485433173397544) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 9437185) != 0):
                    self.state = 575
                    localctx._pattern = self.pattern(0)
                    localctx.patterns.append(localctx._pattern)
                    self.state = 580
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 576
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 577
                        localctx._pattern = self.pattern(0)
                        localctx.patterns.append(localctx._pattern)
                        self.state = 582
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 585
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 5:
                localctx = stellaParser.PatternRecordContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 586
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 595
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==84:
                    self.state = 587
                    localctx._labelledPattern = self.labelledPattern()
                    localctx.patterns.append(localctx._labelledPattern)
                    self.state = 592
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 588
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 589
                        localctx._labelledPattern = self.labelledPattern()
                        localctx.patterns.append(localctx._labelledPattern)
                        self.state = 594
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 597
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 6:
                localctx = stellaParser.PatternListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 598
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 607
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2595485433173397544) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 9437185) != 0):
                    self.state = 599
                    localctx._pattern = self.pattern(0)
                    localctx.patterns.append(localctx._pattern)
                    self.state = 604
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 600
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 601
                        localctx._pattern = self.pattern(0)
                        localctx.patterns.append(localctx._pattern)
                        self.state = 606
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 609
                self.match(stellaParser.Surrogate_id_SYMB_14)
                pass

            elif la_ == 7:
                localctx = stellaParser.PatternConsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 610
                self.match(stellaParser.Surrogate_id_SYMB_37)
                self.state = 611
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 612
                localctx.head = self.pattern(0)
                self.state = 613
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 614
                localctx.tail = self.pattern(0)
                self.state = 615
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 8:
                localctx = stellaParser.PatternConsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 617
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 618
                localctx.p1 = self.pattern(0)
                self.state = 619
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 620
                localctx.p2 = self.pattern(0)
                self.state = 621
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 9:
                localctx = stellaParser.PatternFalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 623
                self.match(stellaParser.Surrogate_id_SYMB_41)
                pass

            elif la_ == 10:
                localctx = stellaParser.PatternTrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 624
                self.match(stellaParser.Surrogate_id_SYMB_60)
                pass

            elif la_ == 11:
                localctx = stellaParser.PatternUnitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 625
                self.match(stellaParser.Surrogate_id_SYMB_63)
                pass

            elif la_ == 12:
                localctx = stellaParser.PatternIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 626
                localctx.n = self.match(stellaParser.INTEGER)
                pass

            elif la_ == 13:
                localctx = stellaParser.PatternSuccContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 627
                self.match(stellaParser.Surrogate_id_SYMB_57)
                self.state = 628
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 629
                localctx.pattern_ = self.pattern(0)
                self.state = 630
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 14:
                localctx = stellaParser.PatternVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 632
                localctx.name = self.match(stellaParser.StellaIdent)
                pass

            elif la_ == 15:
                localctx = stellaParser.ParenthesisedPatternContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 633
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 634
                localctx.pattern_ = self.pattern(0)
                self.state = 635
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 648
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 646
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        localctx = stellaParser.PatternAscContext(self, stellaParser.PatternContext(self, _parentctx, _parentState))
                        localctx.pattern_ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_pattern)
                        self.state = 639
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 640
                        self.match(stellaParser.Surrogate_id_SYMB_36)
                        self.state = 641
                        localctx.type_ = self.stellatype(0)
                        pass

                    elif la_ == 2:
                        localctx = stellaParser.PatternCastAsContext(self, stellaParser.PatternContext(self, _parentctx, _parentState))
                        localctx.pattern_ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_pattern)
                        self.state = 642
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 643
                        self.match(stellaParser.CAST)
                        self.state = 644
                        self.match(stellaParser.Surrogate_id_SYMB_36)
                        self.state = 645
                        localctx.type_ = self.stellatype(0)
                        pass

             
                self.state = 650
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LabelledPatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.label = None # Token
            self.pattern_ = None # PatternContext

        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_labelledPattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelledPattern" ):
                listener.enterLabelledPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelledPattern" ):
                listener.exitLabelledPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelledPattern" ):
                return visitor.visitLabelledPattern(self)
            else:
                return visitor.visitChildren(self)




    def labelledPattern(self):

        localctx = stellaParser.LabelledPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_labelledPattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 651
            localctx.label = self.match(stellaParser.StellaIdent)
            self.state = 652
            self.match(stellaParser.Surrogate_id_SYMB_6)
            self.state = 653
            localctx.pattern_ = self.pattern(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StellatypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_stellatype

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TypeTupleContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._stellatype = None # StellatypeContext
            self.types = list() # of StellatypeContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeTuple" ):
                listener.enterTypeTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeTuple" ):
                listener.exitTypeTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeTuple" ):
                return visitor.visitTypeTuple(self)
            else:
                return visitor.visitChildren(self)


    class TypeTopContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOP_TYPE(self):
            return self.getToken(stellaParser.TOP_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeTop" ):
                listener.enterTypeTop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeTop" ):
                listener.exitTypeTop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeTop" ):
                return visitor.visitTypeTop(self)
            else:
                return visitor.visitChildren(self)


    class TypeBoolContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_32(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_32, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeBool" ):
                listener.enterTypeBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeBool" ):
                listener.exitTypeBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeBool" ):
                return visitor.visitTypeBool(self)
            else:
                return visitor.visitChildren(self)


    class TypeRefContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def REF_TYPE(self):
            return self.getToken(stellaParser.REF_TYPE, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeRef" ):
                listener.enterTypeRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeRef" ):
                listener.exitTypeRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeRef" ):
                return visitor.visitTypeRef(self)
            else:
                return visitor.visitChildren(self)


    class TypeRecContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.var = None # Token
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_65(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_65, 0)
        def Surrogate_id_SYMB_25(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_25, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeRec" ):
                listener.enterTypeRec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeRec" ):
                listener.exitTypeRec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeRec" ):
                return visitor.visitTypeRec(self)
            else:
                return visitor.visitChildren(self)


    class TypeAutoContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AUTO_TYPE(self):
            return self.getToken(stellaParser.AUTO_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeAuto" ):
                listener.enterTypeAuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeAuto" ):
                listener.exitTypeAuto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeAuto" ):
                return visitor.visitTypeAuto(self)
            else:
                return visitor.visitChildren(self)


    class TypeSumContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.left = None # StellatypeContext
            self.right = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_21(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_21, 0)
        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSum" ):
                listener.enterTypeSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSum" ):
                listener.exitTypeSum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSum" ):
                return visitor.visitTypeSum(self)
            else:
                return visitor.visitChildren(self)


    class TypeVarContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeVar" ):
                listener.enterTypeVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeVar" ):
                listener.exitTypeVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeVar" ):
                return visitor.visitTypeVar(self)
            else:
                return visitor.visitChildren(self)


    class TypeVariantContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._variantFieldType = None # VariantFieldTypeContext
            self.fieldTypes = list() # of VariantFieldTypeContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_11(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_11, 0)
        def Surrogate_id_SYMB_12(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_12, 0)
        def variantFieldType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.VariantFieldTypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.VariantFieldTypeContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeVariant" ):
                listener.enterTypeVariant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeVariant" ):
                listener.exitTypeVariant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeVariant" ):
                return visitor.visitTypeVariant(self)
            else:
                return visitor.visitChildren(self)


    class TypeUnitContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_34(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_34, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeUnit" ):
                listener.enterTypeUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeUnit" ):
                listener.exitTypeUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeUnit" ):
                return visitor.visitTypeUnit(self)
            else:
                return visitor.visitChildren(self)


    class TypeNatContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_33(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_33, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeNat" ):
                listener.enterTypeNat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeNat" ):
                listener.exitTypeNat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeNat" ):
                return visitor.visitTypeNat(self)
            else:
                return visitor.visitChildren(self)


    class TypeBottomContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOTTOM_TYPE(self):
            return self.getToken(stellaParser.BOTTOM_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeBottom" ):
                listener.enterTypeBottom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeBottom" ):
                listener.exitTypeBottom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeBottom" ):
                return visitor.visitTypeBottom(self)
            else:
                return visitor.visitChildren(self)


    class TypeParensContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeParens" ):
                listener.enterTypeParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeParens" ):
                listener.exitTypeParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeParens" ):
                return visitor.visitTypeParens(self)
            else:
                return visitor.visitChildren(self)


    class TypeFunContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._stellatype = None # StellatypeContext
            self.paramTypes = list() # of StellatypeContexts
            self.returnType = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_43(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_43, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def Surrogate_id_SYMB_8(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_8, 0)
        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeFun" ):
                listener.enterTypeFun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeFun" ):
                listener.exitTypeFun(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeFun" ):
                return visitor.visitTypeFun(self)
            else:
                return visitor.visitChildren(self)


    class TypeForAllContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._StellaIdent = None # Token
            self.types = list() # of Tokens
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def FORALL(self):
            return self.getToken(stellaParser.FORALL, 0)
        def Surrogate_id_SYMB_25(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_25, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)

        def StellaIdent(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.StellaIdent)
            else:
                return self.getToken(stellaParser.StellaIdent, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeForAll" ):
                listener.enterTypeForAll(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeForAll" ):
                listener.exitTypeForAll(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeForAll" ):
                return visitor.visitTypeForAll(self)
            else:
                return visitor.visitChildren(self)


    class TypeRecordContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._recordFieldType = None # RecordFieldTypeContext
            self.fieldTypes = list() # of RecordFieldTypeContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def recordFieldType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.RecordFieldTypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.RecordFieldTypeContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeRecord" ):
                listener.enterTypeRecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeRecord" ):
                listener.exitTypeRecord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeRecord" ):
                return visitor.visitTypeRecord(self)
            else:
                return visitor.visitChildren(self)


    class TypeListContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeList" ):
                listener.enterTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeList" ):
                listener.exitTypeList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeList" ):
                return visitor.visitTypeList(self)
            else:
                return visitor.visitChildren(self)



    def stellatype(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = stellaParser.StellatypeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_stellatype, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 736
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                localctx = stellaParser.TypeBoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 656
                self.match(stellaParser.Surrogate_id_SYMB_32)
                pass

            elif la_ == 2:
                localctx = stellaParser.TypeNatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 657
                self.match(stellaParser.Surrogate_id_SYMB_33)
                pass

            elif la_ == 3:
                localctx = stellaParser.TypeRefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 658
                self.match(stellaParser.REF_TYPE)
                self.state = 659
                localctx.type_ = self.stellatype(15)
                pass

            elif la_ == 4:
                localctx = stellaParser.TypeFunContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 660
                self.match(stellaParser.Surrogate_id_SYMB_43)
                self.state = 661
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 670
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 17652315607080) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 309281) != 0):
                    self.state = 662
                    localctx._stellatype = self.stellatype(0)
                    localctx.paramTypes.append(localctx._stellatype)
                    self.state = 667
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 663
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 664
                        localctx._stellatype = self.stellatype(0)
                        localctx.paramTypes.append(localctx._stellatype)
                        self.state = 669
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 672
                self.match(stellaParser.Surrogate_id_SYMB_3)
                self.state = 673
                self.match(stellaParser.Surrogate_id_SYMB_8)
                self.state = 674
                localctx.returnType = self.stellatype(13)
                pass

            elif la_ == 5:
                localctx = stellaParser.TypeForAllContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 675
                self.match(stellaParser.FORALL)
                self.state = 679
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==84:
                    self.state = 676
                    localctx._StellaIdent = self.match(stellaParser.StellaIdent)
                    localctx.types.append(localctx._StellaIdent)
                    self.state = 681
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 682
                self.match(stellaParser.Surrogate_id_SYMB_25)
                self.state = 683
                localctx.type_ = self.stellatype(12)
                pass

            elif la_ == 6:
                localctx = stellaParser.TypeRecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 684
                self.match(stellaParser.Surrogate_id_SYMB_65)
                self.state = 685
                localctx.var = self.match(stellaParser.StellaIdent)
                self.state = 686
                self.match(stellaParser.Surrogate_id_SYMB_25)
                self.state = 687
                localctx.type_ = self.stellatype(11)
                pass

            elif la_ == 7:
                localctx = stellaParser.TypeTupleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 688
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 697
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 17652315607080) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 309281) != 0):
                    self.state = 689
                    localctx._stellatype = self.stellatype(0)
                    localctx.types.append(localctx._stellatype)
                    self.state = 694
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 690
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 691
                        localctx._stellatype = self.stellatype(0)
                        localctx.types.append(localctx._stellatype)
                        self.state = 696
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 699
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 8:
                localctx = stellaParser.TypeRecordContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 700
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 701
                localctx._recordFieldType = self.recordFieldType()
                localctx.fieldTypes.append(localctx._recordFieldType)
                self.state = 706
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 702
                    self.match(stellaParser.Surrogate_id_SYMB_0)
                    self.state = 703
                    localctx._recordFieldType = self.recordFieldType()
                    localctx.fieldTypes.append(localctx._recordFieldType)
                    self.state = 708
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 709
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 9:
                localctx = stellaParser.TypeVariantContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 711
                self.match(stellaParser.Surrogate_id_SYMB_11)
                self.state = 720
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==84:
                    self.state = 712
                    localctx._variantFieldType = self.variantFieldType()
                    localctx.fieldTypes.append(localctx._variantFieldType)
                    self.state = 717
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 713
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 714
                        localctx._variantFieldType = self.variantFieldType()
                        localctx.fieldTypes.append(localctx._variantFieldType)
                        self.state = 719
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 722
                self.match(stellaParser.Surrogate_id_SYMB_12)
                pass

            elif la_ == 10:
                localctx = stellaParser.TypeListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 723
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 724
                localctx.type_ = self.stellatype(0)
                self.state = 725
                self.match(stellaParser.Surrogate_id_SYMB_14)
                pass

            elif la_ == 11:
                localctx = stellaParser.TypeUnitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 727
                self.match(stellaParser.Surrogate_id_SYMB_34)
                pass

            elif la_ == 12:
                localctx = stellaParser.TypeTopContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 728
                self.match(stellaParser.TOP_TYPE)
                pass

            elif la_ == 13:
                localctx = stellaParser.TypeBottomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 729
                self.match(stellaParser.BOTTOM_TYPE)
                pass

            elif la_ == 14:
                localctx = stellaParser.TypeAutoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 730
                self.match(stellaParser.AUTO_TYPE)
                pass

            elif la_ == 15:
                localctx = stellaParser.TypeVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 731
                localctx.name = self.match(stellaParser.StellaIdent)
                pass

            elif la_ == 16:
                localctx = stellaParser.TypeParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 732
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 733
                localctx.type_ = self.stellatype(0)
                self.state = 734
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 743
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = stellaParser.TypeSumContext(self, stellaParser.StellatypeContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stellatype)
                    self.state = 738
                    if not self.precpred(self._ctx, 14):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                    self.state = 739
                    self.match(stellaParser.Surrogate_id_SYMB_21)
                    self.state = 740
                    localctx.right = self.stellatype(15) 
                self.state = 745
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RecordFieldTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.label = None # Token
            self.type_ = None # StellatypeContext

        def Surrogate_id_SYMB_7(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_7, 0)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_recordFieldType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecordFieldType" ):
                listener.enterRecordFieldType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecordFieldType" ):
                listener.exitRecordFieldType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecordFieldType" ):
                return visitor.visitRecordFieldType(self)
            else:
                return visitor.visitChildren(self)




    def recordFieldType(self):

        localctx = stellaParser.RecordFieldTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_recordFieldType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 746
            localctx.label = self.match(stellaParser.StellaIdent)
            self.state = 747
            self.match(stellaParser.Surrogate_id_SYMB_7)
            self.state = 748
            localctx.type_ = self.stellatype(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariantFieldTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.label = None # Token
            self.type_ = None # StellatypeContext

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def Surrogate_id_SYMB_7(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_7, 0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_variantFieldType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariantFieldType" ):
                listener.enterVariantFieldType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariantFieldType" ):
                listener.exitVariantFieldType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariantFieldType" ):
                return visitor.visitVariantFieldType(self)
            else:
                return visitor.visitChildren(self)




    def variantFieldType(self):

        localctx = stellaParser.VariantFieldTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_variantFieldType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 750
            localctx.label = self.match(stellaParser.StellaIdent)
            self.state = 753
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 751
                self.match(stellaParser.Surrogate_id_SYMB_7)
                self.state = 752
                localctx.type_ = self.stellatype(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expr_sempred
        self._predicates[13] = self.pattern_sempred
        self._predicates[15] = self.stellatype_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 59)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 58)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 32)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 1)
         

    def pattern_sempred(self, localctx:PatternContext, predIndex:int):
            if predIndex == 21:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 2)
         

    def stellatype_sempred(self, localctx:StellatypeContext, predIndex:int):
            if predIndex == 23:
                return self.precpred(self._ctx, 14)
         




