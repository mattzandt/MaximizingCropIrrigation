# MaximizingCropIrrigation
You run a farm which isn't doing so well. Your crops that you planted aren't coming up, and your bills are bigger than your expected proceeds. So, you have to conserve water and focus instead on the plants that are growing. You have a center pivot watering system which has a rotating sprinkler around a central pivot, creating a circular watered area. For this challenge, you just have to decide where to locate it based on this year's crops.

Some notes:

Because this is a simple grid, we're only dealing with integers in this challenge.
For partially covered squares, round down: the sprinkler covers the crop if the distance from the sprinkler is less than or equal to the sprinklers radius.
If you place the sprinkler on a square with a crop, you destroy the crop so handle accordingly (e.g. deduct 1 from the calculation).
If in the event you find two or more placements that yield identical scores, pick any one of them (or even emit them all if you so choose), this is entirely possible.

Input Description:

You'll be given three integers (h w r) which correspond to the number of rows (h) and columns (w) for the ASCII map (respectively) and then the radius (r) of the watering sprinkler. The ASCII map will have a "." for no crop planted and an "x" for a growing crop.

Output Description:

You should emit the coordinates (0-indexed) of the row and column showing where to place the center of the sprinkler. Your coordinates should be integers.