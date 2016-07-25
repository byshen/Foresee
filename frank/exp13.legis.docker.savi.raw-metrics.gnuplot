reset
set multiplot layout 4, 1

#set size ratio 0.145 # 4 plots
set size ratio 0.120 # 4 plots
#set xlabel "Time" font "Arial, 10"
set ytics nomirror
set y2tics
set xrange [*:*]
set yrange [*:*]
set y2range [*:*]
set tics font "Arial, 10"
set key font "Arial, 10" below
#set style fill  transparent solid 0.50 noborder
set grid front y2tics layerdefault linetype 0 linewidth 1.000 linecolor rgb "#555555"






# use "dashtype 2" for dashed line
set style line  1 linewidth 2 linecolor rgb "#0060ad" linetype 1 # blue
set style line  2 linewidth 2 linecolor rgb "#dd181f" linetype 1 # red
set style line  3 linewidth 2 linecolor rgb "#008000" linetype 1 # green
set style line  4 linewidth 2 linecolor rgb "#FFA500" linetype 1 # orange
set style line  5 linewidth 2 linecolor rgb "#C849C3" linetype 1 # purple
set style line  6 linewidth 2 linecolor rgb "#39B396" linetype 1 # 
set style line  7 linewidth 2 linecolor rgb "#C8A385" linetype 1 # 
set style line  8 linewidth 2 linecolor rgb "#5C402A" linetype 1 # 
set style line  9 linewidth 2 linecolor rgb "#F4E28A" linetype 1 # 
set style line 10 linewidth 2 linecolor rgb "#2185F4" linetype 1 # 
set style line 11 linewidth 2 linecolor rgb "#0060ad" linetype 1 dashtype 3 # blue
set style line 12 linewidth 2 linecolor rgb "#dd181f" linetype 1 dashtype 3 # red
set style line 13 linewidth 2 linecolor rgb "#008000" linetype 1 dashtype 3 # green
set style line 14 linewidth 2 linecolor rgb "#FFA500" linetype 1 dashtype 3 # orange
set style line 15 linewidth 2 linecolor rgb "#C849C3" linetype 1 dashtype 3 # purple
set style line 16 linewidth 2 linecolor rgb "#39B396" linetype 1 dashtype 3 # 
set style line 17 linewidth 2 linecolor rgb "#C8A385" linetype 1 dashtype 3 #
set style line 18 linewidth 2 linecolor rgb "#5C402A" linetype 1 dashtype 3 #
set style line 19 linewidth 2 linecolor rgb "#F4E28A" linetype 1 dashtype 3 # 
set style line 20 linewidth 2 linecolor rgb "#2185F4" linetype 1 dashtype 3 # 



#  smooth acsplines

set ylabel "CPU VMs (%)" font "Arial, 10"
set y2label "Memory VMs (MB)" font "Arial, 10"
set format y "%4.0f"
set format y2 "%4.0f"
set yrange [-5:*]
set y2range [*:*]
plot "exp13.legis.docker.savi.raw-metrics.data" using  2 with lines axis x1y1 linestyle  1 title "cpu.manager", \
     "exp13.legis.docker.savi.raw-metrics.data" using  4 with lines axis x1y1 linestyle  2 title "cpu.worker-1", \
     "exp13.legis.docker.savi.raw-metrics.data" using  5 with lines axis x1y1 linestyle  3 title "cpu.worker-2", \
     "exp13.legis.docker.savi.raw-metrics.data" using  6 with lines axis x1y1 linestyle  4 title "cpu.worker-3", \
     "exp13.legis.docker.savi.raw-metrics.data" using  7 with lines axis x1y1 linestyle  5 title "cpu.cass-1", \
     "exp13.legis.docker.savi.raw-metrics.data" using (7984)- ($8)/(1024) with lines axis x1y2 linestyle 11 title "mem.manager", \
     "exp13.legis.docker.savi.raw-metrics.data" using (7984)- ($9)/(1024) with lines axis x1y2 linestyle 12 title "mem.worker-1", \
     "exp13.legis.docker.savi.raw-metrics.data" using (7984)-($10)/(1024) with lines axis x1y2 linestyle 13 title "mem.worker-2", \
     "exp13.legis.docker.savi.raw-metrics.data" using (7984)-($11)/(1024) with lines axis x1y2 linestyle 14 title "mem.worker-3", \
     "exp13.legis.docker.savi.raw-metrics.data" using (7984)-($12)/(1024) with lines axis x1y2 linestyle 15 title "mem.cass-1", \


set ylabel "CPU Containers (%)" font "Arial, 10"
set y2label "Memory Container (MB)" font "Arial, 10"
set format y "%4.0f"
set format y2 "%4.0f"
set yrange [-0.001:*]
set y2range [-1:*]
plot "exp13.legis.docker.savi.raw-metrics.data" using ($16)*(1.00) with lines axis x1y1 linestyle  1 title "cpu.spark-master", \
     "exp13.legis.docker.savi.raw-metrics.data" using ($17)*(1.00) with lines axis x1y1 linestyle  2 title "cpu.spark-worker (avg)", \
     "exp13.legis.docker.savi.raw-metrics.data" using ($18)*(1.00) with lines axis x1y1 linestyle  3 title "cpu.load-balancer", \
     "exp13.legis.docker.savi.raw-metrics.data" using ($19)*(1.00) with lines axis x1y1 linestyle  4 title "cpu.web-worker (avg)", \
     "exp13.legis.docker.savi.raw-metrics.data" using ($27)/(1024)/(1024) with lines axis x1y2 linestyle  11 title "mem.spark-master", \
     "exp13.legis.docker.savi.raw-metrics.data" using ($31)/(1024)/(1024) with lines axis x1y2 linestyle  12 title "mem.spark-worker-1", \
     "exp13.legis.docker.savi.raw-metrics.data" using ($71)/(1024)/(1024) with lines axis x1y2 linestyle  13 title "mem.load-balancer", \
     "exp13.legis.docker.savi.raw-metrics.data" using ($75)/(1024)/(1024) with lines axis x1y2 linestyle  14 title "mem.web-worker-1", \


set ylabel "VMs (#)" font "Arial, 10"
set y2label "Containers (#)" font "Arial, 10"
set format y "%4.0f"
set format y2 "%4.0f"
set yrange [0:*]
set y2range [0:*]
plot 3 with lines axis x1y1 linestyle  1 title "vm.workers", \
     "exp13.legis.docker.savi.raw-metrics.data" using ($13)*(1.00) with lines axis x1y2 linestyle  4 title "containers.web", \
     "exp13.legis.docker.savi.raw-metrics.data" using ($14)*(1.00) with lines axis x1y2 linestyle  5 title "containers.spark", \
     "exp13.legis.docker.savi.raw-metrics.data" using ($15)*(1.00) with lines axis x1y2 linestyle  6 title "containers.cassandra"


set ylabel "Arrival Rate (req / s)" font "Arial, 10"
set y2label "Response Time (s)" font "Arial, 10"
set format y "%4.2f"
set format y2 "%4.2f"
set yrange [0:*]
set y2range [0:*]
plot "exp13.legis.docker.savi.raw-metrics.data" using 21 with lines axis x1y1 linestyle  2 title "arrival rate", \
     "exp13.legis.docker.savi.raw-metrics.data" using ($23)/1000 with lines axis x1y2 linestyle  3 title "response time", \


#pause 60
#reread
