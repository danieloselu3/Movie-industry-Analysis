# MOVIE INDUSTRY ANALYSIS FOR MICROSOFT
**Author:** [Daniel Omondi Oselu](https://github.com/danieloselu3)

## OVERVIEW
For this project, we will use exploratory data analysis to generate insights about some of the best performing movies in the Box office between 2010 and 2020

## BUSINESS PROBLEM
Microsoft sees all the big companies creating original video content and they want to get in on the fun. 
They have decided to create a new movie studio, but they don’t know anything about creating movies. 
You are charged with exploring what types of films are currently doing the best at the box office.
You must then translate those findings into actionable insights that the head of Microsoft's new movie studio can use to help decide what type of films to create.

![Clapperboard in production](images/avel-chuklanov-Hn3S90f6aak-unsplash-edited.jpg)

<span>Photo by <a href="https://unsplash.com/@chuklanov?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Avel Chuklanov</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></span>

## DATA
The data for this analysis will be pulled from two sites, [The Numbers](https://www.the-numbers.com/movie/budgets/all), and [IMDB](https://www.imdb.com/interfaces/).

The data from IMDB will contain detail about the movies including m`ovie ratings`, `number of movie votes`, `length of movie`, `year of release`. While the data from The Numbers will contain data about the `Revenues generated` by the movie, `name of the movie`, `domestic gross`, `worldwide gross`, and when the count was done.

## METHODS
The project uses analysis to understand the data and extract useful information from the data.

## RESULTS
Movie from the Adventure genre dominated the most profitable Movies, with over 80% of the movies being `adventure` movies, followed by `action`, then `Sci-Fi`.

![most popular movie genre](images/most%20popular%20movie%20genre.png)

As a combination of genres, `"Action, Adventure, Sci-Fi"` dominated the most profitable movies, with more than 25% of the movies coming from this genre combination, followed by `"Adventure,Animation,Comedy"`, then `"Action,Adventure,Fantasy"`

![most popular movie genre combinations](images/Most%20popular%20Movies%20Genre%20combinations.png)

## CONCLUSIONS
This analysis leads to a couple of recommendations for gettting into the movie industry.

- **The genre to invest most on to get the highest Return on Investment** To get the most out of the movie industry, produce movies in the genres `Adventure`, `Action`, `Sci-Fi`, `Comedy` and `animation`. Also produce movies that combine genres, like `"Action,Adventure,Sci-Fi"` ,as this gets a broader reach to the fans.

- **The Average budget to produce a movie that is among the top 100 grossing movies** Our mean production budget was `158,772,000`. Meaning on average, set aside this amount per movie production budget for the top grossers.

- **The right time to Release the movies to the cinemas/public** the second quater of the year, `April-June` is the best time of the year to release the movies, followed by `September-December`.

![most popular release quater](images/Most%20popular%20Quater%20of%20year.png)

## NEXT STEPS
With the above analysis, the next steps to mmake our analysis whole can include:
- **Who are the best producers, durectors, and writters** Identifying these individuals can help with knowing the best team that can help with producing a top grosser.

- **Who are the Most successful Studios** these can help with bench-marking, to identify what the top grossing studios are doing right, that can be incorporated in the new studio.

## REPOSITORY STRUCTURE

```
├── code
│   ├── __init__.py
|
├── data
├── images
├── __init__.py
├── README.md
├── most_grossing_analysis_presentation.pdf
└── most_grossing_movies_analysis.ipynb
└── most_grossing_analysis_eda.ipynb
```
