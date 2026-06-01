# Examples

This directory contains example prompts and expected output structures for the skills in this repository.

The `haven-*` names use "haven" in the sense of a harbor, refuge, or safe environment: a consistent namespace for structured, reviewable Web3 agent workflows.

These examples are documentation and evaluation aids. They are not financial advice, and they should not be treated as permission for an agent to execute transactions without human review.

## Available Examples

| Example | Skill | Purpose |
| --- | --- | --- |
| [`evm-wallet-workflow.md`](./evm-wallet-workflow.md) | `haven-evm-wallet.skill` | Inspect an EVM wallet using public data and produce a structured report. |
| [`bsc-defi-workflow.md`](./bsc-defi-workflow.md) | `haven-bsc-defi.skill` | Prepare a safety-scoped BNB Chain DeFi transaction plan before execution. |
| [`yield-scouting-workflow.md`](./yield-scouting-workflow.md) | `haven-yields-scout.skill` | Discover and rank stablecoin yield opportunities with risk-aware scoring. |

## Review Checklist

Before using any wallet or DeFi workflow:

- Use public addresses for analysis whenever possible.
- Do not paste private keys, seed phrases, or API credentials into prompts.
- Run transaction-producing workflows as dry runs first.
- Verify token addresses, chain IDs, amounts, slippage, approvals, and recipient addresses.
- Require human confirmation before broadcasting any transaction.
