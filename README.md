# Opening and closing credit detection

## Working assumptions
* Across series, credits will likely be structurally similar enough per episode to correlate their sequences.
* Repeated sequeces of images across episodes are generally exclusive to credit sequences.
* Opening credits are longer that n seconds (at least 5, shorter than this arguably dosen't need skipping) 
* There might be clips before or after credits.
* Opening and closing credits are within the first and last n minitues (~=5) of a episode.

## Existing IBL Credit classification
On initial inspection, it seems that it uses the assumption that closing credit sequences have similarity accross programmes. E.g. Text, dark background. This uses some form of binary classifier to detect wether frames are a credit or not credit—have not looked into the details of model yet. 
* https://confluence.dev.bbc.co.uk/display/IBL/iBL+Credibl+Image+Classifier
* https://confluence.dev.bbc.co.uk/display/IBL/iBL+Credibl+Gif+Generator
* https://confluence.dev.bbc.co.uk/display/IBL/iBL+Credibl+Detector