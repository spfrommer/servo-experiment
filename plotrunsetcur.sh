gnuplot << EOF
set term svg size 1500,1200 font 'Verdana,25'
set output "output/runsetcur$1.svg"
set style fill transparent solid 0.5 noborder

set key below
set ylabel "Current(amps)"
set xlabel "Time(ms)"
set title "Current as a Function of Time and Torque"
plot "processed/processed0-$1.txt" u (\$1):(\$3) t "0 kg-cm" pt 5 ps 0.5, "processed/processed250-$1.txt" u (\$1):(\$3) t "2.5 kg-cm" pt 7 ps 0.5, \
"processed/processed500-$1.txt" u (\$1):(\$3) t "5 kg-cm" pt 9 ps 0.5, "processed/processed700-$1.txt" u (\$1):(\$3) t "7 kg-cm" pt 13 ps 0.5
set out
EOF
