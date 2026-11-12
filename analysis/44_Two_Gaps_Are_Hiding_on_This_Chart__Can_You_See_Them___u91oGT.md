# Two Gaps Are Hiding on This Chart: Can You See Them?

## 1. Strategy & Concept Overview
- **Core Concept:** Body Gaps vs. Wick Gaps, The **Suspension Block** Model, and Non-Standard Price Imbalances.
- **Market Context & High-Level Premise:**
  - Standard Smart Money Concepts define a Fair Value Gap (FVG) strictly by the three-candle wick relationship (where Wick 1 and Wick 3 do not overlap). When long wicks overlap across a displacement sequence, traditional traders conclude that no imbalance exists.
  - Institutional auction theory recognizes **Body Gaps (Opening/Closing Price Jumps)**. Even if wicks overlap, when candle bodies gap open beyond previous candle body closes, true delivery inefficiencies occur at interbank/liquidity provider settlement levels.
  - When a candle experiences an opening body gap below it and another opening body gap above it, that central candle becomes suspended between dual imbalances. This unique structural phenomenon is termed a **Suspension Block**.
  - Because price skipped continuous auction delivery between the body boundaries, algorithmic market makers frequently retrace to deliver orders back into the Suspension Block before continuing trend expansion.

---

## 2. Step-by-Step Setup Mechanics

### Step 1: Identifying Body Gaps (Bypassing Wick Overlap)
1. Observe a strong displacement sequence following a downtrend or consolidation.
2. Notice that the upper and lower candle wicks overlap, masking conventional 3-candle Fair Value Gaps.
3. Inspect the candle body boundaries:
   - **First Body Gap:** Candle 1 closes at price $P_{\text{close1}}$. Candle 2 gaps open higher at price $P_{\text{open2}}$ ($P_{\text{open2}} > P_{\text{close1}}$). Price completely skipped the space between the bodies.
   - **Second Body Gap:** Candle 2 rallies and closes at $P_{\text{close2}}$. Candle 3 immediately opens higher at $P_{\text{open3}}$ ($P_{\text{open3}} > P_{\text{close2}}$), creating a consecutive opening gap.

### Step 2: Isolating the Suspension Block
1. Candle 2 is now completely isolated—suspended between the lower body gap and the upper body gap.
2. Mark the entirety of Candle 2 (body and relevant boundary) as the **Suspension Block**.
3. Understand the institutional objective: Institutional algorithms treat this neglected zone as an unfinished auction node that requires rebalancing.

---

## 3. Trade Execution Plan

- **Bias / Market Regime:** Bullish continuation following aggressive gap-driven upward displacement.
- **Entry Trigger:**
  - Set a limit order at the **top boundary of the Suspension Block** (the upper body gap edge), or enter upon a tap and LTF rejection at the block.
- **Stop Loss:** Placed strictly below the bottom boundary of the Suspension Block (protecting against fill failure).
- **Invalidation:** A candle body closing below the lowest boundary of the Suspension Block cancels the setup and indicates trend failure.
- **Take Profit Target:**
  - **Standard Target:** A minimum of **2R (2x the risk distance)** above the entry.
  - **Extended Target:** The swing high of the impulse sequence or higher-timeframe resistance/external buy-side liquidity.

---

## 4. Key Nuances, Traps & Rules
- **The "Wick Blindness" Trap:** Most algorithmic screeners and retail traders ignore setups where wicks cross, entirely missing the powerful institutional rebalance potential of body gaps.
- **Rarity & Volatility Filter:** Two consecutive body gaps in intraday Forex or indices typically occur during heavy news releases, session opens (e.g., NY open / London open), or weekend gaps in crypto/futures. Treat them as high-volatility anomalies.
- **Rule of Thumb vs. Law:** As emphasized in the video, Suspension Blocks are an empirical heuristic ("rule of thumb"), not an infallible physical law. They must be validated against prevailing higher-timeframe order flow.
- **Clean Invalidation:** Never hold a long position if price closes inside or below the lower gap; when a Suspension Block fails to hold price, it often triggers an accelerated cascade in the opposite direction.
