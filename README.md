# BOTConfessions

Anonymous on-chain confession board for BOTChain. Built for **GMT Build Week Hackathon**.

## DApp Overview

- **Post** a confession — 0.001 BOT
- **Heart** a confession — 0.001 BOT (max 1 per user per post)
- No author stored on-chain — truly anonymous
- Random ID instead of sequential (privacy)
- Connect MetaMask, no backend needed

## Live

Live at **`https://fazly.web.id`** (mainnet).

## Contracts

| Network | Address | Explorer |
|---------|---------|----------|
| **Mainnet** | `0x2983b7A9BE9EACE315a0cf6A368FA3D8DDb787F3` | [scan.botchain.ai](https://scan.botchain.ai/address/0x2983b7A9BE9EACE315a0cf6A368FA3D8DDb787F3) |
| Testnet | `0x04e6db5BE9861fbEd3E7a4192A3444a7D0e07cb4` | [scan.botchain.ai](https://scan.botchain.ai/address/0x04e6db5BE9861fbEd3E7a4192A3444a7D0e07cb4) |

Both verified on explorer.

## Adding BOT Chain Mainnet to MetaMask

| Field | Value |
|-------|-------|
| Network Name | BOT Chain Mainnet |
| RPC | `https://rpc.botchain.ai` |
| Chain ID | `677` |
| Symbol | `BOT` |
| Explorer | `https://scan.botchain.ai/` |

## Branches

- **master** — testnet config
- **mainnet** — mainnet config (`CONTRACT`, `CHAIN`, `HAS_RANGE=true`)

## Files
- `BOTConfessions.sol` — Solidity contract (v0.8.20)
- `index.html` — Web3 frontend (dark theme)
