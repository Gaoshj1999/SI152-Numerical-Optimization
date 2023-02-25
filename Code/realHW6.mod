set CITYI;
set CITYJ;
param cost {CITYI} >= 0; 
param population {CITYJ} >= 0; 
param distance {CITYI,CITYJ} >= 0; 
var open {CITYI} binary; 
var proportion {CITYI,CITYJ} >= 0;
var time {CITYI,CITYJ} binary;
minimize Total_Cost:
sum {i in CITYI} cost[i] * open[i];
subject to Proportion {j in CITYJ}:
sum {i in CITYI} proportion[i,j] = 1;
subject to Open {i in CITYI,j in CITYJ}:
proportion[i,j] <= open[i];
subject to  Distance1 {i in CITYI,j in CITYJ}:
distance[i,j] <= 30+2579.1*(1-time[i,j]);
subject to  Distance2 {i in CITYI,j in CITYJ}:
distance[i,j] >= 30+0.000000000000001-2579.1*time[i,j];
subject to Requirement :
sum {j in CITYJ} sum {i in CITYI} population[j]*proportion[i,j]*time[i,j]>=0.9*66243219;