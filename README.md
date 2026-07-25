# BOTConfessions

Anonymous on-chain confession board for BOTChain. Built for **GMT Build Week Hackathon**.

## DApp Overview

- **Post** a confession — 0.001 BOT
- **Heart** a confession — 0.001 BOT (max 1 per user per post)
- No author stored on-chain — truly anonymous
- Random ID instead of sequential (privacy)
- Connect MetaMask, no backend needed

## Status

🚧 **Mainnet migration pending** — admin allocating BOT tokens, then redeploy.

### Current (testnet)
- Contract: `0x04e6db5BE9861fbEd3E7a4192A3444a7D0e07cb4`
- Site: `https://fazly.web.id`

### Adding Mainnet to MetaMask
| Field | Value |
|-------|-------|
| Network Name | BOT Chain Mainnet |
| RPC | `https://rpc.botchain.ai` |
| Chain ID | `677` |
| Symbol | `BOT` |
| Explorer | `https://scan.botchain.ai/` |

### Redeploy Steps (when tokens arrive)
1. Buka `https://remix.ethereum.org`
2. Paste `BOTConfessions.sol` — compiler v0.8.20
3. Deploy via Injected Provider (MetaMask on mainnet)
4. Copy new address → update `index.html`:
   - `CONTRACT` → new address
   - `const CHAIN = MAINNET_CHAIN;` (uncomment that line)
5. Commit & push → auto deploy to GitHub Pages

## Submission (due Aug 4, 11:59 PM)
Submit all 4:
  1. Deployed contract address (mainnet)
  2. Live website URL: `https://fazly.web.id`
  3. GitHub repo: `https://github.com/AtharFazli/BOTConfessions`
  4. Demo video (2-3 min, show connect wallet → post → heart)

## Judging Criteria
| Item | Points |
|------|--------|
| Contract deployed & working | 30 |
| Anyone can connect & use | 25 |
| Unique wallets interacted | 20 |
| Use case originality | 15 |
| Demo video quality | 10 |
| **Total** | **100** |

## Files
- `BOTConfessions.sol` — Solidity contract (v0.8.20)
- `index.html` — Web3 frontend (dark theme)
