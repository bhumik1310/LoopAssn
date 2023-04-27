##Interpolation.

## This algorithm basically assumes that the interpolated timings lie on a normal curve with a set mean and standard deviation with store_status(open) having a bias of 2
# against a bias of 1 for a store_status(closed)
## The algorithm would take in the start and end times from the rel_times datasheet , with the datapoints into a set , iterate over the set like so:


## for every date in a store id:
##  if set(date) == set(date+1): move n store times to date_set
##  start = menu_start_time
## for all times in date_set till last second timestamp
##  curr = first date point in the set
##  generate random numbers using numpy.random.normal with mean = 30 mins and std-dev = 5 mins with status 'closed' for every second status'open'
##  new_time = add these minute marks to the hour marks of curr a and add to interpolated_set
##  recurse till new_time>curr && count<5  Inserting only 5 values between two succesive relevant timings.
## start = time+1
## curr = curr+1

## The interpolated_set has a list of all interpolated timings between start and end time and thus this can be iterated over to get the required csv outputted via aiostream
## to the endpoint


