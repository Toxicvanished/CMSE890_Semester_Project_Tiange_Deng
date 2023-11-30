def read_keyword_list(premade_file):
    """This function reads the premade category-keywords .csv file and return a
    dictionary contains the pertinent keywords to be submitted to modifications.

    Parameters
    ----------
    fpremade_file : str
        Path to the category-keywords file.

    Returns
    -------
    keyword_list : dictionary
        The dictionary classifies corresponding keywords to certain categories as lists.
    """
    keyword_list = {}
    with open(premade_file) as p:
        for line in p.readlines():
            next(f)
            L = line.strip().split(',')
            for i, cat_key in enumerate(L):
                if cat_key == None:
                    L.pop(i)
                keyword_list[L[0]] = L[1:-1]
    
    return keyword_list






def make_modified_keyword(keyword_list):
    """This function ask for the desired pertinent modified keywords and returns a 
       dictionary for making the new input file.

    Parameters
    ----------
    keyword_list : dictionary
        The dictionary classifies corresponding keywords to certain categories as lists.

    Returns
    -------
    modified_keywords : dictionary
        The dictionary with modified value for each chosen keyword.
    """
    modified_keywords = {}
    for category in keyword_list.keys():
        option_1 = input('Do you want to modify the' + category + 'category?(y/n)')
        if option_1.lower() = 'n':
            continue
        else:
            modified_keyword = {}
            for keyword in keyword_list[category]:
                option_2 = input('Do you want to modify the' + keyword + 'keyword in the' + category + 'category?(y/n)')
                if option_2.lower() == 'n':
                    continue
                else:
                    option_3 = input('Please input the keyword value:')
                    modified_keyword[keyword] = option_3
            modified_keywords[category] = modified_keyword
    return modified_keywords





def make_new_input(template,modified_keywords):
    """This function use the modified keywords to make new input files.

    Parameters
    ----------
    template : str
        Specify the 

    Returns
    -------
    modified_keywords : dictionary
        The dictionary with modified value for each chosen keyword.
    """