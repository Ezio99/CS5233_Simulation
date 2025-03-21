# On Modeling

Each attraction have the same components that I duplicated across all of them. I can make it into submodels when we submit to make it more 'readable' but now I am more concerned in debugging where we can access every component without digging into individual submodels.

Below are the values that you might want to take note or tweak in experiment. Note that the replication process base time is in minutes.

## Variables

There are 8 variables but only two values to tweak `AvailableBicycle` and `AvailableDock`. I can't get areana reading the variables from file so you will need to set the values individually.

- `AvailableBicycle_A`: set to 80
- `AvailableBicycle_B`: set to 80
- `AvailableBicycle_C`: set to 80
- `AvailableBicycle_D`: set to 80
- `AvailableDock_A`: set to 0
- `AvailableDock_B`: set to 0
- `AvailableDock_C`: set to 0
- `AvailableDock_D`: set to 0

Note: `AvailableDock` + `AvailableBicycle` must be equal to number of docks we have. In this case, we have 80 docks (0 available docks, 80 bicycles avaiable) 

## Attributes

These attributes assign the values of speed and number of visits. They are under the `Assign Number of Visits and Speed at {attractiion}`.

- `Number of visits`: Currently this is set to `DISC(0.33333, 2, 0.66666, 3, 1.0, 4)`. Basically, this assigns probability in accumulative fashion (don't ask me why is this the case); it's equally probably to have the same probability assign to each visit.
- `Speed`: Currently set to 1 km/h. Please refer to the report for the input distribution.


## Visiting time

Time spent in visiting are in the delay module. Please refer to the report for the input distribution.

- `Visit A`
- `Visit B`
- `Visit C`
- `Visit D`

All of them are set to 20 mins. You will need to replace this with the time spent distribution in each attraction

## Arrival time

Arrival time are determined by the Create module. Please refer to the report for the input distribution.

- `Tourist Enters A`
- `Tourist Enters B`
- `Tourist Enters C`
- `Tourist Enters D`

All of them are set to 20 mins. You will need to replace this with the arrival time distribution for each attraction

## Time taken to cycle

This is determined by the Route module (the one with green arrow). 

- `Cycle to A`: Set `1/Speed`
- `Cycle to B`: Set `2 / Speed`
- `Cycle to C`: Set `2.5 / Speed`
- `Cycle to D`: Set `3 / Speed`

Where `Speed` refers to the speed attribute assigned in `Assign Number of Visits and Speed at {attractiion}`. Also note, this returns in hours to keep it consistent with the distance and speed reported.

## Files written

There will be 8 files written. Each file store the waiting time of each entity.

- `bicycle_queue_A.csv`
- `bicycle_queue_B.csv`
- `bicycle_queue_C.csv`
- `bicycle_queue_D.csv`
- `dock_queue_A.csv`
- `dock_queue_B.csv`
- `dock_queue_C.csv`
- `dock_queue_D.csv`

Each file as the following field: `replication_no`,`time`, `id`, `prev_WaitTime`, `curr_WaitTime`. `time` is current timestamp. `replication_no` refers to which replication run this row comes from. Each entity is tagged with their unique ID. To get the waiting time of each entity you will need to do `curr_WaitTime - prev_WaitTime`. This is because I can't write the difference directly to file.

In order to find the average waiting time of each individual, you will need to find the waiting time for each queue and divide it by all the queues it had. For example if tourist 67 spend 2 mins in bicycle queue A, 3 mins dock queue B, 2 mins in bicycle queue C, the average waiting time is `(2+3+2) / 3`. So to calculate the average waiting time of everybody, it's the total waiting time / the total number of queues that everybody had gone through.