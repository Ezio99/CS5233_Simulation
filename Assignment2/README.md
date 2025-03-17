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
- `Speed`: Currently set to 1 km/h. You will need to replace this with the speed distribution.


## Visiting time

Time spent in visiting are in the delay module:

- `Visit A`
- `Visit B`
- `Visit C`
- `Visit D`

All of them are set to 20 mins. You will need to replace this with the time spent distribution in each attraction

## Arrival time

Arrival time are determined by the Create module:

- `Tourist Enters A`
- `Tourist Enters B`
- `Tourist Enters C`
- `Tourist Enters D`

All of them are set to 20 mins. You will need to replace this with the arrival time distribution for each attraction

## Time taken to cycle

This is determined by the Route module (the one with green arrow)

- `Cycle to A`: Set `1/Speed`
- `Cycle to B`: Set `2 / Speed`
- `Cycle to C`: Set `2.5 / Speed`
- `Cycle to D`: Set `3 / Speed`

Where `Speed` refers to the speed attribute assigned in `Assign Number of Visits and Speed at {attractiion}`. Also note, this returns in hours to keep it consistent with the distance and speed reported.