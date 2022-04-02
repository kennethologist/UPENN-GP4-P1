# Low Correlation Crypto
#### Creating a crypto portfolio weakly correlated with the tech sector

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About The Project</a>
      <ul>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#technology">Technologies</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

## About The Project
The explosion of the crypto sector in recent years has many people interested in crypto investment, despite high volatility. At the same time, the non-crypto tech sector, FAANGMULA, has appreciated greatly in recent years, with high correlation between downturns in both markets. The main goal of this project is to find crypto portfolios weakly correlated with the tech sector, relative to other more highly-correlated crypto portfolios, and analyze their expected future performance, in hopes of finding portfolios with high expected performance even given a major tech sector downturn, effectively hedging against such a downturn while still heavily investing in crypto.

## Questions
1. What is the correlation between a given crypto portfolio and FAANGMULA?
2. What is the expected future performance of such a portfolio using Monte Carlo simulation against the S&P500?
3. What are the lowest correlation crypto portfolios with top 30 cryptoassets as elements, from a randomly-generated set of portfolios?
4. How strongly are those portfolios correlated with other sectors, apart from the tech sector?
5. What is the expected performance of those portfolios against the S&P500 using Monte Carlo?

## Datasets
1. Alpaca
2. Kraken

## Tasks
1. Pull data from Alpaca and Kraken, the former for FAANGMULA and the latter for the crypto sector.
2. Visualize price hitory of a given portfolio.
3. Calculate correlation with FAANGMULA given crypto portfolio as input.
4. Model future performance of a given portfolio using Monte Carlo simulation.
5. Generate random portfolios from top 30 market capitalization cryptoassets and analyze their correlation with the tech sector, using our already-created correlation algorithm.
6. Analyze performance of randomly generated portfolios against the S&P500 using Monte Carlo simulation.

## Bonus
1. Create parameter for setting number of included top cryptoassets by market capitalization.
2. Create parameter for projected tech sector performance.

## Project Members
1. Ken Smith - @kennethologist
2. Alex - @allsmit
