gnuplot << EOF
set term svg size 1500,1200 font 'Verdana,25'
set output "output/run$1-$2.svg"

set key below

set title "Servo Angle and Current as a Function of Time with $3 kg-cm of Torque"
set xlabel "Time(ms)"
set ylabel "Position(degrees)"
set y2label "Current(amps)"

set yrange [-30:180]
set y2range [-.5:3]
set ytics 20 nomirror tc lt 1
set y2tics 0.5 nomirror tc lt 2

stats "processed/processed$1-$2.txt" u 1:2

f(x) = a*x + b
fit [200:(STATS_max_x-200)] f(x) "processed/processed$1-$2.txt" u 1:2 via a,b
g(x) = d
fit [200:(STATS_max_x-200)] g(x) "processed/processed$1-$2.txt" u 1:3 via d

title_f(a,b) = sprintf('f(x) = %.6fx + %.6f', a, b)
title_g(b) = sprintf('f(x) = %0.6f', b)

plot "processed/processed$1-$2.txt" u 1:2 lt 1 axes x1y1 ti "Position(degrees)", "processed/processed$1-$2.txt" u 1:3 lt 2 axes x1y2 ti "Current(amps)", f(x) axes x1y1 lc rgb "blue" ti title_f(a,b), g(x) axes x1y2 lc rgb "green" ti title_g(d)
set out
EOF
