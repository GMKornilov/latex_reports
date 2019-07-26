from subprocess import Popen, PIPE, STDOUT, run
import os
import sys

correct = "17_07_work.tex"
wrong = "18_07.tex"

#code_correct = subprocess.call("pdflatex " + correct)
#print(code_correct)

#code_wrong = subprocess.call("pdflatex " + wrong)
#print(code_wrong)
correct_proc = run(['pdflatex', correct], input="X", encoding="ascii")
print(correct_proc.returncode)
wrong_proc = run(['pdflatex', wrong], input="X", encoding="ascii")
print(wrong_proc.returncode)

