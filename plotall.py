import os
import errno

def run_svg_name(weight, run):
    return "run" + str(weight) + "-" + str(run) + ".svg"

def run_pdf_name(weight, run):
    return "run" + str(weight) + "-" + str(run) + ".pdf"

def runsetpos_svg_name(run):
    return "runsetpos" + str(run) + ".svg"

def runsetpos_pdf_name(run):
    return "runsetpos" + str(run) + ".pdf"

def runsetcur_svg_name(run):
    return "runsetcur" + str(run) + ".svg"

def runsetcur_pdf_name(run):
    return "runsetcur" + str(run) + ".pdf"

def plot_run(weight, run):
    kgcm = weight / 100.0
    svg_command = "./plotrun.sh " + str(weight) + " " + str(run) + " " + str(kgcm)
    print svg_command
    os.system(svg_command)
    pdf_command = "svg2pdf " + "output/" + run_svg_name(weight, run) + " output/" + run_pdf_name(weight, run)
    print pdf_command
    os.system(pdf_command)

def plot_runsetpos(run):
    svg_command = "./plotrunsetpos.sh " + str(run)
    print(svg_command)
    os.system(svg_command)
    pdf_command = "svg2pdf " + "output/" + runsetpos_svg_name(run) + " output/" + runsetpos_pdf_name(run)
    print pdf_command
    os.system(pdf_command)

def plot_runsetcur(run):
    svg_command = "./plotrunsetcur.sh " + str(run)
    print(svg_command)
    os.system(svg_command)
    pdf_command = "svg2pdf " + "output/" + runsetcur_svg_name(run) + " output/" + runsetcur_pdf_name(run)
    print pdf_command
    os.system(pdf_command)    

os.mkdir("output")

weights=[0, 85, 100, 125, 150, 175, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700]

for weight in weights:
    for run in range(0, 6):
        plot_run(weight, run)

# plot these explicitly because there are not six of them
plot_run(750, 0)
plot_run(750, 1)
plot_run(750, 3)

for run in range(0, 6):
    plot_runsetpos(run)
    plot_runsetcur(run)

os.system("rm -rf svg-graphs")
os.system("rm -rf graphs")
os.rename("output", "svg-graphs")
os.mkdir("graphs")
os.system("mv svg-graphs/*.pdf graphs")
os.system("rm -rf svg-graphs")
os.remove("fit.log")
