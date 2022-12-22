# jakDojade-Ostrow-Wielkopolski

This is an application used to find a transport connection in my hometown of Ostrow Wielkopolski.

Little description: // HOW TO LAUNCH IT
At the beginning, You have to choose first Stop from where you want to start your travel (all stops and buses you can find in JSON files), and the last one, you are made to specify also the start hour.
Compile it, and...
After that the answear is ready!

Algorithm that I use:
I used my self-made algorithm, its similar to an DFS algorithm.
At the beginning when you compile the program properly, it create a few data like departure hours, and so on...
After that It create array of buses from first stop and last stop, if on the array is similar bus, you can drive directly without chaning the bus.
If there is more than one option it compare them, and give you only the best two (first is the bus that is first on the last stop and the second one option is the bus that is faster than the others, so the trip is the shortest).

If there is no option to drive directly, my algorithm is looking for every next stop from first one. When you are already on new stop, it will again create array of buses, and compare it. After that the code is similar as in first option.
