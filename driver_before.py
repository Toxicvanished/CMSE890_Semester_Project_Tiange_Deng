import workflow_functions as wf

"""Read in keywords, modify keywords, and generate a new input file based on the template"""

premade_file = input("Please input the path of the .csv file for keywords:")
keyword_list = wf.read_keyword_list(premade_file)
modified_keywords = wf.make_modified_keyword(keyword_list)
template_input_file = input("Please input the path of the template input file:")
wf.make_new_input(template_input_file, modified_keywords)
