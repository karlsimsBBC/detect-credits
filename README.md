# POC for opening and closing sequence detection across series episodes
Proof of concept for automatic detection of program title and credit sequences per series. Process is achieved using sequence matching and frame similarity metrics across collections of episodes without the need for supplementary data or model.

See [notebook exlploration](https://github.com/karlsimsBBC/detect-credits/blob/master/_notebooks/initial.ipynb) which successfully detects introductions across 6 Eastenders episodes whose introductions have been randomly offset.

Works under the assumptions that:
* Title and credit sequences normally occur within ~5 min of the program start and end time respectively
* Title and credit sequences are at least ~5 seconds long.
* Apart from the opening and closing sequences, there are very few repeated sequences that are both more than 5 seconds long and within the first 5 minutes of the show.
* Opening and closing sequences are similar enough to correlate across episodes.

### Todo
Refactor implementation.
Test on more examples and find cases where it fails.

