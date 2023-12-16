import workflow_functions as wf

for i in snakemake.input:
    wf.print_result(i, snakemake.output[0])
