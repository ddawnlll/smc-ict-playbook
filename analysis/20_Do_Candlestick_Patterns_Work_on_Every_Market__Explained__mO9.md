# Do Candlestick Patterns Work on Every Market? Explained

**Source File:** `imperial-research/Do Candlestick Patterns Work on Every Market？ Explained [mO9s4qf84To].mp4`  
**Analysis Index:** 20 of 54  
**Topic:** Cross-Asset Candlestick Viability: Structural Discrepancies Across Stocks, Forex, Gold, and Crypto

---

## 1. Strategy & Concept Overview
- **Core Concept:** Market Microstructure & Structural Comparability of Candlestick Patterns Across Asset Classes.
- **Market Context & High-Level Premise:**
  - Japanese candlestick patterns are universally presented as identical 2D formations (defined by Open, High, Low, Close / OHLC). A Hammer or Morning Star looks identical whether plotted on Stocks, Forex, Gold Futures, or Crypto.
  - However, market architecture differs radically across asset classes in three decisive structural dimensions:
    1. **Operating Trading Hours:** Closed sessions vs. 24/5 vs. 24/7 continuous auction.
    2. **Overnight Gapping Mechanics:** Session gap frequency and pattern formation integrity.
    3. **Volume Quality:** Centralized contract volume vs. decentralized tick volume.
  - Consequently, identical candlestick geometries deliver vastly different statistical probabilities depending on the underlying asset's market mechanics.

```
+------------------+-----------------------+-------------------------+-------------------------+
| Market Category  | Trading Hours         | Gapping Characteristics | Volume Mechanism        |
+------------------+-----------------------+-------------------------+-------------------------+
| Equities/Stocks  | ~6.5 hrs/day, Mon-Fri | Frequent Overnight Gaps | Centralized Real Volume |
| Forex / Gold     | 24 hrs/day, Mon-Fri   | Minimal (Weekend Only)  | Decentralized Tick Flow |
| Cryptocurrency   | 24/7 Continuous       | Virtual Zero Gaps       | Fragmented Spot/Perps   |
+------------------+-----------------------+-------------------------+-------------------------+
```

---

## 2. Step-by-Step Setup Mechanics

1. **Step 1: Universal Geometry vs. Underlying Reality:**
   - Confirm the mathematical basis: all candles reflect four pricing data points (Open, High, Low, Close).
   - Recognize that while geometric shapes (e.g., Hammer, Doji, Engulfing) render identically, their market context is dictated by liquidity access.
2. **Step 2: Evaluate Trading Hours:**
   - **Equities (e.g., Indian / US Stocks):** Trade ~6–6.5 hours per business day. 17.5 hours of daily macro information is compressed into the next session open.
   - **Forex & Gold Futures:** Trade nearly 24 hours continuously from Sunday evening to Friday afternoon.
   - **Crypto:** Operates 24/7/365 with uninterrupted order flow matching.
3. **Step 3: Account for Gapping Mechanics:**
   - Classical Japanese patterns (e.g., Morning Star, Evening Star, Abandoned Baby) theoretically require an opening gap between the mother body and the star candle.
   - In 24/7 continuous crypto or 24/5 forex, candles almost always open precisely at the prior close. Patterns must be adapted for continuous markets rather than textbook gap definitions.
4. **Step 4: Distinguish Real vs. Tick Volume:**
   - **Equities & Futures:** Central exchange clearinghouses report exact executed share/contract volume. Volume-supported candlestick patterns have verifiable institutional weight.
   - **Spot Forex:** Decentralized OTC market with no single exchange. Charts display **Tick Volume** (frequency of price ticks), which measures quote volatility rather than transactional capital size.
5. **Step 5: Review Empirical Backtesting Data:**
   - Quantitative research displays divergent outcomes:
     - S&P 500 academic studies found measurable predictive edge for specific candlestick reversal patterns.
     - Comparable studies on Dow Jones components showed zero statistical edge over random distribution.

---

## 3. Trade Execution Plan

- **Asset-Specific Calibration:**
  - **For Stocks:** Trade classical gap-and-go or gap-fill reversal patterns; incorporate centralized exchange volume spikes at open/close.
  - **For Forex / Gold:** Discard gap-dependent candlestick requirements; focus strictly on session opens (London/NY overlaps), round numbers, and wick liquidity sweeps.
  - **For Crypto:** Trade continuous price displacement and Fair Value Gaps (FVGs) rather than traditional multi-candle gap patterns.
- **Entry Trigger:**
  - Never execute solely on the appearance of an isolated candlestick pattern. Require confluence with higher-timeframe market structure (BOS/CHoCH) and key liquidity zones.
- **Stop Loss Placement:**
  - Above/below the extreme rejection wick of the pattern regardless of the asset.
- **Invalidation Condition:**
  - A close beyond the pattern boundary invalidates the setup.
- **Profit Target:**
  - Asset-specific average true range (ATR) or opposing liquidity pool.

---

## 4. Key Nuances, Traps & Rules

- **The "Copy-Paste" Trap:**
  - The primary beginner trap is assuming a pattern backtested on Apple stock will yield identical win rates on EUR/USD or Bitcoin.
- **Decentralized Volume Warning:**
  - In Spot Forex, high tick volume does not necessarily equal smart money accumulation—it may simply reflect high algorithmic quoting speed during news events.
- **Backtesting Mandate:**
  - "The shape is the same everywhere, but the results are not." Every candlestick pattern must be backtested independently on the exact instrument, session, and timeframe traded over a sample of at least 100+ executions.
