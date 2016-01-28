gnuplot << EOF
set term svg size 1500,1200 font 'Verdana,25'
set output "output/runsetpos$1.svg"

set key below
set ylabel "Position(degrees)"
set xlabel "Time(ms)"
set title "Servo Angle as a Function of Time and Torque"
plot "processed/processed0-$1.txt" u (\$1):(\$2) t "0 kg-cm", "processed/processed85-$1.txt" u (\$1):(\$2) t "0.85 kg-cm", \
"processed/processed100-$1.txt" u (\$1):(\$2) t "1 kg-cm", "processed/processed125-$1.txt" u (\$1):(\$2) t "1.25 kg-cm", \
"processed/processed150-$1.txt" u (\$1):(\$2) t "1.5 kg-cm", "processed/processed175-$1.txt" u (\$1):(\$2) t "1.75 kg-cm", \
"processed/processed200-$1.txt" u (\$1):(\$2) t "2 kg-cm", "processed/processed250-$1.txt" u (\$1):(\$2) t "2.5 kg-cm", \
"processed/processed300-$1.txt" u (\$1):(\$2) t "3 kg-cm", "processed/processed350-$1.txt" u (\$1):(\$2) t "3.5 kg-cm", \
"processed/processed400-$1.txt" u (\$1):(\$2) t "4 kg-cm", "processed/processed450-$1.txt" u (\$1):(\$2) t "4.5 kg-cm", \
"processed/processed500-$1.txt" u (\$1):(\$2) t "5 kg-cm", "processed/processed550-$1.txt" u (\$1):(\$2) t "5.5 kg-cm", \
"processed/processed600-$1.txt" u (\$1):(\$2) t "6 kg-cm", "processed/processed650-$1.txt" u (\$1):(\$2) t "6.5 kg-cm", \
"processed/processed700-$1.txt" u (\$1):(\$2) t "7 kg-cm", "processed/processed750-$1.txt" u (\$1):(\$2) t "7.5 kg-cm"
set out
EOF
