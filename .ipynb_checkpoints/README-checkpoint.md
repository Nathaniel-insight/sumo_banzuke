# sumo_banzuke
ML pipline to predict the rankings of Honbasho

# purpose
Set of modules and notebooks for scraping hon-basho tournament results and making banzuke (rankings) results predictions.

Every 2 months a Sumo hon-basho is held in Japan.
4 weeks..? after the commpletion of the tournament new rankings of the wrestlers are published bassed on the results of the most recently completed tournament.

There are a few known rankings rules.
1. If a wrestler finishes the tournament with a kachi-koshi (8+ wins out of 15) they either keep or increase in rank in porpotion to the number of wins above 8 they get (i.e. 10 wins increases more ranks than 8 wins).
2. If a wrestler finishes the tournament with a make-koshi (1- wins out of 15) they either keep or decrease in rank in proportion to how many they lose below 8 (i.e 4 wins decreases more ranks than 7 wins)
3. Yokozuna (grand champions) never lose their tier or "top" position in the banzuke - but they may shift within the Yokozuna tier
4. Ozeki (champions) only lose their title if they have losing records in 2 consecutive tournaments.
    4.b if an ozeki has a record of 10+ wins on the tournament directly after losing ozeki title they regain their ozeki title
    4.c to get to ozeki a wreslter usually has to win 33 times across 3 tournaments at san-yaku or above (although this isn't always the case)
    
Despite the above rules being largley "predictable" there is a large human component in deciding final rankings. For example if a wrestler has performed well against the san-yaku ranks they may receive a higher promotion than wrestler who did not despite having the same number of wins.

## Current version
MVP pipelines (read scrappy notebooks with few notes)
See evaluation notebook for final results
See exploration notebook for linear regression scroes

## Initial takeaways
There is a high degree of linearity in previous rankings, wins and next rankings (R^2 = 0.94) in terms of absolute rankings.

Despite this, the task of predicting exact rank has several considerations.
1. Tier (Yokozuna, Ozeki, Sekiwake, Komusubi, Maaegashia) is a categorical target with disparte rules for entering or leaving
2. East / West is a binary variable with east being considered slightly "better" than west
3. Rank is a numerical ordinal variable within tiers that are ordered highest to lowest in ascending order (1 being the highest rank, etc...)

While working rather well for the Yokozuna and Ozeki rankings, the decision rules for predicting exact banzuke performs poorly
( in top 10 ranks only 2 out of 20 wrestlers were accutately predicted)

## Future ideas
use ordinal regressors instead of linear regressors

create 3 predictors (Tier, east/west, rank)

