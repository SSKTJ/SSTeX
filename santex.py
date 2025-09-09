print("SanTeX Interpreter V0.1")

input_source = input("Enter the input source: ")
inp = open(input_source, "r")
output_file = input("Enter the output file: ")
out = open(output_file, "w")
out.close()
out = open(output_file, "a")

x = inp.readlines()
print(x)

out.write("""\\documentclass[a4paper,10pt]{article}
\\usepackage{graphicx}
\\usepackage[margin=1in]{geometry}\n""")

if "#index\n" in x:
    out.write("\\usepackage{tocloft}\n")

for i in x:

    if i.startswith("#index"):
        out.write("\\tableofcontents\n")

    elif i.startswith("#title "):
        s = "\\title{" + i.partition(" ")[2][:-1] + "}\n"
        out.write(s)

    elif i.startswith("#author "):
        s = "\\author{" + i.partition(" ")[2][:-1] + "}\n"
        out.write(s)

    elif i.startswith("#date "):
        s = "\\date{" + i.partition(" ")[2][:-1] + "}\n"
        out.write(s)

    elif i.startswith("#begin"):
        s = "\\begin{document}\n"
        out.write(s)

    elif i.startswith("#maketitle"):
        s = "\\maketitle\n"
        out.write(s)

    elif i.startswith("# "):
        s = "\\section{" + i.partition(" ")[2][:-1] + "}\n"
        out.write(s)

    elif i.startswith("## "):
        s = "\\subsection{" + i.partition(" ")[2][:-1] + "}\n"
        out.write(s)

    elif i.startswith("### "):
        s = "\\subsubsection{" + i.partition(" ")[2][:-1] + "}\n"
        out.write(s)

    elif i.startswith("#ul"):
        s = "\\begin{itemize}\n"
        out.write(s)

    elif i.startswith("- "):
        s = "\\item{" + i.partition(" ")[2][:-1] + "}\n"
        out.write(s)

    elif i.startswith("#endul"):
        s = "\\end{itemize}\n"
        out.write(s)

    elif i.startswith("#l"):
        s = "\\begin{enumerate}\n"
        out.write(s)

    elif i.startswith("#endl"):
        s = "\\end{enumerate}\n"
        out.write(s)

    elif i.startswith("#end"):
        s = "\\end{document}\n"
        out.write(s)

    elif i.startswith("#table "):
        arr = i.split()
        s = "\\begin{tabular}{" + arr[1] + "}"
        out.write(s)
        s="\\hline"
    
    elif i.startswith("#endtable"):
        s ="\\end{tabular}"
        out.write(s)

    else:
        out.write(i)

inp.close()