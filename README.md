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

To accomplish this, we'll first create a procedure taking crypto portfolios as input, calculating correlation with FAANGMULA, and a procedure modeling future performance of that portfolio using Monte Carlo simulation. Then, we'll create a procedure that generates random portfolios from top 30 market capitalization cryptoassets and analyzes their correlation with the tech sector, using our already-created correlation algorithm. Then, we'll analyze the performance of the randomly generated portfolios against the S&P500 using Monte Carlo simulation.

This app allows its users to select a single or a group cryptocurrencies to view its over time and to access its correlation to Tech Stocks. This app also includes a Monte Carlo simulation to forecast future performance of their portfolio based on the allocations within their portfolio. The SPY500 is the baseline for the portfolio performance analysis as we believe the SPY500 returns should be the absolute lowest any custom portfolio should return. 

It is our goal that investors will be able to use this application, with its vizualization tools and other features to make decisions that are best aligned to their individual investment goals.

## Bonus

1. Create parameter for setting number of included top cryptoassets by market capitalization.
2. Create parameter for projected tech sector performance.

## Project Members
Ken Smith - @kennethologist