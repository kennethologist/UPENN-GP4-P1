def random_portfolios_generator(tickers, n):
    random_portfolios = pd.DataFrame(tickers, columns = ['ticker'])
    for n in range(0, n):
        random_portfolios[f'Random Portfolio {n+1}'] = [np.random.rand() for i in range (0, 9)]
        random_portfolios[f'Random Portfolio {n+1}'] = random_portfolios[f'Random Portfolio {n+1}'] / sum(random_portfolios[f'Random Portfolio {n+1}'])
    return(random_portfolios)