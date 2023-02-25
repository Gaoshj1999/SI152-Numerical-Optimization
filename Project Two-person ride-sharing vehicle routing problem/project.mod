set rider; # set of riders
set request; # set of requests
set trip {rider}; #for each riders,there will be a feasible trip set
set Trip;
param cost {i in rider,trip[i]}; # cost of response
param exist {request,Trip}; #whether request is in the trip
var response {i in rider,trip[i]} binary; # whether rider is response to the trip
minimize totalcost:
sum {i in rider} sum {j in trip[i]} cost[i,j]*response[i,j];
subject to Response {i in rider}:
sum {j in trip[i]} response[i,j]<=1;
subject to Completeresponse {k in request}:
sum{i in rider} sum{j in trip[i]} exist[k,j]*response[i,j]=1;