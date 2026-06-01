# lay-skill

Open-source AI skills for Web3, EVM wallet workflows, BNB Chain DeFi automation, and yield research.

This repository is maintained by [LayChen66](https://github.com/LayChen66) as a reusable collection of `.skill` packages for AI coding agents, research assistants, and agent-compatible development environments.

## What Is This?

`lay-skill` provides reusable skill packages that give AI agents structured domain knowledge, workflow rules, safety constraints, and reference material for Web3 tasks.

The project focuses on practical workflows such as:

- EVM wallet creation, inspection, balance checks, signing, and transaction helpers
- BNB Chain DeFi workflows with explicit protocol and action boundaries
- Stablecoin yield discovery and scoring across DeFi protocols
- On-chain research patterns for builders, maintainers, and analysts

## Included Skills

| Skill | Purpose |
| --- | --- |
| `haven-evm-wallet.skill` | EVM wallet management and on-chain interaction workflows across Ethereum-compatible chains. |
| `haven-bsc-defi.skill` | Safety-scoped BNB Chain DeFi workflows, including PancakeSwap and Venus interaction patterns. |
| `haven-yields-scout.skill` | Stablecoin yield discovery, filtering, ranking, and structured risk scoring. |

## Why This Matters

AI coding agents are increasingly used in developer workflows, but Web3 work requires domain-specific context that generic prompts often miss.

Wallet operations, DeFi execution, protocol research, and yield analysis involve chain-specific rules, security-sensitive inputs, transaction risk, token ambiguity, RPC dependencies, and rapidly changing market data. These skills package that context into reusable open-source workflows so agents can operate with clearer boundaries and better documentation.

## Usage

1. Clone this repository.
2. Copy the `.skill` files into your skill-compatible agent environment.
3. Enable the relevant skill for your workflow.
4. Review the skill instructions before using any wallet, transaction, or DeFi-related action.
5. Customize thresholds, RPC providers, and workflow rules for your own project needs.

Example:

```bash
git clone https://github.com/LayChen66/lay-skill.git
cd lay-skill
```

Then import one or more `.skill` files into your agent environment.

## Security

These skills are intended for research, development, and carefully scoped automation.

Do not commit private keys, seed phrases, API keys, RPC credentials, wallet secrets, or production configuration files to this repository. Any transaction-producing workflow should be reviewed and confirmed by a human operator before execution.

For wallet and DeFi workflows:

- Prefer testnets before mainnet usage.
- Pass private keys through environment variables or a secure secrets manager.
- Verify token addresses, recipient addresses, chain IDs, and transaction parameters.
- Treat AI-generated transaction plans as proposals until reviewed.
- Never allow an agent to execute unbounded or ambiguous financial actions.

## Repository Structure

```text
.
├── haven-bsc-defi.skill
├── haven-evm-wallet.skill
├── haven-yields-scout.skill
└── haven-bsc-defi/
```

The `.skill` files are packaged skills. The `haven-bsc-defi/` directory contains the unpacked source for the BNB Chain DeFi skill.

## Roadmap

- Add examples for each skill.
- Add test prompts and expected outputs.
- Add documentation for skill package structure.
- Add more EVM and DeFi workflow skills.
- Add contribution guidelines.
- Add release notes for packaged `.skill` updates.

## Contributing

Contributions are welcome. Good contributions include:

- New Web3 skill workflows
- Safer transaction review rules
- Better protocol references
- Test prompts and expected outputs
- Documentation improvements
- Bug fixes for packaged skill scripts

Please keep security-sensitive workflows explicit, scoped, and reviewable.

## License

MIT
