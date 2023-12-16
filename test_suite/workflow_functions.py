"""Following functions are the functions for the first part of the workflow"""
import re

def read_keyword_list(premade_file):
    """This function reads the premade category-keywords .csv file and return a
    dictionary contains the pertinent keywords to be submitted to modifications.

    Parameters
    ----------
    premade_file : str
        Path to the category-keywords file.

    Returns
    -------
    keyword_list : dict
        The dictionary classifies corresponding keywords to certain categories as lists.
    """
    keyword_list = {}
    with open(premade_file) as p:
        next(p)
        for line in p.readlines():
            L = line.strip().split(",")
            L2 = [l for l in L if l]
            keyword_list[L2[0]] = L2[1:-1]

    return keyword_list


def make_modified_keyword(keyword_list):
    """This function ask for the desired pertinent modified keywords and returns a
       dictionary for making the new input file.

    Parameters
    ----------
    keyword_list : dict
        The dictionary classifies corresponding keywords to certain categories as lists.

    Returns
    -------
    modified_keywords : dict
        The dictionary with modified value for each chosen keyword.
    """
    modified_keywords = {}
    for category in keyword_list.keys():
        option_1 = input("Do you want to modify the" + ' ' + category + ' ' + "category?(y/n)")
        if option_1.lower() == "n":
            continue
        else:
            modified_keyword = {}
            for keyword in keyword_list[category]:
                option_2 = input(
                    "Do you want to modify the"
                    + ' ' + keyword + ' ' 
                    + "keyword in the"
                    + ' ' + category + ' '
                    + "category?(y/n)"
                )
                if option_2.lower() == "n":
                    continue
                else:
                    option_3 = input("Please input the keyword value:")
                    modified_keyword[keyword] = option_3
            modified_keywords[category] = modified_keyword
    return modified_keywords


def make_new_input(template, new_input_file, modified_keywords):
    """This function use the modified keywords to make new input files.

    Parameters
    ----------
    template : str
        Specify the path of template input file

    Returns
    -------
    None. Generate a new modified input file.
    """
    with open(new_input_file, "a", encoding="utf-8") as f, open(
        template, "r", encoding="utf-8"
    ) as t:
        for line in t:
            write = False
            for category in modified_keywords.keys():
                if category not in line:
                    continue
                else:
                    write = True
                    tline_split = line.strip().split(" ")
                    new_line = ' ' + tline_split[0]
                    for keyword in tline_split[1:-1]:
                        sub_keyword = keyword.strip().split('=')[0]
                        if (
                            sub_keyword in modified_keywords[category].keys()
                        ):
                            new_line += (
                                ' '
                                + keyword.strip().split('=')[0]
                                + '='
                                + modified_keywords[category][sub_keyword]
                            )
                        else:
                            new_line += ' ' + keyword
                    new_line += ' ' + '$END' + '\n'
            if not write: 
                f.write(line)
            else:
                f.write(new_line)
                    


"""Following functions are the functions for the second part of the workflow"""


def print_result(read_log_file, result_condensed):
    """This function reads the output .log files and returns a dictionary contains
       pertinent energy for different approaches

    Parameters
    ----------
    read_log_file : str
        Specify the path of template input file

    Returns
    -------
    energy : dict
        The dictionary which contains target eneretics.
    """
    with open(read_log_file, 'r') as r, open(result_condensed, "a", encoding="utf-8") as t:
        lines = r.readlines()
        for line in lines:
            if "Copying input file" in line:
                name = line.strip().split('/')[-1].strip().split(' ')[0]
            if "FINAL ROHF ENERGY IS" in line:
                match = re.search(r'-?\d+\.\d+', line)
                new_line = name + ' ' + 'SCF' + ' ' + match.group()
            if "CCSDt ENERGY" in line:
                match_2 = re.search(r'-?\d+\.\d+', line)
                new_line += ' ' + 'CCSDt' + ' ' + match_2.group() + '\n'
        t.write(new_line)

