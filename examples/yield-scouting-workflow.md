# Example: Yield Scouting Workflow

## Goal

Use `haven-yields-scout.skill` to discover stablecoin yield opportunities and rank them with risk-aware scoring.

This example is for research and comparison. It should not recommend depositing funds without additional protocol, smart contract, and user-specific risk review.

## Example Prompt

```text
Use haven-yields-scout to find stablecoin yield opportunities on Arbitrum and Base.

Filters:
- Minimum TVL: 30,000,000 USD
- Minimum APY: 4%
- Stablecoin pools only
- Exclude obvious outliers if the data source flags them

Please return:
- Top pools by APY
- Top pools by TVL
- Top pools by score
- A short risk note for each top scored pool
```

## Expected Output Structure

```text
Stablecoin Yield Scout Report

1. Scope
   - Chains reviewed
   - Data source
   - Filters used
   - Timestamp or refresh note

2. Top By APY
   - Chain
   - Protocol
   - Pool
   - APY
   - TVL
   - Score

3. Top By TVL
   - Chain
   - Protocol
   - Pool
   - TVL
   - APY
   - Score

4. Top By Score
   - Chain
   - Protocol
   - Pool
   - Score
   - Rating
   - Recommendation category

5. Risk Notes
   - Yield source
   - Protocol maturity
   - Liquidity considerations
   - Smart contract or mechanism risks
```

## Safety Notes

- APY changes quickly and should be refreshed before decision-making.
- High APY can reflect temporary incentives, low liquidity, or elevated risk.
- Stablecoin pools still carry smart contract, bridge, oracle, depeg, and protocol governance risks.
- Treat the output as research, not financial advice.
