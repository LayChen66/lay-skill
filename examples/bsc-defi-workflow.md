# Example: BSC DeFi Workflow

## Goal

Use `haven-bsc-defi.skill` to prepare a safety-scoped BNB Chain DeFi action plan before any transaction is broadcast.

This example focuses on preflight review. It should produce a transaction plan, not execute one automatically.

## Example Prompt

```text
Use haven-bsc-defi to prepare a dry-run plan for swapping 100 USDT to CAKE on BNB Chain through PancakeSwap.

Requirements:
- Do not execute the transaction yet
- Resolve token addresses
- Explain the expected route
- List approvals that may be required
- Include slippage and amount checks
- Provide a final human confirmation checklist
```

## Expected Output Structure

```text
BSC DeFi Preflight Plan

1. Intent
   - Action: swap
   - Input token: USDT
   - Output token: CAKE
   - Input amount: 100 USDT
   - Chain: BNB Chain

2. Token Resolution
   - USDT contract address
   - CAKE contract address
   - Source of token metadata

3. Route And Quote
   - PancakeSwap route
   - Estimated output amount
   - Price impact
   - Slippage setting

4. Approval Review
   - Existing allowance, if checked
   - Required approval amount
   - Approval target contract

5. Transaction Plan
   - Step 1: approve, if needed
   - Step 2: swap
   - Gas and nonce assumptions

6. Human Confirmation Checklist
   - Verify chain ID
   - Verify token addresses
   - Verify amount and slippage
   - Verify recipient wallet
   - Confirm that execution is intended
```

## Safety Notes

- Default to dry-run planning before execution.
- Never execute ambiguous instructions such as "buy 100 BNB" without clarifying whether the user means 100 USDT worth of BNB or 100 BNB.
- Require explicit confirmation before broadcasting a transaction.
- Verify PancakeSwap router addresses and token contracts before signing.
- Private keys should be provided only through environment variables or a secure secrets manager.
