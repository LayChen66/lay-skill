# Example: EVM Wallet Workflow

## Goal

Use `haven-evm-wallet.skill` to inspect an EVM wallet with public information and produce a structured wallet report.

This example is designed for analysis and review. It does not require private keys and should not produce transactions.

## Example Prompt

```text
Use haven-evm-wallet to review this public wallet on Ethereum mainnet:

Address: 0x0000000000000000000000000000000000000000
Chain: Ethereum

Please provide:
- Native ETH balance
- ERC-20 balance summary if available
- Recent transaction observations
- Any obvious risk notes
- Suggested next checks

Do not ask for or use a private key.
Do not prepare or send any transaction.
```

## Expected Output Structure

```text
Wallet Review

1. Scope
   - Chain
   - Address
   - Data source or RPC endpoint

2. Balance Summary
   - Native token balance
   - ERC-20 token balances, if available

3. Transaction Observations
   - Recent activity pattern
   - Contract interactions
   - Notable token transfers

4. Risk Notes
   - Unknown contracts
   - Suspicious approvals or interactions
   - High-value transfers, if any

5. Suggested Next Checks
   - Approval review
   - Token address verification
   - Explorer links or manual review steps
```

## Safety Notes

- Public wallet analysis should not require a private key.
- Do not sign messages or transactions unless the user explicitly asks and confirms the purpose.
- Treat explorer and RPC data as inputs to review, not as proof of safety.
- For any transaction-related follow-up, switch to a dry-run or preflight checklist first.
