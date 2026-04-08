# Investments: Course Notes

## Table of Contents

1. [Introduction and Bond Pricing](#chapter-1-introduction-and-bond-pricing)
2. [Saving and the Time Value of Money](#chapter-2-saving-and-the-time-value-of-money)
3. [Returns](#chapter-3-returns)
4. [Portfolio Returns and Risk](#chapter-4-portfolio-returns-and-risk)
5. [Stocks and Equity Markets](#chapter-5-stocks-and-equity-markets)
6. [Treasury Securities and the Term Structure](#chapter-6-treasury-securities-and-the-term-structure)
7. [Arbitrage and No-Arbitrage Pricing](#chapter-7-arbitrage-and-no-arbitrage-pricing)
8. [Markets and Trading](#chapter-8-markets-and-trading)
9. [Leverage and Margin](#chapter-9-leverage-and-margin)
10. [Short Selling](#chapter-10-short-selling)
11. [Diversification](#chapter-11-diversification)
12. [Portfolio Theory and Optimization](#chapter-12-portfolio-theory-and-optimization)
13. [Portfolio Constraints and Frictions](#chapter-13-portfolio-constraints-and-frictions)
14. [Backtesting and Input Sensitivity](#chapter-14-backtesting-and-input-sensitivity)
15. [The Market Model](#chapter-15-the-market-model)
16. [The CAPM](#chapter-16-the-capm)
17. [Cross-Sectional Predictability](#chapter-17-cross-sectional-predictability)
18. [Multifactor Models](#chapter-18-multifactor-models)
19. [Duration](#chapter-19-duration)
20. [Convexity](#chapter-20-convexity)
21. [Credit Risk](#chapter-21-credit-risk)
22. [Performance Evaluation](#chapter-22-performance-evaluation)
23. [Taxes and Tax-Advantaged Investing](#chapter-23-taxes-and-tax-advantaged-investing)

---

# Part I: Foundations

---

## Chapter 1: Introduction and Bond Pricing

### Why Study Investments?

Investing is one of the most consequential financial decisions individuals and institutions face.  Whether saving for retirement, managing an endowment, or running a hedge fund, a solid understanding of how securities are priced, how risk and return relate to one another, and how to construct portfolios is essential.  This course develops that understanding from first principles, combining financial theory with empirical analysis and computation.

We begin with bonds because they are the simplest securities to value: their future cash flows are known (or at least promised) in advance.  This makes bonds an ideal starting point for learning the discounted cash flow framework that underlies all of asset pricing.

### Bond Basics

A bond is a debt instrument in which the issuer promises to make a series of payments to the bondholder.  The key terms of a bond are:

- **Face value (par)**: The principal amount repaid at maturity, typically \$100 or \$1,000.
- **Coupon rate**: The annual interest rate paid on the face value.
- **Maturity**: The date on which the face value is repaid.
- **Coupon frequency**: How often coupon payments are made (typically semi-annually for U.S. bonds).

A bond with a 6% coupon rate, \$100 face value, and semi-annual payments pays \$3 every six months plus \$100 at maturity.

### Pricing a Bond

The price of a bond equals the present value of its future cash flows, discounted at an appropriate rate.  For a bond with annual coupon payments:

$$P = \sum_{t=1}^{T} \frac{C}{(1+y)^t} + \frac{\text{Face}}{(1+y)^T}$$

where $C$ is the coupon payment, $y$ is the yield to maturity (YTM), and $T$ is the number of periods to maturity.

For semi-annual payments, we halve the coupon and yield and double the number of periods:

$$P = \sum_{t=1}^{2T} \frac{C/2}{(1+y/2)^t} + \frac{\text{Face}}{(1+y/2)^{2T}}$$

The coupon payments form an annuity, so we can use the annuity formula:

$$P = \frac{C}{y}\left[1 - \frac{1}{(1+y)^T}\right] + \frac{\text{Face}}{(1+y)^T}$$

**Example.**  A bond has a 6% annual coupon, 8-year maturity, \$100 face, and a YTM of 5%.  Its price is:

$$P = \frac{6}{0.05}\left[1 - \frac{1}{1.05^8}\right] + \frac{100}{1.05^8} = 38.74 + 67.68 = \$106.46$$

### Zero-Coupon Bonds

A zero-coupon bond makes no coupon payments.  Its price is simply the discounted face value:

$$P = \frac{\text{Face}}{(1+y)^T}$$

Zero-coupon bonds are sold at a discount to face value, and the investor's return comes entirely from the price appreciation as the bond approaches maturity.

### The Price--Yield Relationship

Bond prices and yields move in opposite directions.  When yields rise, prices fall; when yields fall, prices rise.  This is a direct consequence of the discounting formula: a higher discount rate reduces the present value of future cash flows.

Three important relationships:

1. **Premium bonds**: When the coupon rate exceeds the yield, the bond trades above par ($P > \text{Face}$).
2. **Discount bonds**: When the yield exceeds the coupon rate, the bond trades below par ($P < \text{Face}$).
3. **Par bonds**: When the coupon rate equals the yield, the bond trades at par ($P = \text{Face}$).

As a bond approaches maturity, its price converges to par regardless of whether it is a premium or discount bond---a phenomenon known as *pull to par*.

### Yield to Maturity

The yield to maturity is the internal rate of return on a bond, assuming all cash flows are received as promised and reinvested at the same rate.  It is the single discount rate that equates the bond's price with the present value of its cash flows.  For a given price $P$, the YTM $y$ solves:

$$P = \sum_{t=1}^{T} \frac{C}{(1+y)^t} + \frac{\text{Face}}{(1+y)^T}$$

There is generally no closed-form solution for $y$; it must be found numerically.

---

## Chapter 2: Saving and the Time Value of Money

### The Time Value of Money

A dollar today is worth more than a dollar in the future because today's dollar can be invested to earn a return.  This principle---the time value of money---is foundational to all of finance.

The two basic operations are:

- **Future value**: Given a present amount $PV$, the future value after $T$ periods at rate $r$ is $FV = PV \times (1+r)^T$.
- **Present value**: Given a future amount $FV$, its present value is $PV = FV / (1+r)^T$.

### Annuities

Many financial problems involve a stream of equal payments.  The future value of an ordinary annuity (payments at end of each period) is:

$$FV = PMT \times \frac{(1+r)^T - 1}{r}$$

The present value of an ordinary annuity is:

$$PV = PMT \times \frac{1 - (1+r)^{-T}}{r}$$

### Retirement Planning

Retirement planning is a canonical application of time-value-of-money concepts.  The problem typically has two phases:

1. **Accumulation phase**: Save a fixed amount each year for $T_1$ years, earning return $r$.
2. **Distribution phase**: Withdraw a fixed amount each year for $T_2$ years.

**Example.**  Suppose you want to withdraw \$100,000 per year for 20 years in retirement, and you can earn 5% annually.  How much must you save per year for the prior 30 years?

*Step 1*: Find the lump sum needed at retirement to fund the withdrawals.

$$PV = 100{,}000 \times \frac{1 - 1.05^{-20}}{0.05} = \$1{,}246{,}221$$

*Step 2*: Find the annual savings required to accumulate that lump sum.

$$PMT = \frac{FV \times r}{(1+r)^T - 1} = \frac{1{,}246{,}221 \times 0.05}{1.05^{30} - 1} = \$18{,}747$$

### Real vs. Nominal Returns

Inflation erodes purchasing power.  When planning over long horizons, it is important to distinguish between:

- **Nominal returns**: The stated return, not adjusted for inflation.
- **Real returns**: The return after accounting for inflation.

The Fisher equation relates the two:

$$(1 + r_{\text{nominal}}) = (1 + r_{\text{real}})(1 + \pi)$$

where $\pi$ is the inflation rate.  Rearranging:

$$r_{\text{real}} = \frac{1 + r_{\text{nominal}}}{1 + \pi} - 1$$

For small values, $r_{\text{real}} \approx r_{\text{nominal}} - \pi$, but for precise calculations (especially over long horizons), use the exact formula.

**Example.**  If the nominal return is 5% and inflation is 2%, the real return is $(1.05/1.02) - 1 = 2.94\%$, not 3%.

When doing retirement planning under inflation, you can either (a) work entirely in nominal terms (inflate the withdrawals, use the nominal rate) or (b) work entirely in real terms (keep withdrawals constant, use the real rate).  Both approaches give the same answer in present-value terms.

---

## Chapter 3: Returns

### Defining Returns

The **gross return** over a single period is the ratio of ending value to beginning value:

$$R_t = \frac{V_t}{V_{t-1}}$$

The **net return** (or simply "return") is:

$$r_t = R_t - 1 = \frac{V_t - V_{t-1}}{V_{t-1}}$$

### Stock Returns

For a stock with price $P_t$ and dividend $D_t$:

$$r_t = \frac{P_t + D_t - P_{t-1}}{P_{t-1}}$$

In practice, data providers supply **adjusted prices** that account for dividends and stock splits, so that simple price returns on adjusted data give total returns.  The ex-dividend date is the date on which the dividend is credited to the holder of record.

### Bond Returns

For a bond, returns must account for coupon payments and accrued interest:

$$r_t = \frac{P_t + AI_t + C_t - (P_{t-1} + AI_{t-1})}{P_{t-1} + AI_{t-1}}$$

where $AI_t$ is accrued interest and $C_t$ is the coupon payment (if any) during the period.  The *clean price* excludes accrued interest; the *dirty price* (or invoice price) includes it.

### Compounding Returns

The cumulative return over multiple periods is:

$$1 + r_{1 \to T} = \prod_{t=1}^{T}(1 + r_t)$$

This reflects the compounding of returns: gains in one period earn returns in subsequent periods.

### Summary Statistics for Returns

**Arithmetic mean return**:

$$\bar{r} = \frac{1}{T}\sum_{t=1}^{T} r_t$$

The arithmetic mean is the best estimator of the expected return for a single future period.

**Geometric mean return**:

$$\bar{r}_g = \left[\prod_{t=1}^{T}(1+r_t)\right]^{1/T} - 1$$

The geometric mean gives the constant rate that, compounded over $T$ periods, would produce the same cumulative return.  It is always less than or equal to the arithmetic mean (with equality only when all returns are identical).  It measures the time-weighted return actually earned by an investor.

**Standard deviation** (volatility):

$$\sigma = \sqrt{\frac{1}{T-1}\sum_{t=1}^{T}(r_t - \bar{r})^2}$$

Standard deviation is the most common measure of risk.  It captures the typical dispersion of returns around the mean.

### Annualizing Returns and Risk

If returns are measured at a frequency of $m$ periods per year:

- **Annualized mean**: $\bar{r}_{\text{annual}} = m \times \bar{r}_{\text{period}}$
- **Annualized standard deviation**: $\sigma_{\text{annual}} = \sqrt{m} \times \sigma_{\text{period}}$

For monthly data ($m=12$): multiply the mean by 12 and the standard deviation by $\sqrt{12} \approx 3.46$.

### Data Sources

Common data sources for investments analysis include:

- **Yahoo Finance** (via the `yfinance` Python package): Daily equity prices, adjusted for splits and dividends.
- **FRED** (Federal Reserve Economic Data): Interest rates, inflation, macroeconomic series.
- **Ken French Data Library**: Factor returns, benchmark portfolios, and industry returns for academic research.

---

## Chapter 4: Portfolio Returns and Risk

### Portfolio Returns

A portfolio is a collection of assets held in specified proportions.  If asset $i$ has weight $w_i$ (fraction of total portfolio value) and return $r_i$, the portfolio return is:

$$r_p = \sum_{i=1}^{N} w_i \, r_i$$

The weights must sum to one: $\sum_{i=1}^{N} w_i = 1$.

The portfolio expected return is the weighted average of individual expected returns:

$$E[r_p] = \sum_{i=1}^{N} w_i \, E[r_i]$$

### Portfolio Variance

The portfolio variance is *not* the weighted average of individual variances.  It depends on the covariances between all pairs of assets:

$$\text{Var}[r_p] = \sum_{i=1}^{N}\sum_{j=1}^{N} w_i \, w_j \, \text{Cov}[r_i, r_j]$$

For two assets:

$$\text{Var}[r_p] = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \, \text{Cov}[r_1, r_2]$$

### Covariance and Correlation

The covariance between two returns measures how they move together:

$$\text{Cov}[r_i, r_j] = E\left[(r_i - E[r_i])(r_j - E[r_j])\right]$$

Correlation standardizes covariance to lie between $-1$ and $+1$:

$$\rho_{ij} = \frac{\text{Cov}[r_i, r_j]}{\sigma_i \, \sigma_j}$$

We can express covariance in terms of correlation: $\text{Cov}[r_i, r_j] = \rho_{ij} \, \sigma_i \, \sigma_j$.

### Matrix Notation

For $N$ assets, let $\mathbf{w}$ be the $N \times 1$ vector of weights, $\boldsymbol{\mu}$ the vector of expected returns, and $\mathbf{V}$ the $N \times N$ covariance matrix.  Then:

$$E[r_p] = \mathbf{w}' \boldsymbol{\mu}$$

$$\text{Var}[r_p] = \mathbf{w}' \mathbf{V} \mathbf{w}$$

This compact notation is essential for working with portfolios of many assets.

### The Power of Diversification

When correlation is less than one ($\rho < 1$), the portfolio standard deviation is less than the weighted average of individual standard deviations.  This is the fundamental benefit of diversification: combining imperfectly correlated assets reduces risk without a proportional reduction in expected return.

**Example.**  Suppose Asset 1 has $\sigma_1 = 20\%$, Asset 2 has $\sigma_2 = 12\%$, and $\rho_{12} = 0.3$.  An equal-weighted portfolio has:

$$\sigma_p = \sqrt{0.5^2(0.04) + 0.5^2(0.0144) + 2(0.5)(0.5)(0.3)(0.20)(0.12)} = 12.8\%$$

The weighted average of the individual standard deviations is $0.5(20\%) + 0.5(12\%) = 16\%$.  Diversification reduced portfolio risk from 16% to 12.8%.

---

# Part II: Financial Markets

---

## Chapter 5: Stocks and Equity Markets

### Empirical Facts About Stock Returns

The U.S. stock market has a long history of data, allowing us to document several important stylized facts:

1. **Stocks have earned high average returns.**  Over the long run, U.S. stocks have returned roughly 8--10% per year (nominal), substantially exceeding the returns on bonds and Treasury bills.  The excess of stock returns over the risk-free rate is called the **equity risk premium**.

2. **Stock returns are volatile.**  Annual stock returns have a standard deviation of roughly 15--20%.  The distribution of returns has fatter tails than the normal distribution (more extreme outcomes than expected) and is negatively skewed (large losses are more likely than large gains of the same magnitude).

3. **Past returns do not predict future returns.**  Autocorrelations of stock returns are approximately zero, meaning that knowing this month's return tells you little about next month's return.  This is consistent with the idea that prices quickly incorporate new information.

4. **Volatility is persistent.**  Unlike returns themselves, volatility is predictable.  Periods of high volatility tend to be followed by more high volatility.  Autocorrelations of squared or absolute returns are significantly positive.

### Stock Market Indices

Stock market indices track the performance of a basket of stocks:

- **S&P 500**: A value-weighted index of 500 large-cap U.S. stocks.  It is the most widely used benchmark for U.S. equity performance.
- **Dow Jones Industrial Average**: A price-weighted index of 30 large stocks.
- **Russell 2000**: An index of small-cap stocks.

In a **value-weighted** index, each stock's weight is proportional to its market capitalization.  In a **price-weighted** index, each stock's weight is proportional to its share price.

### Long-Run Stock Performance

Over long horizons, stocks have been a powerful wealth-building tool, but outcomes vary dramatically:

- **Worst 20-year period** (1929--1948): \$1 grew to \$1.73 (2.8% annual return).
- **Best 20-year period** (1980--1999): \$1 grew to \$24.65 (17.4% annual return).

These wide ranges underscore that even over 20-year horizons, stock market outcomes are uncertain.

---

## Chapter 6: Treasury Securities and the Term Structure

### Types of Treasury Securities

The U.S. Treasury issues several types of securities:

| Security | Maturity | Coupon | Notes |
|----------|----------|--------|-------|
| Treasury bills | $\leq$ 1 year | None (discount) | Sold at discount to face |
| Treasury notes | 2--10 years | Semi-annual | Most actively traded |
| Treasury bonds | $>$ 10 years | Semi-annual | Longest maturity |
| TIPS | Various | Semi-annual | Principal indexed to CPI |
| STRIPS | Various | None | Stripped from notes/bonds |

**TIPS** (Treasury Inflation-Protected Securities) adjust their principal based on the Consumer Price Index.  If inflation is 2% per half-year and the original principal is \$100, the adjusted principal becomes \$102, and the coupon is paid on the adjusted amount.  This provides a guaranteed real return.

### The Term Structure of Interest Rates

The **term structure** (or **yield curve**) describes the relationship between yields and maturities for bonds of the same credit quality.  Key features of the yield curve include:

- **Level**: The overall height of the curve (driven by monetary policy and inflation expectations).
- **Slope**: The difference between long-term and short-term yields.  A positively sloped curve is "normal."
- **Curvature**: How the curve bends, particularly at intermediate maturities.

An **inverted yield curve** (short rates above long rates) has historically been a reliable predictor of recessions.

### Spot Rates

The **spot rate** $z_t$ is the yield on a zero-coupon bond maturing in $t$ periods.  Spot rates are the building blocks of the term structure: any bond can be priced by discounting each cash flow at the appropriate spot rate.

The price of a coupon bond using spot rates is:

$$P = \sum_{t=1}^{T} \frac{C}{(1+z_t)^t} + \frac{\text{Face}}{(1+z_T)^T}$$

Note that this uses a different discount rate for each cash flow, unlike the YTM approach which uses a single rate.

### Bootstrapping Spot Rates

Spot rates are not directly observed for all maturities (most traded bonds pay coupons).  We extract them through **bootstrapping**:

1. The shortest-maturity zero-coupon bond directly gives $z_1$:  $z_1 = (\text{Face}/P_1)^{1/1} - 1$.
2. Use $z_1$ to strip the first cash flow from a 2-period coupon bond, then solve for $z_2$.
3. Continue iteratively for longer maturities.

**Example.**  Suppose we observe:

- A 1-year zero at price \$97.50: $z_1 = (100/97.50) - 1 = 2.56\%$
- A 2-year zero at price \$95.00: $z_2 = (100/95.00)^{1/2} - 1 = 2.60\%$
- A 3-year 5% coupon bond at price \$103.00:

$$103 = \frac{5}{1.0256} + \frac{5}{1.0260^2} + \frac{105}{(1+z_3)^3}$$

Solve for $z_3$ by isolating the final term.

This process builds up the entire spot curve from observable prices.

---

## Chapter 7: Arbitrage and No-Arbitrage Pricing

### What Is Arbitrage?

An **arbitrage** is a trading strategy that generates a positive profit in some states of the world and a loss in none.  In other words, it is a risk-free profit opportunity.

The **law of one price** states that two securities (or portfolios) with identical cash flows must have the same price.  If they don't, an arbitrageur can buy the cheaper one and sell the more expensive one, locking in a risk-free profit.

### Replicating Portfolios

A **replicating portfolio** is a combination of known securities that produces the same cash flows as a target security.  If we can replicate a bond's cash flows using other traded bonds, then the target bond's price must equal the cost of the replicating portfolio.

**Example.**  Suppose we want to price a bond that pays \$15 at time 1 and \$115 at time 2.  We have two zero-coupon bonds available:

- Bond A: Pays \$100 at time 1, price = \$97.50
- Bond B: Pays \$100 at time 2, price = \$95.00

To replicate: buy 0.15 units of Bond A and 1.15 units of Bond B.

- Time 1 cash flow: $0.15 \times 100 = \$15$
- Time 2 cash flow: $1.15 \times 100 = \$115$

Replicating portfolio cost: $0.15 \times 97.50 + 1.15 \times 95.00 = \$14.625 + \$109.25 = \$123.875$

If the target bond trades at any price other than \$123.875, an arbitrage opportunity exists.

### Matrix Approach to Replication

For more complex cases with multiple bonds and cash flow dates, we can set up a system of linear equations.  Let $\mathbf{CF}$ be the matrix of cash flows from available bonds (columns = bonds, rows = dates), $\mathbf{x}$ the vector of positions, and $\mathbf{cf}$ the vector of target cash flows.  The replicating portfolio solves:

$$\mathbf{CF} \, \mathbf{x} = \mathbf{cf}$$

The solution is $\mathbf{x} = \mathbf{CF}^{-1} \, \mathbf{cf}$, and the no-arbitrage price of the target is $\mathbf{p}' \mathbf{x}$, where $\mathbf{p}$ is the vector of available bond prices.

---

## Chapter 8: Markets and Trading

### Information Asymmetry

Many features of financial markets arise from the fact that some participants know more than others.

**Adverse selection** occurs when one party to a transaction has an information advantage.  In securities markets, informed traders profit at the expense of less-informed traders and market makers.  This creates costs for providing liquidity.

The **winner's curse** arises in auctions: winning may signal that you overvalued the asset relative to better-informed bidders.

### Primary and Secondary Markets

- **Primary markets**: Where new securities are issued (IPOs, seasoned equity offerings, Treasury auctions).
- **Secondary markets**: Where existing securities are traded among investors.

**IPO underpricing** is a well-documented phenomenon: new shares are typically offered at a price below their first-day trading price, resulting in a "first-day pop."  One explanation is that underpricing compensates uninformed investors for the winner's curse---without it, uninformed investors would receive disproportionate allocations of overpriced offerings and would eventually exit the market.

### Market Structures

Financial markets operate through several mechanisms:

1. **Limit order book (continuous market)**: Buyers and sellers post limit orders specifying price and quantity.  Trades execute when a buy order's price meets or exceeds a sell order's price.  Most equity and options markets use this structure.

2. **Over-the-counter (OTC) / dealer market**: Buyers and sellers negotiate directly with dealers who stand ready to buy and sell.  Corporate bonds and most fixed-income instruments trade OTC.

3. **Call market / auction**: Orders are batched and executed at a single clearing price at specific times.  Treasury auctions and equity market opens/closes use this structure.

### Brokers vs. Dealers

- **Brokers** are agents who match buyers and sellers, earning a commission.  They do not take positions.
- **Dealers** are principals who buy and sell from their own inventory, earning the bid-ask spread.  They take position risk.

### The Bid-Ask Spread

The **bid price** is the highest price a dealer will pay (the price at which you sell).  The **ask price** is the lowest price a dealer will accept (the price at which you buy).  The difference is the **bid-ask spread**.

The spread exists because of:

- **Adverse selection costs**: Dealers lose money to informed traders and must recoup losses from uninformed traders.
- **Inventory costs**: Holding positions creates risk for the dealer.
- **Order processing costs**: Administrative costs of executing trades.

The spread is a measure of **liquidity**---the ease of converting an asset to cash.  Narrower spreads indicate greater liquidity.

---

## Chapter 9: Leverage and Margin

### What Is Leverage?

**Leverage** means using borrowed money to invest.  It amplifies both gains and losses.

Suppose an investor has \$100,000 in equity and borrows \$50,000 at interest rate $r_b$ to invest \$150,000 in stocks.  The leverage ratio is $150{,}000 / 100{,}000 = 1.5\times$.

The levered return on equity is:

$$r_{\text{levered}} = r_{\text{asset}} + \frac{D}{E}(r_{\text{asset}} - r_b)$$

where $D/E$ is the debt-to-equity ratio.

**Example.**  With $D/E = 0.5$, $r_b = 5\%$:

- If the stock returns 10%: $r_{\text{levered}} = 10\% + 0.5(10\% - 5\%) = 12.5\%$
- If the stock returns $-10\%$: $r_{\text{levered}} = -10\% + 0.5(-10\% - 5\%) = -17.5\%$

Leverage magnifies the gain from 10% to 12.5%, but also magnifies the loss from $-10\%$ to $-17.5\%$.

### Margin Accounts

To use leverage, investors open **margin accounts** with their brokers.  Key concepts:

- **Percent margin** = Equity / Total Asset Value
- **Initial margin** (Regulation T): At least 50% of the purchase must be equity.
- **Maintenance margin**: A minimum margin level (typically 30--35%) set by the broker.

If the margin falls below the maintenance level, the broker issues a **margin call**, requiring the investor to deposit additional funds or liquidate positions.

**Margin call trigger** (long position): A margin call occurs when the return falls below:

$$r < \frac{L}{S_0(1 - MM)} - 1$$

where $L$ is the loan amount, $S_0$ is the initial stock value, and $MM$ is the maintenance margin.

### Repurchase Agreements (Repos)

A **repurchase agreement** is a simultaneous sale of a security and agreement to repurchase it at a higher price later.  Economically, it is a collateralized loan.

- The **repo rate** is the interest rate implied by the price difference.
- The **haircut** is the excess of collateral value over the loan amount, protecting the lender against declines in collateral value.
- Most repos are **overnight**; general collateral repo rates are close to the federal funds rate.

The repo rate can be decomposed as:

$$\text{Repo rate} = \text{Short-term rate} - \text{Collateral fee}$$

For "general collateral" (e.g., Treasuries), the collateral fee is near zero.  For special or hard-to-borrow securities, the collateral fee can be significant.

---

## Chapter 10: Short Selling

### What Is Short Selling?

**Short selling** means selling a security you do not own by borrowing it first, with the obligation to return it later.

The mechanics:

1. Borrow shares from a lender (typically through a broker).
2. Sell the borrowed shares in the market.
3. At some future date, buy shares in the market ("cover" the short).
4. Return the shares to the lender.

The short seller profits if the price falls and loses if the price rises.  A **long** position means you own the asset; a **short** position means you owe the asset.

### Margin for Short Sales

Short selling requires posting margin (collateral).  At initiation, the short seller's account must contain:

- The short sale proceeds (100% of the short's value).
- Additional margin (typically 50% of the short value under Reg T).

The percent margin for a short position is:

$$\text{Percent margin} = \frac{\text{Equity}}{\text{Short position value}} = \frac{\text{Assets} - \text{Short position value}}{\text{Short position value}}$$

A margin call occurs when this falls below the maintenance margin (typically 30%).

**Example.**  Short 100 shares at \$60 with 50% initial margin:

- Short proceeds: \$6,000; margin deposit: \$3,000; total assets: \$9,000
- Initial margin: $3{,}000 / 6{,}000 = 50\%$

If the stock rises to \$70:
- Short liability: \$7,000; equity: $9{,}000 - 7{,}000 = \$2{,}000$
- Margin: $2{,}000 / 7{,}000 = 28.6\%$ --- below 30%, triggering a margin call.

### The Equity Lending Market

When shares are borrowed for short selling, the borrower must post cash collateral.  The lender earns interest on this collateral but pays back a **rebate rate** to the borrower:

$$\text{Rebate rate} = \text{Short-term rate} - \text{Lending fee}$$

For most liquid stocks, the lending fee is small and the rebate is close to the short-term rate.  Stocks with high borrowing fees are called **special**; their rebate rates can be very low or even negative.

The lender also retains the right to **recall** shares, which can force the short seller to close the position at an inopportune time.

### Limits to Arbitrage

The Palm/3Com case (2000) illustrates that arbitrage can be limited in practice.  3Com owned 95% of Palm but traded at a price implying a negative value for 3Com's non-Palm assets---an obvious mispricing.  Yet the mispricing persisted for over six weeks because it was nearly impossible to borrow Palm shares for short selling.

This case demonstrates that **limits to arbitrage**---borrowing costs, margin requirements, recall risk, and price risk during the holding period---can prevent even sophisticated investors from correcting mispricings.

---

# Part III: Portfolio Theory

---

## Chapter 11: Diversification

### The Core Insight

Diversification is the idea that combining assets reduces portfolio risk.  As long as assets are not perfectly correlated ($\rho < 1$), a portfolio's standard deviation will be less than the weighted average of its components' standard deviations.

### Two-Asset Diversification

For two assets with weights $w_1$ and $w_2 = 1 - w_1$:

$$\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{12} \sigma_1 \sigma_2$$

The key insight: the cross-term $2 w_1 w_2 \rho_{12} \sigma_1 \sigma_2$ is smaller when $\rho_{12}$ is lower.

- If $\rho_{12} = 1$: $\sigma_p = w_1 \sigma_1 + w_2 \sigma_2$ (no diversification benefit).
- If $\rho_{12} = 0$: $\sigma_p = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2}$ (substantial reduction).
- If $\rho_{12} = -1$: $\sigma_p = |w_1 \sigma_1 - w_2 \sigma_2|$ (risk can be eliminated entirely).

### The Investment Opportunity Set

By varying the weights across all assets, we trace out the **investment opportunity set**---the set of all achievable mean--standard deviation combinations.  This set is bounded on the left by the **minimum variance frontier**, the curve of portfolios that achieve the lowest possible variance for each level of expected return.

### The Efficient Frontier

The upper portion of the minimum variance frontier (above the global minimum variance portfolio) is the **efficient frontier**.  Portfolios on the efficient frontier offer the highest expected return for any given level of risk.  A rational mean-variance investor would never hold a portfolio below the efficient frontier, because a portfolio with the same risk but higher expected return is available.

### Global Minimum Variance (GMV) Portfolio

The **GMV portfolio** minimizes variance across all possible weight combinations, subject to weights summing to one.  It is the leftmost point on the efficient frontier.

Importantly, the GMV portfolio does not depend on expected returns---only on the covariance matrix.  This makes it more robust to estimation error than portfolios that optimize on expected returns.

In matrix notation, the GMV portfolio solves:

$$\min_{\mathbf{w}} \quad \mathbf{w}' \mathbf{V} \mathbf{w} \quad \text{s.t.} \quad \mathbf{w}' \mathbf{1} = 1$$

The solution is:

$$\mathbf{w}_{\text{GMV}} = \frac{\mathbf{V}^{-1} \mathbf{1}}{\mathbf{1}' \mathbf{V}^{-1} \mathbf{1}}$$

---

## Chapter 12: Portfolio Theory and Optimization

### Adding a Risk-Free Asset

When investors can lend and borrow at a risk-free rate $r_f$, the efficient frontier becomes a straight line called the **Capital Allocation Line (CAL)**:

$$E[r_p] = r_f + \frac{E[r_T] - r_f}{\sigma_T} \cdot \sigma_p$$

where $T$ denotes the **tangency portfolio**---the risky portfolio that maximizes the Sharpe ratio.

The slope of the CAL is the Sharpe ratio of the tangency portfolio:

$$S_T = \frac{E[r_T] - r_f}{\sigma_T}$$

### The Tangency Portfolio

The tangency portfolio is found by maximizing the Sharpe ratio over all possible portfolios of risky assets:

$$\max_{\mathbf{w}} \quad \frac{\mathbf{w}' \boldsymbol{\mu} - r_f}{\sqrt{\mathbf{w}' \mathbf{V} \mathbf{w}}} \quad \text{s.t.} \quad \mathbf{w}' \mathbf{1} = 1$$

The analytical solution is:

$$\mathbf{w}_T = \frac{\mathbf{V}^{-1}(\boldsymbol{\mu} - r_f \mathbf{1})}{\mathbf{1}' \mathbf{V}^{-1}(\boldsymbol{\mu} - r_f \mathbf{1})}$$

### Two-Fund Separation

A powerful result of portfolio theory is **two-fund separation**: all efficient portfolios are combinations of the risk-free asset and the tangency portfolio.  Investors differ only in how much they allocate to the tangency portfolio (based on their risk aversion), not in the composition of their risky holdings.

- **Conservative investors**: Hold mostly the risk-free asset with a small allocation to the tangency portfolio.
- **Moderate investors**: Hold 100% in the tangency portfolio.
- **Aggressive investors**: Borrow at $r_f$ and invest more than 100% in the tangency portfolio.

### Risk Aversion and Optimal Allocation

An investor with mean-variance preferences and risk aversion parameter $A$ chooses the fraction $y$ invested in the tangency portfolio to maximize:

$$\max_y \quad E[r_p] - \frac{A}{2} \text{Var}[r_p] = r_f + y(E[r_T] - r_f) - \frac{A}{2} y^2 \sigma_T^2$$

The optimal allocation is:

$$y^* = \frac{E[r_T] - r_f}{A \, \sigma_T^2}$$

Higher risk aversion ($A$) leads to a smaller allocation to risky assets.

### Computing Optimal Portfolios in Practice

For small problems, the analytical formulas above are tractable.  For larger problems with many assets, we use numerical optimization (quadratic programming).  In Python, the `cvxopt` library provides efficient solvers for these problems.

---

## Chapter 13: Portfolio Constraints and Frictions

### Borrowing Frictions

In practice, investors cannot borrow at the risk-free rate.  When the borrowing rate $r_b$ exceeds the lending rate $r_f$, the CAL develops a **kink**:

- For $\sigma_p \leq \sigma_{T_L}$: The investor lends at $r_f$ and invests in tangency portfolio $T_L$ (computed using $r_f$).
- For $\sigma_p$ between $\sigma_{T_L}$ and $\sigma_{T_B}$: The investor holds a portfolio on the risky efficient frontier (no borrowing or lending).
- For $\sigma_p \geq \sigma_{T_B}$: The investor borrows at $r_b$ and invests in tangency portfolio $T_B$ (computed using $r_b$).

This breaks two-fund separation: different investors may hold different risky portfolios depending on where they fall on the frontier.

### Short-Sale Constraints

Many investors (mutual funds, pension funds, individual investors) cannot short-sell.  Adding the constraint $w_i \geq 0$ for all $i$:

- Moves the efficient frontier inward (higher risk for the same return).
- May exclude some assets entirely from optimal portfolios.
- Requires numerical optimization (no closed-form solution).

The constrained optimization problem is:

$$\min_{\mathbf{w}} \quad \mathbf{w}' \mathbf{V} \mathbf{w} \quad \text{s.t.} \quad \mathbf{w}' \boldsymbol{\mu} = \mu_{\text{target}}, \quad \mathbf{w}' \mathbf{1} = 1, \quad w_i \geq 0 \;\; \forall i$$

### Position Limits

In practice, investors often impose maximum position sizes (e.g., no more than 10% in any single asset).  These constraints further restrict the efficient frontier but produce more diversified and implementable portfolios.

### Rebalancing

Over time, asset returns cause portfolio weights to drift from their target values.  **Rebalancing** means periodically trading to restore target weights.

Without rebalancing, a portfolio with a 50/50 stock/bond target will drift toward higher stock weights as stocks (with higher expected returns) appreciate, increasing portfolio risk over time.

Rebalancing strategies:

- **Calendar rebalancing**: Rebalance at fixed intervals (monthly, quarterly).
- **Threshold rebalancing**: Rebalance when any weight drifts beyond a specified band.

Rebalancing involves a trade-off between maintaining target risk and incurring transaction costs.

---

## Chapter 14: Backtesting and Input Sensitivity

### The Error-Maximization Problem

Mean-variance optimization is highly sensitive to its inputs (expected returns, variances, and covariances).  Small errors in estimated expected returns can lead to dramatically different optimal portfolios.  The optimizer tends to:

- Overweight assets whose expected returns are overestimated.
- Underweight assets whose expected returns are underestimated.
- Exploit spurious correlations in the covariance matrix.

This has been called the **error-maximization problem**: the optimizer effectively magnifies estimation errors instead of diversifying them away.

### Estimation Strategies

Different strategies use different subsets of estimated inputs:

| Strategy | Estimates Used | Key Feature |
|----------|---------------|-------------|
| **Est-All** | Means, SDs, correlations | Full optimization; most sensitive to error |
| **Est-SD-Corr** | SDs, correlations | GMV portfolio; ignores expected returns |
| **Est-SD** | SDs only | Assumes equal correlations |
| **Est-None** | Nothing estimated | Equal-weighted portfolio (1/N) |

### Empirical Evidence from Backtesting

Backtests using historical data reveal a surprising pattern:

- **Simpler strategies often outperform complex ones** out of sample, especially when the estimation window is short or the number of assets is large.
- The **equal-weighted (1/N) portfolio** is a surprisingly strong benchmark.  It requires no estimation and is fully diversified.
- The **GMV portfolio** (Est-SD-Corr) tends to perform well because it avoids the noisy estimation of expected returns.
- **Est-All** frequently underperforms because estimation error in expected returns overwhelms the theoretical benefits of optimization.

### Dealing with Estimation Error

Several approaches help mitigate estimation error:

1. **Position limits**: Cap the maximum weight on any asset to prevent extreme positions.
2. **Shrinkage**: Pull extreme estimates toward moderate values.  For example, shrink estimated betas toward 1: $\beta_{\text{shrunk}} = 0.67 \hat{\beta} + 0.33$.
3. **Use models**: Factor models, Black-Litterman, or other structured approaches reduce the number of parameters to estimate.
4. **Simplify**: When in doubt, use simpler strategies (GMV, equal-weighted, risk parity) that require fewer inputs.

### Sensitivity to Estimation Window and Number of Assets

- **Shorter estimation windows** increase estimation error, favoring simpler strategies.
- **More assets** increase the number of parameters to estimate (especially covariances), also favoring simpler approaches.

The curse of dimensionality is real in portfolio optimization: with $N$ assets, the covariance matrix has $N(N+1)/2$ unique elements, but the number of data points is limited by the estimation window.

---

# Part IV: Equity Asset Pricing

---

## Chapter 15: The Market Model

### The Market Model Regression

The **market model** relates an asset's excess return to the market's excess return:

$$r_{i,t} - r_{f,t} = \alpha_i + \beta_i (r_{m,t} - r_{f,t}) + \varepsilon_{i,t}$$

where:

- $\alpha_i$ (**alpha**): The average return of asset $i$ that is not explained by the market.  A positive alpha indicates historical outperformance.
- $\beta_i$ (**beta**): The sensitivity of asset $i$'s excess return to the market's excess return.  If $\beta = 1.5$, a 1% market move implies a 1.5% expected move in the asset.
- $\varepsilon_{i,t}$ (**residual**): The idiosyncratic, asset-specific component of returns, uncorrelated with the market by construction.

### Interpreting Beta

Beta measures **systematic risk**---the portion of an asset's risk that is related to the market and cannot be diversified away.

- $\beta > 1$: The asset is more volatile than the market (aggressive).
- $\beta = 1$: The asset moves with the market.
- $\beta < 1$: The asset is less volatile than the market (defensive).
- $\beta < 0$: The asset moves opposite to the market (rare).

Beta is estimated via OLS regression using historical returns data.

### Variance Decomposition

The market model decomposes total variance into systematic and idiosyncratic components:

$$\text{Var}(r_i) = \beta_i^2 \, \text{Var}(r_m) + \text{Var}(\varepsilon_i)$$

The $R^2$ of the regression measures the fraction of variance explained by the market:

$$R^2 = \frac{\beta_i^2 \, \text{Var}(r_m)}{\text{Var}(r_i)}$$

### Market-Model Covariances

If we assume that the idiosyncratic terms are uncorrelated across assets ($\text{Cov}(\varepsilon_i, \varepsilon_j) = 0$), then:

$$\text{Cov}(r_i, r_j) = \beta_i \beta_j \, \text{Var}(r_m)$$

This dramatically reduces the number of parameters needed to estimate the covariance matrix.  Instead of $N(N-1)/2$ pairwise covariances, we need only $N$ betas plus 1 market variance: $N + 1$ parameters total (plus $N$ idiosyncratic variances for the diagonal).

**Example.**  With 100 assets: direct estimation requires $100 \times 99 / 2 = 4{,}950$ covariances plus 100 variances.  The market model requires only 201 parameters.

### Beta Persistence and Shrinkage

Estimated betas are moderately persistent over time but exhibit **mean reversion toward 1**.  To improve out-of-sample predictions, we apply shrinkage:

$$\beta_{\text{adjusted}} = 0.67 \, \hat{\beta} + 0.33$$

This pulls extreme betas toward 1, reflecting the empirical tendency for betas to revert over time.  Alphas are much less persistent than betas and are generally not reliable for forecasting.

---

## Chapter 16: The CAPM

### The Capital Asset Pricing Model

The **CAPM** (Sharpe, 1964; Lintner, 1965) is the foundational equilibrium model of asset pricing.  It predicts that the expected excess return on any asset is proportional to its beta:

$$E[r_i - r_f] = \beta_i \cdot E[r_m - r_f]$$

or equivalently:

$$E[r_i] = r_f + \beta_i \left(E[r_m] - r_f\right)$$

### Assumptions

The CAPM requires strong assumptions:

1. All investors have identical beliefs about expected returns, variances, and covariances.
2. All investors have mean-variance preferences over a single-period horizon.
3. Markets are frictionless (no transaction costs, taxes, or short-selling constraints).
4. All investors are price-takers (perfect competition).

### The Security Market Line

The CAPM prediction can be graphed as the **Security Market Line (SML)**: a straight line in $(\beta, E[r])$ space passing through:

- The risk-free asset at $(\beta = 0, E[r] = r_f)$.
- The market portfolio at $(\beta = 1, E[r] = E[r_m])$.

According to the CAPM, all assets should lie on the SML.  Assets above the line offer too much return for their beta (underpriced); assets below offer too little (overpriced).

### The Market Portfolio

A key prediction of the CAPM is that the **market portfolio**---the value-weighted portfolio of all investable assets---is the tangency portfolio.  In equilibrium, all investors hold the market portfolio as their risky portfolio and adjust their risk exposure only by varying their allocation to the risk-free asset.

### Empirical Performance

The CAPM performs poorly empirically:

- The empirical SML is **too flat**: low-beta stocks earn higher returns than the CAPM predicts, and high-beta stocks earn lower returns.  This is known as the **low-beta anomaly**.
- Many characteristics (size, value, momentum) predict returns beyond what beta can explain.
- The market risk premium is estimated with substantial error: with annual standard deviation of 20%, even 50 years of data yields a standard error of $20\% / \sqrt{50} \approx 2.8\%$.

Despite its empirical shortcomings, the CAPM remains important as a conceptual framework and as a building block for more sophisticated models.

---

## Chapter 17: Cross-Sectional Predictability

### Anomalies

An **anomaly** is a characteristic of a stock that predicts its future returns, beyond what is explained by a benchmark model (like the CAPM).  Major documented anomalies include:

| Anomaly | Reference | Finding |
|---------|-----------|---------|
| **Size** | Banz (1981) | Small firms earn higher average returns than large firms |
| **Value** | Fama & French (1992) | High book-to-market (B/M) firms outperform low B/M firms |
| **Momentum** | Jegadeesh & Titman (1993) | Past winners continue to outperform past losers over 3--12 months |
| **Liquidity** | Amihud & Mendelson (1986) | Illiquid stocks earn a premium |
| **Idiosyncratic volatility** | Ang et al. (2006) | High idiosyncratic volatility stocks earn lower returns |
| **Low beta** | Black, Jensen & Scholes (1972) | Low-beta stocks outperform high-beta stocks on a risk-adjusted basis |

### Methodology 1: Portfolio Sorts

The standard approach to documenting anomalies:

1. At the beginning of each period, sort stocks into portfolios (e.g., quintiles) based on the characteristic.
2. Calculate the average return of each portfolio over the subsequent period.
3. Examine whether there is a monotonic relationship between the characteristic and average returns.
4. The **long-short spread** (high minus low) measures the premium.

**Example.**  Sorting stocks by book-to-market into quintiles, the high B/M (value) portfolio has outperformed the low B/M (growth) portfolio by about 0.89% per month, or roughly 10.7% annualized.

### Methodology 2: Cross-Sectional Regression

An alternative is to run cross-sectional regressions:

$$r_{i,t} = a_t + b_t \cdot \text{Characteristic}_{i,t-1} + e_{i,t}$$

Each month, we regress returns on the lagged characteristic.  The coefficient $b_t$ measures the return premium associated with the characteristic in month $t$.

### Fama-MacBeth Regressions

The **Fama-MacBeth** procedure (1973) formalizes the cross-sectional regression approach:

1. Each month $t$, run a cross-sectional regression of returns on lagged characteristics.
2. Collect the time series of estimated coefficients $\{b_t\}$.
3. Report the time-series average $\bar{b} = \frac{1}{T}\sum_t b_t$ and its $t$-statistic.

The $t$-statistic is $t = \bar{b} / \text{SE}(\bar{b})$, where $\text{SE}(\bar{b}) = \sigma_b / \sqrt{T}$.  A $t$-statistic above 2 (in absolute value) is considered statistically significant.

This approach allows multiple characteristics to be tested simultaneously, controlling for the others, and naturally handles time-varying effects.

---

## Chapter 18: Multifactor Models

### Beyond the CAPM: Factor Models

The CAPM's single factor (the market) is insufficient to explain the cross section of returns.  **Multifactor models** add additional systematic risk factors.

### The Fama-French Three-Factor Model

Fama and French (1993) augmented the market model with two additional factors:

$$r_{i,t} - r_{f,t} = \alpha_i + \beta_i (r_{m,t} - r_{f,t}) + s_i \, SMB_t + h_i \, HML_t + \varepsilon_{i,t}$$

- **SMB** (Small Minus Big): The return on a portfolio long small-cap stocks and short large-cap stocks.  Captures the size premium.
- **HML** (High Minus Low): The return on a portfolio long high book-to-market (value) stocks and short low book-to-market (growth) stocks.  Captures the value premium.

The factors are constructed from double sorts: stocks are sorted into six portfolios based on size (2 groups) and book-to-market (3 groups), then:

$$SMB = \frac{1}{3}(S/L + S/M + S/H) - \frac{1}{3}(B/L + B/M + B/H)$$

$$HML = \frac{1}{2}(S/H + B/H) - \frac{1}{2}(S/L + B/L)$$

### The Fama-French-Carhart Four-Factor Model

Carhart (1997) added a momentum factor:

$$r_{i,t} - r_{f,t} = \alpha_i + \beta_i (r_{m,t} - r_{f,t}) + s_i \, SMB_t + h_i \, HML_t + m_i \, WML_t + \varepsilon_{i,t}$$

- **WML** (Winners Minus Losers): The return on a portfolio long past 12-month winners and short past 12-month losers.

### The Fama-French Five-Factor Model

Fama and French (2015) added profitability and investment factors:

$$r_{i,t} - r_{f,t} = \alpha_i + \beta_i (r_{m,t} - r_{f,t}) + s_i \, SMB_t + h_i \, HML_t + r_i \, RMW_t + c_i \, CMA_t + \varepsilon_{i,t}$$

- **RMW** (Robust Minus Weak): Long firms with high operating profitability, short firms with low profitability.
- **CMA** (Conservative Minus Aggressive): Long firms with low asset growth (conservative investment), short firms with high asset growth.

### Using Factor Models for Expected Returns

Factor models can estimate expected returns in two steps:

1. **Estimate factor loadings**: Regress each asset's excess returns on the factors to obtain $\hat{\beta}_i, \hat{s}_i, \hat{h}_i$, etc.
2. **Estimate factor risk premiums**: Use the historical average factor returns as estimates of $\lambda_m, \lambda_{SMB}, \lambda_{HML}$, etc.

Then the expected return for asset $i$ is:

$$E[r_i] = r_f + \hat{\beta}_i \hat{\lambda}_m + \hat{s}_i \hat{\lambda}_{SMB} + \hat{h}_i \hat{\lambda}_{HML} + \cdots$$

### Characteristic-Based Expected Return Models

An alternative to factor models uses **Fama-MacBeth regressions** directly:

1. Run cross-sectional regressions of returns on firm characteristics (size, B/M, momentum, etc.) each month.
2. Average the coefficients over time.
3. Forecast expected returns as: $E[r_i] = r_f + \bar{a} + \sum_j \bar{b}_j \times \text{Characteristic}_{i,j}$

This approach is more flexible than factor models because it uses observable characteristics rather than estimated factor loadings.

---

# Part V: Fixed Income

---

## Chapter 19: Duration

### Interest Rate Risk

When interest rates change, bond prices change.  **Duration** quantifies this sensitivity.

### Macaulay Duration

**Macaulay duration** is the weighted average time to receive a bond's cash flows, where the weights are the present values of each cash flow divided by the bond price:

$$D = \sum_{t=1}^{T} t \cdot \frac{PV(CF_t)}{P} = \frac{1}{P} \sum_{t=1}^{T} t \cdot \frac{CF_t}{(1+y)^t}$$

Duration is measured in the same units as the payment periods (years, half-years, etc.).

**Properties of duration:**

- A zero-coupon bond's duration equals its maturity.
- For coupon bonds, duration is less than maturity (because some cash flows arrive before maturity).
- Higher coupon $\Rightarrow$ shorter duration (more weight on earlier cash flows).
- Higher yield $\Rightarrow$ shorter duration (later cash flows are discounted more heavily).
- Longer maturity $\Rightarrow$ longer duration (in most cases).

### Modified Duration

**Modified duration** adjusts Macaulay duration for the compounding frequency:

$$D_{\text{mod}} = \frac{D}{1 + y/m}$$

where $m$ is the number of compounding periods per year.  Modified duration directly measures the percentage price sensitivity:

$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y$$

**Example.**  A bond has modified duration of 6.4 years.  If yields rise by 0.50%, the approximate price change is:

$$\frac{\Delta P}{P} \approx -6.4 \times 0.005 = -3.2\%$$

### Duration as an Investment Horizon

Duration also identifies the investment horizon at which interest rate risk and reinvestment risk exactly offset.  An investor with a horizon equal to the bond's duration is approximately immunized against small parallel shifts in the yield curve.

### Portfolio Duration

The duration of a portfolio of bonds is the weighted average of the individual bond durations:

$$D_p = \sum_{i=1}^{N} w_i \, D_i$$

This allows managers to target a specific duration for the overall portfolio, useful for asset-liability matching (e.g., pension funds matching the duration of their assets to the duration of their liabilities).

---

## Chapter 20: Convexity

### The Limits of Duration

Duration provides a linear (first-order) approximation to the price-yield relationship.  But the actual relationship is curved (convex for standard bonds).  For large yield changes, the linear approximation becomes inaccurate.

### Convexity Defined

**Convexity** measures the curvature of the price-yield relationship:

$$\text{Convexity} = \frac{1}{P} \frac{d^2P}{dy^2}$$

For a coupon bond:

$$\text{Convexity} = \frac{1}{P(1+y)^2} \sum_{t=1}^{T} t(t+1) \frac{CF_t}{(1+y)^t}$$

### The Second-Order Approximation

Adding convexity gives a more accurate price-change estimate:

$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y + \frac{1}{2} \cdot \text{Convexity} \cdot (\Delta y)^2$$

The convexity term is always positive (for positive convexity bonds), which means:

- When yields fall, the actual price increase is **larger** than the duration approximation.
- When yields rise, the actual price decrease is **smaller** than the duration approximation.

**Example.**  For a bond with $D_{\text{mod}} = 7.0$ and Convexity = 60:

- If yields fall 2%: $\Delta P / P \approx -7.0(-0.02) + 0.5(60)(0.02)^2 = 14.0\% + 1.2\% = 15.2\%$
- If yields rise 2%: $\Delta P / P \approx -7.0(0.02) + 0.5(60)(0.02)^2 = -14.0\% + 1.2\% = -12.8\%$

The asymmetry (gaining more than you lose) is the benefit of positive convexity.

### Positive vs. Negative Convexity

**Positive convexity** (standard coupon bonds): The price-yield curve bows toward the origin.  Investors benefit from convexity---they are willing to accept a lower yield on bonds with higher convexity.

**Negative convexity** (callable bonds, mortgages): The price-yield curve bows away from the origin at low yields.  This occurs because when rates fall, the issuer can call the bond (or homeowners refinance), capping the price at the call price.

- **Callable bonds**: The issuer has the right to redeem the bond before maturity at a predetermined call price.  The bond's price cannot rise much above the call price, creating a ceiling on the investor's gains.
- Investors demand a higher yield on callable bonds as compensation for negative convexity.

### Empirical Estimation

Duration and convexity can be estimated numerically from three bond prices:

$$\widehat{D}_{\text{mod}} = \frac{P_{-} - P_{+}}{2 \, P_0 \, \Delta y}$$

$$\widehat{\text{Convexity}} = \frac{P_{-} + P_{+} - 2P_0}{P_0 \, (\Delta y)^2}$$

where $P_0$ is the current price, $P_{-}$ is the price at yield $y - \Delta y$, and $P_{+}$ is the price at yield $y + \Delta y$.

---

## Chapter 21: Credit Risk

### What Is Credit Risk?

**Credit risk** is the risk that a bond issuer fails to make promised payments (default).  Unlike Treasury securities, which are considered default-free, corporate bonds carry credit risk.

### Credit Ratings

Rating agencies (Moody's, S&P, Fitch) assess the creditworthiness of issuers:

| Grade | Moody's | S&P/Fitch | Description |
|-------|---------|-----------|-------------|
| Investment Grade | Aaa | AAA | Highest quality |
| | Aa | AA | High quality |
| | A | A | Upper medium |
| | Baa | BBB | Medium grade |
| High Yield (Junk) | Ba | BB | Speculative |
| | B | B | Highly speculative |
| | Caa-C | CCC-D | Substantial risk to default |

The boundary between investment grade (BBB/Baa and above) and high yield (BB/Ba and below) is particularly important: many institutional investors are restricted to investment-grade bonds only.

### YTM vs. Expected Return

For a risky bond, the YTM overstates the expected return because it assumes all promised payments are made:

$$E[r] = (1 - p_d) \times YTM + p_d \times r_{\text{default}}$$

where $p_d$ is the probability of default and $r_{\text{default}}$ is the return in the event of default (which depends on the recovery rate).  Since $r_{\text{default}} < YTM$, the expected return is less than the YTM.

### Credit Spreads

The **credit spread** is the difference between a corporate bond's yield and the yield on a comparable-maturity Treasury:

$$\text{Spread} = YTM_{\text{corporate}} - YTM_{\text{Treasury}}$$

Credit spreads compensate investors for:

- **Expected default losses**: $p_d \times (1 - \text{recovery rate})$
- **Credit risk premium**: Compensation for bearing the systematic component of default risk.
- **Liquidity premium**: Corporate bonds are less liquid than Treasuries.

Empirical evidence shows that credit spreads increase substantially with lower ratings:

| Rating | Typical Spread (bps) |
|--------|---------------------|
| AA | ~23 |
| A | ~35 |
| BBB | ~167 |
| B | ~882 |

### Credit Default Swaps (CDS)

A **credit default swap** is a financial contract that provides insurance against default:

- The **protection buyer** pays a periodic premium (the CDS spread) to the protection seller.
- If the reference entity defaults, the **protection seller** pays the buyer the loss (par minus recovery value).

By the law of one price, the CDS spread should approximately equal the bond's credit spread.  Deviations create arbitrage opportunities (the "basis trade").

CDS can be used to:

- **Hedge** credit exposure on bonds already held.
- **Speculate** on changes in credit quality without holding the underlying bond.
- Isolate **pure credit risk** from interest rate risk.

---

# Part VI: Performance Evaluation and Taxes

---

## Chapter 22: Performance Evaluation

### The Efficient Markets Hypothesis

The **Efficient Markets Hypothesis (EMH)** states that security prices reflect available information:

- **Weak form**: Prices reflect all past trading data (prices, volume).  Technical analysis cannot consistently generate excess returns.
- **Semi-strong form**: Prices reflect all publicly available information.  Fundamental analysis cannot consistently generate excess returns.
- **Strong form**: Prices reflect all information, including private information.  Even insider trading cannot consistently generate excess returns.

### The Grossman-Stiglitz Paradox

If markets are perfectly efficient, no one has an incentive to gather information (since it's already in prices).  But if no one gathers information, prices cannot be informative.  The resolution: markets must be *nearly* efficient---just inefficient enough to compensate informed investors for their information-gathering costs.

### Equilibrium in the Asset Management Industry

In equilibrium with skilled managers:

1. Investors allocate capital to skilled managers.
2. As assets under management grow, returns diminish (decreasing returns to scale).
3. In equilibrium, the expected net-of-fee return to investors converges toward the benchmark.
4. Skilled managers earn economic rents (fees), not alpha for their investors.
5. Unskilled managers underperform and eventually exit the industry.

### Measuring Performance: Alpha

**Alpha** ($\alpha$) measures the average return that is not explained by exposure to systematic risk factors.

**Market-model alpha**:

$$\alpha_p = \overline{r_p - r_f} - \hat{\beta}_p \, \overline{r_m - r_f}$$

or equivalently, the intercept from the regression:

$$r_{p,t} - r_{f,t} = \alpha_p + \beta_p(r_{m,t} - r_{f,t}) + \varepsilon_{p,t}$$

**Multifactor alpha** (e.g., Fama-French-Carhart):

$$r_{p,t} - r_{f,t} = \alpha_p + \beta_p(r_{m,t} - r_{f,t}) + s_p \, SMB_t + h_p \, HML_t + m_p \, WML_t + \varepsilon_{p,t}$$

A positive alpha indicates outperformance after adjusting for factor exposures; a negative alpha indicates underperformance.

### Survivorship Bias

**Survivorship bias** arises when poorly performing funds close and disappear from the database.  Analyzing only surviving funds overstates average performance.

Empirical evidence shows:

- About 42% of all funds (including those that later closed) have positive market-model alpha.
- About 52% of surviving funds have positive alpha---a 10 percentage point upward bias.
- Funds with negative alpha are significantly more likely to close.

Any study of fund performance must account for survivorship bias, or it will produce misleading conclusions.

### Attribution Analysis

**Attribution analysis** decomposes a fund's return into components:

$$r_{p,t} - r_{f,t} = \underbrace{\alpha_p + \varepsilon_{p,t}}_{\text{Active return}} + \underbrace{\beta_p(r_{m,t} - r_{f,t}) + s_p \, SMB_t + h_p \, HML_t + \cdots}_{\text{Factor returns}}$$

This tells us whether a fund's performance comes from:

- **Security selection** (alpha): Picking individual securities that outperform.
- **Factor tilts**: Systematic exposure to size, value, momentum, etc.

A fund with high returns but high factor loadings may simply be harvesting known risk premiums rather than demonstrating skill.

### Market Timing

**Market timing** is the ability to increase market exposure before market advances and reduce it before declines.  The Henriksson-Merton model tests for timing ability:

$$r_{p,t} - r_{f,t} = \alpha_p + b_p(r_{m,t} - r_{f,t}) + c_p \max(r_{m,t} - r_{f,t}, 0) + \varepsilon_{p,t}$$

A positive $c_p$ indicates successful market timing: the fund increases its market exposure in up markets.

---

## Chapter 23: Taxes and Tax-Advantaged Investing

### Tax Basics

The U.S. tax system is progressive: higher income is taxed at higher marginal rates.

Key concepts:

- **Adjusted Gross Income (AGI)**: Gross income minus certain deductions (e.g., tax-deductible retirement contributions).
- **Taxable income**: AGI minus the standard or itemized deduction.
- **Marginal tax rate**: The rate on the next dollar of income.
- **Capital gains rates**: Long-term capital gains (assets held $>$ 1 year) are taxed at lower rates than ordinary income.  Short-term gains are taxed as ordinary income.

### Tax Treatment of Different Accounts

Different account types receive different tax treatment.  For \$1 of pre-tax income invested for $T$ periods at return $r$:

**1. Taxable account (interest/dividends taxed annually)**:

$$FV = \prod_{t=1}^{T} [1 + r_t(1 - \tau_{oi})]$$

Each period's return is reduced by the tax rate, creating a drag on compounding.

**2. Roth IRA / 529 Plan (tax-free growth)**:

After-tax contribution of $(1 - \tau_{oi,0})$, but withdrawals are tax-free:

$$FV = (1 - \tau_{oi,0}) \prod_{t=1}^{T} (1 + r_t)$$

**3. Traditional IRA / 401(k) (tax-deferred)**:

Pre-tax contribution (tax deduction now), but withdrawals taxed at ordinary rates:

$$FV = (1 - \tau_{oi,T}) \prod_{t=1}^{T} (1 + r_t)$$

**4. Non-dividend stock in taxable account (tax on capital gains at sale)**:

$$FV = (1 - \tau_{cg,T}) \prod_{t=1}^{T}(1 + r_t) + \tau_{cg,T}$$

Taxes are deferred until the stock is sold, and the capital gains rate applies.

### Traditional vs. Roth

The choice between a traditional IRA (tax-deductible contributions, taxable withdrawals) and a Roth IRA (after-tax contributions, tax-free withdrawals) depends on the relationship between current and future tax rates:

- If $\tau_{\text{now}} = \tau_{\text{future}}$: Traditional and Roth are equivalent.
- If $\tau_{\text{now}} < \tau_{\text{future}}$: Roth is better (lock in the low tax rate now).
- If $\tau_{\text{now}} > \tau_{\text{future}}$: Traditional is better (defer to the lower future rate).

Young workers who expect their income (and tax rate) to rise over time often benefit from Roth contributions.

### Asset Location

**Asset allocation** determines *what* to hold (stocks, bonds, etc.).  **Asset location** determines *where* to hold each asset (taxable vs. tax-advantaged accounts).

The general principle: place heavily taxed assets in tax-advantaged accounts and lightly taxed assets in taxable accounts.

- **Bonds** (taxed at ordinary income rates on interest) $\Rightarrow$ Hold in tax-deferred accounts.
- **Stocks** (taxed at lower capital gains rates, with deferral until sale) $\Rightarrow$ Hold in taxable accounts.
- **Highly appreciated or high-growth assets** $\Rightarrow$ Hold in Roth accounts (all future growth is tax-free).

### Tax-Advantaged Securities

Several securities receive favorable tax treatment:

- **Municipal bonds**: Interest is exempt from federal income tax (and often state tax).  The tax-equivalent yield is $y_{\text{muni}} / (1 - \tau)$.  An investor in the 37% bracket finds a 3% muni equivalent to a $3\% / 0.63 = 4.76\%$ taxable yield.
- **ETFs vs. mutual funds**: ETFs are generally more tax-efficient because of the "in-kind" creation/redemption mechanism, which avoids triggering capital gains distributions.
- **Mortgage interest deduction**: Mortgage interest payments are tax-deductible (subject to limits), reducing the effective cost of borrowing.

### The Mortgage Interest Deduction

For homeowners who itemize deductions, mortgage interest reduces taxable income.  The after-tax cost of a mortgage with rate $r_m$ is:

$$r_{\text{after-tax}} = r_m \times (1 - \tau)$$

For a borrower in the 24% bracket with a 6% mortgage: $r_{\text{after-tax}} = 6\% \times 0.76 = 4.56\%$.

This makes home ownership tax-advantaged relative to renting (all else equal), though the benefit depends on whether the borrower itemizes deductions and the size of the mortgage relative to the standard deduction.
